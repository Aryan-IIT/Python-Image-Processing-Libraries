from PIL import Image
from IPython.display import display

def create_gradient_image(width, height, start_color, end_color):
    gradient_pixels = []

    for y in range(height):
        for x in range(width):
            r = int(start_color[0] + (end_color[0] - start_color[0]) * x / width)
            g = int(start_color[1] + (end_color[1] - start_color[1]) * x / width)
            b = int(start_color[2] + (end_color[2] - start_color[2]) * x / width)
            gradient_pixels.append((r, g, b))

    return gradient_pixels

# read image and convert to RGB
original_image = Image.open("readonly/msi_recruitment.gif")
original_image = original_image.convert('RGB')

# create a list of 9 images with different tonalities
tonalities = []

# First row: Cool blue gradient
tonalities.extend([Image.new("RGB", original_image.size) for _ in range(3)])

# Second row: Purple gradient
tonalities.extend([Image.new("RGB", original_image.size) for _ in range(3)])

# Third row: Yellow gradient
tonalities.extend([Image.new("RGB", original_image.size) for _ in range(3)])

# Populate tonalities with gradients
for i in range(3):
    start_color, end_color = (0, 0, 255), (255, 255, 255)  # Cool blue gradient
    tonalities[i].putdata(create_gradient_image(original_image.width, original_image.height, start_color, end_color))

for i in range(3, 6):
    start_color, end_color = (128, 0, 128), (255, 255, 255)  # Purple gradient
    tonalities[i].putdata(create_gradient_image(original_image.width, original_image.height, start_color, end_color))

for i in range(6, 9):
    start_color, end_color = (255, 255, 0), (255, 255, 255)  # Yellow gradient
    tonalities[i].putdata(create_gradient_image(original_image.width, original_image.height, start_color, end_color))

# create a contact sheet with tonalities atop the original image
contact_sheet = Image.new(original_image.mode, (original_image.width * 3, original_image.height * 3))
x = 0
y = 0

for tonality in tonalities:
    blended_image = Image.blend(original_image, tonality, alpha=0.5)
    
    # Lets paste the blended image into the contact sheet
    contact_sheet.paste(blended_image, (x, y))

    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x + original_image.width == contact_sheet.width:
        x = 0
        y = y + original_image.height
    else:
        x = x + original_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
display(contact_sheet)
