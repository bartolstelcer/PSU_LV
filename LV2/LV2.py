# 1.

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,3,3,2,1])
y = np.array([1,1,2,2,1])

plt.plot(x, y, linewidth = 1 , marker = "." , markersize = 1)
plt.axis([0, 4, 0, 4])
plt.xlabel("x os")
plt.ylabel("y os")
plt.title("Primjer")

plt.show()

# 2.

import numpy as np
import matplotlib.pyplot as plt

# a)

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

# b)

plt.scatter(data[:, 1], data[:, 0], label='mpg vs. hp')

# c) 

plt.scatter(data[:, 1], data[:, 0], s=data[:, 5]*10, alpha=0.5, label='mpg vs. hp & wt')

plt.xlabel('Konjske snage')
plt.ylabel('Potrosnja goriva')
plt.title('Ovisnost potrosnje automobila o konjskim snagama')
plt.show()

# d)

mpgVrijednosti = data[:, 0]
minVrijednosti = np.min(mpgVrijednosti)
maxVrijednosti = np.max(mpgVrijednosti)
meanVrijednosti = np.mean(mpgVrijednosti)
print("Minimalna potrosnja:", minVrijednosti)
print("Maksimalna potrosnja:", maxVrijednosti)
print("Srednja potrosnja:", meanVrijednosti)

# e)

cilindar6 = data[data[:, 3] == 6]
mpgVrijednosti6 = cilindar6[:, 0]
minVrijednosti6 = np.min(mpgVrijednosti6)
maxVrijednosti6 = np.max(mpgVrijednosti6)
meanVrijednosti6 = np.mean(mpgVrijednosti6)
print("Minimalna potrosnja:", minVrijednosti6)
print("Maksimalna potrosnja:", maxVrijednosti6)
print("Srednja potrosnja:", meanVrijednosti6)

# 3.

import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("C:\\Users\\Admin\\Desktop\\Bartol\\pythonProgrami\\tiger.png")

# a)

brightened_img = np.clip(img * 1.2, 0, 1)

# b)

rotated_img = np.rot90(img)

# c)

flipped_img = np.fliplr(img)

# d)

downsample_factor = 10
downsampled_img = img[::downsample_factor, ::downsample_factor]

# e)

height, width, _ = img.shape
cropped_img = np.zeros_like(img)

start_x = width // 2
end_x = width

cropped_img[:, :end_x - start_x, :] = img[:, start_x:end_x, :]

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

axes[0, 0].imshow(img)
axes[0, 0].set_title('Originalna slika')

axes[0, 1].imshow(brightened_img)
axes[0, 1].set_title('Posvijetljena slika')

axes[0, 2].imshow(rotated_img)
axes[0, 2].set_title('Rotirana slika')

axes[1, 0].imshow(flipped_img)
axes[1, 0].set_title('Zrcaljena slika')

axes[1, 1].imshow(downsampled_img)
axes[1, 1].set_title('Smanjena rezolucija')

axes[1, 2].imshow(cropped_img)
axes[1, 2].set_title('Prepolovljena slika')

plt.tight_layout()
plt.show()

# 4.

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
