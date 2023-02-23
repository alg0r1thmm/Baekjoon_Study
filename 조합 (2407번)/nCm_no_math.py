#math 라이브러리 활용해서 쉽게 구현 가능
import math #math 라이브러리 선언

n, m = map(int, input().split())

result = math.factorial(n) // (math.factorial(m) * math.factorial(n-m))

print(result)