"""Módulo com a classe que define o anúncio.

"""


import validacao as valid


class Anuncio:
    """Classe que modela os anúncios.
    """
    def __init__(self, nome, cliente, data_inicio, data_termino, investimento_dia):
        self.nome = nome
        self.cliente = cliente
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.investimento_dia = float(investimento_dia)

    def investimento_total(self):
        """Calcula o todal investido.

        :return: O todal investido em reais de acordo com a quatidade de dias vigentes do anúncio.
        """
        d1 = valid.data_valida(self.data_inicio)
        d2 = valid.data_valida(self.data_termino)

        total_dias = (d2 - d1).days + 1
        return self.investimento_dia * total_dias


