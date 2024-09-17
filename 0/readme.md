# Description
Setting up a little K8s deployment using MiniKube locally.




------------------------------------

## Resources

<div style="display: flex; justify-content: center;">
  <div style="margin: 0 10px;">
    <img src="Misc/Minikube.png" alt="MiniKube" width="200" />
  </div>
</div>

<details>
<summary> Install Mini-Kube (Ubuntu)</summary>

```bash
https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download

- curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
- sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```
</details>

---------------------------------------
<details>
<summary> Install kubectl</summary>

```bash
https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

- curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
- curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
- echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
```
</details>


<details>
<summary> Install kubectl</summary>

```bash
https://kind.sigs.k8s.io/docs/user/quick-start/

- [ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.24.0/kind-linux-amd64
- chmod +x ./kind
- sudo mv ./kind /usr/local/bin/kind
```
</details>





------------------------------------

### Utils
Take into consideration using the MongoDB extension for VisualStudio code.

### Bash commands for usage



#### Build images

Go to the Docker folder and check for the Web/Db folders.

```bash
    docker build -t mongodb:v1.1 .
```

```bash
    docker build -t tiny-web:1.19 .
```

#### Run different environment configurations

Allow minikube to have docker env
```bash
    eval $(minikube docker-env)
```

```bash
    minikube tunnel
```



```bash
    kubectl apply -f web-deploy.yaml
```
```bash
    kubectl apply -f web-services.yaml
```
```bash
    kubectl apply -f db-deploy.yaml
```

Db service is only for testing/dev purposes. DB Shouldn't be accesible from out the cluster, only by web.

```bash
    kubectl apply -f db-service.yaml
```
```bash
    kubectl apply -f db-pvc.yaml
```


```bash
    docker-compose down ## Set all down
```