from channels.generic.websocket import AsyncWebsocketConsumer
import json
from datetime import datetime
from asgiref.sync import async_to_sync
import json
import asyncio
import random

SYMBOLS = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB', 'TSLA', 'NVDA']

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
        hour=datetime.now().strftime("%H:%M")

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'time':hour
            }
        )
        
    async def chat_message(self,event):
          messagge=event['message']
          hour=event['time']
          await self.send(text_data=json.dumps({'message':messagge,'time':hour}))



class StocksConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'stock_data'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        # Start updating stock data every second
        await self.update_stock_data()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        pass

    async def update_stock_data(self):
        while True:
            secons=random.randint(2,4)
            stock_data = generate_fake_stock_data()
            await self.send_stock_data(stock_data)
            await asyncio.sleep(secons)  # Update every second

    async def send_stock_data(self, stock_data):
        await self.send(text_data=json.dumps(stock_data))

def generate_fake_stock_data():
    symbol = random.choice(SYMBOLS)  # Select a random symbol from the list
    price = round(random.uniform(100, 200), 2)  # Generate a random price between 100 and 200
    volume = random.randint(1000, 5000)  # Generate a random volume between 1000 and 5000
    return {'symbol': symbol, 'price': price, 'volume': volume}
