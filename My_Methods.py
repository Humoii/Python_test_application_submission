from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class My_Methods:

    def send_key(driver, xpath, key, tries=3):

        for i in range(tries):
            try:
                el = driver.find_element(by=By.XPATH, value=xpath)
                el.send_keys(key)
                return True
            except Exception:
                return False

    def click_ENTER(driver, xpath, tries=3):
        for i in range(tries):
            try:
                el = driver.find_element(by=By.XPATH, value=xpath)
                el.send_keys(Keys.ENTER)
                return True
            except Exception:
                el.send_keys(Keys.ENTER)
                return False

    def click(driver, xpath, tries=3):

        for i in range(tries):
            try:
                el = driver.find_element(by=By.XPATH, value=xpath)
                el.click()
                return True
            except Exception:
                return False
    def farewell_message():
        print("201")
        
    # def test_assert(driver, xpath):

    #     try:
    #         el = driver.find_element(by=By.XPATH, value=xpath)
    #         if el.text == 'ОСТАВИТЬ ОТЗЫВ':
    #             return print("201")
    #     except Exception:
    #         return False