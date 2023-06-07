from flask import Flask, request
from flask_restful import Resource, Api
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'Dart']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] = posicao
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]

class habilidade(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}