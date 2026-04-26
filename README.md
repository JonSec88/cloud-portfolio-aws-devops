# 🚀 Cloud DevOps Engineer Portfolio (AWS Production Simulation)

## 👤 Jonathan Hinds

Cloud / DevOps Engineer  
GitHub: https://github.com/JonSec88  

---

## 🧭 Overview

Production-style AWS DevOps environment demonstrating CI/CD automation, containerised deployment, infrastructure as code, and real-world cloud debugging.

This project simulates a real-world cloud system deployed on AWS using modern DevOps practices.

---

## 🌐 Live Systems

### EC2 Application (CI/CD Enabled)
http://3.25.181.34  

### S3 Static Resume Site
http://jonsec88-s3-site-83927-579986815910-ap-southeast-2-an.s3-website-ap-southeast-2.amazonaws.com/

---

## 🧱 System Architecture

- **Frontend:** Static resume site hosted on AWS S3  
- **Backend:** Flask application running in Docker on AWS EC2  
- **CI/CD:** GitHub Actions automated deployment pipeline  
- **Infrastructure:** Terraform-managed AWS resources  

---

## 🔧 Core Engineering Components

### EC2 + Docker Deployment
Containerised Flask application deployed to EC2 with automated redeployment via CI/CD.

---

### CI/CD Pipeline
Automated workflow using GitHub Actions:
- Triggered on Git push  
- SSH into EC2  
- Rebuild Docker container  
- Redeploy application  

---

### S3 Static Website
Static HTML resume hosted using AWS S3 static website hosting.

---

### Networking Debugging
Security group misconfiguration identified and resolved in a real cloud incident simulation.

---

### Infrastructure as Code (Terraform)
AWS infrastructure defined and managed using Terraform for reproducibility.

---

## 🧠 Engineering Value

- CI/CD automation  
- Containerised workloads  
- Infrastructure as Code  
- Cloud networking debugging  
- Multi-service AWS architecture  

---

## 📁 Repository Structure

