# Cloud DevOps Portfolio — AWS End-to-End Deployment

## Overview

This repository demonstrates a complete DevOps workflow from development to production using AWS and Docker. It highlights real-world deployment practices including CI/CD, infrastructure as code, containerisation, and serverless architecture.

---

## Architecture

System 1: CI/CD Deployment Pipeline  
GitHub → GitHub Actions → Docker Build → Docker Hub → AWS EC2 → Live Application

System 2: Serverless Resume Platform  
User → S3 Static Website → API Gateway → Lambda → DynamoDB

---

## Live Projects

Flask Application (Docker + EC2)  
http://3.25.181.34

Cloud Resume Website  
http://YOUR-S3-WEBSITE-ENDPOINT

---

## Tech Stack

AWS (EC2, S3, Lambda, API Gateway, DynamoDB)  
Docker  
Terraform  
GitHub Actions  
Python (Flask)

---

## Project Structure

cloud-portfolio-aws-devops

app/                Flask application (Dockerised)  
terraform/          Infrastructure as Code (EC2 provisioning)  
.github/workflows/  CI/CD pipeline (build and push Docker image)  
resume-site/        Static resume site with API integration  
screenshots/        Deployment proof (pipeline, EC2, live app)  

README.md           Project documentation  

---

## Proof of Work

CI/CD pipeline successfully builds and pushes Docker image  
Container is running on EC2 and publicly accessible  
Live application reachable via public IP  
Serverless API updates visitor counter dynamically  

---

## Key Features

Automated Docker build and push via CI/CD  
Infrastructure provisioning using Terraform  
Container deployment on AWS EC2  
Serverless visitor counter using Lambda and DynamoDB  
Static website hosted on S3  

---

## What This Demonstrates

Ability to design and deploy end-to-end cloud systems  
Understanding of DevOps workflows and automation  
Experience with cloud-native and serverless architecture  
Production-style project structure and delivery  

---

## Author

Jon Hinds  
Cloud / DevOps Engineer
