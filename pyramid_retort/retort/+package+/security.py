from pyramid.security import (
    Allow,
    Everyone,
    Authenticated,
)

# Permissions example
class Root(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'add'),
    ]

    def __init__(self, request):
        self.request = request
