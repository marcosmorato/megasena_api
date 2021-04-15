from selenium import webdriver
import geckodriver_autoinstaller

geckodriver_autoinstaller.install()


def get_megasena_result():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")

    driver = webdriver.Firefox(options=firefox_options)

    driver.get("https://www.google.com/search?q=caixa+mega+sena")

    elem = driver.find_elements_by_class_name("zSMazd.UHlKbe")

    numbers = [e.get_property("innerText") for e in elem]
    driver.close()

    return numbers
