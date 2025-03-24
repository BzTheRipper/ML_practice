from rembg import remove
from PIL import Image
import os

# Load the uploaded image
input_path = "./asd.png"
print(os.path.exists(input_path))
output_path = "asd.png"

# Open image
image = Image.open(input_path)

# Remove background
image_no_bg = remove(image)

# Create a new blue background
blue_bg = Image.new("RGB", image_no_bg.size, (0, 0, 255))

# Paste the image onto the blue background
blue_bg.paste(image_no_bg, (0, 0), image_no_bg)

# Save the processed image
blue_bg.save(output_path)

# Return the path of the processed image
output_path