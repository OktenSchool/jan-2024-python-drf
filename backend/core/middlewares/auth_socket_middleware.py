from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware

from core.services.jwt_service import JWTService, SocketToken


@database_sync_to_async
def get_user(token):
    try:
        return JWTService.verify_token(token, SocketToken)
    except (Exception,):
        return None


class AuthSocketMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        token = dict(
            [item.split('=') for item in scope['query_string'].decode('utf-8').split('&') if item]
        ).get('token', None)
        scope['user'] = await get_user(token) if token else None
        return await super().__call__(scope, receive, send)
