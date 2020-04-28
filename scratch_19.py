from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    # Открываем страницу http://suninjuly.github.io/alert_accept.html
    browser.get(link)

    # Нажимаем на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Ждем загрузки страницы
    time.sleep(1)

    # Переходим на вторую вкладку
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    # Считываем значение x
    x = browser.find_element_by_id('input_value').text

    # Вводим значение функции calc() для х
    browser.find_element_by_id('answer').send_keys(calc(x))

    # Нажимаем на кнопку Submit
    browser.find_element_by_tag_name('button').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
