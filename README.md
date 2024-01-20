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

## Docker containers documentaion
**after run docker-compose 8 containers are created**

Image|Container|Port|Volume|Role-Container
:-:|:-:|:-:|:-:|:-:


