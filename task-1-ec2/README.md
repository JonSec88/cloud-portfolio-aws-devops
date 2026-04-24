# Task 1 - EC2 Web Server Deployment

## Objective
Deploy a live Apache web server on AWS EC2.

## What Was Done
- Launched EC2 instance (Amazon Linux 2023, t3.micro)
- Configured Security Group (SSH + HTTP)
- Connected via SSH using .pem key
- Installed Apache (httpd)
- Started and enabled web server
- Deployed custom HTML page

## Commands Used

```bash
chmod 400 ec2-key.pem
ssh -i ec2-key.pem ec2-user@YOUR_PUBLIC_IP
sudo dnf install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
