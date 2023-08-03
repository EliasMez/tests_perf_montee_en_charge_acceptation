Feature: Recherche PS5 sur Amazon.fr

  Scenario: Recherche d'un produit
    Given J'ouvre la page d'accueil Amazon.fr
    When J'accepte les cookies
    And Je recherche le produit "PS5"
    Then Les résultats de la recherche devraient s'afficher
