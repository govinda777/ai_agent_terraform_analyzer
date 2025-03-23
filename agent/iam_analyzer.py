#!/usr/bin/env python3

class IAMAnalyzer:
    @staticmethod
    def analyze_required_vs_current(stack):
        """
        Analisa as diferenças entre as permissões requeridas e as permissões atuais dos recursos da stack.
        Para esta simulação, assume que as políticas atuais estão vazias.
        Retorna um dicionário com recursos e as ações necessárias.
        """
        resources = stack.get_resources()
        iam_diff = {}
        for resource in resources:
            if "s3_bucket" in resource or "s3" in resource:
                iam_diff[resource] = {
                    "required": ["s3:PutObject", "s3:GetObject"],
                    "current": []
                }
            elif "instance" in resource or "ec2" in resource:
                iam_diff[resource] = {
                    "required": ["ec2:DescribeInstances"],
                    "current": []
                }
            else:
                iam_diff[resource] = {
                    "required": ["iam:PassRole"],
                    "current": []
                }
        return iam_diff

    @staticmethod
    def suggest_policy_patch(iam_diff):
        """
        Gera sugestões de patches para a IAM Policy com base na diferença entre
        as permissões requeridas e as atuais.
        Retorna um dicionário onde a chave é o recurso e o valor é a sugestão de patch.
        """
        suggestions = {}
        for resource, diff in iam_diff.items():
            required = diff.get("required", [])
            current = diff.get("current", [])
            # Determina as permissões ausentes
            missing = set(required) - set(current)
            if missing:
                suggestions[resource] = f"Adicionar as actions: {', '.join(missing)}"
            else:
                suggestions[resource] = "Nenhuma alteração necessária"
        return suggestions

# Exemplo de uso:
if __name__ == "__main__":
    class DummyStack:
        def get_resources(self):
            return ["aws_s3_bucket.my_bucket", "aws_instance.my_instance"]

    stack = DummyStack()
    diff = IAMAnalyzer.analyze_required_vs_current(stack)
    patches = IAMAnalyzer.suggest_policy_patch(diff)
    print("Diff de IAM:", diff)
    print("Sugestões de patch:", patches)