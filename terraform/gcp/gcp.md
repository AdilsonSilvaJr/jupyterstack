# Google cloud - GCS and GKE

## Google Cloud CLI

```
# Run Google Cloud CLI
docker run -it --rm -v ${PWD}:/work -w /work --entrypoint /bin/bash google/cloud-sdk:latest

cd ./gcp
```
## Login to GCloud
```
#login and follow prompts
gcloud auth login

gcloud projects list

gcloud projects create gke-jupyter

gcloud config set project gke-jupyter

```
# Enable APIs for your Project on Google cloud console.
- Compute engine API

- Kubernetes engine API

# Terraform CLI
```
# Install Terraform
curl -o /tmp/terraform.zip -LO https://releases.hashicorp.com/terraform/1.1.8/terraform_1.1.8_linux_amd64.zip

unzip /tmp/terraform.zip

chmod +x terraform && mv terraform /usr/local/bin/

## Terraform GCS Prerequisites
cd /work/terraform/roots/prerequisites

terraform init

terraform plan

terraform apply

## Terraform GCS buckets
cd /work/terraform/roots/storage

terraform init

terraform plan

terraform apply

```

## Create our cluster

```
# Extra commands
## See all machine types
gcloud compute machine-types list > machine-types.log

## Get k8s versions for your zone
gcloud container get-server-config --zone us-central1

# Install kubectl
```
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl

chmod +x ./kubectl

mv ./kubectl /usr/local/bin/kubectl
```

## Get a kubeconfig for our cluster
gcloud container clusters get-credentials plexiform-dream-347014-gke --region us-central1

## Copy config in your machine
cp ~/.kube/config /work
```

# Aplly k8s .yaml
```
cd /work

kubectl apply -f k8s/deployment.yaml
```
# Clean cluster
```
cd /work/terraform/roots/app-ml

terraform destroy
```