# 🚀 Cloud DevOps Engineer Portfolio (AWS Production Simulation)

## 👤 Jonathan Hinds
DevOps / Cloud Engineer  
GitHub: https://github.com/JonSec88

---

# 🧭 SUMMARY

End-to-end AWS DevOps portfolio demonstrating real-world cloud engineering across infrastructure provisioning, deployment automation, containerisation, and debugging workflows.

This system demonstrates hands-on engineering across:

- EC2 deployment and Linux server configuration
- Docker containerised application deployment
- AWS S3 static website hosting
- Terraform Infrastructure as Code
- CI/CD automation via GitHub Actions (if included in repo workflow)
- Real-world cloud troubleshooting and network fixes

---

# 🌐 LIVE SYSTEMS

### EC2 Application (Docker / Web Service)
http://3.25.181.34

### S3 Static Website (Resume Site)
http://jonsec88-s3-site-83927-579986815910-ap-southeast-2-an.s3-website-ap-southeast-2.amazonaws.com/

---

# 🧱 SYSTEM BREAKDOWN (REAL IMPLEMENTATION)

## 1. EC2 + Docker Application
- Flask application containerised with Docker
- Linux EC2 instance hosting runtime service
- Public HTTP endpoint exposed via security groups

Files:
- app/app.py
- app/Dockerfile

---

## 2. AWS S3 STATIC WEBSITE
- Static HTML resume site
- Public S3 bucket hosting
- Website hosting configuration enabled

Files:
- resume-site/index.html
- docs-task-3-s3-website/

---

## 3. NETWORKING + DEBUGGING (BREAK/FIX ENGINEERING)
- Security group misconfiguration diagnosis
- HTTP access restoration
- Real cloud incident debugging workflow

Evidence:
- docs-task-2-break-fix/screenshots/
  - sg-no-http.png
  - sg-http-restored.png
  - broken-site.png
  - site-working.png

---

## 4. INFRASTRUCTURE AS CODE (TERRAFORM)
- AWS infrastructure defined as reproducible code
- EC2 provisioning via main.tf
- State-based infrastructure management

Files:
- terraform/main.tf

---

# 📁 REPOSITORY STRUCTURE

app/ → Flask Docker application  
docs-task-2-break-fix/ → Networking + incident resolution  
docs-task-3-s3-website/ → Static S3 deployment  
resume-site/ → Frontend HTML site  
terraform/ → Infrastructure as Code  
.gitignore → Repo hygiene  

---

# 📸 ENGINEERING EVIDENCE (REAL PROOF)

## EC2 Deployment
- Application running on EC2 instance
- Docker container execution verified

## Break/Fix Engineering
- Security group misconfiguration resolved
- HTTP access restored successfully
- Live site recovery demonstrated

## S3 Hosting
- Bucket configuration completed
- Static site deployment verified
- Public access confirmed

## Terraform
- Infrastructure defined via code (main.tf)
- Reproducible AWS provisioning approach

---

# 🧰 TECH STACK

### AWS
EC2 • S3

### DevOps Tools
Terraform • Docker

### Languages
Python • HTML • Bash

### OS
Linux (Amazon EC2)

---

# 🧠 ENGINEERING VALUE

This project demonstrates:

✔ Real AWS infrastructure deployment  
✔ Containerised application hosting  
✔ Cloud networking debugging (real failure + fix cycle)  
✔ Infrastructure as Code implementation  
✔ Static + dynamic workload deployment  
✔ Production-style repository structure  

---

# 🔥 OUTCOME

This repository demonstrates practical DevOps engineering capability across AWS infrastructure, containerisation, infrastructure automation, and real-world cloud troubleshooting workflows.
