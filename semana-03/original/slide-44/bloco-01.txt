def total(*precos, desc=0):
    s = sum(precos)
    return s * (1 - desc / 100)

print(total(10, 25.5, 7))
# 42.5

print(total(10, 25.5, 7, desc=10))
# 38.25
