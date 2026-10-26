limit = 1000
history = 100
words_per_page = 100
reasoning_percent = 20

reasoning_per_page = words_per_page * reasoning_percent // 100
answer_per_page = words_per_page

units_per_page = words_per_page + reasoning_per_page + answer_per_page
available_units = limit - history
max_pages = available_units // units_per_page

print("Свободно после истории:", available_units)
print("Исходный текст одной страницы:", words_per_page)
print("Рассуждения для одной страницы:", reasoning_per_page)
print("Ответ для одной страницы:", answer_per_page)
print("Всего на одну страницу:", units_per_page)
print("Максимальное число полных страниц:", max_pages)
print("Фактически занято:", history + max_pages * units_per_page)
