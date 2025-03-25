# Classe responsavel executar o melhor prompt para ser enviado para o LLM

class LLMService:
    def __init__(self):
        self.llm = LLM()

    def get_script(self, script):
        # TODO: Implementar a logica para montar o melhor script para ser enviado para o LLM
        return script
