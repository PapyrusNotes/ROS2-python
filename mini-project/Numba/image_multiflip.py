import numpy as np
import numba
from numba import cuda
from PIL import Image

import os


# CUDA Kernel to flip images by X-axis
@cuda.jit
def flip_images_x_axis(input_images, output_images, width, height, channels, num_images):
    # Get thread indices
    img_idx = cuda.blockIdx.x  # Each block processes a different image
    x = cuda.threadIdx.x + cuda.blockIdx.y * cuda.blockDim.x
    y = cuda.threadIdx.y + cuda.blockIdx.z * cuda.blockDim.y

    # Check bounds
    if img_idx >= num_images or x >= width or y >= height:
        return

    # Calculate flipped row index
    flipped_y = height - 1 - y

    # Compute linear indices for input and output
    img_offset = img_idx * width * height * channels
    input_idx = img_offset + (y * width + x) * channels
    output_idx = img_offset + (flipped_y * width + x) * channels

    # Copy pixel data for all channels
    for c in range(channels):
        output_images[output_idx + c] = input_images[input_idx + c]


# Function to process multiple images using CUDA
def flip_multiple_images_cuda(images):
    num_images, height, width, channels = images.shape
    total_pixels = num_images * height * width * channels

    # Flatten images into a 1D buffer for CUDA processing
    d_input_images = cuda.to_device(images.flatten())
    d_output_images = cuda.device_array_like(d_input_images)

    # Define grid and block sizes
    block_size = (16, 16)  # Each block contains 16x16 threads
    grid_size = (
    num_images, (width + block_size[0] - 1) // block_size[0], (height + block_size[1] - 1) // block_size[1])

    # Launch the CUDA kernel
    flip_images_x_axis[grid_size, block_size](d_input_images, d_output_images, width, height, channels, num_images)

    # Copy back the result
    flipped_images = d_output_images.copy_to_host().reshape((num_images, height, width, channels))

    return flipped_images


def load_samples(directory):
    images = []

    for filename in sorted(os.listdir(directory)):
        img_path = os.path.join(directory, filename)
        img = Image.open(img_path)
        img_array = np.array(img, dtype=np.uint8)
        images.append(img_array)

    return np.array(images)


# Test the CUDA function
if __name__ == "__main__":
    num_images = 221  # Number of images
    height = 512  # Image height
    width = 1400  # Image width
    channels = 3  # RGB channels

    # Create test images (random RGB images)
    # images = np.random.randint(0, 256, (num_images, height, width, channels), dtype=np.uint8)
    # print(type(images))
    # print(type(images[0]))
    images = load_samples('')

    # CUDA Job start
    flipped_images = flip_multiple_images_cuda(images)
    # CUDA Job ends

