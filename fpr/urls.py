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
    url(r'^format/(?P<format_slug>[-\w]+)/create/$', 'formatversion_edit',
        name='formatversion_create'),
    url(r'^format/(?P<format_slug>[-\w]+)/(?P<slug>[-\w]+)/$', 'formatversion_detail',
        name='formatversion_detail'),
    url(r'^format/(?P<format_slug>[-\w]+)/(?P<slug>[-\w]+)/edit/$',
        'formatversion_edit',
        name='formatversion_edit'),
    url(r'^format/(?P<format_slug>[-\w]+)/(?P<slug>[-\w]+)/delete/$',
        'formatversion_delete',
        name='formatversion_delete'),

    # Format groups
    url(r'^formatgroup/$', 'formatgroup_list',
        name='formatgroup_list'),
    url(r'^formatgroup/create/$', 'formatgroup_edit',
        name='formatgroup_create'),
    url(r'^formatgroup/(?P<slug>[-\w]+)/$', 'formatgroup_edit',
        name='formatgroup_edit'),
    url(r'^formatgroup/delete/(?P<slug>[-\w]+)/$', 'formatgroup_delete',
        name='formatgroup_delete'),

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
    url(r'^idtool/(?P<idtool_slug>[-\w]+)/create/$', 'idtoolconfig_edit',
        name='idtoolconfig_create'),
    url(r'^idtool/(?P<idtool_slug>[-\w]+)/(?P<slug>[-\w]+)/edit/$',
        'idtoolconfig_edit',
        name='idtoolconfig_edit'),
    url(r'^idtool/(?P<idtool_slug>[-\w]+)/(?P<slug>[-\w]+)/delete/$',
        'idtoolconfig_delete',
        name='idtoolconfig_delete'),
    url(r'^idtool/(?P<idtool_slug>[-\w]+)/(?P<slug>[-\w]+)/$',
        'idtoolconfig_detail',
        name='idtoolconfig_detail'),

    # ID Rules
    url(r'^idrule/$', 'idrule_list',
        name='idrule_list'),
    url(r'^idrule/create/$', 'idrule_edit',
        name='idrule_create'),
    url(r'^idrule/(?P<uuid>' + UUID_REGEX + ')/edit/$', 'idrule_edit',
        name='idrule_edit'),
    url(r'^idrule/(?P<uuid>' + UUID_REGEX + ')/$', 'idrule_detail',
        name='idrule_detail'),
    url(r'^idrule/(?P<uuid>' + UUID_REGEX + ')/delete/$',
        'idrule_delete',
        name='idrule_delete'),



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

    # Revisions
    url(r'^revisions/(?P<entity_name>[-\w]+)/(?P<uuid>' + UUID_REGEX + ')/$', 'revision_list',
        name='revision_list'),
)
