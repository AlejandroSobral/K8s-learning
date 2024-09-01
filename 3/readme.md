# Description
This time we are producing the same working environment but using a Dockercompose file instead of two Dockerfiles.
It can be called "First Orchestation" approach.

---------------------------------------

### Utils
Take into consideration using the MongoDB extension for VisualStudio code.

### Bash commands for usage

#### Change directory to 0 location


```bash
  cd to Docker/3
```
#### Fresh start

Before running it for the first time, prune networks, containers and volumes.

```bash
    docker system prune -a --volumes -f
```


#### Build images
```bash
    docker build -t mongodb:v1.1 .
```

```bash
    docker build -t tiny-web:v1.181 .
```

#### Run both containers

Check for existing volumes, networks and stuff once compose has been ran.

```bash
    docker volume ls
```

```bash
docker network ls
```

```bash
    docker-compose up -d
```