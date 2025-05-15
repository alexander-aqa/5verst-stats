from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Запуск браузера
    page = browser.new_page()
    page.goto("https://5verst.ru")
    print("Заголовок страницы:", page.title())  # Проверка заголовка страницы
    browser.close()