resource "helm_release" "argocd_applications" {
  name       = "argocd-applications"
  chart      = "../helm/argocd-applications"

  namespace  = var.namespace
  create_namespace = true

  values = [
    file("${path.module}/../environments/test/configuration/values.yaml")
  ]
}