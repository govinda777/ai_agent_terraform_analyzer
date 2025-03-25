# Prompt Builder Documentation

Esta documentação descreve a funcionalidade dos Builders de Prompt na aplicação.

## Introdução

O Prompt Builder é um componente fundamental que prepara as requisições para a LLM, garantindo que a resposta gerada esteja no formato correto e contenha as informações esperadas.

## LlmPromptBuilder

A classe `LlmPromptBuilder`, definida em `llm_prompt_builder.py`, é responsável por:
- Receber uma solicitação e uma ação.
- Validar que a ação pertence a um conjunto de ações permitidas.
- Construir um prompt que instrui a LLM a retornar um arquivo com um nome específico (ex: provider.tf).

### Ações Suportadas
A classe suporta as seguintes ações:
- **FIX_ERROR**: Indica que a LLM deve corrigir um erro detectado.
- **NO_COMPLIANCE**: Indica que a solicitação não está em conformidade.
- **GET_SUGGESTION**: Solicita sugestões de melhorias.
- **IAM AJUST**: Aciona ajustes em políticas ou configurações IAM.
- **IMPLEMENTACAO DE DOCUMENTAÇÃO**: Indica que a LLM deve gerar ou atualizar documentação.

### Funcionamento

Ao chamar o método `build_prompt`:
- O método recebe dois parâmetros:
  - `solicitacao`: Uma string contendo os detalhes da solicitação.
  - `acao`: Uma string contendo a ação desejada.
- O método converte a ação para letras maiúsculas e valida se ela está no conjunto de ações permitidas.
- Se a ação não for permitida, um `ValueError` é lançado.
- Caso a ação seja válida, o método retorna um prompt formatado que instrui a LLM a retornar um arquivo com o nome especificado.

#### Exemplo de Uso

```python
from llm_prompt_builder import LlmPromptBuilder

# Inicializa com o arquivo de destino desejado, por exemplo, 'provider.tf'
prompt_builder = LlmPromptBuilder(arquivo_target='provider.tf')

# Constrói o prompt passando a solicitação e a ação
prompt = prompt_builder.build_prompt("Detalhes da solicitação", "GET_SUGGESTION")
print(prompt)
```

O prompt gerado terá o seguinte formato:

```
Solicitacao: Detalhes da solicitação
Acao: GET_SUGGESTION

Por favor, retorne um arquivo chamado 'provider.tf' com a resposta.
```

## Conclusão

A classe `LlmPromptBuilder` facilita a integração com a LLM ao padronizar as solicitações e as ações, assegurando que a resposta seja sempre entregue no formato adequado e contenha as informações relevantes para a aplicação.