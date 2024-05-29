import matplotlib.pyplot as plt
import numpy as np
 
# Line Chart
x = np.array([1, 2, 3, 4])
y = x*2
 
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Any suitable title") 
plt.show()
 
# Annotation Line Chart
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
 
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-')
 
for i, (xi, yi) in enumerate(zip(x, y)):
    plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')
 
plt.title('Line Chart with Annotations')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
 
plt.grid(True)
 
plt.show()

# Multiple Line Chart
x = np.array([1, 2, 3, 4])
y = x*2
 
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Any suitable title")
plt.show() 

plt.figure()
x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]
plt.plot(x1, y1, '-.')
 
plt.show()