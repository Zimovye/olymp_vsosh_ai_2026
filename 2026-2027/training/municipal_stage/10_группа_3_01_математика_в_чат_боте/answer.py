difference = 110

is_found = False
for a in range(2, difference + 1):
    b = 1
    while a**b - a * b <= difference:
        correct = a**b
        model = a * b
        if correct - model == difference:
            print(model)
            is_found = True
            break
        b += 1
    if is_found:
        break
