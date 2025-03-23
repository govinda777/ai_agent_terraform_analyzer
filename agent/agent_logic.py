#!/usr/bin/env python3
import os
from agent.terraform_wrapper import TerraformStack
from agent.doc_updater import DocUpdater
from agent.iam_analyzer import IAMAnalyzer

def run_cycle():
    print("Iniciando ciclo de melhoria da stack Terraform...")
    stack = TerraformStack(path="../infra/terraform")
    print("Aplicando a stack Terraform...")
    stack.apply()
    print("Analisando documentação...")
    doc_issues = DocUpdater.find_missing_tags(stack)
    if doc_issues:
        fixes = DocUpdater.suggest_fixes(doc_issues)
        print("Sugestões de atualização da documentação:")
        for fix in fixes:
            print(fix)
    else:
        print("Nenhuma issue de documentação encontrada.")
    
    print("Analisando permissões de IAM...")
    iam_diff = IAMAnalyzer.analyze_required_vs_current(stack)
    if iam_diff:
        policy_patch = IAMAnalyzer.suggest_policy_patch(iam_diff)
        print("Sugestões para ajuste de IAM Policy:")
        for resource, patch in policy_patch.items():
            print(f"{resource}: {patch}")
    else:
        print("Nenhuma alteração na IAM Policy necessária.")

    print("Ciclo de melhoria concluído.")

if __name__ == "__main__":
    run_cycle()