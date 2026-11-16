limit = 128000
history = 500
words_per_page = 400
reasoning_percent = 15

reasoning_per_page = words_per_page * reasoning_percent // 100
answer_per_page = words_per_page

units_per_page = words_per_page + reasoning_per_page + answer_per_page
available_units = limit - history
max_pages = available_units // units_per_page

print(max_pages)
