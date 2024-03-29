
import random
import numpy.random as ran
import numpy as np
import matplotlib.pyplot as plt
import pickle
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

'''voxelization.py - A program to map pixelated images / topological maps
to voxelated renderings based on pixel intensities 
Andrew Garcia, 2019'''
        
def build(N=2):
   
    'converting image to code; in command line:'
    import matplotlib.image as mpimg
    
    'load your .png file and process to .p format'  
    img = mpimg.imread("mountn.png")
    pickle.dump( img, open( "mountn.p", "wb" ) )
    
    'loading encrypted image'
    img = pickle.load( open( "mountn.p", "rb" ) )

    
    lum_img = img[:,:,0]
    
    'pixel dimensions (px x py)'

    
    px=lum_img.shape[0]
    py=lum_img.shape[1]

    pixcrit=np.linspace(0.1,0.9,N)[::-1]
    
    '''voxels'''
    px,py = int(px), int(py)
    x, y, z = np.indices((px, py, N))
    
    # draw cuboids in the top left and bottom right corners, and a link between them
    cube0 = (z == -1)
    voxels = cube0 
    
    for a in range(N):
        for i in range(px):
            for j in range(py):
                if lum_img[i,j] < pixcrit[a]:
                    newcube = (x == i) & (y == j) & (z == a) 
                    voxels = voxels | newcube
    
    'color map of voxels:'
#    camp=mpl.cm.Greens
    camp=mpl.cm.Reds

    colors = np.empty(voxels.shape, dtype=object)
    colors[voxels] = 'pink'
    
    kolors=['crimson','red','pink','black','grey','black']
    for a in range(N):
        for i in range(px):
            for j in range(py):
                colors[i][j][a] = camp(220-5*a)
        
    fig = plt.figure('output')
#    ax = plt.axes(projection='3d') 
    ax = fig.gca(projection='3d')
    
    ax.voxels(voxels, facecolors=colors, edgecolor='k')  
    
    plt.xlabel('')
    plt.ylabel('')
    plt.show()
    
build(50)