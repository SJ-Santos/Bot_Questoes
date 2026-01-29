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
        #TODO:colocar os prompts
        template_gerar_questao = ChatPromptTemplate.from_template([
            ("system",""),
            ("human","")
            ])
        
        chain = template_gerar_questao | self.llm.with_structured_output(Questao)
        return chain.invoke({"assunto": assunto}).dict()

    def corrigir_questao(self, questao: dict, resposta_usuario: str) -> str:
        #TODO:colocar os prompts
        template_corrigir_questao = ChatPromptTemplate.from_template([
            ("systen",""),
            ("human","")
            ])
        
        chain = template_corrigir_questao | self.llm.with_structured_output(CorrecaoQuestao)

        return chain.invoke({"questão":questao,"reposta":resposta_usuario}).dict()
    
    def ensinar(self, assunto) -> str:
        
        pass