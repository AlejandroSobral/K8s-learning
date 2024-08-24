# Description

Second mini-project. Stablish a second container creating a tiny MongoDB database.
DB interaction through the web as well.

---------------------------------------

### Bash commands for usage

#### Change directory to 0 location


```bash
  cd to Docker/1
```


#### Build image
```bash
    docker build -t mongodb:v1 .
```


#### Run Image
```bash
    docker run -p 5002:27017 -v /vol:/data/db --cpus=1 --memory=512m -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=firstmongo --name tiny-mongodb mongodb:v1 

```

#### Connect to web-server

```bash
    curl localhost:5002
```

#### Connect info

```bash
mongosh mongodb://localhost:5002

mongosh mongodb://mongoadmin:firstmongo@localhost:5002
```