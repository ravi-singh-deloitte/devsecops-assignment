provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "hu-devops-25-rsingh95-s3" {
  bucket = "hu-devops-25-rsingh95-s3"

  tags = {
    Name       = "My bucket"
    Environment = "Dev"
  }
}