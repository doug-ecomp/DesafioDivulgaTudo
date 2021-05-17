import unittest
from relatorio import RelatorioAnuncio as RA


class TestCalculadora(unittest.TestCase):
    """Classe dos testes unitários da calculadora de visualizações máxima de um anúncio.
    Cada função que compõe a calculadora tem dois métodos nessa classe, um para o cálculo proporcional e o outro para o cálculo truncado"""

    def test_visualizacao_inicial_truncado(self):
        proporcional = False
        lista_valores = [(405, 12150), (399, 11970), (10.5, 300), (216.1, 6480)]
        for entrada, saida in lista_valores:
            result = RA.visualizacao_inicial(entrada, proporcional)
            self.assertEqual(result, saida)

    def test_visualizacao_inicial_proporcional(self):
        proporcional = True
        lista_valores = [(111.11, 3333.30), (500.675, 15020.25), (10.5, 315), (216.1, 6483)]
        for entrada, saida in lista_valores:
            result = RA.visualizacao_inicial(entrada, proporcional)
            self.assertEqual(result, saida)

    def test_cliques_truncado(self):
        proporcional = False
        lista_valores = [(3000, 360), (9210, 1104), (25, 0), (7250.5, 864)]
        for entrada, saida in lista_valores:
            result = RA.cliques(entrada, proporcional)
            self.assertEqual(result, saida)

    def test_cliques_proporcional(self):
        proporcional = True
        lista_valores = [(50.5549, 6.07), (9210, 1105.20), (25, 3), (7250.5, 870.06)]
        for entrada, saida in lista_valores:
            result = RA.cliques(entrada, proporcional)
            self.assertEqual(result, saida)

    def test_compartilhamentos_truncado(self):
        proporcional = False
        lista_valores = [(768, 114), (384, 57), (19, 0), (111.11, 15)]
        for entrada, saida in lista_valores:
            result = RA.compartilhamentos(entrada, proporcional)
            self.assertEqual(result, saida)

    def test_compartilhamentos_proporcional(self):
        proporcional = True
        lista_valores = [(777.96, 116.69), (290.4, 43.56), (19, 2.85), (111.11, 16.67)]
        for entrada, saida in lista_valores:
            result = RA.compartilhamentos(entrada, proporcional)
            self.assertEqual(result, saida)

    def test_novas_interacoes_truncado(self):
        proporcional = False
        lista_valores = [(3000, (360, 54, 2160)), (2160, (252, 36, 1440)), (1440, (168, 24, 960)), (960, (108, 15, 600))]
        for entrada, saida in lista_valores:
            result = RA.novas_interacoes(entrada, proporcional)
            self.assertEqual(result, saida)

    def test_novas_interacoes_proporcional(self):
        proporcional = True
        lista_valores = [(2420.40, (290.45, 43.57, 1742.80)), (85.5345, (10.26, 1.54, 61.60)), (178.29, (21.39, 3.21, 128.40)), (30, (3.6, 0.54, 21.60))]
        for entrada, saida in lista_valores:
            result = RA.novas_interacoes(entrada, proporcional)
            self.assertEqual(result, saida)

    def test_interacoes_total_truncado(self):
        proporcional = False
        lista_valores = [(100, (888, 129, 8160)), (6542, (61440, 9213, 564780)), (664, (6192, 924, 56880)), (233, (2112, 312, 19470))]
        for entrada, saida in lista_valores:
            result = RA.interacoes_total(entrada, proporcional)
            self.assertEqual(result, saida)

    def test_interacoes_total_proporcional(self):
        proporcional = True
        lista_valores = [(82.24, (773.23, 115.99, 7106.80)), (30, (282.05, 42.31, 2592.40)), (1, (9.4, 1.41, 86.40)), (33.333, (313.39, 47.01, 2880.39))]
        for entrada, saida in lista_valores:
            result = RA.interacoes_total(entrada, proporcional)
            self.assertEqual(result, saida)
