
provider "kubernetes" {
  host                   = var.host
  client_certificate     = var.client_certificate
  client_key             = var.client_key
  cluster_ca_certificate = var.cluster_ca_certificate
}


resource "kubernetes_deployment" "example" {
  metadata {
    name = var.k8s_name
    labels = {
      app = var.k8s_label
    }
  }

  spec {
    replicas = var.k8s_replicas

    selector {
      match_labels = {
        app = var.k8s_label
      }
    }

    template {
      metadata {
        labels = {
          app = var.k8s_label
        }
      }

      spec {
        container {
          image = "${var.k8s_path_image}:${var.k8s_image_version}"
          name  = var.k8s_name

          resources {
            requests = {
              memory = "2048Mi"
              cpu    = "250m"
            }
            limits = {
              memory = "4096Mi"
              cpu    = "500m"
            }
          }
          security_context {
            privileged = true
          }
          port {
            container_port = var.k8s_container_port
            name           = "http"
            protocol       = "TCP"
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "example" {
  metadata {
    name = "${var.k8s_name}-service"
  }
  spec {
    selector = {
      app = var.k8s_label
    }
    port {
      port        = var.k8s_pod_port
      target_port = var.k8s_container_port
    }

    type = var.k8s_type
  }
}