````md id="single_block_final"
# 🚀 Cloud DevOps Portfolio — AWS Multi-Architecture Engineering Project

## 👤 Jonathan Hinds
Cloud / DevOps Engineer Portfolio  
GitHub: https://github.com/JonSec88

---

# 🎯 EXECUTIVE SUMMARY

Production AWS DevOps portfolio demonstrating:

EC2 Docker deployment  
S3 static hosting  
Terraform Infrastructure as Code  
GitHub Actions CI/CD  
Lambda + API Gateway + DynamoDB serverless stack  
Real AWS debugging and networking fixes  

---

# 🌐 LIVE SYSTEMS

EC2: http://3.25.181.34  
S3: http://jonsec88-s3-site-83927-579986815910-ap-southeast-2-an.s3-website-ap-southeast-2.amazonaws.com/

---

# 🏗 ARCHITECTURE

```mermaid
flowchart LR
User[User]
EC2[EC2 Docker App]
S3[S3 Static Site]
APIGW[API Gateway]
Lambda[Lambda]
DDB[DynamoDB]
GH[GitHub Actions CI/CD]
TF[Terraform IaC]

User --> EC2
User --> S3
User --> APIGW
APIGW --> Lambda --> DDB
GH --> EC2
TF --> EC2
TF --> S3
TF --> Lambda
TF --> DDB
````

---

# ⚙️ CI/CD PIPELINE

GitHub push triggers:
Docker build → EC2 deployment update

---

# 📁 REPOSITORY STRUCTURE

app/ → Flask Docker application
terraform/ → AWS Infrastructure as Code
resume-site/ → S3 static website
docs-task-1-ec2/ → EC2 evidence
docs-task-2-break-fix/ → Networking fixes
docs-task-3-s3-website/ → S3 deployment
docs-task-4-terraform/ → Terraform setup
docs-task-5-docker/ → Docker deployment
docs-task-6-cicd/ → CI/CD pipeline
.github/workflows/ → GitHub Actions automation

---

# 📸 EVIDENCE MAP

EC2 → docs-task-1-ec2/screenshots
S3 → docs-task-3-s3-website/screenshots
Terraform → docs-task-4-terraform/screenshots
Docker → docs-task-5-docker/screenshots
CI/CD → docs-task-6-cicd/screenshots

---

# 🧰 TECH STACK

AWS: EC2, S3, Lambda, API Gateway, DynamoDB
DevOps: Docker, GitHub Actions, Terraform
Languages: Python, Bash
OS: Linux (Amazon EC2)

---

# 🔥 OUTCOME

End-to-end DevOps portfolio demonstrating real AWS infrastructure, automation, CI/CD, and production deployment workflows.

```
```

