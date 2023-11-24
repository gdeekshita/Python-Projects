'''
    planets.py
    calculating the euclidean distance and plotting planets on an xy plane
'''
# Test cases
# Sun to Earth (Euclidean): 493.14 
# Sun to Pluto (Euclidean): 972.59
# Average distance to sun: 732.87

import matplotlib.pyplot as plt

sun_x = 100
sun_y = -100
sun_MSIZE = 20
sun_color = str('yellow')

def main():
    #ask user what two planets they want the distance of
    planet1 = str(input("Name of planet 1 whose distance from the sun you want to calculate? \n"))
    planet2 = str(input("Name of planet 2 whose distance from the sun you want to calculate? \n")) 
    #define filename based on planet chosen
    filename1 = planet1 + '.txt'
    filename2 = planet2 + '.txt'
    #open corresponding files and read lines
    with open (filename1, 'r') as infile:
        x1 = int(infile.readline())
        y1 = int(infile.readline())
        p1_MSIZE = int(infile.readline())
        p1_color = infile.readline().strip()
    with open (filename2, 'r') as infile:
        x2 = int(infile.readline())
        y2 = int(infile.readline())
        p2_MSIZE = int(infile.readline())
        p2_color = infile.readline().strip()    
        
    #computation for euclidean distance for planet 1 
    diffxsq1 = (x1 - sun_x) ** 2
    diffysq1 = (y1 - sun_y) ** 2
    elucidean1 = (diffxsq1 + diffysq1) ** 0.5
    
    #computation for euclidean distance for planet 2 
    diffxsq2 = (x2 - sun_x) ** 2
    diffysq2 = (y2 - sun_y) ** 2
    elucidean2 = (diffxsq2 + diffysq2) ** 0.5    
    
    #computation for average distance to sun
    avg = (elucidean1 + elucidean2)/2
    
    #display to users
    print("Sun to", planet1, "(Euclidean):", round(elucidean1,2))
    print("Sun to", planet2, "(Euclidean):", round(elucidean2,2))
    print("Average distance to sun:", round(avg,2))
    
    #graph points of planets and sun
    plt.plot(sun_x, sun_y, 'o', color = sun_color, markersize = sun_MSIZE, label = 'sun')
    plt.plot(x1, y1, 'o', color = p1_color, markersize = p1_MSIZE, label = planet1)
    plt.plot(x2, y2, 'o', color = p2_color, markersize = p2_MSIZE, label = planet2)
    
    #graph axes
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    
    #graph a title 
    plt.title("Y Position vs X Position of the sun/planets")
    
    #range of the axes
    plt.xlim(-200, 300)
    plt.ylim(-200, 1000)
    plt.legend() 
    
main ()        
