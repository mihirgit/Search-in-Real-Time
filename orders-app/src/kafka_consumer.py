

import base64
import requests
from kafka import KafkaConsumer

from config import BOOTSTRAP_SERVER, INDEX, TOPIC, GROUP_ID, ZINCSEARCH_SERVER


# create consumer to consume latest msgs from given topic and auto-commit offsets
consumer = KafkaConsumer(TOPIC, group_id=GROUP_ID, bootstrap_servers=BOOTSTRAP_SERVER,
                         auto_offset_reset='earliest')


# login
user = "admin"
password = "admin"

base64_encoded_credentials = base64.b64encode(bytes(user + ":" + password, "utf-8")).decode("utf-8")
headers = {"Content-type": "application/json",
           "Authorization": "Basic " + base64_encoded_credentials }
ZINC_URL = ZINCSEARCH_SERVER + "api/" + INDEX + "/_doc"

for message in consumer:
    print(f"{message.topic}:{message.partition}:{message.offset}: key={message.key.decode('utf-8')} "
          f"value={message.value.decode('utf-8')}")

    data = message.value.decode("utf-8")

    # post to server
    requests.post(ZINC_URL, headers=headers, data=data)
