# Chapter05
# standalone_pika.py
import pika
import requests
from requests.exceptions import ReadTimeout, ConnectionError

FLASK_ENDPOINT = 'http://localhost:5000/event'

def on_message(channel, method_frame, header_frame, body):
    message = {'delivery_tag': method_frame.delivery_tag,
                'message': body.decode('utf-8')}

    try:
        res = requests.post(FLASK_ENDPOINT, json=message,
                            timeout=1.)
    except (ReadTimeout, ConnectionError):
        print('Failed to connect to %s.' % FLASK_ENDPOINT)
        # 재접속 기능 구현 필요
        return

    if res.status_code == 200:
        print('플라스크로 메시지 전달 성공!')
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)

connection = pika.BlockingConnection()
channel = connection.channel()
channel.basic_consume(on_message, queue='race')
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()
