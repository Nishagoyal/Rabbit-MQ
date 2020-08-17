#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials(username='virtual', password='MkkI2785****')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='52.156.70.14',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello d!'")
connection.close()
