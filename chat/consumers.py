import json
from channels.generic.websocket import WebsocketConsumer
from chat.views import respond_to_websockets
from django.contrib.auth import get_user_model
from users.models import UserClickCount

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass
    def add_user_count(self,json):
            user_name=self.scope['user'].username
            User=get_user_model()
            user_instance=User.objects.filter(username=user_name).first()
            click_count_instance = UserClickCount.objects.filter(type=json['text'],user=user_instance,joke=json['joke']['text']).first()
            if not click_count_instance:
                click_count_instance = UserClickCount.objects.create(type=json['text'],user=user_instance,joke=json['joke']['text'])
            click_count_instance.count = (click_count_instance.count or 0) + 1
            click_count_instance.save()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # message = text_data_json['message']
        if 'text' in text_data:

            text_data_json['joke']=respond_to_websockets(text_data_json)
            self.add_user_count(text_data_json)

        self.send(text_data=json.dumps(
            text_data_json
        ))
