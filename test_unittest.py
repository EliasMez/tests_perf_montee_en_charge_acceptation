import unittest
from unittest.mock import patch
from calculatrice import additionner, soustraire
from random_string import len_random_string


class TestCalculatrice(unittest.TestCase):
    # test de qualité/fonctionnel et test de non-régression/régression
    def test_additionner(self):
        # non-régression (ancien code)
        self.assertEqual(additionner(2, 3),5)
        self.assertEqual(additionner(-1, 1),0)
        # fonctionnel (nouveau code)
        self.assertEqual(additionner([1, 2, 3], 4),10)

    # test de qualité
    def test_soustraire(self):
        self.assertEqual(soustraire(5, 3),2)
    
    # Test d'intégration : Vérifier que l'addition et la soustraction fonctionnent ensemble.
    def test_additionner_et_soustraire(self):
        resultat_addition = additionner(5, 3)        
        self.assertEqual(soustraire(resultat_addition, 3), 5)
        resultat_addition_list = additionner([1, 2, 3], 4)
        self.assertEqual(soustraire(resultat_addition_list, 3), 7)

class TestRandomString(unittest.TestCase):

    @patch('random_string.get_random_string')
    def test_len_random_string(self,mock_get_random_string):
        mock_get_random_string.return_value = "Hello"
        self.assertEqual(len_random_string(),5)

if __name__ == "__main__":
    unittest.main()
