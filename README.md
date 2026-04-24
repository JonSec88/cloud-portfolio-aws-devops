# Jon Hinds | Cloud DevOps Portfolio | AWS End-to-End Deployment

## 📌 Overview

This project demonstrates a complete DevOps workflow from development to production using AWS, Docker, and CI/CD automation.

It is designed to reflect real-world engineering practices, focusing on delivering and running cloud-native applications.

---

## 🏗️ Architecture

### System 1 — CI/CD Container Deployment

GitHub → GitHub Actions → Docker Build → Docker Hub → AWS EC2 → Live Application

### System 2 — Serverless Cloud Resume

User → S3 Static Website → API Gateway → Lambda → DynamoDB

---

## 🌐 Live Projects

### 🔹 Flask Application — Docker + AWS EC2

Containerised Flask application deployed to AWS EC2 using Docker, built and delivered via CI/CD.

Live Application:  
👉 http://3.25.181.34

Key Capabilities Demonstrated:
- Automated Docker image build and push via CI/CD  
- Container deployment on EC2  
- Network configuration and port exposure  
- Public-facing application hosting  

---

### 🔹 Cloud Resume — Serverless AWS Architecture

Static resume website with a dynamic visitor counter powered by serverless AWS services.

Live Website:  
👉 http://YOUR-S3-ENDPOINT

Key Capabilities Demonstrated:
- Static site hosting via S3  
- API-driven backend using Lambda + API Gateway  
- Persistent visitor tracking with DynamoDB  
- Lightweight serverless architecture  

---

## ⚙️ Tech Stack

- AWS (EC2, S3, Lambda, API Gateway, DynamoDB)
- Docker
- Terraform
- GitHub Actions
- Python (Flask)

---

## 📂 Project Structure

cloud-portfolio-aws-devops

├─ app                → Flask API (Dockerised application)  
├─ terraform          → Infrastructure as Code (EC2 provisioning)  
├─ .github/workflows  → CI/CD pipelines  
├─ resume-site        → S3 static site + API integration  
├─ screenshots        → Deployment proof  
│  
└─ README.md          → Project documentation  

---

## 📸 Proof of Work

### CI/CD Pipeline  
pipeline

### Docker Container Running on EC2  
ec2

### Live Application Output  
app

---

## 🔧 Key Features

- End-to-end CI/CD pipeline from GitHub to production  
- Dockerised application deployment on AWS EC2  
- Infrastructure provisioning using Terraform  
- Serverless backend with Lambda and DynamoDB  
- Publicly accessible cloud-hosted applications  

---

## 📈 What This Demonstrates

- Ability to design and deliver complete cloud systems  
- Understanding of DevOps workflows and automation  
- Practical experience with AWS production services  
- Deployment, networking, and infrastructure management  

---

## 👤 Author

Jon Hinds  
Aspiring Cloud / DevOps Enginee
