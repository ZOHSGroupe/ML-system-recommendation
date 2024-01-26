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

# setup Kubeflow in azure with use Charmed Kubeflow for run data pipeline
1. **create instence in azure Linux (ubuntu 22.04) Has at least 4 cores, 32GB RAM and 50GB of disk space available.:**
2. **For Charmed Kubeflow run this command conecte a instence open locle terminal:**
   ```
   $ ssh -i ~/.ssh/myKey.pem -D 9999
   ```
3. **Set the SOCKS host to: 127.0.0.1 and port 9999**
4. **Install MicroK8s**
   ```
   $ sudo snap install microk8s --classic --channel=1.26/stable
   ```
5. **Now it’s time to configure it, to get it ready for Kubeflow**
   ```
   $ sudo usermod -a -G microk8s $USER
   $ newgrp microk8s
   ```
6. **we need to grant ownership of any kubectl configuration files to the user running kubectl. Run this command to do that:**
   ```
   $ sudo chown -f -R $USER ~/.kube
   ```
7. **Enable MicroK8s addons**
   ```
   $ microk8s enable dns hostpath-storage ingress metallb:10.64.140.43-10.64.140.49
   ```
8. **we can do is to ask MicroK8s for a status output. Run the following command:**
   ```
   $ microk8s status
   ```
9. **Install Juju**
   ```
   $ sudo snap install juju --classic --channel=3.1/stable
   ```
10. **On some machines there might be a missing folder which is required for juju to run correctly. Because of this please make sure to create this folder with:**
    ```
    $ mkdir -p ~/.local/share
    ```
11. **As a next step we can configure microk8s to work properly with juju by running:**
    ```
    $ microk8s config | juju add-k8s my-k8s --client
    ```
12. **Now, run the following command to deploy a Juju controller to the Kubernetes we set up with MicroK8s:**
    ```
    $ juju bootstrap my-k8s uk8sx
    ```
13. **we’ll need to add a model for Kubeflow to the controller**
    ```
    $ juju add-model kubeflow
    ```
14. **Before deploying kubflow, run these commands:**
    ```
    $ sudo sysctl fs.inotify.max_user_instances=1280
    $ sudo sysctl fs.inotify.max_user_watches=655360
    ```
15. **Deploy Charmed Kubeflow usually this will take somewhere between 15 minutes and 1 hour.**
    ```
    $ juju deploy kubeflow --trust  --channel=1.8/stable
    ```
16. **status of all the components of Juju**
    ```
    $ juju status
    ```
17. **If you see your oidc-gatekeeper/0 unit in juju status output in waiting state with**
    **oidc-gatekeeper/0*         waiting      idle   10.1.121.241                 Waiting for pod startup to complete.**
    **You can reconfigure the public-url configuration for the charm with following commands**
    ```
    $ juju config oidc-gatekeeper public-url=""
    $ juju config oidc-gatekeeper public-url=http://10.64.140.43.nip.io
    ```
18. **To see if this is the issue, manually check the state of the pods in the cluster by running**
    ```
    $ microk8s kubectl get po -n kubeflow
    ```
## Configure Dashboard Access

19. **this command to check the IP address of the Istio ingress gateway load balancer, which is the entry point for our entire bundle:**
    ```
    $ microk8s kubectl -n kubeflow get svc istio-ingressgateway-workload -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
    ```
20. **configure the bundle a bit so that it supports authentication and authorization.**
    ```
    $ juju config dex-auth public-url=http://10.64.140.43.nip.io
    $ juju config oidc-gatekeeper public-url=http://10.64.140.43.nip.io
    ```
21. **enable simple authentication, and set a username and password for your Kubeflow deployment:**
    ```
    $ juju config dex-auth static-username=admin
    $ juju config dex-auth static-password=admin
    ```
## finaly Open a browser and visit the following URL:
    ```
   $ http://10.64.140.43.nip.io
    ```





    












    
   
