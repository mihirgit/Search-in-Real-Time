# Search-in-Real-Time
Using Redpanda and ZincSearch to perform searching in real-time


### Working example:
![ZincSearch UI](https://github.com/mihirgit/Search-in-Real-Time/blob/main/ZincSearch.png)

##

### Search with query for sales value < 500: 
![ZincSearch with Query](https://github.com/mihirgit/Search-in-Real-Time/blob/main/ZincSearch_withQuery.png)

## orders-app directory:

 - config.py: Configurations for Redpanda and ZincSearch servers
 - orders.py: Generate sample data in JSON format for producers and consumers. Consists of order_id and sales_value
 - kafka_producer.py: Generates data in format required by Kafka producer at regular intervals
 - kafka_consumer.py: Consumer data from the producer, and additionally pushes the data to ZincSearch via api endpoints


## Commands used:
 - Docker
   - $docker-compose up -d
     - Build and run docker image and start container based on configurations listed in docker-compose.yaml file
   - $docker ps
     - Check if services are up and running    
   - $docker exec -ti redpanda bash
     - Connect to Redpanda container   
 - Redpanda
   - $rpk topic create orders
     - Create topic named orders, which will be used by ZincSearch as an index 
   - $rpk topic list
     - List topics in redpanda container

##

### Instructions to run:
 1. Setup redpanda and ZincSearch containers with Docker with help of commands listed above
 2. Run kafka_producer.py file
 3. While kafka_producer.py is running, open up a separate terminal and run kafka_consumer.py
 4. See the respective data being printed in the terminal
 5. Go to ZincSearch UI in browser at _http://localhost:4080_
 6. Select orders in select index tab
 7. Run desired queries in search query tab

### Applications
 - This application demonstrates that the Redpanda streaming platform can be used to perform real-time search operations with minimal overhead
 - We can harness the capabilities of Kafka and go further
 - Redpanda has lower latency and is developer-friendly too.

