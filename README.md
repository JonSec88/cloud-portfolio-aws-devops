# 🚀 Cloud Portfolio DevOps Project (AWS + Docker + CI/CD)

## 📌 Overview
End-to-end DevOps project demonstrating real-world cloud deployment using AWS, Docker, and CI/CD automation.

This project shows production-style deployment of:
- A containerized web application on AWS EC2
- A static website hosted on AWS S3
- A CI/CD pipeline using GitHub Actions
- A structured multi-service repository

---

## 🌐 Live Deployments

### EC2 Application (Docker Container)
http://3.25.181.34

### S3 Static Resume Site
http://jonsec88-s3-site-83927-579986815910-ap-southeast-2-an.s3-website-ap-southeast-2.amazonaws.com/

---

## ⚙️ CI/CD Pipeline
Triggered on every push to `main`:

1. GitHub Actions runs
2. Docker image is built
3. Image is pushed to Docker Hub
4. EC2 instance pulls and runs updated container

---

## 🧰 Tech Stack
- AWS EC2 (Amazon Linux 2023)
- AWS S3 (Static hosting)
- Docker
- GitHub Actions (CI/CD)
- Python (Flask app)
- Linux administration
- Bash scripting

---

## 📁 Repository Structure
app/                      → Flask application  
resume-site/             → Static portfolio website  
terraform/               → Infrastructure as Code (AWS)  
docs-task-1-ec2/         → EC2 setup evidence  
docs-task-2-break-fix/   → Debugging logs  
docs-task-3-s3-website/  → S3 deployment  
docs-task-4-terraform/   → IaC setup  
docs-task-5-docker/     → Docker setup  
docs-task-6-cicd/       → CI/CD pipeline  
.github/workflows/      → GitHub Actions  

---

## 🧠 What This Demonstrates
- Real AWS cloud deployment (EC2 + S3)
- Containerized application architecture
- CI/CD automation pipeline
- Infrastructure as Code concepts
- Production-style repo organization

---

## 🔥 Outcome
This project simulates real DevOps engineering workflows used in production environments and demonstrates full-stack cloud deployment capability.

