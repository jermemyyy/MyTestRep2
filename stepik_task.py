import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        
        # Заполняем обязательные поля
        self.browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
        self.browser.find_element_by_css_selector(".first_block .second").send_keys("Petrov")
        self.browser.find_element_by_css_selector(".first_block .third").send_keys("test@test.com")
        
        # Отправляем форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()
        
        # Проверяем результат
        welcome_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        
        # Пытаемся заполнить обязательные поля (второй тест должен упасть)
        self.browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
        self.browser.find_element_by_css_selector(".first_block .second").send_keys("Petrov")
        self.browser.find_element_by_css_selector(".first_block .third").send_keys("test@test.com")
        
        # Отправляем форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()
        
        # Проверяем результат
        welcome_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()