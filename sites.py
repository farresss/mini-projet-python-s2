from selenium.webdriver.common.by import By
sites = {
    "github": {
      "url": "https://github.com/login",
      "email": (By.ID, "login_field"),
      "mdp": (By.ID, "password"),
      "submit": (By.NAME, "commit")
    },

    "stackoverflow": {
      "url": "https://stackoverflow.com/users/login",
      "email": (By.ID, "email"),
      "mdp" : (By.ID, "password"),
      "submit" : (By.ID, "submit-button")
    },

     "leetcode": {
      "url": "https://leetcode.com/accounts/login/",
      "email": (By.ID, "id_login"),
      "mdp" : (By.ID, "id_password"),
      "submit" : (By.ID, "signin_btn")
    },

    

    











}