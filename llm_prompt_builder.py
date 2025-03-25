"""
llm_prompt_builder.py

Responsabilidade:
Receber uma solicitação e uma ação, garantindo que a LLM devolva um arquivo (ex: provider.tf).

Ações Suportadas:
- FIX_ERROR
- NO_COMPLIANCE
- GET_SUGGESTION
- IAM AJUST
- IMPLEMENTACAO DE DOCUMENTAÇÃO

Exemplo:
    prompt = LlmPromptBuilder().build_prompt("Detalhes da solicitação", "GET_SUGGESTION")
    print(prompt)

"""
class LlmPromptBuilder:
    ALLOWED_ACTIONS = {'FIX_ERROR', 'NO_COMPLIANCE', 'GET_SUGGESTION', 'IAM AJUST', 'IMPLEMENTACAO DE DOCUMENTAÇÃO'}

    def __init__(self, arquivo_target='provider.tf'):
        """
        Inicializa o construtor de prompts com o nome do arquivo que a LLM deverá retornar.
        """
        self.arquivo_target = arquivo_target

    def build_prompt(self, solicitacao: str, acao: str) -> str:
        """
        Constrói o prompt para a LLM com base na solicitação e ação.

        Parâmetros:
            solicitacao (str): A solicitação a ser processada.
            acao (str): A ação a ser executada (deve ser uma das ações permitidas).

        Retorna:
            str: O prompt construído.

        Exceções:
            ValueError: Se a ação não for permitida.
        """
        acao_upper = acao.upper().strip()
        if acao_upper not in self.ALLOWED_ACTIONS:
            raise ValueError(f"Ação inválida: {acao}. As ações permitidas são: {', '.join(self.ALLOWED_ACTIONS)}")
        
        prompt = (
            f"Solicitacao: {solicitacao}\n"
            f"Acao: {acao_upper}\n\n"
            f"Por favor, retorne um arquivo chamado '{self.arquivo_target}' com a resposta."
        )
        return prompt