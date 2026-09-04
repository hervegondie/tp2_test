""" tp2"""


import pytest
from app.utils import predict


def test_predict_success():
    # Données d'entrée
    input_data = [1.0, 2.0, 3.0]

    # Valeur attendue
    expected_output = 6.0

    # Exécution de la fonction
    result = predict(input_data)

    # Vérification
    #assert result == expected_output
 
 

    