import numpy as np
import matplotlib.pyplot as plt

def alternating_squares(square_size, num_squares_height, num_squares_width):
    
    height = square_size * num_squares_height
    width = square_size * num_squares_width
    
    black_square = np.zeros((square_size, square_size))
    white_square = np.ones((square_size, square_size)) * 255
    
    img = np.zeros((height, width))

    for i in range(num_squares_height):
        for j in range(num_squares_width):
            if (i + j) % 2 == 0:
                img[i * square_size: (i + 1) * square_size, j * square_size: (j + 1) * square_size] = black_square
            else:
                img[i * square_size: (i + 1) * square_size, j * square_size: (j + 1) * square_size] = white_square
    
    return img.astype(np.uint8)

square_size = 50
num_squares_height = 8
num_squares_width = 8

img = alternating_squares(square_size, num_squares_height, num_squares_width)

plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')
plt.show()