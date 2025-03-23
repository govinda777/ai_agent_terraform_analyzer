#!/usr/bin/env python3

class DocUpdater:
    @staticmethod
    def find_missing_tags(stack):
        """
        Analisa os recursos da stack Terraform e identifica quais tags estão faltando.
        Para esta simulação, assume que todos os recursos estão sem as tags necessárias.
        """
        resources = stack.get_resources()
        # Tags requeridas para cada recurso.
        required_tags = ["Name", "Owner", "Env", "Namespace"]
        missing_tags = {}
        for resource in resources:
            # Simular que todos os recursos estão sem as tags exigidas.
            missing_tags[resource] = required_tags
        return missing_tags

    @staticmethod
    def suggest_fixes(doc_issues):
        """
        Gera uma lista de sugestões para atualizar a documentação,
        com base nas tags faltantes identificadas.
        """
        suggestions = []
        for resource, tags in doc_issues.items():
            suggestion = (f"O recurso '{resource}' está faltando as tags: " +
                          f"{', '.join(tags)}. Sugerimos adicionar essas tags " +
                          "com valores apropriados.")
            suggestions.append(suggestion)
        return suggestions