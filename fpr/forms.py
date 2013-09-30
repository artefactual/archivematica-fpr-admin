# Django core, alphabetical
from django import forms

# External dependencies, alphabetical
from annoying.functions import get_object_or_None

# This project, alphabetical
from fpr import models as fprmodels

############ FORMATS ############

class FormatForm(forms.ModelForm):
    group = forms.ChoiceField(choices=fprmodels.FormatGroup.objects.all())

    def __init__(self, *args, **kwargs):
        super(FormatForm, self).__init__(*args, **kwargs)
        
        # add 'create' option to the FormatGroup dropdown
        choices = [(f.uuid, f.description) for f in fprmodels.FormatGroup.objects.all()]
        choices.insert(0, ('', '---------'))
        choices.append(('new', 'Create New'))
        self.fields['group'].choices = choices
        if hasattr(self.instance, 'group') and self.instance.group:
            self.fields['group'].initial = self.instance.group.uuid

    class Meta:
        model = fprmodels.Format
        fields = ('description',)

class FormatVersionForm(forms.ModelForm):
    class Meta:
        model = fprmodels.FormatVersion
        fields = ('description', 'version', 'pronom_id', 'access_format', 'preservation_format')

class FormatGroupForm(forms.ModelForm):
    class Meta:
        model = fprmodels.FormatGroup
        fields = ('description',)

############ ID TOOLS ############

class IDToolForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(IDToolForm, self).clean()
        if self.instance.pk == None:
            submitted_description = cleaned_data.get('description') # request.POST.get('description', '')
            submitted_version = cleaned_data.get('version') #request.POST.get('version', '')

            existing_idtool = get_object_or_None(
                fprmodels.IDTool,
                description=submitted_description,
                version=submitted_version
            )

            if existing_idtool != None:
                raise forms.ValidationError('An ID tool with this description and version already exists')

        return cleaned_data

    class Meta:
        model = fprmodels.IDTool
        fields = ('description', 'version')

class IDToolConfigForm(forms.ModelForm):
    command = forms.ChoiceField(choices=fprmodels.IDCommand.objects.all())

    def __init__(self, *args, **kwargs):
        super(IDToolConfigForm, self).__init__(*args, **kwargs)

        # Add 'create' option to the IDCommand dropdown
        choices = [(f.uuid, f.description) for f in fprmodels.IDCommand.active.all()]
        choices.insert(0, ('', '---------'))
        choices.append(('new', 'Create New'))
        self.fields['command'].choices = choices
        if hasattr(self.instance, 'command'):
            self.fields['command'].initial = self.instance.command.uuid

    class Meta:
        model = fprmodels.IDToolConfig
        fields = ('config',) #TODO: Add more fields

class IDCommandForm(forms.ModelForm):
    class Meta:
        model = fprmodels.IDCommand
        fields = ('description', 'script_type', 'script',)

############ ID RULES ############

class IDRuleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IDRuleForm, self).__init__(*args, **kwargs)
        # Limit to only enabled formats/commands
        self.fields['format'].queryset = fprmodels.FormatVersion.active.all()
        self.fields['command'].queryset = fprmodels.IDCommand.active.all()

    class Meta:
        model = fprmodels.IDRule
        fields = ('format', 'command', 'command_output')

############ FP RULES ############

class FPRuleForm(forms.ModelForm):
    command = forms.ChoiceField(choices=fprmodels.FPCommand.objects.all())

    def __init__(self, *args, **kwargs):
        super(FPRuleForm, self).__init__(*args, **kwargs)

        # Add 'create' option to the FPCommand dropdown
        choices = [(f.uuid, f.description) for f in fprmodels.FPCommand.active.all().filter(command_usage='normalization')]
        choices.insert(0, ('', '---------'))
        choices.append(('new', 'Create New'))
        self.fields['command'].choices = choices
        if hasattr(self.instance, 'command'):
            self.fields['command'].initial = self.instance.command.uuid

        # Show only active format versions in the format dropdown
        self.fields['format'].queryset = fprmodels.FormatVersion.active.all()
        
    

    class Meta:
        model = fprmodels.FPRule
        fields = ('purpose','format')

############ FP TOOLS ############

class FPToolForm(forms.ModelForm):
    class Meta:
        model = fprmodels.FPTool
        fields = ('description', 'version')

class FPCommandForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FPCommandForm, self).__init__(*args, **kwargs)

        verification_commands = fprmodels.FPCommand.objects.filter(command_usage='verification')
        event_detail_commands = fprmodels.FPCommand.objects.filter(command_usage='event_detail')

        # don't allow self-relation
        if hasattr(self.instance, 'uuid'):
            verification_commands = verification_commands.exclude(uuid=self.instance.uuid)
            event_detail_commands = event_detail_commands.exclude(uuid=self.instance.uuid)

        self.fields['verification_command'].queryset = verification_commands
        self.fields['event_detail_command'].queryset = event_detail_commands

    class Meta:
        model = fprmodels.FPCommand
        fields = ('tool', 'description', 'command', 'script_type', 'output_format', 'output_location', 'command_usage', 'verification_command', 'event_detail_command')
