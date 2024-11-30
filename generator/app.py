from kafka import KafkaProducer
import os
from time import sleep
from transactions import create_random_transaction
import json

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = float(os.environ.get("TRANSACTIONS_PER_SECOND"))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND

if __name__ == "__main__":
    while True:
        try:
            producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER_URL,
            #Encode values as JSON
            value_serializer = lambda value: json.dumps(value).encode(),
            )
            break
        except Exception as e:
            print(f'failed to connect to broker: {e}')
            sleep(5)

    while True:
        transaction: dict = create_random_transaction()
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        print(transaction) #for debugging
        sleep(SLEEP_TIME)
