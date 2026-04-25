# 🚀 Cloud DevOps Portfolio — AWS Multi-Architecture Project

## 👤 Jonathan Hinds
Cloud / DevOps Engineer Portfolio

GitHub: https://github.com/JonSec88

---

# 📌 Project Overview

This repository demonstrates a complete AWS-based DevOps engineering workflow including:

- EC2 infrastructure deployment
- Serverless architecture (S3 + Lambda + API Gateway + DynamoDB)
- Infrastructure as Code using Terraform
- Containerisation using Docker
- CI/CD automation using GitHub Actions
- Real-world debugging, networking, and deployment fixes
- Production-style repository structure across multiple services

This project simulates real-world cloud engineering workflows used in DevOps environments.

---

# 🌐 Live Deployments

## 🖥 EC2 Application
http://3.25.181.34

- Linux EC2 server
- Docker container deployment
- Public access via Security Groups

---

## ☁️ S3 Static Website
http://jonsec88-s3-site-83927-579986815910-ap-southeast-2-an.s3-website-ap-southeast-2.amazonaws.com/

- Static website hosted on S3
- Serverless frontend deployment
- Highly available architecture

---

# ⚙️ CI/CD Pipeline (GitHub Actions)

- Code pushed to GitHub triggers pipeline
- Docker image built automatically
- Deployment pushed to EC2
- Fully automated delivery workflow

---

# 🧠 System Architecture

## EC2 Layer
- Dockerised Flask application
- Linux server hosting

## S3 Layer
- Static resume website hosting

## Serverless Layer
- API Gateway → Lambda → DynamoDB

## CI/CD Layer
- GitHub Actions automation pipeline

## Infrastructure Layer
- Terraform manages AWS resources

---

# 🏗 Architecture Diagram

flowchart LR

User[User / Browser]

EC2[EC2 Instance<br/>Docker App<br/>3.25.181.34]

S3[S3 Static Website<br/>Resume Site]

APIGW[API Gateway]

Lambda[AWS Lambda<br/>Visitor Counter]

DDB[DynamoDB]

GH[GitHub Actions CI/CD]

TF[Terraform IaC]

User --> EC2
User --> S3
User --> APIGW

APIGW --> Lambda --> DDB

GH --> EC2
GH --> Docker[Docker Build]

TF --> EC2
TF --> S3
TF --> Lambda
TF --> DDB

---

# 🧰 Tech Stack

AWS (EC2, S3, Lambda, API Gateway, DynamoDB)
Docker • GitHub Actions • Terraform
Python • Flask • Linux • Bash

---

# 📁 Repository Structure

app/ → Flask Docker application
terraform/ → Infrastructure as Code
resume-site/ → S3 static website
docs-task-1-ec2/ → EC2 evidence
docs-task-2-break-fix/ → Networking fixes
docs-task-3-s3-website/ → S3 deployment
docs-task-4-terraform/ → Terraform infrastructure
docs-task-5-docker/ → Docker deployment
docs-task-6-cicd/ → CI/CD pipeline

---

# 📸 Evidence Map

EC2 → docs-task-1-ec2/screenshots  
S3 → docs-task-3-s3-website/screenshots  
Terraform → docs-task-4-terraform/screenshots  
Docker → docs-task-5-docker/screenshots  
CI/CD → docs-task-6-cicd/screenshots  

---

# 🧠 Engineering Summary

✔ Multi-service AWS architecture  
✔ Infrastructure as Code (Terraform)  
✔ Containerised deployment (Docker)  
✔ CI/CD automation (GitHub Actions)  
✔ Cloud networking and debugging  
✔ Production-grade repo structure  

---

# 🔥 Outcome

Production-ready DevOps portfolio demonstrating real AWS infrastructure, automation, and deployment workflows.
