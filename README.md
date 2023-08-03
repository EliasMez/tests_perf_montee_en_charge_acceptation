pip install -r requirements.txt

# tests unitaire, intégration, performance

lancer tous les tests (unittests et pytest):
pytest

lancer les tests unittest :
python -m unittest discover


# tests de couverture

unittest:
coverage erase
coverage run --source=calculatrice test_unittest.py
coverage -m report
coverage html -d ./html_coverage_report -> visualiser dans calculatrice_py.html

pytest:
pytest --cov=calculatrice test_pytest_calculatrice.py


# test de montée en charge
lancer l'API dans un terminal:
uvicorn items_api:app --reload
lancer locust dans un autre terminal:
locust -f locust_scenario.py


# test d'acceptation

se placer dans le dossier features/steps
behave
