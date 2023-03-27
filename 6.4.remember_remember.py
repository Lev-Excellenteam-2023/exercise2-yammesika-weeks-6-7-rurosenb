from PIL import Image


def decrypt_message(image_path):
    """
    Decrypts a message from an image file and returns it.
    """
    # Load the image and get its dimensions
    img = Image.open(image_path)
    img = img.convert('RGB')
    width, height = img.size
    pixels = img.load()

    # Extract the line numbers from the black pixels in each column
    lines = []
    for w in range(width):
        for h in range(height):
            if pixels[w, h] == (1, 1, 1):
                lines.append(h)

    # Convert the line numbers to characters using the chr() function
    message = ''.join(chr(line_number) for line_number in lines)

    return message


if __name__ == '__main__':
    print(decrypt_message('C:/Users/rosen/Downloads/Notebooks-master/Notebooks-master/week06/resources/code.png'))
