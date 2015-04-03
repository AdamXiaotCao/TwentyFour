from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'twentyFour.views.home', name = 'home'),
    # url(r'^add_follow/(?P<id>\d+)$','twentyFour.views.add_follow', name='follow'),
    # url(r'^un_follow/(?P<id>\d+)$','twentyFour.views.un_follow', name='unfollow'),
    # url(r'^block/(?P<id>\d+)$','twentyFour.views.block', name='block'),
    # url(r'^unblock/(?P<id>\d+)$','twentyFour.views.un_block', name='unblock'),
    # Route for built-in authentication with our own custom login page
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^create_multigame$', 'twentyFour.views.create_multigame', name='create_game'),
    # Route to logout a user and send them back to the login page
    url(r'^check_game/(?P<id>\d+)$','twentyFour.views.check_game',name='check_game'),
    url(r'^get_games','twentyFour.views.get_games',name = 'get_games'),
    url(r'^get_players/(?P<id>\d+)$','twentyFour.views.get_players',name = 'get_players'),
    url(r'^get_progress/(?P<id>\d+)$','twentyFour.views.get_progress',name ='get_progress'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^register$', 'twentyFour.views.register', name='register'),
    url(r'^single_game$','twentyFour.views.single_game',name='single_game'),
    url(r'^multi_game$','twentyFour.views.start_multigame',name='start_game'),
    url(r'^determine$','twentyFour.views.determine_result',name='determine'),
    url(r'^lobby$', 'twentyFour.views.lobby', name='lobby'),
    url(r'^join_multigame/(?P<id>\d+)$','twentyFour.views.join_multigame',name= 'join_multigame'),
    url(r'^create_game$', 'twentyFour.views.create_multigame', name='create_game'),
    url(r'^photo/(?P<id>\d+)$', 'twentyFour.views.get_photo', name='photo'),
    url(r'^end_game/(?P<id>\d+)$', 'twentyFour.views.end_game', name='end_game'),
    url(r'^join_multigame/determine$', 'twentyFour.views.determine_result'),
    # url(r'^change_password/(?P<id>\d+)$','twentyFour.views.change_password', name='change_password'),
    # url(r'^forgot_password$', 'twentyFour.views.forgot_password', name='forgot_password'),
    # url(r'^set_password/(?P<id>\d+)$', 'twentyFour.views.set_password', name='set_password'),
    # url(r'^confirm-reset/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$','twentyFour.views.confirm_reset', name='confirm_reset'),
)

