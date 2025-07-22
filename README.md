# EKS Workloads

This repository manages ArgoCD applications via Terraform and stores the workload configurations for applications deployed on EKS clusters using Helm charts.

## 📋 Overview

This repository serves as a GitOps-managed configuration store for EKS workloads, providing:

- **ArgoCD Application Management**: Terraform-managed ArgoCD applications for automated deployment
- **Helm Chart Storage**: Environment-specific Helm charts for application workloads
- **Multi-Environment Support**: Separate configurations for test and production environments
- **Automated Deployment**: GitOps workflow with automated sync and self-healing capabilities

## 📁 Repository Structure

```
eks-workloads/
├── environments/           # Environment-specific configurations
│   ├── test/              # Test environment
│   │   ├── applications/  # Application Helm charts
│   │   └── configuration/ # ArgoCD applications values
│   └── prod/              # Production environment
│       ├── applications/  # Application Helm charts
│       └── configuration/ # ArgoCD applications values
├── helm/                  # Helm chart definitions
│   └── argocd-applications/ # ArgoCD applications chart
├── terraform/             # Terraform configuration
├── scripts/               # Utility scripts
└── README.md
```

## 🏗️ Architecture

### 🔄 ArgoCD Application Management
- **Terraform Deployment**: ArgoCD applications are deployed using Terraform with Helm provider
- **Helm Chart**: The `helm/argocd-applications` chart defines ArgoCD Application resources
- **Environment Separation**: Separate ArgoCD application instances for test and production environments

### ⚙️ Workload Management
- **Helm Charts**: Each application has its own Helm chart in the environments directory
- **ArgoCD Application Values**: Environment-specific values for ArgoCD applications are stored in `environments/{env}/configuration/values.yaml`
- **GitOps Workflow**: Changes to charts trigger automatic deployments via ArgoCD

## 🚀 Getting Started

### 📋 Prerequisites
- Terraform
- Helm
- Access to EKS clusters
- ArgoCD installed on target clusters

### 🚀 Deployment

1. **Configure Terraform Backend**:
   ```bash
   cd terraform
   terraform init
   ```

2. **Deploy ArgoCD Applications**:
   ```bash
   terraform plan
   terraform apply
   ```

3. **Verify Deployment**:
   - Check ArgoCD UI for application status
   - Verify applications are syncing correctly

## 🔄 Development Workflow

### ➕ Adding a New Application

The process for adding a new application involves using an issue template and automated workflows:

1. **Create an Issue**: Open a new issue using the application creation template
   - The template will prompt for application details (name, repository, Helm chart, etc.)
   - Fill in all required information about the new application

2. **Automated PR Creation**: The `create-app-pr` workflow will automatically:
   - Create a PR in this repository (`eks-workloads`) with:
     - New application Helm chart in `environments/{env}/applications/{app-name}/`
     - Updated ArgoCD applications configuration in `environments/{env}/configuration/values.yaml`
   - Create a PR in `unir-tfm-devops/infra-rds` repository to:
     - Provision a new database in the RDS instance for the application
     - Configure database access and permissions

3. **Review and Merge**: 
   - Review both PRs to ensure configurations are correct
   - Merge the PRs in the appropriate order
   - ArgoCD will automatically detect and deploy the new application

### 🔧 Updating Application Configuration

1. Modify the appropriate `values.yaml` file in the application's Helm chart directory
2. Commit and push changes
3. ArgoCD will automatically sync the changes

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Test in the test environment first
4. Submit a pull request
5. Ensure ArgoCD applications sync successfully
