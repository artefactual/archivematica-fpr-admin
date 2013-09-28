# stdlib, alphabetical
import os

# Django core, alphabetical
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


def home(request):
    # once per session, display the welcome text
    if not 'welcome_message_shown' in request.session: # or not request.session['welcome_message_shown']:
        file_path = os.path.join(os.path.dirname(__file__), 'templates/welcome.html')
        file = open(file_path, 'r')
        messages.info(request, file.read())        
        request.session['welcome_message_shown'] = True
    return redirect('format_list')

############ FORMATS ############

def format_list(request):
    formats = fprmodels.Format.objects.filter()
    # TODO Formats grouped by FormatGroup for better display in template
    return render(request, 'fpr/format/list.html', locals())

def format_detail(request, slug):
    format = get_object_or_404(fprmodels.Format, slug=slug)
    format_versions = fprmodels.FormatVersion.active.filter(format=format)
    return render(request, 'fpr/format/detail.html', locals())

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

    return render(request, 'fpr/format/form.html', locals())

############ FORMAT VERSIONS ############

def formatversion_detail(request, format_slug, slug=None):
    format = get_object_or_404(fprmodels.Format, slug=format_slug)
    version = get_object_or_404(fprmodels.FormatVersion, slug=slug)
    return render(request, 'fpr/format/version/detail.html', locals())

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

    return render(request, 'fpr/format/version/form.html', locals())

def formatversion_delete(request, format_slug, slug):
    format = get_object_or_404(fprmodels.Format, slug=format_slug)
    version = get_object_or_404(fprmodels.FormatVersion, slug=slug, format=format)
    dependent_objects = utils.dependent_objects(version)
    if request.method == 'POST':
        if 'delete' in request.POST:
            version.enabled = False
            version.save()
            messages.info(request, 'Disabled.')
            for obj in dependent_objects:
                obj['value'].enabled = False
                obj['value'].save()
        return redirect('format_detail', format.slug)
    return render(request, 'fpr/format/version/delete.html', locals())

############ FORMAT GROUPS ############

def formatgroup_list(request):
    groups = fprmodels.FormatGroup.objects.all()
    return render(request, 'fpr/format/group/list.html', locals())

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

    return render(request, 'fpr/format/group/form.html', locals())

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
        return render(request, 'fpr/format/group/delete.html', locals())

############ ID TOOLS ############

def idtool_list(request):
    idtools = fprmodels.IDTool.objects.filter(enabled=True)
    # TODO Add IDToolConfig info??
    return render(request, 'fpr/idtool/list.html', locals())

def idtool_detail(request, slug):
    idtool = get_object_or_404(fprmodels.IDTool, slug=slug, enabled=True)
    idtool_config = fprmodels.IDToolConfig.active.filter(tool=idtool)
    return render(request, 'fpr/idtool/detail.html', locals())

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

    return render(request, 'fpr/idtool/form.html', locals())

############ ID TOOL CONFIGURATIONS ############

def idtoolconfig_detail(request, idtool_slug, slug):
    idtool = get_object_or_404(fprmodels.IDTool, slug=idtool_slug, enabled=True)
    config = get_object_or_404(fprmodels.IDToolConfig, slug=slug, tool=idtool)
    return render(request, 'fpr/idtool/config/detail.html', locals())

def idtoolconfig_edit(request, idtool_slug, slug=None):
    idtool = get_object_or_404(fprmodels.IDTool, slug=idtool_slug, enabled=True)
    if slug:
        action = "Replace"
        config = get_object_or_404(fprmodels.IDToolConfig, slug=slug, tool=idtool)
        command = config.command
    else:
        action = "Create"
        config = None
        command = None

    form = fprforms.IDToolConfigForm(request.POST or None, instance=config)
    config_command_form = fprforms.IDCommandForm(request.POST or None, instance=command, prefix='c')

    if form.is_valid():
        replaces = utils.determine_what_replaces_model_instance(fprmodels.IDToolConfig, config)
        if form.cleaned_data['command'] == 'new' and config_command_form.is_valid():
            config = form.save(commit=False)
            command = config_command_form.save()
            config.tool = idtool
            config.command = command
            config.save(replacing=replaces)
            messages.info(request, 'Saved.')
            return redirect('idtool_detail', idtool.slug)
        elif form.cleaned_data['command'] != 'new':
            config = form.save(commit=False)
            config.tool = idtool
            command = fprmodels.IDCommand.objects.get(uuid=form.cleaned_data['command'])
            config.command = command
            config = form.save()
            config.save(replacing=replaces)
            messages.info(request, 'Saved.')
            return redirect('idtool_detail', idtool.slug)
    else:
        utils.warn_if_replacing_with_old_revision(request, config)

    return render(request, 'fpr/idtool/config/form.html', locals())

def idtoolconfig_delete(request, idtool_slug, slug):
    idtool = get_object_or_404(fprmodels.IDTool, slug=idtool_slug)
    config = get_object_or_404(fprmodels.IDToolConfig, slug=slug, tool=idtool)
    dependent_objects = utils.dependent_objects(config)
    if request.method == 'POST':
        if 'delete' in request.POST:
            config.enabled = False
            config.save()
            messages.info(request, 'Disabled.')
            for obj in dependent_objects:
                obj['value'].enabled = False
                obj['value'].save()
        return redirect('idtool_detail', idtool.slug)
    return render(request, 'fpr/idtool/config/delete.html', locals())


############ ID RULES ############

def idrule_list(request):
    idrules = fprmodels.IDRule.active.all()
    return render(request, 'fpr/idrule/list.html', locals())

def idrule_detail(request, uuid=None):
    idrule = get_object_or_404(fprmodels.IDRule, uuid=uuid)
    return render(request, 'fpr/idrule/detail.html', locals())

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

    return render(request, 'fpr/idrule/form.html', locals())

def idrule_delete(request, uuid):
    idrule = get_object_or_404(fprmodels.IDRule, uuid=uuid)
    if request.method == 'POST':
        if 'delete' in request.POST:
            idrule.enabled = False
            idrule.save()
            messages.info(request, 'Disabled.')
        return redirect('idrule_detail', idrule.uuid)
    return render(request, 'fpr/idrule/delete.html', locals())

############ ID COMMANDS ############

def idcommand_list(request):
    idcommands = fprmodels.IDCommand.active.all()
    return render(request, 'fpr/idcommand/list.html', locals())

def idcommand_detail(request, uuid):
    idcommand = get_object_or_404(fprmodels.IDCommand, uuid=uuid)
    idtoolconfigs = fprmodels.IDToolConfig.active.filter(command=idcommand)
    return render(request, 'fpr/idcommand/detail.html', locals())

def idcommand_edit(request, uuid=None):
    if uuid:
        action = "Edit"
        idcommand = get_object_or_404(fprmodels.IDCommand, uuid=uuid)
    else:
        action = "Create"
        idcommand = None
    form = fprforms.IDCommandForm(request.POST or None, instance=idcommand)
    if form.is_valid():
        new_idcommand = form.save(commit=False)
        replaces = utils.determine_what_replaces_model_instance(fprmodels.IDCommand, idcommand)
        new_idcommand.save(replacing=replaces)
        utils.update_references_to_object(fprmodels.IDCommand, 'uuid', replaces, new_idcommand)
        messages.info(request, 'Saved.')
        return redirect('idcommand_list')
    else:
        utils.warn_if_replacing_with_old_revision(request, idcommand)

    return render(request, 'fpr/idcommand/form.html', locals())

############ FP RULES ############

def fprule_list(request):
    fprules = fprmodels.FPRule.objects.filter(enabled=True).filter(~Q(purpose='Characterize'))
    return render(request, 'fpr/fprule/list.html', locals())

def fprule_detail(request, uuid):
    fprule = get_object_or_404(fprmodels.FPRule, uuid=uuid)
    return render(request, 'fpr/fprule/detail.html', locals())

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

    return render(request, 'fpr/fprule/form.html', locals())

############ FP TOOLS ############

def fptool_list(request):
    fptools = fprmodels.FPTool.objects.filter(enabled=True)
    return render(request, 'fpr/fptool/list.html', locals())

def fptool_detail(request, slug):
    fptool = get_object_or_404(fprmodels.FPTool, slug=slug, enabled=True)
    fpcommands = fprmodels.FPCommand.objects.filter(tool__uuid=fptool.uuid)
    return render(request, 'fpr/fptool/detail.html', locals())

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

    return render(request, 'fpr/fptool/form.html', locals())

############ FP COMMANDS ############

def fpcommand_list(request):
    fpcommands = fprmodels.FPCommand.objects.filter(enabled=True).filter(~Q(command_usage='Characterization'))
    return render(request, 'fpr/fpcommand/list.html', locals())

def fpcommand_detail(request, uuid):
    fpcommand = get_object_or_404(fprmodels.FPCommand, uuid=uuid, enabled=True)
    return render(request, 'fpr/fpcommand/detail.html', locals())

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
            # remove existing relations
            commandtools = fprmodels.FPCommandTool.objects.filter(command=fpcommand)
            for commandtool in commandtools:
                commandtool.delete()

            new_fpcommand = form.save(commit=False)
            replaces = utils.determine_what_replaces_model_instance(fprmodels.FPCommand, fpcommand)
            new_fpcommand.save(replacing=replaces)
            utils.update_references_to_object(fprmodels.FPCommand, 'uuid', replaces, new_fpcommand)
            # TODO: add many to many reference updating

            for tool_id in request.POST.getlist('tool'):
                tool = fprmodels.FPCommandTool(
                    command=new_fpcommand,
                    tool=fprmodels.FPTool.objects.get(pk=tool_id)
                )
                tool.save()

            messages.info(request, 'Saved.')
            return redirect('fpcommand_list')
    else:
        if 'parent' in request.GET:
            fptool = get_object_or_None(fprmodels.FPTool, uuid=request.GET.get('parent', ''), enabled=True)
            initial = {'tool': [fptool]}
        else:
            initial = None
        form = fprforms.FPCommandForm(instance=fpcommand, initial=initial)
        utils.warn_if_replacing_with_old_revision(request, fpcommand)

    return render(request, 'fpr/fpcommand/form.html', locals())

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
        _augment_revisions_with_detail_url(entity_name, model, [revision])

        # get revision ancestor data and augment with detail URLs
        ancestors = utils.get_revision_ancestors(model, uuid, [])
        _augment_revisions_with_detail_url(entity_name, model, ancestors)

        # get revision descendant data and augment with detail URLs
        descendants = utils.get_revision_descendants(model, uuid, [])
        _augment_revisions_with_detail_url(entity_name, model, descendants)
        descendants.reverse()

        return render(request, 'fpr/revisions/list.html', locals())
    except AttributeError:
        raise Http404

def _augment_revisions_with_detail_url(entity_name, model, revisions):
    for revision in revisions:
        detail_view_name = entity_name + '_edit'
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
