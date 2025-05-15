# 5verst-stats
collecting statistics

**Цель проекта**: Парсинг моих пробежек с сайта [5verst.ru](https://5verst.ru), анализ статистики и тестирование работы сайта.  
**Технологии**: Python, Playwright, Pandas (для анализа), Git.

## 📌 Задачи
1. **Парсинг данных**:
   - Сбор данных о пробежках (дата, дистанция, время, маршрут).
   - Сохранение в CSV/SQLite.
2. **Визуализация**:
   - Графики прогресса (Matplotlib/Plotly).
3. **Тестирование сайта**:
   - Автоматические тесты через Playwright (логин, отображение статистики).


📅 План действий
***************************************************************
День 1-2: Парсинг данных о пробежках
Изучить, как устроен сайт 5verst.ru (через DevTools → Network).

Написать скрипт, который заходит в мой профиль и собирает:

Даты пробежек
Дистанции
Время
Темп

***************************************************************
День 3-4: Сохранение данных (CSV/SQLite)
Использовать pandas или стандартный csv модуль:

python
import csv
with open('runs.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Distance", "Time"])

***************************************************************
День 5-6: Визуализация (Matplotlib/Plotly)
Установить pip install matplotlib и построить простой график:

python
import matplotlib.pyplot as plt
plt.plot(dates, distances)
plt.savefig('runs.png')  # Сохраняем график

***************************************************************
День 7-8: Docker + GitHub Actions
Создать Dockerfile:

dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install playwright requests
RUN playwright install
CMD ["python", "scraper.py"]
Настроить GitHub Actions для автоматического запуска (создай .github/workflows/main.yml).

***************************************************************
День 9-10: Тестирование сайта 5verst (Playwright)
Написать UI-тесты:

python
def test_login(page):
    page.goto("https://5verst.ru/login")
    page.fill("#email", "ваш-email")
    page.fill("#password", "пароль")
    page.click("#submit")
    assert page.url == "https://5verst.ru/dashboard"


🚀 Напоминалки 
***************************************************************
GitHub:
.gitignore для Python → шаблон.
GitHub Actions → документация.

Playwright:
Использовать page.wait_for_selector() для надёжности.
Режим headless=False для отладки.


## 🛠 Установка
1. Клонирование репозитория:
   git clone https://github.com/alexander-aqa/5verst-stats.git
   cd 5verst-stats


## 🛠 Создание виртуальнго окружения:

	bash
	python -m venv .venv
	source .venv/bin/activate  # Linux/Mac


## 🛠 Установка зависимости:

	bash
	pip install -r requirements.txt
	playwright install

🚀 Запуск
	Основной скрипт:
	python scraper.py

	Тесты:
	python -m pytest tests/


📂 Структура проекта

5verst-stats/

	├── .venv/               # Виртуальное окружение (не в Git)
	├── data/                # Данные пробежек (CSV)
	├── scraper.py           # Основной скрипт
	├── requirements.txt     # Зависимости
	└── README.md            # Описание

📈 Пример вывода

	python
	# Пример данных из data/runs.csv:
		Дата,		Дистанция (км), Время		Темп
		2024-05-20, 	5.2, 		00:28:15	5:30 кин/км
		2024-05-18, 	3.8,		00:21:40 	5:30 кин/км


# Этот файл можно (желательно/рекомендуется) редактировать по мере развития проекта!

	1. **Цель** — напоминает, зачем вы это делаете (важно для мотивации и понимания проекта).  
	2. **Технологии** — помогает мне (и, возможно, другим участникам проекта) быстро вспомнить стек.  
	3. **Структура** — чтобы не потеряться в файлах.  
	4. **Примеры** — даже простой вывод даёт понимание результата.  

	**Что дальше?**  
	- Добавить реальные примеры данных после парсинга.  
	- Обновлять раздел **"Пример вывода"** по мере развития.
	- Парсинг данных по мне лично.
	- Сделать парсинг для любого юзера (из 5_вёрст)
	- Парсить данные с других ресурсов (russiarunning.com)
	- Опредеоиться с кахих еще ресурсов можно парсить данные.


# Важно для виртуального окружения

	Папка .venv не должна коммититься (убедитесь, что она в .gitignore).
	Для установки зависимостей в новом окружении используйте:
	pip install -r requirements.txt

# Документация в помощь
.gitignore для Python → шаблон.   https://github.com/github/gitignore/blob/main/Python.gitignore

GitHub Actions → документация.   https://docs.github.com/en/actions
