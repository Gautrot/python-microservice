"""App"""
from flask import Flask, request, jsonify, render_template, Response
from dotenv import load_dotenv
from flasgger import Swagger
import os

from classes.person import Person

load_dotenv()
app = Flask(__name__)
Swagger(app)


@app.route('/')
def home() -> Response | str:
    """Page d'accueil"""
    return render_template('index.html')


@app.route('/api/bmi', methods=['POST'])
def calculate_bmi_endpoint() -> Response | tuple:
    """
    Calcule le BMI
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            height:
              type: number
              description: Hauteur (cm)
              example: 1.75
            weight:
              type: number
              description: Poids (kg)
              example: 70
    responses:
      200:
        description: Résultat du calcul BMI
        examples:
          application/json: |
            {
              "bmi": 22.86
            }
      400:
        description: height et weight sont requis.
    """
    data = request.json
    height = data.get('height')
    weight = data.get('weight')

    if not height or not weight:
        return jsonify({"error": "'height' et 'weight' sont requis."}), 400

    try:
        height = float(height)
        weight = float(weight)
    except ValueError:
        return jsonify({"error": "'height' et 'weight' doit être des nombres."}), 400

    person = Person(height, weight)
    bmi = person.calculate_bmi()
    return jsonify({"bmi": bmi})


@app.route('/api/bmr', methods=['POST'])
def calculate_bmr_endpoint() -> Response | tuple:
    """
    Calculate BMR
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            height:
              type: number
              description: Hauteur (cm)
              example: 175
            weight:
              type: number
              description: Poids (kg)
              example: 70
            age:
              type: number
              description: Age
              example: 30
            gender:
              type: string
              description: Genre
              example: male
    responses:
      200:
        description: Résultat du calcul BMR
        examples:
          application/json: |
            {
              "bmr": 1745.4
            }
      400:
        description: "'height', 'weight', 'age' et 'gender' sont requis."
    """
    data = request.json
    height = data.get('height')
    weight = data.get('weight')
    age = data.get('age')
    gender = data.get('gender')

    if not height or not weight or not age or not gender:
        return jsonify({"error": "'height', 'weight', 'age' et 'gender' sont requis."}), 400

    try:
        height = float(height)
        weight = float(weight)
        age = int(age)
    except ValueError:
        return jsonify({"error": "'height', 'weight' et 'age' doit être des nombres."}), 400

    person = Person(height, weight, age, gender)
    bmr = person.calculate_bmr()
    return jsonify({"bmr": bmr})


@app.route('/bmi')
def bmi_page() -> Response | str:
    """Render the BMI calculator page."""
    return render_template('bmi.html')


@app.route('/bmr')
def bmr_page() -> Response | str:
    """Render the BMR calculator page."""
    return render_template('bmr.html')


if __name__ == '__main__':
    app.run(
        host=os.getenv("FLASK_HOST", '0.0.0.0'),
        port=os.getenv("FLASK_PORT", 5000),
        debug=os.getenv("FLASK_DEBUG", False),
    )
