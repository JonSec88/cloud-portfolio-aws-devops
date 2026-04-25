# Task 5 - Docker Containerized Application

## Objective
Run an application inside a Docker container.

## What Was Done
- Created Python Flask app
- Wrote Dockerfile
- Built Docker image
- Ran container locally

## Commands Used

```bash
docker build -t cloud-app .
docker run -p 80:80 cloud-app
