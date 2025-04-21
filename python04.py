# 1번
i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("------")

# 2번
i = 5
while i >= 1:
    print("*" * i)
    i -= 1
print("------")

# 3번
i = 1
while i <= 5:
    print("*" * i)
    i += 1

i = 4
while i >= 1:
    print("*" * i)
    i -= 1
print("------")

# 4번
dan = 2
while dan <= 9:
    i = 1
    while i <= dan:
        print(f"{dan} x {i} = {dan * i}")
        i += 1
    print("-" * 20)
    dan += 1
