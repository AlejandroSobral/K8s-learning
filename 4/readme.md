# Description
Docker compose and env management.

---------------------------------------

### Utils
Take into consideration using the MongoDB extension for VisualStudio code.

### Bash commands for usage

#### Change directory to 0 location


```bash
  cd to Docker/4
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

#### Run different environment configurations


Check that accesing the database on localhost:5002 is possible on this env. Resources are limited.
```bash
    docker-compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d
```

Check that accesing the database on localhost:5002 is NOT ossible on this env. Resources are enough for heavier workloads.
```bash
    docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```


```bash
    docker-compose down ## Set all down
```