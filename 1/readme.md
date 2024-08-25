# Description

Second mini-project. Stablish a second container creating a tiny MongoDB database.
DB interaction through the web as well.

---------------------------------------

### Utils
Take into consideration using the MongoDB extension for VisualStudio code.

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
    docker run -p 5002:27017 -v /vol:/data/db --cpus=1 --memory=512m --name tiny-mongodb mongodb:v1 

```

#### Connect to web-server

```bash
    curl localhost:5002
```

#### Connect to instance

```bash
mongosh mongodb://localhost:5002
```

#### Try first insert

```bash

const database = 'FirstDB';
const collection = 'CollectOne';

// Create a new database.
use(database);

// Create a new collection.
db.createCollection(collection);

db.getCollection('CollectOne').insertOne({
    "name": "AleSb",
    "role": "Professional Student"
});

// Find documents where the name is "AleSb"
db.CollectOne.find({name: "AleSb"}).pretty()

```

### Try stop and run the container again

``` bash

docker stop tiny-mongodb
docker start tiny-mongodb
```

