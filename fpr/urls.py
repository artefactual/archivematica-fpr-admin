from django.conf.urls import patterns, url

UUID_REGEX = '[\w]{8}(-[\w]{4}){3}-[\w]{12}'

urlpatterns = patterns('fpr.views',

    url(r'^$', 'home', name='fpr_index'),

    # Formats
    url(r'^format/$', 'format_list',
        name='format_list'),
    url(r'^format/create/$', 'format_edit',
        name='format_create'),
    url(r'^format/(?P<slug>[-\w]+)/$', 'format_detail',
        name='format_detail'),
    url(r'^format/(?P<slug>[-\w]+)/edit/$', 'format_edit',
        name='format_edit'),

    # Format Versions
    url(r'^format/(?P<format_slug>[-\w]+)/create/$', 'format_version_edit',
        name='format_version_create'),
    url(r'^format/(?P<format_slug>[-\w]+)/(?P<slug>[-\w]+)/edit/$',
        'format_version_edit',
        name='format_version_edit'),
    url(r'^format/(?P<format_slug>[-\w]+)/(?P<slug>[-\w]+)/delete/$',
        'format_version_delete',
        name='format_version_delete'),

    # Format groups
    url(r'^formatgroup/$', 'format_group_list',
        name='format_group_list'),
    url(r'^formatgroup/create/$', 'format_group_edit',
        name='format_group_create'),
    url(r'^formatgroup/(?P<slug>[-\w]+)/$', 'format_group_edit',
        name='format_group_edit'),

    # ID Tools
    url(r'^idtool/$', 'idtool_list',
        name='idtool_list'),
    url(r'^idtool/create/$', 'idtool_edit',
        name='idtool_create'),
    url(r'^idtool/(?P<slug>[-\w]+)/$', 'idtool_detail',
        name='idtool_detail'),
    url(r'^idtool/(?P<slug>[-\w]+)/edit/$', 'idtool_edit',
        name='idtool_edit'),

    # ID Tool Configurations
    url(r'^idtool/(?P<idtool_slug>[-\w]+)/create/$', 'idtool_config_edit',
        name='idtool_config_create'),
    url(r'^idtool/(?P<idtool_slug>[-\w]+)/(?P<slug>[-\w]+)/edit/$',
        'idtool_config_edit',
        name='idtool_config_edit'),
    url(r'^idtool/(?P<idtool_slug>[-\w]+)/(?P<slug>[-\w]+)/delete/$',
        'idtool_config_delete',
        name='idtool_config_delete'),

    # ID Rules
    url(r'^idrule/$', 'idrule_list',
        name='idrule_list'),
    url(r'^idrule/create/$', 'idrule_edit',
        name='idrule_create'),
    url(r'^idrule/(?P<uuid>' + UUID_REGEX + ')/edit/$', 'idrule_edit',
        name='idrule_edit'),

    # FP Rules
    url(r'^fprule/$', 'fprule_list',
        name='fprule_list'),
    url(r'^fprule/create/$', 'fprule_edit',
        name='fprule_create'),
    url(r'^fprule/(?P<uuid>' + UUID_REGEX + ')/$', 'fprule_detail',
        name='fprule_detail'),
    url(r'^fprule/(?P<uuid>' + UUID_REGEX + ')/edit/$', 'fprule_edit',
        name='fprule_edit'),

    # Normalization Tools
    url(r'^normalizationtool/$', 'normalizationtool_list',
        name='normalizationtool_list'),
    url(r'^normalizationtool/create/$', 'normalizationtool_edit',
        name='normalizationtool_create'),
    url(r'^normalizationtool/(?P<slug>[-\w]+)/$', 'normalizationtool_detail',
        name='normalizationtool_detail'),
    url(r'^normalizationtool/(?P<slug>[-\w]+)/edit/$', 'normalizationtool_edit',
        name='normalizationtool_edit'),
)
