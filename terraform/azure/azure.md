# Getting Started with AKS

## Azure CLI

```
# Run Azure CLI
docker run -it --rm -v ${PWD}:/work -w /work --entrypoint /bin/sh mcr.microsoft.com/azure-cli:latest

```

## Login to Azure

```
#login and follow prompts
az login 

TENTANT_ID=<your-tenant-id>

# view and select your subscription account

az account list -o table
SUBSCRIPTION=<id>
az account set --subscription $SUBSCRIPTION

```
## Create Service Principal

Kubernetes needs a service account to manage our Kubernetes cluster </br>
Lets create one! </br>

```

SERVICE_PRINCIPAL_JSON=$(az ad sp create-for-rbac --skip-assignment --name terraform-admin-aks-sp -o json)

#Keep the `appId` and `password` for later use!

SERVICE_PRINCIPAL=$(echo $SERVICE_PRINCIPAL_JSON | jq -r '.appId')
SERVICE_PRINCIPAL_SECRET=$(echo $SERVICE_PRINCIPAL_JSON | jq -r '.password')

#grant contributor role over the resource group to our service principal

az role assignment create --assignee $SERVICE_PRINCIPAL \
--scope "/subscriptions/$SUBSCRIPTION" \
--role Contributor

```
For extra reference you can also take a look at the Microsoft Docs: [here](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/aks/kubernetes-service-principal.md) </br>


# Terraform CLI
```
# Get Terraform

curl -o /tmp/terraform.zip -LO https://releases.hashicorp.com/terraform/1.1.8/terraform_1.1.8_linux_amd64.zip

unzip /tmp/terraform.zip

chmod +x terraform && mv terraform /usr/local/bin/

```

# Generate SSH key

```
ssh-keygen -t rsa -b 4096 -N "Jupyterteste@1234" -C "jupyter@teste.com" -q -f  ~/.ssh/id_rsa
SSH_KEY=$(cat ~/.ssh/id_rsa.pub)
```

## Terraform Azure Kubernetes Provider 

Documentation on all the Kubernetes fields for terraform [here](https://www.terraform.io/docs/providers/azurerm/r/kubernetes_cluster.html)

```
cd /work/azure/terraform/roots/app-ml

terraform init

terraform plan -var serviceprinciple_id=$SERVICE_PRINCIPAL \
    -var serviceprinciple_key="$SERVICE_PRINCIPAL_SECRET" \
    -var tenant_id=$TENTANT_ID \
    -var subscription_id=$SUBSCRIPTION \
    -var ssh_key="$SSH_KEY"

terraform apply -var serviceprinciple_id=$SERVICE_PRINCIPAL \
    -var serviceprinciple_key="$SERVICE_PRINCIPAL_SECRET" \
    -var tenant_id=$TENTANT_ID \
    -var subscription_id=$SUBSCRIPTION \
    -var ssh_key="$SSH_KEY"
```

# Get a kubeconfig for our cluster
```
# grab our AKS config
az aks get-credentials -n aks-jupyter -g aks-jupyter

cp ~/.kube/config /work/azure

## In your machine you have increment copy the content file "config" for ~/.kube/config

sudo cat config >> ~/.kube/config-Azure

## Get kubectl

curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod +x ./kubectl
mv ./kubectl /usr/local/bin/kubectl

kubectl get svc
```

# Clean all config

```
terraform destroy -var serviceprinciple_id=$SERVICE_PRINCIPAL \
    -var serviceprinciple_key="$SERVICE_PRINCIPAL_SECRET" \
    -var tenant_id=$TENTANT_ID \
    -var subscription_id=$SUBSCRIPTION \
    -var ssh_key="$SSH_KEY"
```