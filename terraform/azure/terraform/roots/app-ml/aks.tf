module "cluster" {
  source               = "../../modules/cluster/"
  serviceprinciple_id  = var.serviceprinciple_id
  serviceprinciple_key = var.serviceprinciple_key
  ssh_key              = var.ssh_key
  location             = var.location
  kubernetes_version   = var.kubernetes_version

}

module "k8s-ml" {
  source                 = "../../modules/k8s/"
  host                   = module.cluster.host
  client_certificate     = base64decode(module.cluster.client_certificate)
  client_key             = base64decode(module.cluster.client_key)
  cluster_ca_certificate = base64decode(module.cluster.cluster_ca_certificate)
  k8s_name               = "api-ml"
  k8s_label              = "api-ml"
  k8s_replicas           = "1"
  k8s_path_image         = "adilsonsilvajr/diabetes-ml"
  k8s_image_version      = "latest"
  k8s_container_port     = "80"
  k8s_pod_port           = "3000"
  k8s_type               = "NodePort"
}

module "k8s-app" {
  source                 = "../../modules/k8s/"
  host                   = module.cluster.host
  client_certificate     = base64decode(module.cluster.client_certificate)
  client_key             = base64decode(module.cluster.client_key)
  cluster_ca_certificate = base64decode(module.cluster.cluster_ca_certificate)
  k8s_name               = "app"
  k8s_label              = "app"
  k8s_replicas           = "1"
  k8s_path_image         = "adilsonsilvajr/diabetes-app"
  k8s_image_version      = "latest"
  k8s_container_port     = "8501"
  k8s_pod_port           = "80"
  k8s_type               = "LoadBalancer"
}