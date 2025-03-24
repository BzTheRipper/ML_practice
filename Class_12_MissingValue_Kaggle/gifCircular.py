import imageio
import numpy as np

# Load the GIF file
file_path = "./Scene-2.gif"  # Change this to your actual file path
gif = imageio.mimread(file_path)

# Get image dimensions
height, width, _ = gif[0].shape
center = (width // 2, height // 2)
radius = min(center)  # Radius for circular crop

# Create a circular mask
y, x = np.ogrid[:height, :width]
mask = (x - center[0])**2 + (y - center[1])**2 <= radius**2

# Apply circular mask and ensure correct dtype
circular_gif_transparent = []
for frame in gif:
    frame = frame.astype(np.uint8)  # Convert frame to uint8
    alpha_channel = np.where(mask, 255, 0).astype(np.uint8)  # Ensure alpha is also uint8
    frame_rgba = np.dstack([frame, alpha_channel])  # Add alpha channel
    circular_gif_transparent.append(frame_rgba)

# Save the transparent circular GIF with infinite looping
output_path = "circular_scene_transparent-2.gif"
imageio.mimsave(output_path, circular_gif_transparent, format="GIF", duration=0.1, loop=0)

print("Circular transparent looping GIF 2 saved as:", output_path)
