# 3.5.2.-*7.+@

str = input()
l = len(str)
digits = []
i = 0
while i < l - 1:
    c = str[i]
    if c.isdigit():
        j = i
        while j < l and str[j].isdigit():
            j += 1
        digits.append(int(str[i:j]))
        i = j + 1
    else:
        b = digits.pop()
        a = digits.pop()
        res = 0
        if c == "+":
            res = a + b
        elif c == "-":
            res = a - b
        elif c == "*":
            res = a * b
        elif c == "/":
            res = a // b
        digits.append(res)
        i += 1

print(digits.pop())
