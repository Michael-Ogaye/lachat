from channels.generic.websocket import AsyncWebsocketConsumer
import json

class Chatconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name=f'lachat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,self.channel_name
        )

        await self.accept()
    
    async  def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):

        text_data_jso=json.loads(text_data)
        message=text_data_jso['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )
        
    async def chat_message(self,event):
          messagge=event['message']
          await self.send(text_data=json.dumps({'message':messagge}))