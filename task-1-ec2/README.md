# Task 1 — AWS EC2 Web Server Deployment

## Overview
Provisioned and configured a virtual server on AWS EC2 to host a basic web server. This demonstrates foundational cloud infrastructure deployment and remote server access.

---

## Objective
Deploy and access a publicly reachable EC2 instance to understand compute provisioning, security groups, and SSH access in AWS.

---

## Tools
- AWS EC2
- Amazon Linux 2
- SSH (Terminal)
- AWS Security Groups

---

## Architecture
User → Internet → AWS Security Group → EC2 Instance → Web Server

---

## Implementation

### 1. Launch EC2 Instance
- Selected Amazon Linux 2 AMI
- Chose t2.micro instance type
- Configured key pair for SSH access

### 2. Configure Security Group
Allowed inbound traffic:
- SSH (22)
- HTTP (80)

### 3. Connect via SSH
```bash
ssh -i key.pem ec2-user@<public-ip>
