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

    class Meta:
        model = fprmodels.IDRule
        fields = ('format', 'command', 'command_output')

############ FP RULES ############

class FPRuleForm(forms.ModelForm):
    command = forms.ChoiceField(choices=fprmodels.FPCommand.objects.all())

    def __init__(self, *args, **kwargs):
        super(FPRuleForm, self).__init__(*args, **kwargs)

        # Add 'create' option to the FPCommand dropdown
        choices = [(f.uuid, f.description) for f in fprmodels.FPCommand.objects.all()]
        choices.insert(0, ('', '---------'))
        choices.append(('new', 'Create New'))
        self.fields['command'].choices = choices
        if hasattr(self.instance, 'command'):
            self.fields['command'].initial = self.instance.command.uuid

    class Meta:
        model = fprmodels.FPRule
        fields = ('purpose','format')

class FPCommandForm(forms.ModelForm):
    class Meta:
        model = fprmodels.FPCommand
        fields = ('tool', 'description', 'command', 'script_type',
          'output_file_format', 'output_location', 'command_usage',
          'verification_command', 'event_detail_command', 'supported_by')

############ NORMALIZATION TOOLS ############

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

        self.fields['verification_command'] = forms.ModelChoiceField(queryset=verification_commands, required=False)
        self.fields['event_detail_command'] = forms.ModelChoiceField(queryset=event_detail_commands, required=False)

    class Meta:
        model = fprmodels.FPCommand
        fields = ('tool', 'description', 'command', 'script_type', 'output_file_format', 'output_location', 'command_usage', 'verification_command', 'event_detail_command')
