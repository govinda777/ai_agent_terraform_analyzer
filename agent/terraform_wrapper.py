#!/usr/bin/env python3
import subprocess
import os

class TerraformStack:
    def __init__(self, path):
        self.path = path
        self.resources = []
    
    def apply(self):
        print(f"Inicializando e aplicando Terraform stack em {self.path}")
        # Simulação de aplicação do Terraform.
        # Em um ambiente real, você poderia rodar:
        # subprocess.run(["terraform", "init"], cwd=self.path, check=True)
        # subprocess.run(["terraform", "apply", "-auto-approve"], cwd=self.path, check=True)
        self.resources = [
            "aws_s3_bucket.my_bucket",
            "aws_instance.my_instance"
        ]
        print("Recursos criados:", self.resources)
        return True
    
    def get_resources(self):
        return self.resources