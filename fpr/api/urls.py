from django.conf.urls import patterns, include, url
from tastypie.api import Api
from fpr.api import resources

v1_api = Api(api_name='v1')
v1_api.register(resources.FPRFileIDResource())
v1_api.register(resources.FPRFileIDsBySingleIDResource())
v1_api.register(resources.FPRCommandResource())
v1_api.register(resources.FPRCommandRelationshipResource())
v1_api.register(resources.FPRCommandTypeResource())
v1_api.register(resources.FPRCommandClassificationResource())
v1_api.register(resources.FPRFileIDTypeResource())
v1_api.register(resources.FPRUserAgent())

v2_api = Api(api_name='v2')
v2_api.register(resources.FormatResource())
v2_api.register(resources.IDCommandResource())
v2_api.register(resources.IDRuleResource())
v2_api.register(resources.IDToolResource())
v2_api.register(resources.IDToolConfigResource())


urlpatterns = patterns('',
    (r'', include(v1_api.urls)),
    (r'', include(v2_api.urls)),
)
