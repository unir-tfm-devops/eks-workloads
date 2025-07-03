resource "helm_release" "argocd_applications" {
  name  = "argocd-applications"
  chart = "../helm/argocd-applications"

  namespace        = var.namespace
  create_namespace = true

  values = [for valuesFile in fileset(path.module, "../environments/**/configuration/values.yaml") : 
    file(valuesFile)
  ]
}