import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the figure and axes
fig, ax = plt.subplots(figsize=(12, 9))  # Keeping the figure size consistent

# Define colors
green_color = '#78AB46'  # Replace with the correct green color code
yellow_color = '#F9E814'  # Replace with the correct yellow color code
Red_color = '#FF0000'  # Replace with the correct RED color code
Gray_color = '#808080'  # Assuming the top bar is the Gray color as
Colors= '#808080' #Placeholder

# Create a thinner black line separator, extending across the entire width including the white box

for x in range(11):
    ax.add_patch(patches.Rectangle((-5, -3*x+27.5), 30, 0.01, edgecolor='black', facecolor='black'))
    
    
#crate the line
def my_function(Y,Z):
    #Crate the asesment for the 
    if(True):#what ever rull you make wither it was another class or anothe data strucsher matherd
        Colors=green_color
    ax.add_patch(patches.Rectangle((3, Y), Z, 0.4, edgecolor='none', facecolor=yellow_color))    
    if(True):#what ever rull you make wither it was another class or anothe data strucsher matherd
        Colors=green_color
    ax.add_patch(patches.Rectangle((10.3, Y), 4, 0.4, edgecolor='none', facecolor=yellow_color))
    if(True):#what ever rull you make wither it was another class or anothe data strucsher matherd
        Colors=green_color
    ax.add_patch(patches.Rectangle((14.6, Y), 4, 0.4, edgecolor='none', facecolor=yellow_color))
    if(True):#what ever rull you make wither it was another class or anothe data strucsher matherd
        Colors=green_color
    ax.add_patch(patches.Rectangle((18.9, Y), 3, 0.4, edgecolor='none', facecolor=yellow_color))
    if(True):#what ever rull you make wither it was another class or anothe data strucsher matherd
        Colors=green_color
    ax.add_patch(patches.Rectangle((22.2, Y), 2, 0.4, edgecolor='none', facecolor=yellow_color))
#crate MILs
def my_MIL1(X,Y,Z):
    for i in range(Z):
        square = patches.Rectangle((X+i+3, Y),0.93, 2, edgecolor='none', facecolor=Colors)
        ax.add_patch(square)
        # Add the text
        ax.text(X+i+3.5, Y+1, f'G{i+1}', color='black', weight='bold', fontsize=6, ha='center', va='center')
        
def my_MIL2(X,Y):
    for i in range(4):
        square = patches.Rectangle((X+i+3, Y),0.93, 2, edgecolor='none', facecolor=Colors)
        ax.add_patch(square)
        # Add the text
        ax.text(X+i+3.5, Y+1, f'Q{i+1}', color='black', weight='bold', fontsize=6, ha='center', va='center')
    
def my_MIL3(X,Y):
    for i in range(4):
        square = patches.Rectangle((X+i+3, Y),0.93, 2, edgecolor='none', facecolor=Colors)
        ax.add_patch(square)
        # Add the text
        ax.text(X+i+3.5, Y+1, f'Q{i+1}', color='black', weight='bold', fontsize=6, ha='center', va='center')
    
def my_MIL4(X,Y):
    for i in range(3):
        square = patches.Rectangle((X+i+3, Y),0.93, 2, edgecolor='none', facecolor=Colors)
        ax.add_patch(square)
        # Add the text
        ax.text(X+i+3.5, Y+1, f'Q{i+1}', color='black', weight='bold', fontsize=6, ha='center', va='center')
    
def my_MIL5(X,Y):
    for i in range(2):
        square = patches.Rectangle((X+i+3, Y),0.93, 2, edgecolor='none', facecolor=Colors)
        ax.add_patch(square)
        # Add the text
        ax.text(X+i+3.5, Y+1, f'Q{i+1}', color='black', weight='bold', fontsize=6, ha='center', va='center')
    






# Add colem text
ax.text(5.5, 31, "CRR Performance Summary", color='black', weight='bold', fontsize=9, ha='right')
ax.text(1.8, 30, "Domain Summary", color='black', weight='bold', fontsize=6, ha='right')

ax.text(5.7, 30, "MIL-1 Performed", color='black', weight='bold', fontsize=6, ha='right')
ax.text(5.7, 29.1, "Domain practices and\nbeing performed.", color='black', fontsize=5, ha='right')

ax.text(12.8, 30, "MIL-2 Planned:", color='black', weight='bold', fontsize=6, ha='right')
ax.text(13, 28.5, "Domain practices are\nsupported by planning,\npolicy,  stakeholders,\nand standerds.", color='black', fontsize=5, ha='right')

ax.text(17, 30, "MIL-3 Managed:", color='black', weight='bold', fontsize=6, ha='right')
ax.text(17, 28.5, "Domain practices are\nsupported by\ngoverance and\nadequate resources.", color='black', fontsize=5, ha='right')

ax.text(21.5, 30, "MIL-4 Managed:", color='black', weight='bold', fontsize=6, ha='right')
ax.text(21.5, 28.1, "Domain practices are\nsupported by\nmeasurement,\nmonitoring, and\nexecutive oversight.", color='black', fontsize=5, ha='right')

ax.text(25, 30, "MIL-5 Managed:", color='black', weight='bold', fontsize=6, ha='right')
ax.text(25, 28.1, "Domain practices are\nsupported by\nmeasurement,\nmonitoring, and\nexecutive oversight.", color='black', fontsize=5, ha='right')

ax.text(2, 27, "Asset Management", color='black', weight='bold', fontsize=6, ha='right')
ax.text(1.1, 23.5, "Controls\nManagement", color='black', weight='bold', fontsize=6, ha='right')
ax.text(1.2, 19.8, "Configuration\nand Change\nManagement", color='black', weight='bold', fontsize=6, ha='right')
ax.text(1, 17.4, "Vulnerability\nManagement", color='black', weight='bold', fontsize=6, ha='right')
ax.text(1, 14.5, "Incident\nManagement", color='black', weight='bold', fontsize=6, ha='right')
ax.text(1.75, 11.3, "Service Continuity\n Management", color='black', weight='bold', fontsize=6, ha='right')
ax.text(1.75, 8.9, "Risk Management", color='black', weight='bold', fontsize=6, ha='right')
ax.text(1, 4.75, "External\nDependencies\nManagement", color='black', weight='bold', fontsize=6, ha='right')
ax.text(1, 2.35, "Training and\nAwareness", color='black', weight='bold', fontsize=6, ha='right')
ax.text(1, -0.9, "Situational\nAwareness", color='black', weight='bold', fontsize=6, ha='right')
#you can make an equation for this in excel and use a while loop for it
my_function(26.9,7)
my_function(23.9,4)
my_function(20.9,3)
my_function(17.9,4)
my_function(14.9,5)
my_function(11.9,4)
my_function(8.9,5)
my_function(5.9,5)
my_function(2.9,2)
my_function(-.2,3)
#you can make an equation for this in excel and use a while loop for it
my_MIL1(0,24.8,7)
my_MIL2(7.3,24.8)
my_MIL3(11.6,24.8)
my_MIL4(15.9,24.8)
my_MIL5(19.2,24.8)
#you can make an equation for this in excel and use a while loop for it
my_MIL1(0,21.8,4)
my_MIL2(7.3,21.8)
my_MIL3(11.6,21.8)
my_MIL4(15.9,21.8)
my_MIL5(19.2,21.8)
#you can make an equation for this in excel and use a while loop for it
my_MIL1(0,18.75,3)
my_MIL2(7.3,18.75)
my_MIL3(11.6,18.75)
my_MIL4(15.9,18.75)
my_MIL5(19.2,18.75)
#you can make an equation for this in excel and use a while loop for it
my_MIL1(0,15.78,4)
my_MIL2(7.3,15.78)
my_MIL3(11.6,15.78)
my_MIL4(15.9,15.78)
my_MIL5(19.2,15.78)
#you can make an equation for this in excel and use a while loop for it
my_MIL1(0,12.75,5)
my_MIL2(7.3,12.75)
my_MIL3(11.6,12.75)
my_MIL4(15.9,12.75)
my_MIL5(19.2,12.75)
#you can make an equation for this in excel and use a while loop for it
my_MIL1(0,9.8,4)
my_MIL2(7.3,9.8)
my_MIL3(11.6,9.8)
my_MIL4(15.9,9.8)
my_MIL5(19.2,9.8)
#you can make an equation for this in excel and use a while loop for it
my_MIL1(0,6.8,5)
my_MIL2(7.3,6.8)
my_MIL3(11.6,6.8)
my_MIL4(15.9,6.8)
my_MIL5(19.2,6.8)
#you can make an equation for this in excel and use a while loop for it
my_MIL1(0,3.8,5)
my_MIL2(7.3,3.8)
my_MIL3(11.6,3.8)
my_MIL4(15.9,3.8)
my_MIL5(19.2,3.8)
#you can make an equation for this in excel and use a while loop for it
my_MIL1(0,.8,2)
my_MIL2(7.3,.8)
my_MIL3(11.6,.8)
my_MIL4(15.9,.8)
my_MIL5(19.2,.8)
#you can make an equation for this in excel and use a while loop for it
my_MIL1(0,-2.25,3)
my_MIL2(7.3,-2.25)
my_MIL3(11.6,-2.25)
my_MIL4(15.9,-2.25)
my_MIL5(19.2,-2.25)
# Set the x and y limits to make the squares, bar, and line fit well in the figure
ax.set_xlim(-1, 30)
ax.set_ylim(-10, 30)

# Remove the axes
ax.axis('off')

# Show the plot
plt.show()
