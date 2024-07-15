from matplotlib import image 
from matplotlib import pyplot
import os

# Read an image file
path = os.path.dirname(os.path.abspath(__file__))

lennafilename = path + '/samples/' + 'lenna.bmp'
lennadata = image.imread(lennafilename)


usafilename = path + '/Exercises2/' + 'usaxs.bmp'
usadata = image.imread(usafilename)

print(usadata.shape[0], usadata.shape[1])
# Add some color boundaries to modify an image array
lenna_plot_data = lennadata.copy()
usa_plot_data = usadata.copy()

for width in range(262,512):
    for height in range(250):
        lenna_plot_data[height][width] = usa_plot_data[height][width-262]
# Write the modified images
image.imsave(path+'/Exercises2/'+'usaflag-mod.jpg', lenna_plot_data)

# use pyplot to plot the image
pyplot.imshow(lenna_plot_data)
pyplot.show()