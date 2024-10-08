# module_4_1.py

from fake_math import divide as fake_divide
from true_math import divide as true_divide


result_fake = fake_divide(10, 0)  
result_true = true_divide(10, 0)


print(f"Результат деления в fake_math: {result_fake}")
print(f"Результат деления в true_math: {result_true}")


