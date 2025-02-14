"""Test"""

import math
import sys
import os
import pytest

from flask.testing import FlaskClient
from typing import Generator, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def client() -> Generator[FlaskClient, Any, None]:
    """Installations sanitaires pour créer un client de test pour l'application Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestHealthCalculator(object):
    """Classe de tests pour l'application Health Calculator."""

    @classmethod
    def test_home_page(cls, client: FlaskClient) -> None:
        """Test de la page d'accueil."""
        response = client.get('/')
        assert response.status_code == 200
        assert b"Health Calculator Service" in response.data

    @classmethod
    def test_calculate_bmi(cls, client: FlaskClient) -> None:
        """Test du calcul de l'IMC."""
        response = client.post('/api/bmi', json={"height": 175, "weight": 70})
        assert response.status_code == 200
        assert math.isclose(response.json['bmi'], 23, rel_tol=1e-2)

    @classmethod
    def test_calculate_bmr_male(cls, client: FlaskClient) -> None:
        """Test du calcul du BMR pour un homme."""
        response = client.post('/api/bmr', json={"height": 175, "weight": 70, "age": 30, "gender": "male"})
        assert response.status_code == 200
        assert math.isclose(response.json['bmr'], 1695, rel_tol=1e-2)

    @classmethod
    def test_calculate_bmr_female(cls, client: FlaskClient) -> None:
        """Test du calcul du BMR pour une femme."""
        response = client.post('/api/bmr', json={"height": 160, "weight": 60, "age": 25, "gender": "female"})
        assert response.status_code == 200
        assert math.isclose(response.json['bmr'], 1389, rel_tol=1e-2)

    @classmethod
    def test_calculate_bmi_missing_data(cls, client: FlaskClient) -> None:
        """Test du calcul de l'IMC avec des données manquantes."""
        # Weight is missing
        response = client.post('/api/bmi', json={"height": 175})
        assert response.status_code == 400
        assert response.json['error'] == "'height' et 'weight' sont requis."

    @classmethod
    def test_calculate_bmr_missing_data(cls, client: FlaskClient) -> None:
        """Test du calcul du BMR avec des données manquantes."""
        # Gender is missing
        response = client.post('/api/bmr', json={"height": 175, "weight": 70, "age": 30})
        assert response.status_code == 400
        assert response.json['error'] == "'height', 'weight', 'age' et 'gender' sont requis."
