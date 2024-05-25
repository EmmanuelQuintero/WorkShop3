import pandas as pd
import json

import sys
sys.path.insert(0, '../')

from Kafka.feature_selection import*
from Kafka.kafka_functions import*

from sklearn.model_selection import train_test_split
import time

from kafka import KafkaProducer



def etl():
    dt_2015 = pd.read_csv('../Data/2015.csv')
    dt_2016 = pd.read_csv('../Data/2016.csv')
    dt_2017 = pd.read_csv('../Data/2017.csv')
    dt_2018 = pd.read_csv('../Data/2018.csv')
    dt_2019 = pd.read_csv('../Data/2019.csv')

    dt_2015 = rename_15_16_columns(dt_2015, 2015)
    dt_2016 = rename_15_16_columns(dt_2016, 2016)
    dt_2017 = rename_17_columns(dt_2017, 2017)
    dt_2018 = rename_18_19_columns(dt_2018, 2018)
    dt_2019 = rename_18_19_columns(dt_2019, 2019)

    World_Happiness= pd.concat([dt_2015, dt_2016, dt_2017, dt_2018, dt_2019], ignore_index=True)
    World_Happiness = World_Happiness.dropna()
    World_Happiness['Continent'] = World_Happiness['Country'].apply(get_continent)
    World_Happiness = get_continent_dummies(World_Happiness)
    World_Happiness = World_Happiness.astype({'Continent_Africa':'int','Continent_Asia': 'int', 'Continent_Europe': 'int', 'Continent_North America': 'int', 'Continent_Oceania': 'int', 'Continent_South America': 'int'})
    World_Happiness = rename_america(World_Happiness)
    World_Happiness = delete_columns(World_Happiness)
    
    return World_Happiness


def kafka_producer(World_Happiness):
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda m: json.dumps(m).encode('utf-8'),
        )

    for index, row in World_Happiness.iterrows():
        World_Happiness_to_dict = row.to_dict()
        data = json.dumps(World_Happiness_to_dict)
        producer.send('world_happiness_ws3', value=data)
        print('Message sent to Kafka')
        time.sleep(0.2)


if __name__ == '__main__':
    # ETL
    World_Happiness = etl()
    # Split data
    World_Happiness = set_training_test(World_Happiness)

    kafka_producer(World_Happiness)
    


