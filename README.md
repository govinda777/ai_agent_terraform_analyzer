# AI Agent Terraform Analyzer

Este projeto implementa um agente de AI para gerenciar stacks Terraform simuladas utilizando LocalStack para simulação de uma Cloud. O agente é capaz de:

- Criar, alterar e sincronizar stacks Terraform.
- Melhorar a documentação dos recursos, adicionando tags recomendadas.
- Identificar permissões utilizadas via outputs e propor ajustes nas IAM Policies visando o princípio do menor privilégio.

## Estrutura do Projeto

- **/agent**: Código do agente em Python:
  - `main.py`: Ponto de entrada do agente.
  - `agent_logic.py`: Lógica principal que executa o ciclo de melhoria.
  - `terraform_wrapper.py`: Simulação da execução dos comandos Terraform.
  - `doc_updater.py`: Analisa a documentação dos recursos e propõe melhorias.
  - `iam_analyzer.py`: Compara permissões necessárias e atuais, sugerindo patches de IAM Policy.
- **/infra**: Infraestrutura Terraform e demais scripts de suporte.
- **/localstack**: Configuração do LocalStack, utilizado para simular a AWS.

## Como Executar

1. Certifique-se de ter Python 3 instalado.
2. No terminal, execute:
   ```bash
   python3 agent/main.py
   ```
3. O agente simulará a aplicação da stack Terraform e exibirá:
   - Os recursos criados.
   - Sugestões para melhorar a documentação (adicionando tags).
   - Sugestões de patches para IAM Policies com base nas permissões analisadas.

## Notas

- Esta implementação utiliza simulações:
  - O comando `terraform apply` é simulado e não executa operações reais.
  - As análises de documentação e IAM são exemplificativas.
- Futuras melhorias podem incluir a integração real com o LocalStack e parsing avançado dos arquivos Terraform.

---

Projeto desenvolvido como exemplo para o AI Agent Terraform Analyzer.