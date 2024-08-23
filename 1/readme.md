# Description

Second mini-project. Stablish a second container creating a tiny MongoDB database.
DB interaction through the web as well.

---------------------------------------

### Bash commands for usage

#### Change directory to 0 location


```bash
  cd to Docker/0
```


#### Build image
```bash
    docker build -t flask1:v1 .
```


#### Run Image
```bash
    docker run -p 5001:5000 flask1:v1
```

#### Connect to web-server

```bash
    curl localhost:5001
```