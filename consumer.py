import pika
import json

# startapp 명령어로 만든 파일이 아닌 곳에서 Django에 등록된 모델이나 기능을 사용하려면 이렇게 환경 설정을 해줘야 한다.
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()

from config.constants import RABBITMQ_URL
from order.models import Order

# pika로 RabbitMQ 연결
params = pika.URLParameters(RABBITMQ_URL)
# Channel을 만들기 위한 RabbitMQ와의 Connection 생성
connection = pika.BlockingConnection(params)
# Connection의 채널을 생성
channel = connection.channel()

# 'order' 라는 이름으로 된 큐를 선언
channel.queue_declare(queue='order')


def callback(ch, method, properties, body):
    print('---------- Received in order ----------')

    print("properties: ", properties)

    if properties.content_type == 'order_delivery_finished':
        id = json.loads(body)

        print("order id: ", id)

        order = Order.objects.get(id=id)

        order.delivery_finish = True

        order.save()

        print('order delivery finished')


# 'order'로 만들어진 큐에 들어온 메시지를 구독 on_message_callback 으로 메시지가 들어올 때 처리할 callback 함수를 정의
channel.basic_consume(queue='order', on_message_callback=callback, auto_ack=True)

print('Started consuming')

# 채널 구독
channel.start_consuming()

# 채널 종료
channel.close()
