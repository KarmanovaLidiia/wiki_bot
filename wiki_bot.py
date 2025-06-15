from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Укажи путь к chromedriver
driver_path = r"C:\Users\karml\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
browser = webdriver.Chrome(service=service)


def open_article(query):
    search_url = f"https://ru.wikipedia.org/wiki/{query.replace(' ', '_')}"
    browser.get(search_url)
    time.sleep(2)

def show_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        if paragraph.text.strip():
            print("\n🧾", paragraph.text)
            input("👉 Нажми Enter, чтобы прочитать следующий абзац...")

def go_to_random_link():
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        class_name = element.get_attribute("class")
        if class_name == "hatnote navigation-not-searchable":
            hatnotes.append(element)
    if hatnotes:
        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
        time.sleep(2)
        return True
    else:
        print("❌ Связанных страниц не найдено.")
        return False

def main():
    query = input("🔍 Что будем искать в Википедии? ")
    open_article(query)

    while True:
        print("\n💡 Что будем делать дальше?")
        print("1. Читать статью")
        print("2. Перейти на связанную страницу")
        print("3. Выйти")
        choice = input("👉 Введи 1, 2 или 3: ").strip()

        if choice == "1":
            show_paragraphs()
        elif choice == "2":
            if not go_to_random_link():
                print("Попробуй другой запрос или пункт меню.")
        elif choice == "3":
            print("👋 Пока! Спасибо за игру.")
            break
        else:
            print("🤔 Я не понял, выбери 1, 2 или 3.")

    browser.quit()

if __name__ == "__main__":
    main()
