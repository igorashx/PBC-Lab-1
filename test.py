import os
from uuid import uuid4

from kafka import KafkaConsumer, KafkaProducer
from pymongo import MongoClient
from pyspark.sql import SparkSession


KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb://mongodb:27017")

def main():
    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("BigDataLab")
        .getOrCreate()
    )

    print("Spark:", spark.version)

    mongo = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    producer = None
    consumer = None
    topic = f"codespaces-smoke-{uuid4().hex}"
    try:
        mongo.admin.command("ping")
        smoke_collection = mongo.bigdata["_codespaces_smoke"]
        smoke_id = uuid4().hex
        smoke_collection.insert_one({"_id": smoke_id, "ok": True})
        assert smoke_collection.find_one({"_id": smoke_id})["ok"] is True
        smoke_collection.delete_one({"_id": smoke_id})
        print("MongoDB: ping and write/read/delete passed")

        producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
        message = uuid4().hex.encode("ascii")
        producer.send(topic, value=message).get(timeout=20)
        producer.flush()

        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            group_id=f"codespaces-smoke-{uuid4().hex}",
            auto_offset_reset="earliest",
            enable_auto_commit=False,
            consumer_timeout_ms=10000,
        )
        received = next(iter(consumer), None)
        assert received is not None and received.value == message, "Kafka round-trip failed."
        print("Kafka: produce/consume passed")

        assert spark.createDataFrame([(1,)], ["value"]).count() == 1
        print("Spark: local execution passed")
    finally:
        if consumer is not None:
            consumer.close()
        if producer is not None:
            producer.close()
        mongo.close()
        spark.stop()


if __name__ == "__main__":
    main()