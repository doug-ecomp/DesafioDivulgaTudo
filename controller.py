"""Módulo responsável pela integração entre as requisições do usuário e os recursos do sistema.

"""

from persistencia import Persistencia
from anuncio import Anuncio
from relatorio import RelatorioAnuncio as RA


class Controller:
    """Controlador das chamadas do sistema.

    """
    bd = Persistencia()

    def cadastrar_anuncio(self, nome, cliente, data_inicio, data_termino, investimento_dia):
        """Cadastra um novo anúncio.

        :param nome: Nome do anuncio.
        :param cliente: Cliente contratante do anúncio.
        :param data_inicio: Data de início da vigência do anúncio.
        :param data_termino: Data de término da vigência do anúncio.
        :param investimento_dia: Valor em reais do investimento diário.
        :return:
        """
        novo_anuncio = Anuncio(nome, cliente, data_inicio, data_termino, investimento_dia)
        self.bd.salvar(list(novo_anuncio.__dict__.values()))
        return True

    def buscar_anuncio(self, cliente, data_inicio, data_termino):
        """Busca o(s) anúncio(s) na base de dados.

        :param cliente: Cliente contratante do anúncio
        :param data_inicio: Data de início da vigência do anúncio.
        :param data_termino: Data de término da vigência do anúncio.
        :return: Lista de anúncios que atendem aos requisitos da busca
        """
        lista = self.bd.buscar(cliente, data_inicio, data_termino)
        lista_anuncios = []
        if lista:
            for item in lista:
                anuncio = Anuncio(item[0], item[1], item[2], item[3], item[4])
                lista_anuncios.append(anuncio)

        return lista_anuncios

    def gera_relatorio(self, cliente='', data_inicio='', data_termino='', tipo_calculo='truncado'):
        """Computa as informações que compõe o relatório dos anúncios

        Dois tipos de cálculos estão disponívels: proporcional e truncado.
        No cálculo proporcional, o resultado final é aproximado, caso necessário, para até duas casas decimais.
        No cáclulo truncado, valores fracionados tem sua parte decimal desconsiderada, sem causar nenhuma aproximação.
        O cálculo truncado é a opção padrão (caso o valor do parâmetro não seja passado).

        :param cliente: Cliente contratante do anúncio :param data_inicio: Data de início da vigência do anúncio.
        :param data_termino: Data de término da vigência do anúncio. :param Tipo de cálculo: proporcional ou truncado
        :return: Lista de anúncios que atendem aos requisitos de busca juntamente com as informações computadas (
        Investimento total, cliques, compartilhamento e visualizações)
        """
        anuncios = self.buscar_anuncio(cliente, data_inicio, data_termino)
        proporcional = True if tipo_calculo == 'proporcional' else False
        resultado = []
        if anuncios:
            for anuncio in anuncios:
                investimento_total = anuncio.investimento_total()
                interacoes = RA.interacoes_total(investimento_total, proporcional)
                resultado.append([anuncio, investimento_total, interacoes])

        return resultado
