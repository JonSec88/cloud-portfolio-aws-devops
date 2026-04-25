# 🚀 Cloud DevOps Engineering Portfolio (AWS Production Simulation)

## 👤 Jonathan Hinds
Cloud / DevOps Engineer  
GitHub: https://github.com/JonSec88

---

# 🧭 EXECUTIVE SUMMARY

This repository demonstrates a complete AWS-based DevOps system simulating production engineering workflows across:

- Infrastructure provisioning (Terraform)
- CI/CD automation (GitHub Actions)
- Containerised deployment (Docker on EC2)
- Serverless backend (Lambda + API Gateway + DynamoDB)
- Static website hosting (S3)
- Real cloud debugging and network fixes

---

# 🌐 LIVE SYSTEMS

### EC2 Application (Docker)
http://3.25.181.34

### S3 Static Resume Site
http://jonsec88-s3-site-83927-579986815910-ap-southeast-2-an.s3-website-ap-southeast-2.amazonaws.com/

---

# ⚙️ CI/CD PIPELINE

Trigger: GitHub Push to main

Flow:
Code → GitHub Actions → Docker Build → EC2 Deployment

Key capabilities:
- Automated build pipeline
- Container image creation
- Remote EC2 update deployment

---

# 🧱 INFRASTRUCTURE AS CODE (TERRAFORM)

Provisioned AWS resources:

- EC2 instance (application host)
- S3 bucket (static website hosting)
- Lambda function (serverless compute)
- API Gateway (routing layer)
- DynamoDB (persistent storage)

---

# 📦 APPLICATION ARCHITECTURE

System consists of:

### EC2 Layer
- Linux server (Amazon EC2)
- Dockerised Flask application
- Public web endpoint

### Serverless Layer
- API Gateway routing requests
- Lambda processing logic
- DynamoDB data persistence

### Static Layer
- S3-hosted resume website
- Public static asset delivery

---

# 📁 REPOSITORY STRUCTURE

app/ → Flask Docker application  
terraform/ → AWS infrastructure (IaC)  
resume-site/ → S3 static website  
docs-task-1-ec2/ → EC2 deployment evidence  
docs-task-2-break-fix/ → Networking + debugging  
docs-task-3-s3-website/ → S3 hosting evidence  
docs-task-4-terraform/ → Infrastructure setup  
docs-task-5-docker/ → Containerisation  
docs-task-6-cicd/ → CI/CD pipeline  

---

# 📸 EVIDENCE (PROOF OF WORK)

Each module includes real deployment evidence:

- EC2 provisioning + SSH access + runtime verification  
- Security Group debugging and restoration  
- S3 bucket configuration and public hosting  
- Terraform apply outputs  
- Docker build + container execution logs  
- GitHub Actions pipeline runs  

All evidence stored under `/docs-task-* /screenshots`

---

# 🧰 TECH STACK

AWS:
EC2 • S3 • Lambda • API Gateway • DynamoDB

DevOps:
Terraform • Docker • GitHub Actions

Languages:
Python • Bash

OS:
Linux (Amazon EC2)

---

# 🧠 ENGINEERING HIGHLIGHTS

✔ Multi-service AWS architecture design  
✔ Infrastructure as Code implementation (Terraform)  
✔ CI/CD automation pipeline (GitHub Actions)  
✔ Containerised deployment (Docker + EC2)  
✔ Serverless integration (Lambda + API Gateway)  
✔ Real-world cloud debugging and fixes  

---

# 🔥 OUTCOME

This project demonstrates production-grade DevOps capability across AWS infrastructure, automation pipelines, and modern cloud deployment patterns.
