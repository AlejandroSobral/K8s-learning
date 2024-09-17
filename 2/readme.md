# Description
Setting up a little K8s deployment using EKS (Elastic Kubernetes Service AWS)


------------------------------------

## Resources

Since this time deployment will occurr in AWS, be aware that an account will be required. And since it is intended to use the free-tier elements, I'm not responsible for any charges that can occurr as result of using AWS.

<div style="display: flex; justify-content: center;">
  <div style="margin: 0 10px;">
    <img src="Misc/Docker_logo.png" alt="docker-logo" width="200" />
  </div>
  <div style="margin: 0 100px;">
    <img src="Misc/AWS.png" alt="aws-logo" width="200" />
  </div>
</div>


## Pre-setup

Login into AWS Management Console -> IAM Roles -> Create new IAM User with EKS admin permissions at least.
Then download the credentials by hovering the user name on top right -> Security Credentials -> Create access key -> Download CSV.

<details>
<summary> Install aws cli & eksctl (Ubuntu) </summary>

```bash
apt-get install awscli
```

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```


```bash
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp  && \
sudo mv /tmp/eksctl /usr/local/bin
```

</details>

```bash
aws configure
```

Test AWS user cfg by running

```bash
aws sts get-caller-identity
```

Create the cluster itself:

```bash
eksctl create cluster \
  --name small-deploy \
  --version 1.26 \
  --region us-west-1 \
  --nodegroup-name small-nodegroup \
  --node-type t2.small \
  --nodes 1 \
  --nodes-min 1 \
  --nodes-max 2 \
  --managed

```

This is stating that it will be located at region us-west-1; that the cluster name will be "my-cluster"; that the worker nodes will be "t2.micro" one; the min and max amount of nodes (It will autoscale automatically).
This last step can take some minutes, be patient.

Allow kubectl to interact with your Cloud cluster.

```bash
aws eks --region us-west-1 update-kubeconfig --name small-deploy
```

Amazon EBS CSI Driver:
Enable Amazon Elastic Block Storage (EBS) within your cluster:

```bash
eksctl create addon --name aws-ebs-csi-driver --cluster small-deploy --region us-west-1
```



Get <NodeInstanceRole> by executing the following command:

```bash
aws eks describe-nodegroup --cluster-name small-deploy --nodegroup-name small-nodegroup --region us-west-1 | grep nodeRole | awk -F'role/' '{print $2}' | awk -F'"' '{print $1}'
```

Apply the policy to ec2 instance for the current role, to be able to create ec2 volumes. This is for the persistent volume for the mongoDB pod.
```bash
aws iam put-role-policy --role-name <NodeInstanceRole> --policy-name EKS-EBS-Policy --policy-document file://ec2-volume-policy.json
```

------------------------------------

Start the deployment:


```bash
    kubectl apply -f db-deploy.yaml
```

```bash
    kubectl apply -f db-service.yaml
```
```bash
    kubectl apply -f db-pvc.yaml
```
```bash
    kubectl apply -f web-deploy.yaml
```
```bash
    kubectl apply -f web-services.yaml
```

Get the loadbalancer IP to be able to connect to the front-end. Look for external-ip.

```bash
kubectl get svc
```

Then connect to that ip at home or at /items to test the DB out.

------------------------------------

Once testing is complete, scale down:

### 1st try: Kill all
```bash
    kubectl delete all --all --all-namespaces
```

### 2nd try:
```bash
    kubectl delete -f web-deploy.yaml -f web-services.yaml -f db-deploy.yaml -f db-service.yaml -f db-pvc.yaml
```