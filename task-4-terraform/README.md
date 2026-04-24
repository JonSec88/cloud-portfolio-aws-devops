# Task 4 — Terraform EC2 Infrastructure (Infrastructure as Code)

## Summary
Provisioned an AWS EC2 instance using Terraform to demonstrate Infrastructure as Code (IaC) for repeatable cloud deployment.

---

## Objective
Replace manual AWS console provisioning with declarative infrastructure defined in code.

---

## Architecture

Terraform Configuration
→ AWS Provider (ap-southeast-2)
→ EC2 Instance (t3.micro)
→ Running Linux Server

---

## Tools Used
- Terraform
- AWS EC2
- AWS CLI
- Git / GitHub

---

## Implementation

### 1. Initialise Terraform
```bash
terraform init
