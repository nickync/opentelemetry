import pika

connection = pika.BlockingConnection( pika.ConnectionParameters('localhost') )
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body = 'Hello World')
print( " [x] sent  'hello world'")
channel.basic_publish(exchange='', routing_key='hello', body = 'Why is it working')

channel.basic_publish(exchange='', routing_key='hello', body = 'New message')