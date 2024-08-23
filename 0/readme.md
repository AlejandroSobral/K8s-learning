# Description

First mini-project. Just stablish a tiny python image and setup a Flask that returns hello-world when connecting to its root webpage.
Intended to get the basics of Dockerfile.

---------------------------------------

### Bash commands for usage

#### Change directory to 0 location


```bash
  cd to Docker/0
```


#### Build image
```bash
    docker build -t flask0:v1 .
```


#### Run Image
```bash
    docker run -p 5001:5000 --cpus=1 --memory=64m --name tiny-flask flask0:v1
```

#### Connect to web-server

Can easily be test wheter using a web-browser or a bash by executing:

```bash
    curl localhost:5001
```