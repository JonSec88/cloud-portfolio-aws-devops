# 🚀 AWS Cloud DevOps Portfolio (Production Simulation)

## 👤 Jonathan Hinds
Cloud / DevOps Engineer

GitHub: https://github.com/JonSec88

---

# 🧭 System Overview

This project demonstrates a complete AWS DevOps production-style environment including:

- EC2 Linux server deployment with Docker
- Application Load Balancer (ALB) routing layer
- S3 static website hosting
- Terraform Infrastructure as Code (IaC)
- CI/CD automation using GitHub Actions
- Real-world AWS networking troubleshooting

The goal is to demonstrate **job-ready cloud engineering capability** through real deployment and debugging scenarios.

---

# 🌐 Live Systems

## EC2 Application (Direct)
http://3.25.181.34

## Application Load Balancer (Production Routing)
http://devops-alb-1860853383.ap-southeast-2.elb.amazonaws.com

## S3 Static Resume Site
http://jonsec88-s3-site-83927-579986815910-ap-southeast-2-an.s3-website-ap-southeast-2.amazonaws.com/

---

# 🧱 Architecture

User → ALB → Target Group → EC2 (Docker Flask App)

S3 → Static Resume Website

Terraform → Infrastructure Provisioning

GitHub Actions → CI/CD Automation

📸 Diagram:
docs/architecture.png

---

# 🔧 EC2 Deployment (Docker + CI/CD)

- Flask application containerised using Docker
- Hosted on AWS EC2 Linux instance
- Exposed on port 80
- Automatically deployed via GitHub Actions pipeline

### Evidence:
- docs/screenshots/ec2/ec2-live-app.png
- docs/screenshots/ec2/docker-running.png
- docs/screenshots/ec2/cicd-success.png

---

# ⚖️ Application Load Balancer (Production Layer)

- Internet-facing AWS Application Load Balancer
- Routes traffic to EC2 via Target Group
- Health checks ensure backend availability

### Evidence:
- docs/screenshots/alb/alb-live.png
- docs/screenshots/alb/target-healthy.png
- docs/screenshots/alb/listener.png

---

# ☁️ S3 Static Website Hosting

- Static resume website hosted on AWS S3
- Public access enabled
- Fully configured static hosting

### Evidence:
- docs/screenshots/s3/s3-upload.png
- docs/screenshots/s3/s3-hosting-enabled.png
- docs/screenshots/s3/s3-live-site.png
- docs/screenshots/s3/s3-bucket-overview.png

---

# 🌐 Networking & Debugging (Real Incident)

Real AWS troubleshooting performed:

- Security group misconfiguration identified
- HTTP access restored successfully
- Application connectivity recovered

### Evidence:
- docs/screenshots/networking/broken-site.png
- docs/screenshots/networking/sg-no-http.png
- docs/screenshots/networking/sg-http-restored.png

---

# 🏗️ Infrastructure as Code (Terraform)

- AWS infrastructure provisioned using Terraform
- Reproducible infrastructure setup
- Version-controlled cloud resources

---

# ⚙️ CI/CD Pipeline

- GitHub Actions triggered on push
- Docker image build and deployment
- Automated EC2 deployment via SSH
- Zero manual deployment process

---

# 🧰 Tech Stack

AWS • Docker • Terraform • GitHub Actions  
Python • HTML • Bash  
Linux (EC2)

---

# 🧠 Engineering Highlights

✔ Production-style AWS architecture  
✔ Real cloud debugging (networking + security groups)  
✔ Containerised deployment system  
✔ Infrastructure as Code (Terraform)  
✔ Fully automated CI/CD pipeline  
✔ Multi-service AWS system design  

---

# 🚀 Outcome

This project demonstrates practical DevOps engineering capability across:

- Cloud infrastructure design
- Deployment automation
- Container orchestration
- Networking troubleshooting
- Production AWS architecture patterns

---

# 🚀 Future Improvements

- HTTPS (SSL via ACM)
- Custom domain setup
- Auto Scaling Group
- CloudFront CDN
- Monitoring via CloudWatch
