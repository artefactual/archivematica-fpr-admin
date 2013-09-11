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
    url(r'^formatgroup/delete/(?P<slug>[-\w]+)/$', 'format_group_delete',
        name='format_group_delete'),

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

    # ID Commands
    url(r'^idcommand/$', 'idcommand_list',
        name='idcommand_list'),
    url(r'^idcommand/create/$', 'idcommand_edit',
        name='idcommand_create'),
    url(r'^idcommand/(?P<uuid>' + UUID_REGEX + ')/$', 'idcommand_detail',
        name='idcommand_detail'),
    url(r'^idcommand/(?P<uuid>' + UUID_REGEX + ')/edit/$', 'idcommand_edit',
        name='idcommand_edit'),

    # FP Rules
    url(r'^fprule/$', 'fprule_list',
        name='fprule_list'),
    url(r'^fprule/create/$', 'fprule_edit',
        name='fprule_create'),
    url(r'^fprule/(?P<uuid>' + UUID_REGEX + ')/$', 'fprule_detail',
        name='fprule_detail'),
    url(r'^fprule/(?P<uuid>' + UUID_REGEX + ')/edit/$', 'fprule_edit',
        name='fprule_edit'),

    # FP Tools
    url(r'^fptool/$', 'fptool_list',
        name='fptool_list'),
    url(r'^fptool/create/$', 'fptool_edit',
        name='fptool_create'),
    url(r'^fptool/(?P<slug>[-\w]+)/$', 'fptool_detail',
        name='fptool_detail'),
    url(r'^fptool/(?P<slug>[-\w]+)/edit/$', 'fptool_edit',
        name='fptool_edit'),

    # FP Commands
    url(r'^fpcommand/$', 'fpcommand_list',
        name='fpcommand_list'),
    url(r'^fpcommand/create/$', 'fpcommand_edit',
        name='fpcommand_create'),
    url(r'^fpcommand/(?P<uuid>' + UUID_REGEX + ')/$', 'fpcommand_detail',
        name='fpcommand_detail'),
    url(r'^fpcommand/(?P<uuid>' + UUID_REGEX + ')/edit/$', 'fpcommand_edit',
        name='fpcommand_edit'),
)
