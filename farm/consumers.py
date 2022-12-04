from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
class chatwith(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })
        await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })


    async def websocket_receive(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })

    async def websocket_disconnect(self, event):
        pass