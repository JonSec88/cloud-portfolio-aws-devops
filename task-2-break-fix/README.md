# Task 2 - Break and Fix (Security Groups)

## Objective
Simulate and fix a real-world access issue.

## What Happened
- Removed HTTP (port 80) from EC2 security group
- Website became unreachable

## Diagnosis
- EC2 instance still running
- Apache still active
- Issue caused by missing inbound rule

## Fix Applied
- Re-added HTTP rule:
  - Port: 80
  - Source: 0.0.0.0/0

## Result
Website access restored successfully.

## Proof
See screenshots folder:
- Broken site
- Security group without HTTP
- Security group restored
- Working site

## Skills
- AWS Security Groups
- Troubleshooting
- Root cause analysis
