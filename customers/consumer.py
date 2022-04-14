import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class CustomerConsumer(WebsocketConsumer):
    def connect(self):
        self.teller = self.scope['url_route']['kwargs']['pk']
        self.teller_name = 'teller_%s' % self.teller

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.teller_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.teller_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        name = text_data_json["name"]
        async_to_sync(self.channel_layer.group_send)(
            self.teller_name,
            {
                'type': 'customer_message',
                'message': "New customer %s" % name
            }
        )

    def customer_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
