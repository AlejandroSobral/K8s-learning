# Description
Setting up a little K8s deployment in Digital Ocean.

------------------------------------

## Resources

Since this time deployment will occurr in Digital Ocean, no local stuff will happen. That's the reason why there is no Docker folder in here.
Images has been already pushed into the Docker Registry.
Remember to [sign up for 200 USD in credits](https://m.do.co/c/d67ad98bbcf8) for testing purposes.

<div style="display: flex; justify-content: center;">
  <div style="margin: 0 10px;">
    <img src="Misc/AWS.png" alt="docker-logo" width="200" />
  </div>
  <div style="margin: 0 100px;">
    <img src="Misc/DO.png" alt="aws-logo" width="170" />
  </div>
</div>

## Connect to DigitalOcean

Go to Home->Kubernetes->Create a Kubernetes Cluster

Settings:
- 2 nodes
- 12$ month node-plan

Create Cluster. Wait.

Once provisining is done, look for "Download Config file"

Setup the configuration to interact with the Cloud:
```bash
export KUBECONFIG={PATH/TO/FILE}
```
We aware that if you have open terminals, this configuration will not be applied automatically.

Test connection:
```bash
kubectl get nodes
```

<b>Connection is now working</b>

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

Once testing is complete, scale down:

### 1st try: Kill all
```bash
    kubectl delete all --all
```

### 2nd try:
```bash
    kubectl delete -f web-deploy.yaml -f web-services.yaml -f db-deploy.yaml -f db-service.yaml -f db-pvc.yaml
```