from django import forms

from fpr import models as fprmodels

############ FORMATS ############

class FormatForm(forms.ModelForm):
    group = forms.ChoiceField(choices=fprmodels.FormatGroup.objects.all())

    def __init__(self, *args, **kwargs):
        super(FormatForm, self).__init__(*args, **kwargs)

        # Add 'create' option to the FormatGroup dropdown
        choices = [(f.uuid, f.description) for f in fprmodels.FormatGroup.objects.all()]
        choices.insert(0, ('', '---------'))
        choices.append(('new', 'Create New'))
        self.fields['group'].choices = choices
        if hasattr(self.instance, 'group'):
            self.fields['group'].initial = self.instance.group.uuid

    class Meta:
        model = fprmodels.Format
        fields = ('description',)

class FormatVersionForm(forms.ModelForm):
    class Meta:
        model = fprmodels.FormatVersion
        fields = ('description', 'access_format', 'preservation_format')

class FormatGroupForm(forms.ModelForm):
    class Meta:
        model = fprmodels.FormatGroup
        fields = ('description',)

############ ID TOOLS ############

class IDToolForm(forms.ModelForm):
    class Meta:
        model = fprmodels.IDTool
        fields = ('description', 'version')

class IDToolConfigForm(forms.ModelForm):
    command = forms.ChoiceField(choices=fprmodels.IDCommand.objects.all())

    def __init__(self, *args, **kwargs):
        super(IDToolConfigForm, self).__init__(*args, **kwargs)

        # Add 'create' option to the IDCommand dropdown
        choices = [(f.uuid, f.script) for f in fprmodels.IDCommand.objects.all()]
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
        fields = ('script',)

############ FP RULES ############

class FPRuleForm(forms.ModelForm):
    command = forms.ChoiceField(choices=fprmodels.NormalizationCommand.objects.all())

    def __init__(self, *args, **kwargs):
        super(FPRuleForm, self).__init__(*args, **kwargs)

        # Add 'create' option to the NormalizationCommand dropdown
        choices = [(f.uuid, f.description) for f in fprmodels.NormalizationCommand.objects.all()]
        choices.insert(0, ('', '---------'))
        choices.append(('new', 'Create New'))
        self.fields['command'].choices = choices
        if hasattr(self.instance, 'command'):
            self.fields['command'].initial = self.instance.command.uuid

    class Meta:
        model = fprmodels.FPRule
        fields = ('purpose','format')

class NormalizationCommandForm(forms.ModelForm):
    class Meta:
        model = fprmodels.NormalizationCommand
        fields = ('tool', 'description', 'command', 'script_type',
          'output_file_format', 'output_location', 'command_usage',
          'verification_command', 'event_detail_command', 'supported_by')

############ NORMALIZATION TOOLS ############

class NormalizationToolForm(forms.ModelForm):
    class Meta:
        model = fprmodels.NormalizationTool
        fields = ('description', 'version')
