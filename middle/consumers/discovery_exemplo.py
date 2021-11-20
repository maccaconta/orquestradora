# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:13:53 2021

@author: Jota
"""

from __future__ import print_function
import json
import unicodedata
import traceback
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, BearerTokenAuthenticator
import sys
import os
from ibm_watson import IAMTokenManager
from ibm_watson import DiscoveryV2

ignore_ssl_errors = True
discovery_api_key = ""
discovery_api_version = '2020-08-30'
discovery_collection_id = "4f3858f9-2020-e2b8-0000-017c13c85069"
discovery_project_id = '4d6e9afa-1960-4d55-b351-0d48f2fc44b2'
discovery_url = 'https://api.us-south.discovery.watson.cloud.ibm.com/instances/443d8959-8133-47af-a217-49bccc022906'


def init_discovery():
    authenticator = IAMAuthenticator(f'{discovery_api_key}')

    discovery = DiscoveryV2(
        version=f'{discovery_api_version}',
        authenticator=authenticator
    )

    discovery.set_service_url(discovery_url)

    discovery.set_disable_ssl_verification(ignore_ssl_errors)

    return discovery


def pesquisa_documentos(pesquisa_text, discovery_project_id=discovery_project_id,
                        discovery_collection_id=discovery_collection_id):
    discovery = init_discovery()
    print("pesquisando em ", discovery_collection_id)

    res = discovery.query(
        project_id=f'{discovery_project_id}',
        collection_ids=[f'{discovery_collection_id}'],
        natural_language_query=f'{pesquisa_text}',
        highlight=True,
        passages={
            "enabled": True,
            "per_document": True,
            "find_answers": True
        }
        # count=1
    )
    resultado = res.result

    num_docs_relevantes = resultado['matching_results']
    print("numero de documentos relevantes:", num_docs_relevantes)

    ### passagem mais relevante
    try:
        document_mais_relevante = resultado['results'][0]
        passagens = resultado['results'][0]['document_passages']

        passagem_mais_relevante = passagens[0]
        documento_id_mais_relevante = document_mais_relevante['document_id']
        score_id_mais_relevante = passagem_mais_relevante['answers'][0]['confidence']
        passagem_mais_relevante = passagem_mais_relevante['answers'][0]["answer_text"]
        documentos = resultado['results']

        dados_documentos = [
            {"discovery_id": i['document_id'],
             "score": i['result_metadata']['confidence'],
             "confidence": i['result_metadata']['confidence'],
             "highlights": i['document_passages'],
             "filename": i['extracted_metadata']['filename']
             }
            for i in documentos
        ]
    except Exception:
        resp = {
            "passagem": "Não encontrei nenhum conteudo relevante",
            "discovery_id": None,
            "score": None,
            "dados_documentos": None

        }
        return resp
    #### Busca geral 

    resp = {
        "passagem": passagem_mais_relevante,
        "discovery_id": documento_id_mais_relevante,
        "score": score_id_mais_relevante,
        "dados_documentos": dados_documentos
    }
    return resp
