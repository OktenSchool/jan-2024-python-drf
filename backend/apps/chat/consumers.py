from channels.db import database_sync_to_async
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer


class ChatConsumer(GenericAsyncAPIConsumer):
    def __init__(self, *args, **kwargs):
        self.room_name = None
        self.user_name = None
        super().__init__(*args, **kwargs)

    async def connect(self):
        if not self.scope['user']:
            return await self.close()
        await self.accept()
        self.room_name = self.scope['url_route']['kwargs']['room']
        self.user_name = await self.get_profile_name()
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name,
        )
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'sender',
                'message': f'{self.user_name} connected to chat'
            }
        )

    @action()
    async def send_message(self, data, request_id, action):
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'sender',
                'message': data,
                'user': self.user_name,
                'id': request_id
            }
        )

    async def sender(self, data):
        await self.send_json(data)

    @database_sync_to_async
    def get_profile_name(self):
        user = self.scope['user']
        return user.profile.name
