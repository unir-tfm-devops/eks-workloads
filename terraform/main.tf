resource "helm_release" "argocd_applications_test" {
  name  = "argocd-applications-test"
  chart = "../helm/argocd-applications"

  namespace        = var.namespace
  create_namespace = true

  values = [
    file("${path.module}/../environments/test/configuration/values.yaml")
  ]
}

resource "helm_release" "argocd_applications_prod" {
  name  = "argocd-applications-prod"
  chart = "../helm/argocd-applications"

  namespace        = var.namespace
  create_namespace = true

  values = [
    file("${path.module}/../environments/prod/configuration/values.yaml")
  ]
}