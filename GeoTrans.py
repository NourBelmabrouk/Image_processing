import config
import PIL.Image
from PIL import ImageTk




def translate(canvas, xx, yy, wrap_around):
    curr = config.current_image.load()
    x_size = config.current_image.size[0]
    y_size = config.current_image.size[1]

    new_img = PIL.Image.new('RGB', (x_size, y_size))

    for x in range(x_size):
        for y in range(y_size):
            rgb_val = curr[x, y]
            x_new = x + xx if not wrap_around else (x + xx) % x_size
            y_new = y + yy if not wrap_around else (y + yy) % y_size

            if x_new in range(x_size) and y_new in range(y_size):
                new_img.putpixel((x_new, y_new), rgb_val)

    tk_img = ImageTk.PhotoImage(new_img)
    canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
    canvas.image = tk_img       # Reference for Python's GC
    config.current_image = new_img      # Keep reference of current image


def scale(canvas, factor):
    from math import floor
    curr = config.current_image.load()
    x_size = config.current_image.size[0]
    y_size = config.current_image.size[1]

    new_img = PIL.Image.new('RGB', (x_size, y_size))

    # x_ratio = original width / modified width
    # y_ratio = original height / modified height

    scaling_factor = 1 / (factor / 100)

    for x in range(x_size):
        for y in range(y_size):
            px = floor(x * scaling_factor)
            py = floor(y * scaling_factor)
            if px in range(x_size) and py in range(y_size):
                rgb_val = curr[px, py]
                new_img.putpixel((x, y), rgb_val)

    tk_img = ImageTk.PhotoImage(new_img)
    canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
    canvas.image = tk_img       # Reference for Python's GC
    config.current_image = new_img      # Keep reference of current image


def shear(canvas, factor, x_shear):
    curr = config.current_image.load()
    x_size = config.current_image.size[0]
    y_size = config.current_image.size[1]
    if x_shear:
        new_img = PIL.Image.new('RGB', (x_size + int(factor * y_size), y_size))
    else:
        new_img = PIL.Image.new('RGB', (x_size, y_size + int(factor * x_size)))

    for x in range(x_size):
        for y in range(y_size):
            rgb_val = curr[x, y]
            x_new = x + int(factor * y) if x_shear else x
            y_new = y if x_shear else y + int(factor * x)
            new_img.putpixel((x_new, y_new), rgb_val)

    tk_img = ImageTk.PhotoImage(new_img)
    canvas.create_image(400, 300, image=tk_img)     # (xpos, ypos, imgsrc)
    canvas.image = tk_img       # Reference for Python's GC
    config.current_image = new_img      # Keep reference of current image
