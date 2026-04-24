# Jon Hinds | Cloud DevOps Portfolio | AWS End-to-End Deployment 

## 📌 Overview

This project demonstrates a complete DevOps pipeline from code to production using AWS and Docker.

It showcases:

- Infrastructure as Code (Terraform)
- Containerisation (Docker)
- CI/CD (GitHub Actions)
- Cloud Deployment (AWS EC2 & S3)
- Serverless Architecture (Lambda, API Gateway, DynamoDB)

---

## 🏗️ Architecture

### System 1 — CI/CD Deployment Pipeline

GitHub → GitHub Actions → Docker Build → Docker Hub → EC2 → Live Application

### System 2 — Serverless Resume Website

User → S3 Website → API Gateway → Lambda → DynamoDB

---

## 🌐 Live Projects

### 🔹 Flask App (Docker + EC2)
👉 http://3.25.181.34
Public IPv4 address copied


### 🔹 Cloud Resume Website
👉 http://YOUR-S3-WEBSITE-ENDPOINT

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
│
├─ app                → Flask API (Dockerised application)
├─ terraform          → AWS infrastructure (EC2 via IaC)
├─ .github/workflows  → CI/CD pipelines (build & push Docker image)
├─ resume-site        → S3 static site + serverless API integration
├─ screenshots        → Deployment proof (pipeline, EC2, live app)
│
└─ README.md          → Project overview & architecture

---

## 📸 Proof of Work

### CI/CD Pipeline
pipeline

### Docker Running on EC2
ec2

### Live Application
app

---

## 🔧 Key Features

- Automated Docker build & push via CI/CD
- Infrastructure provisioning using Terraform
- Container deployed on AWS EC2
- Serverless visitor counter using Lambda + DynamoDB
- Static website hosted on S3

---

## 📈 What This Demonstrates

- End-to-end deployment capability
- Real-world DevOps workflow
- Cloud-native architecture understanding
- Production-style project structure

---

## 👤 Author

Jon Hinds  
Aspiring Cloud / DevOps Enginee
