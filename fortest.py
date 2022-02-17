from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from urllib.parse import urlparse
from pages.main_page import mainPage
from pages.config import DOMAIN, CHROMEDRPATH


def test_pay_link():
    base = DOMAIN
    driver = webdriver.Chrome(CHROMEDRPATH)

    mp = mainPage(driver, base)
    mp.link_pay_click()
    assert urlparse(driver.current_url).path == '/help/'


def test_certificate_link():
    base = DOMAIN
    driver = webdriver.Chrome(CHROMEDRPATH)

    mp = mainPage(driver, base)
    mp.link_cert_click()
    assert urlparse(driver.current_url).path == '/top/certificates/'


def test_rating_link():
    base = DOMAIN
    driver = webdriver.Chrome(CHROMEDRPATH)

    mp = mainPage(driver, base)
    mp.link_rating_click()
    assert urlparse(driver.current_url).path == '/rating/'


def test_new_link():
    base = DOMAIN
    driver = webdriver.Chrome(CHROMEDRPATH)

    mp = mainPage(driver, base)
    mp.link_new_click()
    assert urlparse(driver.current_url).path == '/novelty/'


def test_discount_link():
    base = DOMAIN
    driver = webdriver.Chrome(CHROMEDRPATH)

    mp = mainPage(driver, base)
    mp.link_discount_click()
    assert urlparse(driver.current_url).path == '/search/'


def test_contacts_link():
    base = DOMAIN
    driver = webdriver.Chrome(CHROMEDRPATH)

    mp = mainPage(driver, base)
    mp.link_contacts_click()
    assert urlparse(driver.current_url).path == '/contact/'


def test_support_link():
    base = DOMAIN
    driver = webdriver.Chrome(CHROMEDRPATH)

    mp = mainPage(driver, base)
    mp.link_support_click()
    assert urlparse(driver.current_url).path == '/support/'


def test_map_link():
    base = DOMAIN
    driver = webdriver.Chrome(CHROMEDRPATH)

    mp = mainPage(driver, base)
    mp.link_map_click()
    assert urlparse(driver.current_url).path == '/maps/'


def test_quantity_in_basket():
    base = DOMAIN
    driver = webdriver.Chrome(CHROMEDRPATH)

    mp = mainPage(driver, base)

    assert mp.get_basket_quan() == '0'


def test_search():
    base = DOMAIN
    driver = webdriver.Chrome(CHROMEDRPATH)
    mp = mainPage(driver, base)

    mp.set_search("Пушкин")
    mp.search_click()

    link_map = driver.find_element(By.CLASS_NAME, "b-stab-e-slider-item-e-txt-m-small")

    L = link_map.text.split()
    quan = int(L[0]+L[1])
    assert quan > 0
