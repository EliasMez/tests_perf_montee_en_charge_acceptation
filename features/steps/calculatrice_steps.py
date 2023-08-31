from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given("J'ouvre la page d'accueil Amazon.fr")
def step_open_amazon_home(context):
    context.driver = webdriver.Chrome('/home/<user>/chromedriver',chrome_options=chrome_options)
    context.driver.get("https://www.amazon.fr")

@when("J'accepte les cookies")
def step_accept_cookies(context):
    try:
        cookies_button =  context.driver.find_element(By.ID,"sp-cc-accept")
        cookies_button.click()
    except:
        pass

@when("Je recherche le produit {product}")
def step_search_product(context, product):
    search_box = context.driver.find_element(By.ID,"twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys(product)
    search_box.send_keys(Keys.RETURN)

@then("Les résultats de la recherche devraient s'afficher")
def step_verify_search_results(context):
    # Ajoutez ici les vérifications que vous souhaitez effectuer sur les résultats de la recherche
    pass

@then("Je ferme le navigateur")
def step_close_browser(context):
    context.driver.quit()
