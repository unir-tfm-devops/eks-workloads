variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "namespace" {
  type        = string
  description = "Namespace to install the applications"
  default     = "argocd"
}

variable "eks_cluster_name" {
  type        = string
  description = "EKS cluster name"
  default     = "unir-tfm-eks-cluster"
}