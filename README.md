# AWS DevOps Portfolio — End-to-End Cloud Engineering System

## Overview
This project demonstrates a complete cloud engineering lifecycle built through progressive infrastructure layers. Each stage was intentionally chosen to simulate real-world production systems, starting from manual cloud provisioning and evolving into fully automated CI/CD workflows.

The goal is not just deployment, but demonstrating engineering reasoning: why each tool was introduced, what problem it solves, and how complexity is reduced over time through automation.

---

# Engineering Progression (WHY THIS ORDER)

This portfolio follows a real DevOps maturity model:

### 1. Manual Infrastructure (AWS EC2)
Why:
- Understand compute fundamentals without abstraction
- Learn SSH, Linux administration, and networking basics
- Establish baseline cloud operations

Outcome:
- Fully working web server on EC2

---

### 2. Network Failure Simulation (Security Groups)
Why:
- Real cloud failures are usually misconfiguration, not code
- Learn how AWS security layers control access
- Build troubleshooting discipline

Outcome:
- Fixed blocked inbound traffic and restored service

---

### 3. Static Cloud Hosting (S3)
Why:
- Separate compute from static delivery
- Learn object storage vs server-based hosting
- Understand public access control models

Outcome:
- Fully hosted static website on S3

---

### 4. Infrastructure as Code (Terraform)
Why:
- Manual AWS is not scalable or repeatable
- Infrastructure must be version-controlled
- Enables reproducibility and automation

Outcome:
- EC2 deployed using declarative configuration

---

### 5. Containerisation (Docker)
Why:
- Solve environment inconsistency problem
- Package applications with dependencies
- Enable portable deployment

Outcome:
- Flask app running inside containerised environment

---

### 6. CI/CD Automation (GitHub Actions)
Why:
- Manual builds are not scalable
- CI ensures every change is validated automatically
- Introduces production-style deployment pipelines

Outcome:
- Automated Docker build triggered on every push

---

# Architecture Evolution

```text id="r3"
Manual AWS → Troubleshooting → Static Hosting → IaC → Containers → Automation 

---

## Live Repository

https://github.com/JonSec88/cloud-portfolio-aws-devops

---

## Author

GitHub: https://github.com/JonSec88  
Email: Jonhinds9@gmail.com
