"""Person"""


class Person(object):
    """
    Class Person
    ----
    La classe Person prend en compte les détails suivants :
    * height (float) : La hauteur de la personne
    * weight (float) : Le poids de la personne
    * age (int) : L'age de la personne
    * gender (str) : Le genre de la personne
    """

    def __init__(self, height: float, weight: float, age: int = 0, gender: str = "Male") -> None:
        """Constructeur"""
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender

    def calculate_bmi(self) -> float:
        """Calculate Body Mass Index (BMI) given height in meters and weight in kilograms."""
        height = self.height / 100
        return self.weight / (height ** 2)

    def calculate_bmr(self) -> float:
        """Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation."""
        if self.gender.lower() == 'male':
            bmr = 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        elif self.gender.lower() == 'female':
            bmr = 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)
        else:
            raise ValueError('Les options "Male" et "Female" sont uniquement disponible pour le moment.')
        return bmr
