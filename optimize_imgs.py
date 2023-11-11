from PIL import Image
import os

# Directory containing images
dir_name = 'imgs'

# Resize, compress, and convert images to WebP
for root, dirs, files in os.walk(dir_name):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(root, file)
            with Image.open(file_path) as img:
                # Resize if the largest dimension is greater than 1600 pixels
                if max(img.size) > 1600:
                    img.thumbnail((1600, 1600))
                # Save to WebP with a quality of 85
                output_path = os.path.splitext(file_path)[0] + '.webp'
                img.save(output_path, 'WEBP', quality=85)

print("Image optimization and conversion to WebP done!")