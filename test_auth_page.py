# python -m pytest -v --driver Chrome --driver-path chromedriver.exe test_auth_page.py
import time
from selenium.webdriver.common.by import By
import pytest
import os
from dotenv import load_dotenv
from pages.locators import AuthLocators

load_dotenv()
email = os.getenv('email')
email2 = os.getenv('email2')
password = os.getenv('password')
valid_email = os.getenv('valid_email')
sign_255 = os.getenv('sing_255')
login = os.getenv('login')
phone = os.getenv('phone')
special = os.getenv('special')
ls = os.getenv('ls')
fake_number = os.getenv('fake_number')
fake_pass = os.getenv('fake_pass')


# Проверка регистрации с валидными данными
def test_1_registr_valid_data(precondition):
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_WITH_PASS).click()
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_REG).click()
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_REG_NAME_FIELD).send_keys('Иван')
    pytest.driver.find_element(*AuthLocators.AUTH_REG_LASTNAME_FIELD).send_keys('Петров')
    pytest.driver.find_element(*AuthLocators.AUTH_EMAIL_FIELD).send_keys(email)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD_CONFIRM).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_BIGBTN_REG).click()
    time.sleep(1)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1').text == 'Подтверждение email'


# Проверка регистрации с вводом уже зарегистрированной почты
def test_2_registr_busy_email(precondition):
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_WITH_PASS).click()
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_REG).click()
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_REG_NAME_FIELD).send_keys('Иван')
    pytest.driver.find_element(*AuthLocators.AUTH_REG_LASTNAME_FIELD).send_keys('Петров')
    pytest.driver.find_element(*AuthLocators.AUTH_EMAIL_FIELD).send_keys(valid_email)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD_CONFIRM).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_BIGBTN_REG).click()
    time.sleep(1)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/h2').text == \
           'Учётная запись уже существует'


# Проверка регистрации с пустыми полями
def test_3_registr_empty_fields(precondition):
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_WITH_PASS).click()
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_REG).click()
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_BIGBTN_REG).click()
    time.sleep(1)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text != ''


# Регистрация с почтой из 255 знаков
def test_4_registr_email255(precondition):
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_WITH_PASS).click()
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_REG).click()
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_REG_NAME_FIELD).send_keys('Иван')
    pytest.driver.find_element(*AuthLocators.AUTH_REG_LASTNAME_FIELD).send_keys('Петров')
    pytest.driver.find_element(*AuthLocators.AUTH_EMAIL_FIELD).send_keys(sign_255)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD_CONFIRM).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_BIGBTN_REG).click()
    time.sleep(1)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/span').text != ''


# Проверка входа с валидныой почтой и не валидным паролем
def test_5_enter_fake_pass(precondition2):
    pytest.driver.find_element(*AuthLocators.AUTH_TAB_LOGIN).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(login)
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(fake_pass)
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_LOGIN).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.ID, 'form-error-message').text != ''


# Проверка входа с валидными данными
def test_6_enter_valid_data(precondition2):
    pytest.driver.find_element(*AuthLocators.AUTH_TAB_LOGIN).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(login)
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_LOGIN).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[1]').text == 'Учетные данные'


# Проверка входа с пустыми полями
def test_7_enter_empty_fields(precondition2):
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_LOGIN).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text != ''


# Проверка входа с введенным логином в поле телефона
def test_8_enter_log_in_phone(precondition2):
    pytest.driver.find_element(*AuthLocators.AUTH_TAB_PHONE).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(login)
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_LOGIN).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[1]').text == 'Учетные данные'


# Проверка входа с введенным действующим номером телефона в поле логина
def test_9_enter_phone_in_log(precondition2):
    pytest.driver.find_element(*AuthLocators.AUTH_TAB_LOGIN).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(phone)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_LOGIN).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[1]').text == 'Учетные данные'


# Проверка входа с логином в 255 знаков
def test_10_enter_log_255(precondition2):
    pytest.driver.find_element(*AuthLocators.AUTH_TAB_LOGIN).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(sign_255)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_LOGIN).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'


# Проверка входа с логином из спецзнаков
def test_11_enter_special_in_log(precondition2):
    pytest.driver.find_element(*AuthLocators.AUTH_TAB_LOGIN).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(special)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_LOGIN).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'


# Проверка входа по коду с валидной почтой
def test_12_enter_by_code_valid_email(precondition3):
    pytest.driver.find_element(*AuthLocators.AUTH_EMAIL_FIELD).send_keys(valid_email)
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_GET_CODE).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.ID, 'rt-code-3').text == ''


# Проверка входа по коду с не зарегистрированной почтой
def test_13_enter_by_code_invalid_email(precondition3):
    pytest.driver.find_element(*AuthLocators.AUTH_EMAIL_FIELD).send_keys(email2)
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_GET_CODE).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/span').text != ''


# Проверка галочки "запомнить меня"
def test_14_checkbox_remember_me(precondition2):
    pytest.driver.find_element(*AuthLocators.AUTH_TAB_LOGIN).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(login)
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_CHECKBOX).click()
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_LOGIN).click()
    time.sleep(2)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_LOGOUT).click()
    assert pytest.driver.find_element(*AuthLocators.AUTH_CHECKBOX).is_selected() == True


# Проверка входа с введенным действующим лицевым номером счета в поле логина
def test_15_enter_ls_in_log(precondition2):
    pytest.driver.find_element(*AuthLocators.AUTH_TAB_LOGIN).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(ls)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_LOGIN).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[1]').text == 'Учетные данные'


# Проверка входа с введенной действующей почтой  в поле с номером телефона
def test_16_enter_valid_email_in_phone(precondition2):
    pytest.driver.find_element(*AuthLocators.AUTH_TAB_PHONE).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(valid_email)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_LOGIN).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[1]').text == 'Учетные данные'


# Проверка входа с введенным номером лицевого счета  в поле с номером телефона
def test_17_enter_ls_in_phone(precondition2):
    pytest.driver.find_element(*AuthLocators.AUTH_TAB_PHONE).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(ls)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_LOGIN).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[1]').text == 'Учетные данные'


# Проверка входа по коду с несуществующим номером телефона
def test_18_enter_by_code_fake_numb(precondition3):
    pytest.driver.find_element(*AuthLocators.AUTH_EMAIL_FIELD).send_keys(fake_number)
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_GET_CODE).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.XPATH,
                                      '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/span').text != ''


# Проверка входа по коду с несуществующей почтой
def test_19_enter_by_code_uregistr_email(precondition3):
    pytest.driver.find_element(*AuthLocators.AUTH_EMAIL_FIELD).send_keys(email)
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_GET_CODE).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="rt-code-0"]').text != ''


# Восстановление пароля с зарегестрированной почтой
def test_20_pass_recovery_valid_email(precondition4):
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(valid_email)
    time.sleep(10)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_CONTINUE).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.ID, 'rt-code-3').text == ''


# Восстановление пароля с не зарегистрированной почтой
def test_21_pass_recovery_invalid_email(precondition4):
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(email)
    time.sleep(10)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_CONTINUE).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.ID, 'form-error-message').text != ''


# Восстановление пароля с несуществующей почтой
def test_22_pass_recovery_fake_email(precondition4):
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(email2)
    time.sleep(10)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_CONTINUE).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.ID, 'form-error-message').text != ''


# Восстановление пароля с зарегистрированным номером телефона
def test_23_pass_recovery_valid_phone(precondition4):
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(phone)
    time.sleep(10)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_CONTINUE).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-radio__label-desc').text != ''


# Восстановление пароля с не зарегистрированным номером телефона
def test_24_pass_recovery_fake_phone(precondition4):
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(fake_number)
    time.sleep(10)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_CONTINUE).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.ID, 'form-error-message').text != ''


# Восстановление пароля с действующим номером лицевого счета
def test_25_pass_recovery_ls(precondition4):
    pytest.driver.find_element(*AuthLocators.AUTH_TAB_LS).click()
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(ls)
    time.sleep(10)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_CONTINUE).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-radio__label-desc').text != ''


# Восстановление пароля с действующим логином
def test_26_pass_recovery_valid_login(precondition4):
    pytest.driver.find_element(*AuthLocators.AUTH_USERNAME_FIELD).send_keys(login)
    time.sleep(13)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_CONTINUE).click()
    time.sleep(2)
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-radio__label-desc').text != ''


# Проверка регистрации с несовпадающими паролями
def test_27_registr_diff_pass(precondition):
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_WITH_PASS).click()
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_REG).click()
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_REG_NAME_FIELD).send_keys('Иван')
    pytest.driver.find_element(*AuthLocators.AUTH_REG_LASTNAME_FIELD).send_keys('Петров')
    pytest.driver.find_element(*AuthLocators.AUTH_EMAIL_FIELD).send_keys(email)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD_CONFIRM).send_keys(fake_pass)
    pytest.driver.find_element(*AuthLocators.AUTH_BIGBTN_REG).click()
    time.sleep(1)
    assert pytest.driver.find_element(By.CLASS_NAME,
                                      'rt-input-container__meta--error').text != ''


# Проверка регистрации с именем введенным латинскими буквами
def test_28_registr_lat_name(precondition):
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_WITH_PASS).click()
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_BTN_REG).click()
    time.sleep(1)
    pytest.driver.find_element(*AuthLocators.AUTH_REG_NAME_FIELD).send_keys('Ivan')
    pytest.driver.find_element(*AuthLocators.AUTH_REG_LASTNAME_FIELD).send_keys('Petrov')
    pytest.driver.find_element(*AuthLocators.AUTH_EMAIL_FIELD).send_keys(email)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_PASSWORD_CONFIRM).send_keys(password)
    pytest.driver.find_element(*AuthLocators.AUTH_BIGBTN_REG).click()
    time.sleep(1)
    assert pytest.driver.find_element(By.CLASS_NAME,
                                      'rt-input-container__meta--error').text != ''
