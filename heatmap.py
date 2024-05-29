import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.colors as colors 
  
data = np.random.random(( 12 , 12 )) 
plt.imshow( data ) 
  
plt.title( "2-D Heat Map" ) 
plt.show() 

# Matplotlib colors
data = np.random.randint(0, 100, size=(8, 8)) 
  
colors_list = ['#0099ff', '#33cc33'] 
cmap = colors.ListedColormap(colors_list) 
  
plt.imshow(data, cmap=cmap, vmin=0,
           vmax=100, extent=[0, 8, 0, 8]) 
for i in range(8): 
    for j in range(8): 
        plt.annotate(str(data[i][j]), xy=(j+0.5, i+0.5), 
                     ha='center', va='center', color='white') 
  
cbar = plt.colorbar(ticks=[0, 50, 100]) 
cbar.ax.set_yticklabels(['Low', 'Medium', 'High']) 
  
plt.title("Customized heatmap with annotations") 
plt.xlabel("X-axis") 
plt.ylabel("Y-axis") 