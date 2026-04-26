# 🚀 Cloud DevOps Engineer Portfolio (AWS Production Simulation)

## 👤 Jonathan Hinds

Cloud / DevOps Engineer
GitHub: https://github.com/JonSec88

---

## 🧭 Summary

End-to-end AWS DevOps portfolio demonstrating real-world cloud engineering across infrastructure provisioning, deployment automation, containerisation, and production debugging workflows.

This system simulates a **production-style DevOps environment**, showcasing how modern cloud applications are built, deployed, and maintained.

---

## 🌐 Live Systems

### EC2 Application (Docker + CI/CD)

http://3.25.181.34

### S3 Static Website (Resume Site)

http://jonsec88-s3-site-83927-579986815910-ap-southeast-2-an.s3-website-ap-southeast-2.amazonaws.com/

---

## 🧱 System Architecture

### Backend Application (EC2 + Docker)

* Flask application containerised with Docker
* Deployed on AWS EC2 instance
* Exposed via public HTTP endpoint
* Automatically redeployed via CI/CD pipeline

---

### Static Website (S3)

* Resume website hosted on AWS S3
* Static HTML deployment
* Public access enabled
* Used as frontend portfolio layer

---

### CI/CD Pipeline (GitHub Actions)

* Automated deployment triggered on Git push
* Connects securely to EC2 via SSH
* Rebuilds Docker image and redeploys container
* Enables continuous delivery workflow

---

### Infrastructure as Code (Terraform)

* AWS infrastructure defined declaratively
* EC2 provisioning managed via Terraform
* Reproducible infrastructure deployment

---

## 🔧 Engineering Breakdown

### 1. EC2 Deployment (CI/CD Enabled)

Dockerised Flask application deployed to AWS EC2 via automated pipeline.

#### Evidence

* docs-task-2-break-fix/screenshots/ec2-live-app.png
* docs-task-2-break-fix/screenshots/cicd-success.png
* docs-task-2-break-fix/screenshots/docker-running.png

---

### 2. S3 Static Website

Static resume site hosted using AWS S3 website hosting.

#### Evidence

* docs-task-3-s3-website/screenshots/s3-upload.png
* docs-task-3-s3-website/screenshots/s3-bucket-overview.png
* docs-task-3-s3-website/screenshots/s3-hosting-enabled.png
* docs-task-3-s3-website/screenshots/s3-live-site.png

---

### 3. Networking & Incident Resolution (Break/Fix)

Real-world cloud debugging scenario involving misconfigured security groups.

#### Evidence

* docs-task-2-break-fix/screenshots/sg-no-http.png
* docs-task-2-break-fix/screenshots/sg-http-restored.png
* docs-task-2-break-fix/screenshots/broken-site.png

---

### 4. Infrastructure as Code (Terraform)

Infrastructure defined and managed using Terraform.

#### Files

* terraform/main.tf

---

## 📁 Repository Structure

```
app/                          # Flask Docker application
docs-task-2-break-fix/        # Networking + incident resolution
docs-task-3-s3-website/       # S3 deployment documentation
resume-site/                  # Static frontend site
terraform/                    # Infrastructure as Code
.github/workflows/            # CI/CD pipelines
docs/                         # Architecture diagrams
```

---

## 🧰 Tech Stack

### AWS

EC2 • S3

### DevOps Tools

Docker • Terraform • GitHub Actions

### Languages

Python • HTML • Bash

### OS

Linux (Amazon EC2)

---

## 🧠 Engineering Value

This project demonstrates:

✔ Real AWS infrastructure deployment
✔ CI/CD pipeline implementation with automated deployment
✔ Containerised application hosting using Docker
✔ Infrastructure as Code using Terraform
✔ Cloud networking debugging and incident resolution
✔ Deployment of both static and dynamic workloads

---

## 🔥 Outcome

This repository demonstrates practical DevOps engineering capability across:

* Cloud infrastructure deployment
* Continuous delivery pipelines
* Containerised applications
* Infrastructure automation
* Real-world debugging workflows

---

## 📌 Architecture Diagram

See:
docs/architecture.png

---

## 🚀 Next Steps (Planned Enhancements)

* Application Load Balancer (ALB)
* HTTPS (SSL/TLS) implementation
* Custom domain integration
* Multi-instance scalability

---

## 📎 Links

GitHub Repository:
https://github.com/JonSec88/cloud-portfolio-aws-devops

---

