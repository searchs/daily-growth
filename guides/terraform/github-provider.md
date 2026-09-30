# Terraform with the GitHub provider

Consolidated from the historical `in-few-steps` repository and updated to avoid placing personal access tokens in Terraform source.

## Provider configuration

```hcl
terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  owner = "YOUR_GITHUB_LOGIN"
}
```

Authenticate outside the configuration, for example with the `GITHUB_TOKEN` environment variable:

```bash
export GITHUB_TOKEN="..."
terraform init
terraform plan
```

Use the narrowest token permissions required for the resources you manage.

## Create a repository

```hcl
resource "github_repository" "example" {
  name        = "example-repo"
  description = "Repository managed with Terraform"
  visibility  = "private"
}
```

Then run:

```bash
terraform fmt -check
terraform validate
terraform plan
terraform apply
```

For shared infrastructure, use remote Terraform state and review plans through CI before applying repository-level changes.
