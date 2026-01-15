from PIL import Image

# ASCII characters to represent different pixel intensities
ASCII_CHARS = ["@", "#", "?", "1", "0", "%", "*", "+", ";", ":", ",", "."]

# resize the image to desired width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    return image.resize((new_width, new_height))

# convert each pixel to grayscale
def grayify(image):
    return image.convert("L")

# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    # 256 (total colors) / 12 (number of ASCII characters) = 22 (every 22 shades of gray will be represented by one ASCII character)
    characters = "".join([ASCII_CHARS[pixel // 22] for pixel in pixels])
    return characters

# convert image to ascii
def generate_ascii(image, new_width=100):
    new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))
    
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] 
                             for index in range(0, pixel_count, new_width)])
    return ascii_image