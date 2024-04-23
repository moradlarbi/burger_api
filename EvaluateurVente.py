from Burger import Burger
from typing import List
import unittest
from unittest.mock import Mock
class EvaluateurVente:
    def __init__(self, date, list_burger: List[Burger]):
        self.date = date
        self.list_burger = list_burger

    def ajouter_burger(self, burger: Burger):
        self.list_burger.append(burger)
    
    def evaluer_list(self):
        return len(self.list_burger)
    
    def evaluer_vente(self):
        total = 0
        for burger in self.list_burger:
            total += burger.prix
        return total
    
    def evaluer_vente_allergene(self):
        for burger in self.list_burger:
            print(burger.list_allergene)
    

class TestEvaluateur(unittest.TestCase):
    def setUp(self):
        self.evaluateurVente = EvaluateurVente(date="2021-01-01", list_burger=[])
        self.burger = Mock(prix=15, description="Burger", list_allergene=["lait", "oeuf"], cuisson="saignant", unite=10000)

    def test_ajouter_burger(self):
        self.evaluateurVente.ajouter_burger(self.burger)
        self.assertIn(self.burger, self.evaluateurVente.list_burger)
    
    def test_evaluer_list(self):
        self.evaluateurVente.ajouter_burger(self.burger)
        self.assertEqual(self.evaluateurVente.evaluer_list(), 1)

    def test_evaluer_vente(self):
        self.evaluateurVente.ajouter_burger(self.burger)
        self.assertEqual(self.evaluateurVente.evaluer_vente(), 15)

    

if __name__ == '__main__':
    unittest.main()


