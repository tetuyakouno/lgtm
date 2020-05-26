from PIL import Image, ImageDraw, ImageFont

# Setting message ratio 
MAX_RATIO = 0.8
# Const for font
FONT_MAX_SIZE = 256
FONT_MIN_SIZE = 24
# The path of font file
FONT_NAME = '/home/vagrant/myDev/tmp/Arial Bold.ttf'
FONT_COLOR_WHITE = (255, 255, 255, 0)
# CONST for output
OUTPUT_NAME = 'output.png'
OUTPUT_FORMAT = 'PNG'

def save_with_message(fp, message):
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)
    # Caluculate size
    image_width, image_height = image.size
    message_area_width = image_width * MAX_RATIO
    message_area_height = image_height * MAX_RATIO
    # Caluculate font size
    for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE, -1):
        font = ImageFont.truetype(FONT_NAME, font_size)
        # Needed size for drawing
        text_width, text_height = draw.textsize(
            message, font=font)
        w = message_area_width - text_width
        h = message_area_height - text_height
        # Accept the values of height and width
        if w > 0 and h > 0:
            position = ((image_width - text_width) / 2,
                        (image_height - text_height) / 2)
            # Draw the massage
            draw.text(position, message,
                      fill=FONT_COLOR_WHITE, font=font)
            break
    #Save the picture
    image.save(OUTPUT_NAME, OUTPUT_FORMAT)

