import json
from datetime import datetime, timedelta

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Customer, Teller


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
        tp = text_data_json["mtype"]

        if tp == "checkin":
            now = datetime.now()
            teller = Teller.objects.get(id=self.teller)
            customer = Customer()
            customer.teller = teller
            customer.name = name
            self.expired_date = now + \
                timedelta(minutes=(teller.wait_time +
                          teller.get_estimated_time()))
            customer.save()
            async_to_sync(self.channel_layer.group_send)(
                self.teller_name,
                {
                    'message': "New customer checked in: <b>%s</b>" % name,
                    "code": customer.code,
                    "mtype": tp,
                    "type": "customer_message"
                }
            )
        else:
            async_to_sync(self.channel_layer.group_send)(
                self.teller_name,
                {
                    'message': text_data_json["message"],
                    "mtype": tp,
                    "sender": name,
                    "type": "customer_message"
                }
            )

    def customer_message(self, event):
        message = event['message']
        tp = event["mtype"]
        print(tp)
        if tp == "checkin":
            data = {
                'code': event["code"],
                "message": message,
                "mtype": tp
            }
            self.send(text_data=json.dumps(data))
        else:
            data = {
                'message': message,
                "sender": event["sender"],
                "mtype": tp
            }
            self.send(text_data=json.dumps(data))
