from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from My_Methods import My_Methods
import pytest
import atexit



@pytest.mark.parametrize('execution_number', range(2))
def test_application_submission(execution_number):
    assert True

    # создание веб драйвера
    driver = webdriver.Chrome()
    driver.get("https://piter-online.net/")
    driver.implicitly_wait(10)

    # поисковая строка и ввод улицы:"Тестовая линия"
    step1 = My_Methods.send_key(driver, "/html/body/div/div/div[1]/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[1]/input", "Тестовая линия")
    assert step1, "ввод улицы (Тестовая линия) не прошел"
        
    # прожать Enter после ввода улицы:"Тестовая линия"
    time.sleep(0.5)
    step2 = My_Methods.click_ENTER(driver, "/html/body/div/div/div[1]/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[1]/input")
    assert step2, "клик Enter не прошел, после ввода улицы: Тестовая линия"

    # ввода номера дома:"1"
    step3 = My_Methods.send_key(driver, "//*[@class='app152 app159 app158 app154 app172']", "1")
    assert step3, "не прошел ввод номера дома:(1)"

    # прожать Enter после ввода номера дома:"1"
    step4 = My_Methods.send_key(driver, "//*[@class='app152 app160 app161 app159 app158 app154 app172']", Keys.ENTER)
    assert step4, "клик Enter не прошел, после ввода номера дома:(1)"

    # нажимаем на выплывающий список "В КВАРТИРУ"
    step5 = My_Methods.click(driver, "//*[@class='app187']")
    assert step5, "не нажали на выплывающий список (В КВАРТИРУ)"

    # В выплывающем списке выбираем в офис
    step6 = My_Methods.click(driver, "//*[@class='app198'][3]", 10)
    assert step6, " В выплывающем списке не смогли выбрать на дачу"

    # прожать кнопку "Показать тарифы"
    step7 = My_Methods.click(driver, "/html/body/div/div/div[1]/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div")
    assert step7, " не смогли нажать на кнопку (Показать тарифы)"

    # вводим имя "Автотест"
    step8 = My_Methods.send_key(driver, "//*[@type='text']", "Автотест")
    assert step8, " не ввели имя (Автотест)"

    # вводим номер телефона "1111111111"
    step9 = My_Methods.send_key(driver, "//*[@type='tel']", "1111111111")
    assert step9, " не ввели номер телефона (1111111111)" 

    # прожимаем кнопку "Отправить заявку"
    time.sleep(0.5)
    step10 = My_Methods.click(driver, "//*[@id='root']/div/div[1]/div[3]/div[2]/div[1]/div/div/div/div[2]/div[1]/div[1]/div[4]/div")
    assert step10, " не нажали на кнопку (Отправить заявку)" 

    # проверка отправлена заявка"201" или выдаст ошибку "Заявка не отправлена"

    step11 = driver.find_element(By.XPATH, value='/html/body/div/div/div[1]/div[3]/div[2]/div[1]/div/div/div/div[2]/div/div/div/a/div')
    if (step11.text == 'ОСТАВИТЬ ОТЗЫВ')== True:
        atexit.register(My_Methods.farewell_message)
    else: assert step11.text == 'ОСТАВИТЬ ОТЗЫВ', "Заявка не отправлена"

    time.sleep(1)
    driver.quit()
