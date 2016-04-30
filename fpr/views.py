# stdlib, alphabetical
import os

# Django core, alphabetical
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render


# External dependencies, alphabetical
from annoying.functions import get_object_or_None

# This project, alphabetical
from fpr import forms as fprforms
from fpr import models as fprmodels
from fpr import utils

CLASS_CATEGORY_MAP = {
    'format': fprmodels.Format,
    'formatgroup': fprmodels.FormatGroup,
    'idrule': fprmodels.IDRule,
    'idcommand': fprmodels.IDCommand,
    'fprule': fprmodels.FPRule,
    'fpcommand': fprmodels.FPCommand,
}


def context(variables):
    """
    This wraps a variables dict, allowing a standard set of values to be
    included in any view without explicitly defining them there.
    Any new default variables should be added to the `default` dict within
    this function.
    """
    # The categories of commands are used to populate separate browse links for
    # each category.
    default = {
        'categories': fprmodels.FPCommand.COMMAND_USAGE_CHOICES
    }
    default.update(variables)
    return default


def home(request):
    return redirect('format_list')


@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def toggle_enabled(request, category, uuid):
    # TODO fix this and use it to genericize deleting things
    klass = CLASS_CATEGORY_MAP[category]
    obj = get_object_or_404(klass, uuid=uuid)
    obj.enabled = not obj.enabled
    obj.save()

    return redirect(category + '_list')

############ FORMATS ############

def format_list(request):
    formats = fprmodels.Format.objects.filter()
    # TODO Formats grouped by FormatGroup for better display in template
    return render(request, 'fpr/format/list.html', context(locals()))

def format_detail(request, slug):
    format = get_object_or_404(fprmodels.Format, slug=slug)
    replacing_versions = [r[0] for r in fprmodels.FormatVersion.objects.filter(replaces__isnull=False, format=format).values_list('replaces_id')]
    format_versions = fprmodels.FormatVersion.objects.filter(format=format).exclude(uuid__in=replacing_versions)
    return render(request, 'fpr/format/detail.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def format_edit(request, slug=None):
    if slug:
        action = "Edit"
        format = get_object_or_404(fprmodels.Format, slug=slug)
        group = format.group
    else:
        action = "Create"
        format = None
        group = None
    form = fprforms.FormatForm(request.POST or None, instance=format, prefix='f')
    format_group_form = fprforms.FormatGroupForm(request.POST or None, instance=group, prefix='fg')
    if form.is_valid():
        if form.cleaned_data['group'] == 'new' and format_group_form.is_valid():
            format = form.save(commit=False)
            group = format_group_form.save()
            format.group = group
            format.save()
            messages.info(request, 'Saved.')
            return redirect('format_detail', format.slug)
        elif form.cleaned_data['group'] != 'new':
            format = form.save(commit=False)
            group = fprmodels.FormatGroup.objects.get(uuid=form.cleaned_data['group'])
            format.group = group
            format = form.save()
            messages.info(request, 'Saved.')
            return redirect('format_detail', format.slug)

    return render(request, 'fpr/format/form.html', context(locals()))

############ FORMAT VERSIONS ############

def formatversion_detail(request, format_slug, slug=None):
    format = get_object_or_404(fprmodels.Format, slug=format_slug)
    version = get_object_or_404(fprmodels.FormatVersion, slug=slug)
    utils.warn_if_viewing_disabled_revision(request, version)
    return render(request, 'fpr/format/version/detail.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def formatversion_edit(request, format_slug, slug=None):
    format = get_object_or_404(fprmodels.Format, slug=format_slug)
    if slug:
        action = "Replace"
        version = get_object_or_404(fprmodels.FormatVersion, slug=slug, format=format)
    else:
        action = "Create"
        version = None
    form = fprforms.FormatVersionForm(request.POST or None, instance=version)
    if form.is_valid():
        # If replacing, disable old one and set replaces info for new one
        new_version = form.save(commit=False)
        new_version.format = format
        replaces = utils.determine_what_replaces_model_instance(fprmodels.FormatVersion, version)
        new_version.save(replacing=replaces)
        utils.update_references_to_object(fprmodels.FormatVersion, 'uuid', replaces, new_version)
        messages.info(request, 'Saved.')
        return redirect('format_detail', format.slug)
    else:
        utils.warn_if_replacing_with_old_revision(request, version)

    return render(request, 'fpr/format/version/form.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def formatversion_delete(request, format_slug, slug):
    format = get_object_or_404(fprmodels.Format, slug=format_slug)
    version = get_object_or_404(fprmodels.FormatVersion, slug=slug, format=format)
    dependent_objects = utils.dependent_objects(version)
    breadcrumbs = [
        {'text': 'Formats', 'link': reverse('format_list')},
        {'text': format.description, 'link': reverse('format_detail', args=[format.slug])},
    ]
    if request.method == 'POST':
        if 'disable' in request.POST:
            version.enabled = False
            messages.info(request, 'Disabled.')
            for obj in dependent_objects:
                obj['value'].enabled = False
                obj['value'].save()
        if 'enable' in request.POST:
            version.enabled = True
            messages.info(request, 'Enabled.')
        version.save()
        return redirect('format_detail', format.slug)
    return render(request, 'fpr/disable.html',
        context({
            'breadcrumbs': breadcrumbs,
            'dependent_objects': dependent_objects,
            'form_url': reverse('formatversion_delete', args=[format.slug, version.slug]),
            'model_name': 'Format Version',
            'object': version,
        }))


############ FORMAT GROUPS ############

def formatgroup_list(request):
    groups = fprmodels.FormatGroup.objects.all()
    return render(request, 'fpr/format/group/list.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def formatgroup_edit(request, slug=None):
    if slug:
        action = "Edit"
        group = get_object_or_404(fprmodels.FormatGroup, slug=slug)
        group_formats = fprmodels.Format.objects.filter(group=group.uuid)
    else:
        action = "Create"
        group = None

    form = fprforms.FormatGroupForm(request.POST or None, instance=group)
    if form.is_valid():
        group = form.save()
        messages.info(request, 'Saved.')
        return redirect('formatgroup_list')

    return render(request, 'fpr/format/group/form.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def formatgroup_delete(request, slug):
    group = get_object_or_404(fprmodels.FormatGroup, slug=slug)
    format_count = fprmodels.Format.objects.filter(group=group.uuid).count()
    other_groups = fprmodels.FormatGroup.objects.exclude(uuid=group.uuid)
    other_group_count = len(other_groups)
    if request.method == 'POST':
        if 'delete' in request.POST:
            # if formats exist that are a member of this group, perform group substitution
            formats = fprmodels.Format.objects.filter(group=group.uuid)
            if (len(formats)) > 0:
                substitute_group_uuid = request.POST.get('substitute', '')
                if 'substitute' in request.POST and substitute_group_uuid != '':
                    substitute_group = fprmodels.FormatGroup.objects.get(uuid=substitute_group_uuid)
                    substitution_count = 0
                    for format in formats:
                        format.group = substitute_group
                        format.save()
                        substitution_count += 1
                    messages.info(request, str(substitution_count) + ' subtitutions were performed.')
                else:
                    messages.warning(request, 'Please select a group to substitute for this group in member formats.')
                    return redirect('formatgroup_delete', slug)
            group.delete()
            messages.info(request, 'Deleted.')
        return redirect('formatgroup_list')
    else:
        return render(request, 'fpr/format/group/delete.html', context(locals()))

############ ID TOOLS ############

def idtool_list(request):
    idtools = fprmodels.IDTool.objects.filter(enabled=True)
    return render(request, 'fpr/idtool/list.html', context(locals()))

def idtool_detail(request, slug):
    idtool = get_object_or_404(fprmodels.IDTool, slug=slug, enabled=True)
    replacing_commands = [r[0] for r in fprmodels.IDCommand.objects.filter(replaces__isnull=False, tool=idtool).values_list('replaces_id')]
    idcommands = fprmodels.IDCommand.objects.filter(tool=idtool).exclude(uuid__in=replacing_commands)
    return render(request, 'fpr/idtool/detail.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def idtool_edit(request, slug=None):
    if slug:
        action = "Replace"
        idtool = get_object_or_404(fprmodels.IDTool, slug=slug, enabled=True)
    else:
        action = "Create"
        idtool = None

    form = fprforms.IDToolForm(request.POST or None, instance=idtool)
    if form.is_valid():
        idtool = form.save()
        messages.info(request, 'Saved.')
        return redirect('idtool_detail', idtool.slug)

    return render(request, 'fpr/idtool/form.html', context(locals()))


############ ID RULES ############

def idrule_list(request):
    replacing_rules = [r[0] for r in fprmodels.IDRule.objects.filter(replaces__isnull=False).values_list('replaces_id')]
    idrules = fprmodels.IDRule.objects.exclude(uuid__in=replacing_rules)
    return render(request, 'fpr/idrule/list.html', context(locals()))

def idrule_detail(request, uuid=None):
    idrule = get_object_or_404(fprmodels.IDRule, uuid=uuid)
    utils.warn_if_viewing_disabled_revision(request, idrule)
    return render(request, 'fpr/idrule/detail.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def idrule_edit(request, uuid=None):
    if uuid:
        action = "Edit"
        idrule = get_object_or_404(fprmodels.IDRule, uuid=uuid)
    else:
        action = "Create"
        idrule = None
    form = fprforms.IDRuleForm(request.POST or None, instance=idrule)
    if form.is_valid():
        new_idrule = form.save(commit=False)
        replaces = utils.determine_what_replaces_model_instance(fprmodels.IDRule, idrule)
        new_idrule.save(replacing=replaces)
        messages.info(request, 'Saved.')
        return redirect('idrule_list')
    else:
        utils.warn_if_replacing_with_old_revision(request, idrule)

    return render(request, 'fpr/idrule/form.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def idrule_delete(request, uuid):
    idrule = get_object_or_404(fprmodels.IDRule, uuid=uuid)
    breadcrumbs = [
        {'text': 'Rules', 'link': reverse('idrule_list')},
        {'text': str(idrule), 'link': reverse('idrule_detail', args=[idrule.uuid])},
    ]
    if request.method == 'POST':
        if 'disable' in request.POST:
            idrule.enabled = False
            messages.info(request, 'Disabled.')
        if 'enable' in request.POST:
            idrule.enabled = True
            messages.info(request, 'Enabled.')
        idrule.save()
        return redirect('idrule_detail', idrule.uuid)
    return render(request, 'fpr/disable.html',
        context({
            'breadcrumbs': breadcrumbs,
            'dependent_objects': None,
            'form_url': reverse('idrule_delete', args=[idrule.uuid]),
            'model_name': 'ID Rule',
            'object': idrule,
        }))

############ ID COMMANDS ############

def idcommand_list(request):
    replacing_commands = [r[0] for r in fprmodels.IDCommand.objects.filter(replaces__isnull=False).values_list('replaces_id')]
    idcommands = fprmodels.IDCommand.objects.exclude(uuid__in=replacing_commands)
    return render(request, 'fpr/idcommand/list.html', context(locals()))

def idcommand_detail(request, uuid):
    idcommand = get_object_or_404(fprmodels.IDCommand, uuid=uuid)
    utils.warn_if_viewing_disabled_revision(request, idcommand)
    return render(request, 'fpr/idcommand/detail.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def idcommand_edit(request, uuid=None):
    if uuid:
        action = "Edit"
        idcommand = get_object_or_404(fprmodels.IDCommand, uuid=uuid)
    else:
        action = "Create"
        idcommand = None
    # Set tool to parent if it exists
    initial = {}
    if 'parent' in request.GET:
        tool_uuid = request.GET['parent']
        tool = get_object_or_None(fprmodels.IDTool, uuid=tool_uuid, enabled=True)
        initial = {'tool': tool}

    form = fprforms.IDCommandForm(request.POST or None, instance=idcommand, initial=initial)
    if form.is_valid():
        new_idcommand = form.save(commit=False)
        replaces = utils.determine_what_replaces_model_instance(fprmodels.IDCommand, idcommand)
        new_idcommand.save(replacing=replaces)
        utils.update_references_to_object(fprmodels.IDCommand, 'uuid', replaces, new_idcommand)
        messages.info(request, 'Saved.')
        return redirect('idcommand_list')
    else:
        utils.warn_if_replacing_with_old_revision(request, idcommand)

    return render(request, 'fpr/idcommand/form.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def idcommand_delete(request, uuid):
    command = get_object_or_404(fprmodels.IDCommand, uuid=uuid)
    dependent_objects = utils.dependent_objects(command)
    breadcrumbs = [
        {'text': 'Commands', 'link': reverse('idcommand_list')},
        {'text': command.description, 'link': reverse('idcommand_detail', args=[command.uuid])},
    ]
    if request.method == 'POST':
        if 'disable' in request.POST:
            command.enabled = False
            messages.info(request, 'Disabled.')
            for obj in dependent_objects:
                obj['value'].enabled = False
                obj['value'].save()
        if 'enable' in request.POST:
            command.enabled = True
            messages.info(request, 'Enabled.')
        command.save()
        return redirect('idcommand_detail', command.uuid)
    return render(request, 'fpr/disable.html',
        context({
            'breadcrumbs': breadcrumbs,
            'dependent_objects': dependent_objects,
            'form_url': reverse('idcommand_delete', args=[command.uuid]),
            'model_name': 'ID Command',
            'object': command,
        }))


############ FP RULES ############

def fprule_list(request, usage=None):
    # Some usage types map to multiple categories of rules,
    # while others have different names between the two models.
    replacing_rules = [r[0] for r in fprmodels.FPRule.objects.filter(replaces__isnull=False).values_list('replaces_id')]

    if usage:
        purpose = fprmodels.FPRule.USAGE_MAP.get(usage, (usage,))
        opts = {'purpose__in': purpose}
    else:
        opts = {}
    # Display disabled rules as long as they aren't replaced by another rule
    fprules = fprmodels.FPRule.objects.filter(**opts).exclude(uuid__in=replacing_rules)
    return render(request, 'fpr/fprule/list.html', context(locals()))

def fprule_detail(request, uuid):
    fprule = get_object_or_404(fprmodels.FPRule, uuid=uuid)
    usage = fprule.command.command_usage
    utils.warn_if_viewing_disabled_revision(request, fprule)
    return render(request, 'fpr/fprule/detail.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def fprule_edit(request, uuid=None):
    if uuid:
        action = "Edit"
        fprule = get_object_or_404(fprmodels.FPRule, uuid=uuid)
        command = fprule.command
    else:
        action = "Create"
        fprule = None
        command = None
    form = fprforms.FPRuleForm(request.POST or None, instance=fprule, prefix='f')
    fprule_command_form = fprforms.FPCommandForm(request.POST or None, instance=command, prefix='fc')
    if form.is_valid():
        replaces = utils.determine_what_replaces_model_instance(fprmodels.FPRule, fprule)
        if form.cleaned_data['command'] == 'new' and fprule_command_form.is_valid():
            fprule = form.save(commit=False)
            command = fprule_command_form.save()
            fprule.command = command
            fprule.save(replacing=replaces)
            messages.info(request, 'Saved.')
            return redirect('fprule_detail', fprule.uuid)
        elif form.cleaned_data['command'] != 'new':
            fprule = form.save(commit=False)
            command = fprmodels.FPCommand.objects.get(uuid=form.cleaned_data['command'])
            fprule.command = command
            fprule = form.save()
            fprule.save(replacing=replaces)
            messages.info(request, 'Saved.')
            return redirect('fprule_list')
    else:
        utils.warn_if_replacing_with_old_revision(request, fprule)

    return render(request, 'fpr/fprule/form.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def fprule_delete(request, uuid):
    fprule = get_object_or_404(fprmodels.FPRule, uuid=uuid)
    breadcrumbs = [
        {'text': 'Rules', 'link': reverse('fprule_list')},
        {'text': str(fprule), 'link': reverse('fprule_detail', args=[fprule.uuid])},
    ]

    if request.method == 'POST':
        if 'disable' in request.POST:
            fprule.enabled = False
            messages.info(request, 'Disabled.')
        if 'enable' in request.POST:
            fprule.enabled = True
            messages.info(request, 'Enabled.')
        fprule.save()
        return redirect('fprule_detail', fprule.uuid)
    return render(request, 'fpr/disable.html',
        context({
            'breadcrumbs': breadcrumbs,
            'dependent_objects': None,
            'form_url': reverse('fprule_delete', args=[fprule.uuid]),
            'model_name': 'FPR Rule',
            'object': fprule,
        }))

############ FP TOOLS ############

def fptool_list(request):
    fptools = fprmodels.FPTool.objects.filter(enabled=True)
    return render(request, 'fpr/fptool/list.html', context(locals()))

def fptool_detail(request, slug):
    fptool = get_object_or_404(fprmodels.FPTool, slug=slug, enabled=True)
    fpcommands = fprmodels.FPCommand.objects.filter(tool__uuid=fptool.uuid)
    return render(request, 'fpr/fptool/detail.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def fptool_edit(request, slug=None):
    if slug:
        action = "Replace"
        fptool = get_object_or_404(fprmodels.FPTool, slug=slug, enabled=True)
    else:
        action = "Create"
        fptool = None
    form = fprforms.FPToolForm(request.POST or None, instance=fptool)
    if form.is_valid():
        fptool = form.save()
        messages.info(request, 'Saved.')
        return redirect('fptool_detail', fptool.slug)

    return render(request, 'fpr/fptool/form.html', context(locals()))

############ FP COMMANDS ############

def fpcommand_list(request, usage=None):
    opts = {}
    if usage:
        opts['command_usage'] = usage
    replacing_commands = [r[0] for r in fprmodels.FPCommand.objects.filter(replaces__isnull=False).values_list('replaces_id')]
    fpcommands = fprmodels.FPCommand.objects.filter(**opts).exclude(uuid__in=replacing_commands)
    return render(request, 'fpr/fpcommand/list.html', context(locals()))

def fpcommand_detail(request, uuid):
    fpcommand = get_object_or_404(fprmodels.FPCommand, uuid=uuid)
    usage = fpcommand.command_usage
    utils.warn_if_viewing_disabled_revision(request, fpcommand)
    return render(request, 'fpr/fpcommand/detail.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def fpcommand_edit(request, uuid=None):
    if uuid:
        action = "Replace"
        fpcommand = get_object_or_404(fprmodels.FPCommand, uuid=uuid)
    else:
        action = "Create"
        fpcommand = None
    if request.method == 'POST':
        form = fprforms.FPCommandForm(request.POST, instance=fpcommand)
        if form.is_valid():
            # save command
            new_fpcommand = form.save(commit=False)
            new_fpcommand.command = new_fpcommand.command.replace('\r\n', '\n')
            # Handle replacing previous rule and setting enabled/disabled
            replaces = utils.determine_what_replaces_model_instance(fprmodels.FPCommand, fpcommand)
            new_fpcommand.save(replacing=replaces)
            utils.update_references_to_object(fprmodels.FPCommand, 'uuid', replaces, new_fpcommand)
            messages.info(request, 'Saved.')
            return redirect('fpcommand_list', new_fpcommand.command_usage)
    else:
        # Set tool to parent if it exists
        initial = {}
        if 'parent' in request.GET:
            tool_uuid = request.GET['parent']
            fptool = get_object_or_None(fprmodels.FPTool, uuid=tool_uuid, enabled=True)
            initial = {'tool': fptool}
        form = fprforms.FPCommandForm(instance=fpcommand, initial=initial)
        utils.warn_if_replacing_with_old_revision(request, fpcommand)

    return render(request, 'fpr/fpcommand/form.html', context(locals()))

@user_passes_test(lambda u: u.is_superuser, login_url='/forbidden/')
def fpcommand_delete(request, uuid):
    command = get_object_or_404(fprmodels.FPCommand, uuid=uuid)
    dependent_objects = utils.dependent_objects(command)
    breadcrumbs = [
        {'text': 'Commands', 'link': reverse('fpcommand_list')},
        {'text': command.description, 'link': reverse('fpcommand_detail', args=[command.uuid])},
    ]
    if request.method == 'POST':
        if 'disable' in request.POST:
            command.enabled = False
            messages.info(request, 'Disabled.')
            for obj in dependent_objects:
                obj['value'].enabled = False
                obj['value'].save()
        if 'enable' in request.POST:
            command.enabled = True
            messages.info(request, 'Enabled.')
        command.save()
        return redirect('fpcommand_detail', command.uuid)
    return render(request, 'fpr/disable.html',
        context({
            'breadcrumbs': breadcrumbs,
            'dependent_objects': dependent_objects,
            'form_url': reverse('fpcommand_delete', args=[command.uuid]),
            'model_name': 'FP Command',
            'object': command,
        }))

############ REVISIONS ############

def revision_list(request, entity_name, uuid):
    # get model using entity name
    available_models = models.get_models()
    model = None
    for model in available_models:
        if model._meta.db_table == 'fpr_' + entity_name:
            break
    if model == None:
        raise Http404

    # human-readable names
    revision_type = entity_name
    human_readable_names = {
        'formatversion': 'Format Version',
        'idtoolconfig': 'ID Tool Configuration',
        'idrule': 'ID Rule',
        'idcommand': 'Identification Command',
        'fpcommand': 'FP Command',
        'fprule': 'FP Rule'
    }
    if entity_name in human_readable_names:
        revision_type = human_readable_names[entity_name]

    # restrict to models that are intended to have revisions
    try:
        getattr(model, 'replaces')

        # get specific revision's data and augment with detail URL
        revision = model.objects.get(uuid=uuid)
        _augment_revisions_with_detail_url(request, entity_name, model, [revision])

        # get revision ancestor data and augment with detail URLs
        ancestors = utils.get_revision_ancestors(model, uuid, [])
        _augment_revisions_with_detail_url(request, entity_name, model, ancestors)

        # get revision descendant data and augment with detail URLs
        descendants = utils.get_revision_descendants(model, uuid, [])
        _augment_revisions_with_detail_url(request, entity_name, model, descendants)
        descendants.reverse()

        return render(request, 'fpr/revisions/list.html', context(locals()))
    except AttributeError:
        raise Http404

def _augment_revisions_with_detail_url(request, entity_name, model, revisions):
    for revision in revisions:
        if request.user.is_superuser:
            detail_view_name = entity_name + '_edit'
        else:
            detail_view_name = entity_name + '_detail'

        try:
            parent_key_value = None
            if entity_name == 'formatversion':
                parent_key_value = revision.format.slug
            if entity_name == 'idtoolconfig':
                parent_key_value = revision.tool.slug

            if parent_key_value:
                revision.detail_url = reverse(detail_view_name, args=[parent_key_value, revision.slug])
            else:
                revision.detail_url = reverse(detail_view_name, args=[revision.slug])

        except:
            revision.detail_url = reverse(detail_view_name, args=[revision.uuid])
