relevances = [8, 3, 1, 1, 6]
ranks = [1, 2, 3, 4, 5]

# Чтобы сумма была минимальной, большие релевантности
# умножаем на маленькие ранги.
sorted_relevances = sorted(relevances, reverse=True)

products = []
for relevance, rank in zip(sorted_relevances, ranks):
    product = relevance * rank
    products.append(product)
    print("Релевантность:", relevance,
          "ранг:", rank,
          "произведение:", product)

minimum_penalty = sum(products)
print("Минимальный штраф:", minimum_penalty)
