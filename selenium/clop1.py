"""""
Напишите программу которая автоматически зайдет на https://store.steampowered.com/ в поле поиска отправит стратегии
и соберет названия всех стратегий на 1 странице.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.ChromiumEdge()
driver.get("https://store.steampowered.com/")
search_field = driver.find_element(by="name", value="term")
search_field.clear()
search_field.send_keys("стратегии")
search_field.submit()
game_titles = []
game_elements = driver.find_elements(By.XPATH, "//span[@class='title']")
for game in game_elements:
    game_titles.append(game.text)
for title in game_titles:
    print(title)
driver.quit()
