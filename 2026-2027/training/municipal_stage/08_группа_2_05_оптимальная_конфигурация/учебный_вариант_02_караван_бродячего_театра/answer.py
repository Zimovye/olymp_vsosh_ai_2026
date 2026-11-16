k, r, B = map(int, input().split(" "))

cnt = 0
min_cart = float("inf")
max_cart = float("-inf")
for storytellers in range(1, 8 * B + 1):
    puppeteers = storytellers * k
    total = puppeteers + storytellers + r
    if total % 8 == 0:
        carts = total // 8

        if carts <= B:
            cnt += 1
            min_cart = min(min_cart, carts)
            max_cart = max(max_cart, carts)

if cnt != 0:
    print(cnt, min_cart, max_cart)
else:
    print("0 0 0")
