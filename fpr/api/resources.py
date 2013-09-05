"""
:mod:`fpr.resources`

Describes the REST resources provided by the FPR

"""

from django.forms.models import model_to_dict

from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie import fields

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='/tmp/fpr.log',level=logging.DEBUG)

from fpr import models

############################## API V2 RESOURCES ##############################

############ FORMATS ############

class FormatGroupResource(ModelResource):
    """ Resource for format groups.  Helper resource for FormatResource. """
    class Meta:
        queryset = models.FormatGroup.objects.all()
        detail_uri_name = 'uuid'
        include_resource_uri = False
        fields = ['uuid', 'description']
        filtering = {
            'uuid': ALL,
            'description': ALL,
        }

class FormatVersionResource(ModelResource):
    """ Resource for details on format versions.  Helper for FormatResource. """
    class Meta:
        queryset = models.FormatVersion.objects.all()
        detail_uri_name = 'uuid'
        include_resource_uri = False
        fields = ['uuid', 'description', 'access_format', 'preservation_format', 'enabled']
        filtering = {
            'uuid': ALL,
            'description': ALL,
            'access_format': ALL,
            'preservation_format': ALL,
            'enabled': ALL,
        }

class FormatResource(ModelResource):
    """ Resource for all the format info, including group, and versions. """
    group = fields.ForeignKey(FormatGroupResource, 'group', full=True)
    versions = fields.ToManyField(FormatVersionResource, 'version_set',
        full=True, null=True)

    class Meta:
        queryset = models.Format.objects.all()
        resource_name = 'format'
        allowed_methods = ['get']
        detail_uri_name = 'uuid'
        always_return_data = True
        fields = ['description', 'uuid']
        filtering = {
            'description': ALL,
            'group': ALL_WITH_RELATIONS,
            'versions': ALL_WITH_RELATIONS,
            'uuid': ALL,
        }

############ ID TOOLS ############

class IDCommandResource(ModelResource):
    replaces = fields.ForeignKey('self', 'replaces', null=True)
    class Meta:
        queryset = models.IDCommand.objects.all()
        resource_name = 'id-command'
        detail_uri_name = 'uuid'
        fields = ['uuid', 'script', 'enabled', 'lastmodified']
        filtering = {
            'uuid': ALL,
            'script': ALL,
            'enabled': ALL,
            'lastmodified': ALL,
            'replaces': ALL_WITH_RELATIONS,
        }

class IDToolConfigResource(ModelResource):
    command = fields.ForeignKey(IDCommandResource, 'command', full=True)
    tool = fields.ForeignKey('fpr.api.resources.IDToolResource', 'tool')
    replaces = fields.ForeignKey('self', 'replaces', null=True)
    class Meta:
        queryset = models.IDToolConfig.objects.all()
        resource_name = 'id-tool-config'
        detail_uri_name = 'uuid'
        fields = ['uuid', 'config', 'enabled', 'lastmodified']
        filtering = {
            'uuid': ALL,
            'config': ALL,
            'command': ALL_WITH_RELATIONS,
            'tool': ALL_WITH_RELATIONS,
            'enabled': ALL,
            'lastmodified': ALL,
            'replaces': ALL_WITH_RELATIONS,
        }

class IDToolResource(ModelResource):
    config = fields.ToManyField(IDToolConfigResource, 'config_set')
    # TODO can we get config to output a dict with config: URI?
    # Currently is a list, and no way to tell which config does what
    class Meta:
        queryset = models.IDTool.objects.all()
        resource_name = 'id-tool'
        detail_uri_name = 'uuid'
        always_return_data = True
        fields = ['description', 'enabled', 'version', 'uuid']
        filtering = {
            'description': ALL,
            'version': ALL,
            'uuid': ALL,
            'enabled': ALL,
            'config': ALL_WITH_RELATIONS,
        }


class IDRuleResource(ModelResource):
    tool = fields.ForeignKey(IDCommandResource, 'tool')
    # FIXME enabling format means IDRuleResource returns no results
    # Probably something to do with FormatResource vs FormatVersionResource
    # format = fields.ForeignKey(FormatVersionResource, 'format', full=True)
    replaces = fields.ForeignKey('self', 'replaces', null=True)
    class Meta:
        queryset = models.IDRule.objects.all()
        resource_name = 'id-rule'
        detail_uri_name = 'uuid'
        always_return_data = True
        fields = ['script_output', 'uuid', 'enabled', 'lastmodified']
        filtering = {
            'uuid': ALL,
            'script_output': ALL,
            'tool': ALL_WITH_RELATIONS,
            'format': ALL_WITH_RELATIONS,
            'enabled': ALL,
            'lastmodified': ALL,
            'replaces': ALL_WITH_RELATIONS,
        }


############################## API V1 RESOURCES ##############################

class FPRUserAgent(ModelResource):
    class Meta:
        queryset = models.Agent.objects.all()
        resource_name = 'Agent'
        authorization = Authorization()
        allowed_methods = ['post']
    
    def hydrate(self, bundle):
        logger.debug(' in hydrate, found ' + bundle.request.client_ip)
        logger.debug(' printing ' + bundle.data['clientIP'])
        #bundle.data['clientIP'] = bundle.request.client_ip
        #TODO compare client_ip (coming from middleware) and clientIP (from remost request) 
        return bundle
 
class FPRFileIDResource(ModelResource):
    class Meta:
        #authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        #authorization = DjangoAuthorization()
        queryset = models.FileID.objects.all()
        resource_name = 'FileID'
        allowed_methods = ['get']
        fields = ['uuid', 'description', 'validpreservationformat', 'validaccessformat', 'fileidtype', 'replaces', 'lastmodified', 'enabled']
        ordering = ['lastmodified']
        filtering = {
            "uuid": ALL,
            "lastmodified": ALL
        }

class FPRFileIDsBySingleIDResource(ModelResource):
    class Meta:
        #authentication = BasicAuthentication()
        #authorization = DjangoAuthorization()
        queryset = models.FileIDsBySingleID.objects.all()
        resource_name = 'FileIDsBySingleID'
        allowed_methods = ['get']
        ordering = ['lastmodified']
        filtering = {
            "pk": ALL,
            "lastmodified": ALL
        }

class FPRCommandResource(ModelResource):
    class Meta:
        #authentication = BasicAuthentication()
        #authorization = DjangoAuthorization()
        queryset = models.Command.objects.all()
        resource_name = 'Command'
        allowed_methods = ['get']
        ordering = ['lastmodified']
        filtering = {
            "uuid": ALL,
            "lastmodified": ALL
        }

class FPRCommandRelationshipResource(ModelResource):
    #FileID = fields.ForeignKey(FPRFileIDResource, 'fileID', full=True)    
    

    class Meta:
        #authentication = BasicAuthentication()
        #authorization = DjangoAuthorization()
        queryset = models.CommandRelationship.objects.all()
        resource_name = 'CommandRelationship'
        allowed_methods = ['get']
        ordering = ['lastmodified']
        filtering = {
            "uuid": ALL,
            "lastmodified": ALL
        }

class FPRCommandTypeResource(ModelResource):
    class Meta:
        #authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        #authorization = DjangoAuthorization()
        queryset = models.CommandType.objects.all()
        resource_name = 'CommandType'
        allowed_methods = ['get']
        ordering = ['lastmodified']
        filtering = {
            "uuid": ALL,
            "lastmodified": ALL
        }
        
class FPRCommandClassificationResource(ModelResource):
    class Meta:
        #authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        #authorization = DjangoAuthorization()
        queryset = models.CommandClassification.objects.all()
        resource_name = 'CommandClassification'
        allowed_methods = ['get']
        ordering = ['lastmodified']
        filtering = {
            "uuid": ALL,
            "lastmodified": ALL
        }
        
class FPRFileIDTypeResource(ModelResource):
    class Meta:
        #authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        #authorization = DjangoAuthorization()
        queryset = models.FileIDType.objects.all()
        resource_name = 'FileIDType'
        allowed_methods = ['get']
        ordering = ['lastmodified']
        filtering = {
            "uuid": ALL,
            "lastmodified": ALL
        }

