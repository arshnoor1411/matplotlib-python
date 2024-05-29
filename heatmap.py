import numpy as np 
import matplotlib.pyplot as plt 
  
data = np.random.random(( 12 , 12 )) 
plt.imshow( data ) 
  
plt.title( "2-D Heat Map" ) 
plt.show() 