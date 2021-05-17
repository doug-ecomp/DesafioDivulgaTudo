# DesafioDivulgaTudo

É recomendável criar um projeto python localmente e adicionar os arquivos e pastas no mesmo nível que estão nesse repositório.
Para iniciar o programa execute o arquivo inicio.py que está na raíz do projeto:
  python inicio.py

No menu inicial escolha entre as opções de cadastrar anúncio e gerar o relatório.

No menu de gerar relatório podem ser adicionadas informações para filtar os anúncios. 
Caso nenhum filtro seja adicionado, será gerado reatório de todos os anúncios cadastrados.
Há duas opções de cálculo: proporcional e truncado.
O proporcional considera a parte racionada de um valor, enquanto que o truncado não faz isso. 
Para o cálculo truncado, 99 visualizações geram 0 cliques, enquanto que no proporcional, gera 11,88 cliques.

Finalmente, o arquivo ondes os anúncios são armazenados fica, por padrão, dentro da pasta 'bd'.
O diretório e o nome do arquivo podem ser alterados nas respectivas variáveis da classe Persistência que encontra-se dentro do arquivo persistencia.py
