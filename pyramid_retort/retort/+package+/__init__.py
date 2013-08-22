from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from .security import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    authentication_policy = AuthTktAuthenticationPolicy('2G5HwRUunV3DM6kbEqd')
    authorization_policy = ACLAuthorizationPolicy()
    session_factory = UnencryptedCookieSessionFactoryConfig(
        'bSQBT3sMA46HNaqgrc')

    config = Configurator(settings=settings,
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy,
                          session_factory=session_factory,
                          root_factory=Root
                          )

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('auth', '/sign/{action}')
    config.scan()
    return config.make_wsgi_app()