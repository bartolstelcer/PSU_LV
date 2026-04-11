import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("tiger.png")

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