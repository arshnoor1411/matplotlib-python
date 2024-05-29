import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
print(x)

# Customized Histogram
data = np.random.randn(1000)
 
sns.histplot(data, bins=30, kde=True, color='lightgreen', edgecolor='red')
 
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Customized Histogram with Density Plot')
 
plt.show()