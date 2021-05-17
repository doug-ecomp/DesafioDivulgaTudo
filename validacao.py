import re
from datetime import datetime, date

FORMATO_DATA = '%d/%m/%Y'


def data_valida(data):
    try:
        return datetime.strptime(data, FORMATO_DATA).date()
    except:
        return False


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False
