# stdlib, alphabetical

# Django core, alphabetical
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

# External dependencies, alphabetical
from annoying.functions import get_object_or_None

# This project, alphabetical
from fpr import forms as fprforms
from fpr import models as fprmodels
from fpr import utils


def home(request):
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
    if request.method == 'POST':
        form = fprforms.FormatForm(request.POST, instance=format, prefix='f')
        format_group_form = fprforms.FormatGroupForm(request.POST, instance=group, prefix='fg')
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
    else:
        form = fprforms.FormatForm(instance=format, prefix='f')
        format_group_form = fprforms.FormatGroupForm(instance=group, prefix='fg')

    return render(request, 'fpr/format/form.html', locals())

############ FORMAT VERSIONS ############

def format_version_edit(request, format_slug, slug=None):
    format = get_object_or_404(fprmodels.Format, slug=format_slug)
    if slug:
        action = "Replace"
        version = get_object_or_404(fprmodels.FormatVersion, slug=slug, format=format)
    else:
        action = "Create"
        version = None
    if request.method == 'POST':
        form = fprforms.FormatVersionForm(request.POST, instance=version)
        if form.is_valid():
            # If replacing, disable old one and set replaces info for new one
            new_version = form.save(commit=False)
            new_version.format = format
            if version:
                old_version = get_object_or_404(fprmodels.FormatVersion, slug=slug, format=format)
                old_version.enabled = False
                old_version.save()
                new_version.replaces = old_version
                new_version.uuid = None
                new_version.pk = None
            new_version.save()
            messages.info(request, 'Saved.')
            return redirect('format_detail', format.slug)
    else:
        form = fprforms.FormatVersionForm(instance=version)

    return render(request, 'fpr/format/version/form.html', locals())

def format_version_delete(request, format_slug, slug):
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

def format_group_list(request):
    groups = fprmodels.FormatGroup.objects.all()
    return render(request, 'fpr/format/group/list.html', locals())

def format_group_edit(request,  slug=None):
    if slug:
        action = "Edit"
        group = get_object_or_404(fprmodels.FormatGroup, slug=slug)
    else:
        action = "Create"
        group = None

    if request.method == 'POST':
        form = fprforms.FormatGroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save()
            messages.info(request, 'Saved.')
            return redirect('format_group_list')
    else:
        form = fprforms.FormatGroupForm(instance=group)

    return render(request, 'fpr/format/group/form.html', locals())

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
    if request.method == 'POST':
        form = fprforms.IDToolForm(request.POST, instance=idtool)
        if form.is_valid():
            new_idtool = form.save(commit=False)
            if idtool:
                old_idtool = get_object_or_404(fprmodels.IDTool, slug=slug, enabled=True)
                old_idtool.enabled = False
                old_idtool.save()
                new_idtool.replaces = old_idtool
                new_idtool.uuid = None
                new_idtool.pk = None
            new_idtool.save()
            messages.info(request, 'Saved.')
            return redirect('idtool_detail', new_idtool.slug)
    else:
        form = fprforms.IDToolForm(instance=idtool)

    return render(request, 'fpr/idtool/form.html', locals())

############ ID TOOL CONFIGURATIONS ############

def idtool_config_edit(request, idtool_slug, slug=None):
    idtool = get_object_or_404(fprmodels.IDTool, slug=idtool_slug)
    if slug:
        action = "Replace"
        config = get_object_or_404(fprmodels.IDToolConfig, slug=slug, tool=idtool)
        command = config.command
    else:
        action = "Create"
        config = None
        command = None
    if request.method == 'POST':
        form = fprforms.IDToolConfigForm(request.POST, instance=config)
        config_command_form = fprforms.IDCommandForm(request.POST, instance=command, prefix='c')

        if form.is_valid():
            if form.cleaned_data['command'] == 'new' and config_command_form.is_valid():
                config = form.save(commit=False)
                command = config_command_form.save()
                config.tool = idtool
                config.command = command
                config.save()
                messages.info(request, 'Saved.')
                return redirect('idtool_detail', idtool.slug)
            elif form.cleaned_data['command'] != 'new':
                config = form.save(commit=False)
                config.tool = idtool
                command = fprmodels.IDCommand.objects.get(uuid=form.cleaned_data['command'])
                config.command = command
                config = form.save()
                messages.info(request, 'Saved.')
                return redirect('idtool_detail', idtool.slug)
    else:
        form = fprforms.IDToolConfigForm(instance=config)
        config_command_form = fprforms.IDCommandForm(instance=command, prefix='c')

    return render(request, 'fpr/idtool/config/form.html', locals())

def idtool_config_delete(request, idtool_slug, slug):
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


def idrule_edit(request, uuid=None):
    if uuid:
        action = "Edit"
        idrule = get_object_or_404(fprmodels.IDRule, uuid=uuid)
    else:
        action = "Create"
        idrule = None
    form = fprforms.IDRuleForm(request.POST or None, instance=idrule, prefix='f')
    if form.is_valid():
        new_idrule = form.save(commit=False)
        old_idrule = get_object_or_None(fprmodels.IDRule, uuid=uuid, enabled=True)
        new_idrule.save(replacing=old_idrule)
        messages.info(request, 'Saved.')
        return redirect('idrule_list')
    return render(request, 'fpr/idrule/form.html', locals())


############ FP RULES ############

def fprule_list(request):
    fprules = fprmodels.FPRule.objects.filter(enabled=True)
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
    if request.method == 'POST':
        form = fprforms.FPRuleForm(request.POST, instance=fprule, prefix='f')
        fprule_command_form = fprforms.NormalizationCommandForm(request.POST, instance=command, prefix='fc')
        if form.is_valid():
            if form.cleaned_data['command'] == 'new' and fprule_command_form.is_valid():
                fprule = form.save(commit=False)
                command = fprule_command_form.save()
                fprule.command = command
                fprule.save()
                messages.info(request, 'Saved.')
                return redirect('fprule_detail', fprule.uuid)
            elif form.cleaned_data['command'] != 'new':
                fprule = form.save(commit=False)
                command = fprmodels.NormalizationCommand.objects.get(uuid=form.cleaned_data['command'])
                fprule.command = command
                fprule = form.save()
                messages.info(request, 'Saved.')
                return redirect('fprule_detail', fprule.uuid)
    else:
        form = fprforms.FPRuleForm(instance=fprule, prefix='f')
        fprule_command_form = fprforms.NormalizationCommandForm(instance=command, prefix='fc')

    return render(request, 'fpr/fprule/form.html', locals())

############ NORMALIZATION TOOLS ############

def normalizationtool_list(request):
    normalizationtools = fprmodels.NormalizationTool.objects.filter(enabled=True)
    return render(request, 'fpr/normalizationtool/list.html', locals())

def normalizationtool_detail(request, slug):
    normalizationtool = get_object_or_404(fprmodels.NormalizationTool, slug=slug, enabled=True)
    return render(request, 'fpr/normalizationtool/detail.html', locals())

def normalizationtool_edit(request, slug=None):
    if slug:
        action = "Replace"
        normalizationtool = get_object_or_404(fprmodels.NormalizationTool, slug=slug, enabled=True)
    else:
        action = "Create"
        normalizationtool = None
    if request.method == 'POST':
        form = fprforms.NormalizationToolForm(request.POST, instance=normalizationtool)
        if form.is_valid():
            new_normalizationtool = form.save(commit=False)
            if normalizationtool:
                old_normalizationtool = get_object_or_404(fprmodels.NormalizationTool, slug=slug, enabled=True)
                old_normalizationtool.enabled = False
                old_normalizationtool.save()
                new_normalizationtool.replaces = old_normalizationtool
                new_normalizationtool.uuid = None
                new_normalizationtool.pk = None
            new_normalizationtool.save()
            messages.info(request, 'Saved.')
            return redirect('normalizationtool_detail', new_normalizationtool.slug)
    else:
        form = fprforms.NormalizationToolForm(instance=normalizationtool)

    return render(request, 'fpr/normalizationtool/form.html', locals())
