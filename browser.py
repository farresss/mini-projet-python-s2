from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from password import get_mdp


driver = webdriver.Chrome()
driver.get("https://google.com")


def login_github_test(id_user, email):
  url = "https://github.com/login"
  mdp = get_mdp("github", id_user)

  driver = webdriver.Chrome()
  driver.get(url)

  driver.find_element(By.ID, "login_field").send_keys(email)
  driver.find_element(By.ID, "password").send_keys(mdp)
  driver.find_element(By.NAME, "commit").click()

  return driver