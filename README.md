# ML-system-recommendation


## Must be you have docker for run containers
* install docker-descktop  [link](https://docs.docker.com/desktop/install/ubuntu/).

## Getting started
* At first you'll need to get the source code of the project. Do this by cloning the [ML-system-recommendation](https://github.com/ZOHSGroupe/ML-system-recommendation.git).
```
$ git clone https://github.com/ZOHSGroupe/ML-system-recommendation.git
$ cd ML-system-recommendation
```
* Create a virtual environment for this project and install dependencies
```
$ virtualenv .venv
```

* Activate the virtual environment
```
$ source .venv/bin/activate
```

* Install the dependencies
```
$ pip install -r requirements.txt
```

* add execution permission a file entrypoint.sh
```
$ chmod +x /script/entrypoint.sh
```
* install images and run containers on docker 
```
$ docker-compose up
```

# Docker containers documentaion
## System Architecture

![System Architecture](https://github.com/ZOHSGroupe/ML-system-recommendation/blob/main/imgs/conception.png)

* after run docker-compose 8 containers are created

Image|Container|Port|Volume|Role-Container
:-:|:-:|:-:|:-:|:-:
| [ml_system_recommendation](#)               | `system_recommendation` | `5000:5000`      | `./src:/app/src:ro` | Machine Learning System for Recommendations |
| [confluentinc/cp-zookeeper:7.4.0](#)        | `zookeeper`             | `2181:2181`      | N/A                 | Apache Zookeeper                            |
| [confluentinc/cp-server:7.4.0](#)           | `broker`                | `9092:9092`, `9101:9101` | N/A                 | Apache Kafka Broker                         |
| [confluentinc/cp-schema-registry:7.4.0](#) | `schema-registry`       | `8081:8081`      | N/A                 | Confluent Schema Registry                   |
| [confluentinc/cp-enterprise-control-center:7.4.0](#) | `control-center` | `9021:9021`      | N/A                 | Confluent Control Center                   |
| [apache/airflow:2.6.0-python3.9](#)          | `airflow`               | `8080:8080`      | N/A                 | Apache Airflow - Webserver                 |
| [apache/airflow:2.6.0-python3.9](#)          | `scheduler`             | N/A              | N/A                 | Apache Airflow - Scheduler                 |
| [postgres:14.0](#)                          | `postgres`              | N/A              | N/A                 | PostgreSQL Database for Airflow           |

* To stop the system, use the following command: 

```
$ docker-compose down
```

   This will stop and remove the containers.
## Container Roles

1. **Machine Learning System for Recommendations (`system_recommendation`):**
   - Provides machine learning-based recommendations.
   - Exposes API on port 5000.

2. **Apache Zookeeper (`zookeeper`):**
   - Manages distributed coordination for Kafka.

3. **Apache Kafka Broker (`broker`):**
   - Kafka message broker.
   - Exposes ports 9092 and 9101.

4. **Confluent Schema Registry (`schema-registry`):**
   - Manages Avro schemas for Kafka topics.
   - Exposes port 8081.

5. **Confluent Control Center (`control-center`):**
   - Web-based UI for monitoring and managing Kafka.
   - Exposes port 9021.

6. **Apache Airflow Webserver (`airflow`):**
   - Apache Airflow component serving the web interface.
   - Exposes port 8080.

7. **Apache Airflow Scheduler (`scheduler`):**
   - Apache Airflow component responsible for scheduling and executing tasks.

8. **PostgreSQL Database for Airflow (`postgres`):**
   - Database server for Apache Airflow.
