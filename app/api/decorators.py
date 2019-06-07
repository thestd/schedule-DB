from functools import wraps
from tornado.options import options


def auth_required(f):

    def _request_auth(handler):
        handler.set_header('WWW-Authenticate', 'Basic realm=JSL')
        handler.set_status(401)
        handler.finish()
        return False

    @wraps(f)
    async def new_f(*args):
        handler = args[0]
        auth_header = handler.request.headers.get('Authorization')
        if auth_header is None:
            _request_auth(handler)
        if not auth_header.startswith("Token "):
            _request_auth(handler)
        else:
            token = auth_header[6:]
            if token == options.auth_token:
                await f(*args)
            else:
                _request_auth(handler)
    return new_f