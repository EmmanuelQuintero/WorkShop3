import pandas as pd
import json

from sklearn.model_selection import train_test_split

from Kafka.feature_selection import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean

import sys
sys.path.insert(0, '../')

def set_training_test(World_Happiness):
    X = World_Happiness.drop('Happiness_Score', axis = 1)
    y = World_Happiness['Happiness_Score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=29)
    return World_Happiness.loc[y_test.index]


with open('../keys.json', 'r') as json_file:
    config = json.load(json_file)
    user = config['user']
    password = config['password']
    host = config['host']
    port = config['port']
    database = config['database']

db_connection= f'postgresql://{user}:{password}@{host}:{port}/{database}'
engine = create_engine(db_connection)
Base = declarative_base()

def engine_creation():
    engine = create_engine(db_connection)
    return engine

def finish_engine(engine):
    engine.dispose()


def session_creation(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def create_table():

    engine = engine_creation()
    session_creation(engine)

    class World_Happiness(Base):
        __tablename__ = 'world_happiness'
        id = Column(Integer, primary_key=True)
        GDP_Per_Capita = Column(Float)
        Social_Support = Column(Float)
        Healthy_Life_Expectancy = Column(Float)
        Freedom = Column(Float)
        Government_Corruption_Perception = Column(Float)
        Generosity = Column(Float)
        Year = Column(Integer)
        Continent_Africa = Column(Integer)
        Continent_Asia = Column(Integer)
        Continent_Europe = Column(Integer)
        Continent_North_America = Column(Integer)
        Continent_Oceania = Column(Integer)
        Continent_South_America = Column(Integer)
        Happiness_Score = Column(Float)
        Happiness_Prediction = Column(Float)

    Base.metadata.create_all(engine)
    World_Happiness.__table__

def extract_db():
   
    query = "SELECT * FROM world_happiness"
    
    engine = engine_creation()
    
    session = session_creation(engine)
    
    World_Happiness = pd.read_sql(query, con=engine)

    #Cerramos la conexion a la db
    finish_engine(engine)

    return World_Happiness
