# import packages
import matplotlib.pyplot as plt
from descartes import PolygonPatch
import csv
from matplotlib import cm, colors
import numpy as np
import pickle

## Do not edit below #################################################################
with open('map_data.pkl', 'rb') as f:
    country_map = pickle.load(f)
    
# create empty list of names
map_countries = []

# iterate through the country_map data
for i in range(len(country_map)):
    # append country name to list
    map_countries.append(country_map[i]['properties']['COUNTRY'])
    
## Do not edit above #################################################################  
    
# In[Step 1]
# load happiness data in below and save in a list. The list should contain a dictionary
# for each country's data

happiness_data = []
with open('happy_2015.csv', 'r') as happiness15_file:
    reader = csv.DictReader(happiness15_file)
    for rows in reader:
        happiness_data.append(rows)


# In[Step 2]
# Create empty list for happy data countries
countries = []
# add all the happy data countries to the list
for i in range(len(happiness_data)):
    countries.append(happiness_data[i]['Country'])

# In[Step 3]
# create numpy array to store the happiness scores
happiness_score = np.zeros(len(happiness_data))
# add the happiness scores to numpy array
for i in range(len(happiness_data)):
    happiness_score[i] = float(happiness_data[i]['Happiness Score'])

# In[Step 4]
# scale the happiness scores by multiplying by 10^(number of decimal places)
scaled_scores = []
for scores in happiness_score:
    scaled_scores.append(scores * 1000)

# In[Step 5]
# Next we need to match the index of the map countries to the happy countries

# create a list for the country indexes
country_index = []

# Use a for-loop and the list.index() method to find the index of the matching country name in
# happy data. Add the index to our list country indexes
for country in countries:
    country_index.append(map_countries.index(country))

# In[Step 6: Create colormap]    

# For our happiness measure create a colormap
# The syntax for a colormap is: color_map = cm.get_cmap('viridis', number_of_colors)
# The following syntax will produce a color for a happiness value eg. happiness 140 -> 
# happy_color = color_map[140]
scaled_range = max(scaled_scores) - min(scaled_scores)
color_map = cm.get_cmap('viridis', scaled_range)
scaled_scores = scaled_scores - min(scaled_scores)

# color all countries grey
map_colors = ['Grey']*265

# create a for-loop, for each country we have in happy data, replace map_colors at the country index
# with the color map converted of happiness score.

for i in range(len(country_index)):
    map_colors[country_index[i]] = color_map(int(scaled_scores[i]))


##### Do not edit below this line ####################################################   
# Create a new figure window
fig = plt.figure()

ax = fig.add_subplot(111)

# iterate through the map and plot each country
for i in range(len(country_map)):
    
    # plot the country patch, fc=facecolor, ec=edgecolor
    ax.add_patch(PolygonPatch(country_map[i]['geometry'], fc=map_colors[i], ec=map_colors[i]))
    
# set the axis to be equal in aspect     
ax.axis('equal')

##### Do not above below this line ################################################
    
# In[Step 7: Add the colorbar code for google docs]   
    
#  Add the colorbar code for google docs

norm = colors.Normalize(vmin=np.min(happiness_score),vmax=np.max(happiness_score))
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_ticks([np.min(happiness_score),np.max(happiness_score)])
cbar.set_ticklabels(['Least happy','Most happy'])

# save the figure output as a png
fig.savefig('test_world.png')
   

    
    
    