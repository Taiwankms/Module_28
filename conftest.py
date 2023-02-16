import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def precondition():
    url = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_decosystems&redirect_uri=https://start.rt.ru/&response_type=code&scope=openid&theme=light"
    pytest.driver = webdriver.Chrome()
    pytest.driver.get(url)
    WebDriverWait(pytest.driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="standard_auth_btn"]')))

    yield

    pytest.driver.quit()


@pytest.fixture
def precondition2():
    url = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=98c21045-0667-40d8-b4ea-1026f64f4225&theme=light&auth_type"
    pytest.driver = webdriver.Chrome()
    pytest.driver.get(url)
    time.sleep(2)

    yield

    pytest.driver.quit()


@pytest.fixture
def precondition3():
    url = "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_decosystems&redirect_uri=https://start.rt.ru/&response_type=code&scope=openid&theme=light"
    pytest.driver = webdriver.Chrome()
    pytest.driver.get(url)
    time.sleep(5)

    yield

    pytest.driver.quit()


@pytest.fixture
def precondition4():
    url = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=ccW2QpRau0w"
    pytest.driver = webdriver.Chrome()
    pytest.driver.get(url)
    time.sleep(5)

    yield

    pytest.driver.quit()
