from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from yaml import serialize

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarConsumer(GenericAsyncAPIConsumer):
    def __init__(self, *args, **kwargs):
        self.room_name = 'cars'
        super().__init__(*args, **kwargs)

    async def connect(self):
        if not self.scope['user']:
            return await self.close()
        await self.accept()
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name,
        )

    @model_observer(CarModel, serializer_class=CarSerializer)
    async def cars_activity(self, message, action, subscribing_request_ids, **kwargs):
        for request_id in subscribing_request_ids:
            await self.reply(data=message, action=action, request_id=request_id)

    @action()
    async def subscribe_to_car_activity(self, request_id, **kwargs):
        await self.cars_activity.subscribe(request_id=request_id)
