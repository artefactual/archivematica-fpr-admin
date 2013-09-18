from django import template
import django.template.base as base

register = template.Library()

@register.tag(name='revisions_link')
def revisions_link(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, revision_type, object_uuid = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires two arguments" % token.contents.split()[0])

    return RevisionLinkNode(revision_type, object_uuid)

class RevisionLinkNode(template.Node):
    def __init__(self, revision_type, object_uuid):
        if (revision_type[0] == '"'):
            self.revision_type = revision_type[1:-1]
        else:
            self.revision_type = template.Variable(revision_type)

        if (object_uuid[0] == '"'):
            self.object_uuid = object_uuid[1:-1]
        else:
            self.object_uuid = template.Variable(object_uuid)

    def render(self, context):
        if (self.revision_type.__class__ == base.Variable):
            revision_type = self.revision_type.resolve(context)
        else:
            revision_type = self.revision_type

        if (self.object_uuid.__class__ == base.Variable):
            object_uuid = self.object_uuid.resolve(context)
        else:
            object_uuid = self.object_uuid

        return '<a class="revisions_link" href="/fpr/revisions/' + revision_type + '/' + object_uuid + '/">Revision History</a>'
