# Chapter05
# rabbitmq.py
from pika import BlockingConnection, BasicProperties

def message(topic, message):
    connection = BlockingConnection()
    try:
        channel = connection.channel()
        props = BasicProperties(content_type='text/plain', delivery_mode=1)
        channel.basic_publish('incoming', topic, message, props)
    finally:
        connection.close()

# race.34 메시지 전송
message('race.34', '새로운 대회(race) 정보!')

# training.12 메시지 전송
message('training.12', "새로운 훈련 계획(training plan) 정보!")