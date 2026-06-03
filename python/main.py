import numpy as np
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print(a + b)   # [11 22 33 44]
print(a - b)   # [ 9 18 27 36]
print(a * b)   # [10 40 90 160]
print(a / b)   # [10. 10. 10. 10.]

# Useful functions
print(np.mean(a))   # Average = 25.0
print(np.max(a))    # 40
print(np.min(a))    # 10
print(np.sqrt(a))   # Square root
