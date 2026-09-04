""" tp2"""


import pytest
from app.utils import predict
from fastapi.testclient import TestClient
from app.main import app


def test_predict_success():
    # Données d'entrée
    input_data = [1.0, 2.0, 3.0]

    # Valeur attendue
    expected_output = 6.0

    # Exécution de la fonction
    result = predict(input_data)

    # Vérification
    assert result == expected_output
 
 
 
 client = TestClient(app)

def test_predict_fails_on_wrong_expectation():
    payload = {"features": [1.0, 2.0, 3.0]}
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    WRONG_PREDICTION = 999.99
    
    # On s'attend à ce que l'assertion suivante ÉCHOUE
    with pytest.raises(AssertionError):
        assert data["prediction"] == WRONG_PREDICTION

    