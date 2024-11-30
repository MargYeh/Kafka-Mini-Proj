# Kafka Mini Project: Building a Streaming Fraud Detection System with Kafka and Python

This project uses Kafka and Python to build a real-time fraud detection system. The generator creates and sends transactions with random accounts and amounts to simulate the transactions being sent from a bank. The detector recieves the transactions sent through the Kafka network, determines whether they are fraudulent or not, and then sends them to the appropiate topics. 

## How to run
Create the network which both the Kafka cluster and the generator/detector will run on:
```
docker network create kafka-network
```

Start the local Kafka cluster with:
```
docker-compose -f docker-compose.kafka.yml up -d
```

To confirm it is running, ```docker ps``` should show the following containers:
![image](https://github.com/user-attachments/assets/3aeebe26-f3a6-4428-81ba-077ee0eb0ea4)

Logs can also be examined using 
```
docker-compose -f docker-compose.kafka.yml logs broker
```

## Testing the Generator
```
docker-compose build generator
docker-compose up -d
docker-compose logs -f generator
```
![image](https://github.com/user-attachments/assets/4712332a-ca94-47c3-b4ab-1afc5d480c67)

## Final results, showing differentiation into legit and fraud topics
Results from topic streaming.transactions.legit:
```
docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.legit
```
![image](https://github.com/user-attachments/assets/d846fe19-f7d2-4a88-9b04-3440fac488eb)

Results from topic streaming.transactions.fraud:
```
docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.legit
```
![image](https://github.com/user-attachments/assets/511c3dba-9ed2-4b61-bcbd-7aeefcf2017d)


