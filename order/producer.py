import pika
import json
from config.constants import RABBITMQ_URL

# pika로 RabbitMQ 연결
params = pika.URLParameters(RABBITMQ_URL)
# Channel을 만들기 위한 RabbitMQ와의 Connection 생성
connection = pika.BlockingConnection(params)
# Connection의 채널을 생성
channel = connection.channel()


# 채널에 전송할 메시지를 만들어내는 함수 method는 식별자라고 생각하면 된다.
# 예를 들어, Shop을 만들어내는 API를 호출하고 그 API에서 이 publish()를 호출할 때 'shop_created'라는 식별자를 던져줘서 어떤 식별자인지 인식한다.
# body는 넘겨받을 데이터. 예를 들어, Shop을 만들어내는 API라면 Shop을 만들기 위해 필요한 데이터들이 넘어올 것
def publish(method, body):

    properties = pika.BasicProperties(method)

    # 큐가 'owner'로 된 곳으로 메시지를 보낸다.
    channel.basic_publish(exchange='', routing_key='owner', body=json.dumps(body), properties=properties)

