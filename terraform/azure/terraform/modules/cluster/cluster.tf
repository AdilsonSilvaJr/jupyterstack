resource "azurerm_resource_group" "aks-jupyter" {
  name     = "aks-jupyter"
  location = var.location
}

resource "azurerm_kubernetes_cluster" "aks-jupyter" {
  name                = "aks-jupyter"
  location            = azurerm_resource_group.aks-jupyter.location
  resource_group_name = azurerm_resource_group.aks-jupyter.name
  dns_prefix          = "aks-jupyter"

  default_node_pool {
    name            = "default"
    node_count      = 1
    vm_size         = "Standard_D2AS_v5"
    type            = "VirtualMachineScaleSets"
    os_disk_size_gb = 250
  }

  service_principal {
    client_id     = var.serviceprinciple_id
    client_secret = var.serviceprinciple_key
  }

  linux_profile {
    admin_username = "azureuser"
    ssh_key {
      key_data = var.ssh_key
    }
  }

  network_profile {
    network_plugin    = "kubenet"
    load_balancer_sku = "standard"
  }


}

/*
resource "azurerm_kubernetes_cluster_node_pool" "monitoring" {
  name                  = "monitoring"
  kubernetes_cluster_id = azurerm_kubernetes_cluster.aks-jupyter.id
  vm_size               = "Standard_DS2_v2"
  node_count            = 1
  os_disk_size_gb       = 250
  os_type               = "Linux"
}

*/