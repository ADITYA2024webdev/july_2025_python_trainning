from add import add,sub,mul
from mymodule import checkNumber

result = add(5, 10)
print(result )

result = sub(10, 5)
print(result)

result = mul(5, 10)
print(result)

try:
    checkNumber(500)
except exception as e:
    print(e)