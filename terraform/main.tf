provider "aws" {
  region = "ap-southeast-2"
}

resource "aws_instance" "dev_server" {
  ami           = "ami-0dbb125f47e8dbdc5"
  instance_type = "t3.micro"

  tags = {
    Name    = "Terraform-EC2-DevServer"
    Project = "CloudPortfolio"
  }
}
