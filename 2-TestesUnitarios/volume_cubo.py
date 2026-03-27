from exceptions import *

from decimal import Decimal, ROUND_HALF_UP
TWO_PLACES = Decimal('0.01')

def volume_cubo (lado):
    if (isinstance(lado, bool) or not isinstance(lado, (int, float))):
        raise TypeError('O valor indicado como lado deve ser inteiro ou real.')
    
    if (lado <= 0):
        raise ValorInvalido("O lado do cubo deve ser maior do que zero.")
    
    return float(Decimal(lado**3).quantize(TWO_PLACES, rounding=ROUND_HALF_UP))