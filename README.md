# AWS Cloud DevOps Portfolio — Production System

## Live Systems

### 🌐 Portfolio (Primary Entry Point)
https://www.jonsec.cloud/

Static production site hosted on S3 + CloudFront.

---

### ⚡ Serverless Visitor Counter API
https://api.jonsec.cloud/

Architecture:
API Gateway → Lambda → DynamoDB

- Persistent state (DynamoDB)
- Real-time counter
- Custom domain + HTTPS
- Browser + API compatible

Example:
{"visits": 128}

---

### 🖥️ EC2 Application (Docker)
http://ec2.jonsec.cloud/

- Flask app
- Containerised deployment
- Linux EC2 host

---

### ⚖️ Application Load Balancer
http://alb.jonsec.cloud/

- Routes traffic to EC2
- Health-checked backend
- Production routing layer

---

## Architecture

User → CloudFront → S3 (portfolio)

User → API Gateway → Lambda → DynamoDB

User → ALB → EC2 → Docker container

---

## What This Proves

- Real AWS system (not demo)
- Serverless backend with persistence
- Containerised application deployment
- Load-balanced infrastructure
- DNS + custom domains
- Debugging under failure conditions

---

## Engineering Highlights

- Fixed CORS failures across API Gateway
- Resolved CloudFront stale cache issues
- Debugged DynamoDB key mismatch (critical bug)
- Integrated frontend with live backend API

---

## Tech Stack

AWS (S3, CloudFront, API Gateway, Lambda, DynamoDB, EC2, ALB, Route53)  
Docker  
Python  
GitHub Actions  
Linux  

---

## Next Evolution

- Observability (CloudWatch dashboards)
- IAM least-privilege design
- Terraform full infrastructure
- HTTPS everywhere
- Async system (SQS-based processing)

---

## Repository

https://github.com/JonSec88/cloud-portfolio-aws-devops
