import os
from typing import Dict
from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field 


class IA_Handler:
    def __init__(self,endpoint,deployment,key):
        self.llm = AzureChatOpenAI(
            azure_endpoint=endpoint,
            azure_deployment=deployment,
            azure_api_key=key,
            api_version="2024-02-15-preview"
        )

    def gerar_questao(self, assunto: str) -> dict:
        pass

    def corrigir_questao(self, questao: str, resposta_usuario: str) -> str:
        pass
    
    def ensinar(self, nova_questao: str, resposta_correta: str) -> str:
        pass