import sys
sys.path.insert(0, '../')

from json import loads

import joblib

from kafka import KafkaConsumer

import pandas as pd 

from Kafka.kafka_functions import *
from kafka import KafkaConsumer

model = joblib.load('../Model/rforest_regressor.pkl')

print('Iniciando consumer')

def kafka_consumer():
    consumer = KafkaConsumer(
    'world_happiness_ws3',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda message: json.loads(message.decode('utf-8')),
    consumer_timeout_ms=15000
    )

    World_Happiness_messages = []

    for message in consumer:
        data = message.value
        print('data received from producer in offset', message.offset) 
        World_Happiness_messages.append(data)
    return World_Happiness_messages


list_of_messages = kafka_consumer()
#print(list_of_messages)
list_of_messages = [json.loads(item) for item in list_of_messages]
World_Happiness= pd.DataFrame(list_of_messages)

prediction = model.predict(World_Happiness.drop(columns=['Happiness_Score'], axis = 1))
World_Happiness['Happiness_Prediction'] = prediction

create_table()

World_Happiness.to_sql('world_happiness', engine, if_exists='append', index=False)
print('Data saved to PostgreSQL', World_Happiness)




