from pyspark.sql import SparkSession
from pymongo import MongoClient
from kafka import KafkaProducer

def main():
    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("BigDataLab")
        .getOrCreate()
    )

    print("Spark:", spark.version)

    mongo = MongoClient("mongodb://mongodb:27017")

    mongo.admin.command("ping")

    print("MongoDB: connected")

    producer = KafkaProducer(
        bootstrap_servers="kafka:9092"
    )

    print("Kafka: connected")

    producer.close()
    mongo.close()
    spark.stop()


if __name__ == "__main__":
    main()