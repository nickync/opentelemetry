import pika

# connection = pika.BlockingConnection( pika.ConnectionParameters('localhost') )
# channel = connection.channel()

# channel.queue_declare(queue='hello')

# channel.basic_publish(exchange='', routing_key='hello', body = 'Hello World')
# print( " [x] sent  'hello world'")
# channel.basic_publish(exchange='', routing_key='hello', body = 'Why is it working')

# channel.basic_publish(exchange='', routing_key='hello', body = 'New message')

class MQ():

    def __init__(self, host='localhost', key='hello', queue = 'hello'):
        self.host = host
        self.connection = pika.BlockingConnection( pika.ConnectionParameters(self.host) )
        self.routing_key = key
        self.queue = queue

    def channel(self):
        return self.connection.channel()

    def send(self, body = '', exchange = '' ):
        channel = self.channel()
        channel.queue_declare(queue = self.queue)
        channel.basic_publish( exchange = exchange, routing_key = self.routing_key, body = body )
        print( " [x] sent  %s" % body)

