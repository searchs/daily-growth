# Terraform: getting started

This guide was consolidated from the historical `in-few-steps` repository and modernised for safer day-to-day use.

## Prerequisites

- Terraform installed locally
- Access to a cloud account
- Provider credentials configured through the provider's normal credential chain, environment variables or an authenticated CLI profile

Avoid hard-coding access keys in Terraform files.

## Minimal AWS example

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "eu-west-2"
}

resource "aws_instance" "example" {
  ami           = "AMI_ID"
  instance_type = "t3.micro"
}
```

## Core workflow

```bash
terraform init
terraform fmt -check
terraform validate
terraform plan
terraform apply
```

Use `terraform plan` before `apply`, keep state out of source control, and prefer a managed remote backend for collaborative or production infrastructure.

## Notes

The original guide covered Terraform installation, provider configuration and basic resource provisioning. This version keeps that intent while removing inline credential examples and adding safer defaults.
