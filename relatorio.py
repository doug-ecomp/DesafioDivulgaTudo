"""Módulo com as funções que computam os dados de interação com o anúncio.
"""

from typing import Union, Tuple

MAX_COMPARTILHAMENTOS = 4
VISUALIZACOES_POR_REAL = 30
VISUALIZACOES_POR_COMPARTILHAMENTO = 40
MULTIPLICADOR_CLIQUES = 12
DIVISOR_CLIQUES = 100
MULTIPLICADOR_COMPARTILHAMENTOS = 3
DIVISOR_COMPARTILHAMENTOS = 20
DIGITOS_APROXIMACAO = 2


class RelatorioAnuncio:
    """Classe com métodos estáticos que encapsula os métodos de calculo das possívels interações com o anúncio.
    """
    @staticmethod
    def visualizacao_inicial(investimento: Union[int, float], proporcional: bool = False) -> Union[int, float]:
        """Calcula a quantiddde de visualizações inicial de acordo com o investimento.

        Dois tipos de cálculos estão disponívels: proporcional e truncado.
        No cálculo proporcional, o resultado final é aproximado, caso necessário, para até duas casas decimais.
        No cáclulo truncado, valores fracionados tem sua parte decimal desconsiderada, sem causar nenhuma aproximação.
        O cálculo truncado é a opção padrão (caso o valor do parâmetro não seja passado).

        :param investimento: Valor intestido em reais.
        :param proporcional: Tipo de cálculo. True para proporcional e False para truncado.
        :return: A quantidade inicial de visualizações gerada pelo anúncio original.
        """
        if proporcional:
            return round(VISUALIZACOES_POR_REAL * investimento, DIGITOS_APROXIMACAO)
        else:
            return VISUALIZACOES_POR_REAL * (investimento // 1)

    @staticmethod
    def cliques(qtd_visualizacoes: Union[int, float], proporcional: bool = False) -> Union[int, float]:
        """Calcula a quatidade de cliques de acordo com o número de visualizações do anúncio.

        Dois tipos de cálculos estão disponívels: proporcional e truncado.
        No cálculo proporcional, o resultado final é aproximado, caso necessário, para até duas casas decimais.
        No cáclulo truncado, valores fracionados tem sua parte decimal desconsiderada, sem causar nenhuma aproximação.
        O cálculo truncado é a opção padrão (caso o valor do parâmetro não seja passado).

        :param qtd_visualizacoes:  Quantidade de visualicações.
        :param proporcional: Tipo de cálculo. True para proporcional e False para truncado.
        :return: Quantidade de cliques gerados pela quantidade de visualizações.
        """
        if proporcional:
            # qtd_visualizacoes = round(qtd_visualizacoes, DIGITOS_APROXIMACAO)
            return round(MULTIPLICADOR_CLIQUES * (qtd_visualizacoes / DIVISOR_CLIQUES), DIGITOS_APROXIMACAO)
        else:
            return MULTIPLICADOR_CLIQUES * ((qtd_visualizacoes // 1) // DIVISOR_CLIQUES)

    @staticmethod
    def compartilhamentos(qtd_cliques: Union[int, float], proporcional: bool = False) -> Union[int, float]:
        """Calcula a quatidade de compartilhamentos de acordo com a quantidade de cliques do anúncio.

        Dois tipos de cálculos estão disponívels: proporcional e truncado.
        No cálculo proporcional, o resultado final é aproximado, caso necessário, para até duas casas decimais.
        No cáclulo truncado, valores fracionados tem sua parte decimal desconsiderada, sem causar nenhuma aproximação.
        O cálculo truncado é a opção padrão (caso o valor do parâmetro não seja passado).

        :param qtd_cliques: Quatidade de cliques.
        :param proporcional: Tipo de cálculo. True para proporcional e False para truncado.
        :return: Quantidade de compartilhamentos gerados pela quantidade de cliques.
        """

        if proporcional:
            # qtd_cliques = round(qtd_cliques, DIGITOS_APROXIMACAO)
            return round(MULTIPLICADOR_COMPARTILHAMENTOS * (qtd_cliques / DIVISOR_COMPARTILHAMENTOS),
                         DIGITOS_APROXIMACAO)
        else:
            return MULTIPLICADOR_COMPARTILHAMENTOS * ((qtd_cliques // 1) // DIVISOR_COMPARTILHAMENTOS)

    @staticmethod
    def novas_interacoes(qtd_visualizacoes: Union[int, float], proporcional: bool = False) -> Tuple[
        Union[int, float], Union[int, float], Union[int, float]]:
        """Calcula a quantidade de interações com o anúncio geradas pelo dado número de visualizações que o mesmo possui.

        Dois tipos de cálculos estão disponívels: proporcional e truncado.
        No cálculo proporcional, o resultado final é aproximado, caso necessário, para até duas casas decimais.
        No cáclulo truncado, valores fracionados tem sua parte decimal desconsiderada, sem causar nenhuma aproximação.
        O cálculo truncado é a opção padrão (caso o valor do parâmetro não seja passado).

        :param qtd_visualizacoes: Quantidade de visualizações que o anúncio possui.
        :param proporcional: Tipo de cálculo. True para proporcional e False para truncado.
        :return: As quantidades de cliques, compartilhamentos e novas visualizações geradas.
        """

        qtd_cliques = RelatorioAnuncio.cliques(qtd_visualizacoes, proporcional)

        qtd_compartilhamentos = RelatorioAnuncio.compartilhamentos(qtd_cliques, proporcional)

        return qtd_cliques, qtd_compartilhamentos, round(qtd_compartilhamentos * VISUALIZACOES_POR_COMPARTILHAMENTO, DIGITOS_APROXIMACAO)

    @staticmethod
    def interacoes_total(investimento: Union[int, float], proporcional: bool = False) -> Tuple[
        Union[int, float], Union[int, float], Union[int, float]]:
        """Calcula a quantidade máxima de interações com o anúncio de acordo com o investimento.

        Dois tipos de cálculos estão disponívels: proporcional e truncado.
        No cálculo proporcional, o resultado final é aproximado, caso necessário, para até duas casas decimais.
        No cáclulo truncado, valores fracionados tem sua parte decimal desconsiderada, sem causar nenhuma aproximação.
        O cálculo truncado é a opção padrão (caso o valor do parâmetro não seja passado).

        :param investimento: Valor investido em reais.
        :param proporcional: Tipo de cálculo. True para proporcional e False para truncado.
        :return: As quantidades totais de cliques, compartilhamentos e de visualizações do anúncio.
        """

        lista_visualizacoes = [RelatorioAnuncio.visualizacao_inicial(investimento, proporcional)]
        lista_cliques = []
        lista_compartilhamentos = []
        for _ in range(MAX_COMPARTILHAMENTOS):
            cliques, compartilhamentos, visualizacoes = RelatorioAnuncio.novas_interacoes(lista_visualizacoes[-1], proporcional)
            lista_cliques.append(cliques)
            lista_compartilhamentos.append(compartilhamentos)
            if visualizacoes > 0:
                lista_visualizacoes.append(visualizacoes)
            else:
                break

        return round(sum(lista_cliques), DIGITOS_APROXIMACAO), round(sum(lista_compartilhamentos), DIGITOS_APROXIMACAO), round(sum(lista_visualizacoes), DIGITOS_APROXIMACAO)
