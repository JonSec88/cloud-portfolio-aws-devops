# AWS Cloud DevOps Portfolio with Docker CI CD and Serverless Architecture

## Overview
This project demonstrates a complete cloud DevOps workflow from development to production using Amazon Web Services and Docker. It includes continuous integration and deployment, infrastructure as code, container deployment, and a serverless application.

## Architecture

System 1 CI CD Deployment Pipeline  
GitHub → GitHub Actions → Docker Build → Docker Hub → AWS EC2 → Live Application  

System 2 Serverless Resume Platform  
User → S3 Static Website → API Gateway → Lambda → DynamoDB  

## Live Projects

Flask Application running on AWS EC2  
http://3.25.181.34  

Cloud Resume Website  
http://YOUR-S3-WEBSITE-ENDPOINT  

## Tech Stack

Amazon Web Services: EC2, S3, Lambda, API Gateway, DynamoDB  
Docker  
Terraform  
GitHub Actions  
Python Flask  

## Project Structure

cloud-portfolio-aws-devops/

app/  
Flask application container  

terraform/  
Infrastructure as code for EC2  

.github/workflows/  
CI CD pipeline automation  

resume-site/  
Static website with API integration  

screenshots/  
Deployment proof and results  

README.md  
Project documentation  

## Proof of Work

CI CD pipeline builds and pushes Docker image automatically  
Container runs on AWS EC2 and is publicly accessible  
Live application responds via public IP address  
Serverless API updates visitor counter dynamically  

## Key Features

Automated Docker build and push using GitHub Actions  
Infrastructure provisioning using Terraform  
Container deployment on AWS EC2  
Serverless backend using Lambda and DynamoDB  
Static website hosted using S3  

## What This Demonstrates

Ability to deploy complete cloud systems end to end  
Understanding of DevOps workflows and automation  
Experience with AWS cloud services and serverless design  
Production style project structure and delivery  

## Author

Jon Hinds  
Cloud DevOps Engineer
