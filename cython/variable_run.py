import pyximport

pyximport.install()
import variable

result = variable.integrate(10, 20, lambda i: 10)
print(result)
