import pika
from datetime import datetime 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

message = str(datetime.now()) + ' Hello World!'

channel.basic_publish(exchange='', routing_key='hello', body=message)
print(" [x] Sent ",message)
connection.close()
