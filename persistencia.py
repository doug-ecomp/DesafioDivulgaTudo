"""Módulo que define o armazenamento dos dos para garantir a persistência dos mesmos.

    Os dados são armazenados num arquivo .csv, com nome e local definidos dentro da classe Persistência.
"""

import os
import csv
from datetime import datetime, date
import validacao as valid


DELIMITER = ';'


class Persistencia:
    """Classe que modela o elemento responsável pela tarefas de armazenagens e busca na base de dados
    """
    diretorio = 'bd'
    arquivo = 'anuncios'
    caminho = '.' + os.path.sep + diretorio + os.path.sep + arquivo + '.csv'

    def salvar(self, novo_anuncio):
        """Salva um novo anúncio na base de dados.

        :param novo_anuncio: lista com os atributos do anúncio.
        """
        with open(self.caminho, mode='a') as arquivo_anuncios:
            arquivo_anuncios = csv.writer(arquivo_anuncios, delimiter=DELIMITER)
            arquivo_anuncios.writerow(novo_anuncio)

    def carrega_todos(self):
        """Carrega todos os anúncios armazenados na base de dados.

        :return: lista com todos os anúncios existentes
        """
        try:
            with open(self.caminho) as arquivo_anuncios:
                reader = csv.reader(arquivo_anuncios, delimiter=DELIMITER)
                lista_anuncios = list(reader)
                arquivo_anuncios.close()
                return lista_anuncios

        except FileNotFoundError:
            print('Arquivo não encontrado')
            return []

    def buscar(self, cliente='', data_inicio='', data_fim=''):
        """Busca anúncios na base de dados.

        :param cliente: Cliente contratante do anúncio.
        :param data_inicio: Data de início da vigência do anúncio.
        :param data_fim: Data de término da vigência do anúncio.
        :return: Lista dos anúncios que atendem aos critérios passados.
        """
        lista_anuncios = self.carrega_todos()
        if lista_anuncios:
            if cliente != '':
                lista_anuncios = list(filter(lambda x: x[1] == cliente, lista_anuncios))
            if data_inicio != '':
                data_inicio = datetime.strptime(data_inicio, valid.FORMATO_DATA).date()
                lista_anuncios = list(
                    filter(lambda x: datetime.strptime(x[2], valid.FORMATO_DATA).date() >= data_inicio, lista_anuncios))
            if data_fim != '':
                data_fim = datetime.strptime(data_fim, valid.FORMATO_DATA).date()
                lista_anuncios = list(
                    filter(lambda x: datetime.strptime(x[3], valid.FORMATO_DATA).date() <= data_fim, lista_anuncios))
        return lista_anuncios

