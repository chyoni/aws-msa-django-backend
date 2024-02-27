import pika
from config.constants import RABBITMQ_URL

params = pika.URLParameters(RABBITMQ_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='order')

def callback(ch, method, properties, body):

    print('Received in order')

    print(body)

channel.basic_consume(queue='order', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()