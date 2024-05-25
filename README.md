# Workshop 3 World Happiness Prediction and Data Streaming

# Overview

Welcome, this project is a project that covers the prediction of world happiness through a selection of features and implementation of Apache Kafka to stream the data and subsequently consume, predict and load into PostgreSQL

Made by Emmanuel Quintero

# WorkShop WorkFlow

![image](https://github.com/EmmanuelQuintero/WorkShop3/assets/111546312/57d1b8ec-205f-4cce-8745-cb6873089235)

# Tools used

- **Python**
- **Jupyter Notebooks**
- **PostgreSQL 15**
- **SQLAlchemy**
- **Pandas**
- **Matplotlib**
- **Docker Desktop**
- **Ploty**
- **Apache Kafka**
- **Scikit Learn**

# About the data

The datasets used are from world happiness during 2015 to 2019, some with different columns and others with similar columns

- Dataset 2015.csv
- Dataset 2016.csv
- Dataset 2017.csv
- Dataset 2018.csv
- Dataset 2019.csv

# Project Features

- Docker Implementation: The Kafka part is located in a Docker container, thus facilitating its operation

- Exploratory data analysis (EDA): In notebooks 001_EDA , there are the EDA carried out on each data set, there are also the transformations that will be applied later.

- Features Selection: Inside the Kafka folder there is a file called features_selection, inside this file the functions are made by renaming and selecting only the characteristics chosen to carry out the analysis and prediction of world happiness, which are subsequently integrated into the producer.

- Kafka: For Kafka, Docker is run and once it is turned on, the topic to which the messages will be sent is created and the consumer and producer are run from the terminal.

- Prediction and Data loading in PostgreSQL: Once all the data has reached the consumer, he is responsible for applying the predictive model and saving the data in the database.

- Model Metrics: Finally, the model metrics are evaluated from Jupyter notebook #2 with metrics such as the R^2 score, the mean square error and some graphs.

# Requirements

- Install Python 3.11
- Install PostgreSQL 15
- Install Docker Desktop
- Install kafka-python

# Database Configuration

In order to create the tables in postgres, I recommend creating a config folder with a file in json format

This is keys.json

```json
{
    "host": "your_postgres_host",
    "port": "your_postgres_port",
    "database": "database_name",
    "user": "your_postgres_user",
    "password": "your_postgres_password"
}
```

### Note: The creation of the folder and file is done once the project is cloned, as we will do below

# To Run this project

1. Clone the project:

```bash
  git clone https://github.com/emmanuelqp/WorkShop3.git
```

2. Go to the project directory

```bash
cd WorkShop3
```

### Note: Once you are at the root of the project you can create the config folder with the mentioned files

3. Create virtual environment for Python:

```bash
python -m venv venv
```

4. Activate virtual environment:

```bash
.\.venv\Scripts\activate
```

5. Install libraries:

```bash
pip install requirements.txt
```

or

```bash
pip install -r requirements.txt
```

Once the dependencies are installed, I recommend you start with the part of notebook 001 to understand the EDA and the transformations along with the selection of characteristics applied to the datasets.

6. Run Docker

```bash
docker compose up
```

6.1 Topic Creation:
Once docker is already running, open a console in vscode and enter the following command:

```bash
docker exec -it kafka-workshop-3 bash                                               
```

Once inside the docker console, run the following command:

```bash
kafka-topics --bootstrap-server localhost:9092 --create --topic world_happiness_ws3                                             
```

Now you can do the following command:

```bash
exit                                           
```

Once the topic has been created, you can open two parallel consoles to run the producer and the consumer

6.2 Kafka Producer and Consumer:

Once both terminals are open, make sure you are within the project path. Once this is verified, do the following command in both terminals:

```bash
cd Kafka                                      
```

Then you can run the producer and the consumer in each one.

```bash
python kafka_producer.py                                   
```

And

```bash
python kafka_consumer.py                                    
```

#### NOTE: I recommend that you allow a few seconds (15 or 20) to launch the consumer since the producer takes a little time to start sending the data due to the process it does before

Once the consumer has finished, it will wait 15 seconds waiting for another message, if it does not arrive, it will continue with the process. That is, Prediction and loading in Postgres

7. Model Metrics

Finally, you can go to notebook 002 where there will be the metrics of the model that was used to predict the data saved in the database and your database should look like this:

![imagen_2024-05-24_232409819](https://github.com/EmmanuelQuintero/WorkShop3/assets/111546312/833c2660-75c3-4d56-b090-ec9a3d673280)
That is, with the columns chosen to predict and additionally the column to be predicted and the column already predicted

## Thanks

If you have any problems, do not hesitate to contact me through GitHub

Thanks for watching and visiting my repository! 😊⭐
