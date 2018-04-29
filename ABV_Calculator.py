# 28 April 2018
# This program will take user inputs for original and final gravities, and output the alcohol by volume.
# I have not decided if I should make this a function, a class, or just a scratch program.

print('___Alcohol by Volume Calculator by Bryce___\n') # Welcome text, new line
OG = input('Enter Original Gravity: ') # User inputs original gravity
FG = input('Enter Final Gravity: ') # User inputs final gravity
ABV = (float(OG)-float(FG))*131.25 # Inputs converted to floats, alcohol by volume is calculated
ABV = round(ABV,2) # rounded to two decimal places
print('Alcohol by volume: ' + str(ABV) +'%') # text-based output

# Here is the same operation implemented as a function:
def ABV(OG,FG):
    return round((OG-FG)*131.25,2)
