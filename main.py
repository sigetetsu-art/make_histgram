import numpy as np
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt

def color_map(input_image, image_name):
    fig, ax = plt.subplots() #グラフを作るための基盤的なもの
    image = ax.imshow(input_image, cmap = plt.get_cmap("jet"), vmin = 0, vmax = 255)
    ax.grid(False)
    #divider = make_axes_locatable(ax)
    fig.colorbar(image)
    ax.axis("off")
    ax.set_title(image_name, fontsize = "xx-large")
    fig.subplots_adjust(left = 0.05, right = 0.91, bottom = 0.05, top = 0.91)
    fig.savefig(f"{image_name}.png")

def histgram(input_image, image_name):
    histo, bins = np.histogram(np.asarray(input_image).flatten(), range = (0, 255), bins = 256) #histo...輝度値の出現回数 bins...輝度値の値（０～２５５）が入る。
    fig, ax = plt.subplots()
    ax.plot(bins[1:], histo)
    normalize = matplotlib.colors.Normalize(vmin = 0, vmax = 255)
    cmap = plt.get_cmap("jet")
    [ax.fill_between(bins[:-1][i:i+2], histo[i:i+2], color=cmap(normalize(bins[:-1][i]))) for i in range(len(histo))]
    plt.savefig(f"{image_name}_graph.png")    

def main():
    input_image = Image.open("airplane.pgm")
    input_image = np.asarray(input_image)
    image_name = "airplane"
    
    color_map(input_image, image_name)
    histgram(input_image, image_name)

main()  

     
    