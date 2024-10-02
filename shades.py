import colorsys
import argparse
import os
import sys
from PIL import Image, ImageDraw, ImageFont
from rich.console import Console
from rich.table import Table

def hex_to_rgb(hex_color):
    """Converts a hex color to RGB."""
    return tuple(int(hex_color[i:i+2], 16) / 255 for i in (1, 3, 5))

def rgb_to_hsl(r, g, b):
    """Converts RGB to HSL."""
    r /= 255
    g /= 255
    b /= 255
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    h = 0
    s = 0
    l = (cmax + cmin) / 2

    if cmax == cmin:
        h = 0
        s = 0
    else:
        if l < 0.5:
            s = (cmax - cmin) / (cmax + cmin)
        else:
            s = (cmax - cmin) / (2 - cmax - cmin)

        if cmax == r:
            h = (g - b) / (cmax - cmin)
        elif cmax == g:
            h = 2 + (b - r) / (cmax - cmin)
        else:
            h = 4 + (r - g) / (cmax - cmin)

        h *= 60
        if h < 0:
            h += 360

    return h, s, l

def hsl_to_hex(h, s, l):
    """Converts HSL to hex."""
    r, g, b = colorsys.hls_to_rgb(h / 360, l, s)
    return "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255), int(b * 255))

def print_swatch(color, name=None):
    """Returns a string representing a color swatch."""
    r, g, b = hex_to_rgb(color)
    return f"<span style='background-color:#{color}; width: 20px; height: 20px; display: inline-block;'></span>"

def generate_shades(hex_color, shades, directory=None):
    """Generates shades of a color."""
    try:
        h, s, l = rgb_to_hsl(*[int(hex_color[i:i+2], 16) for i in (1, 3, 5)])
    except ValueError:
        print("Invalid hex color")
        return

    table = Table(show_header=True, header_style="purple", title_style="bold green", title="Shades of " + hex_color, style="bold magenta")
    table.add_column("Value", style="cyan")
    table.add_column("Hex Code")
    table.add_column("Color")

    image_width = len(shades) * 150
    image_height = 100
    image = Image.new("RGB", (image_width, image_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    markdown_text = f"# Shades of {hex_color}\n\n"

    for i, shade in enumerate(shades):
        try:
            shade_factor = 1 - (shade / 100)
            new_l = l * shade_factor
            new_hex_color = hsl_to_hex(h, s, new_l)
            table.add_row(str(shade) + "%", new_hex_color, f"[{new_hex_color}][b]{new_hex_color}[/b]")            

            draw.rectangle((i * 150, 0, (i + 1) * 150, 50), fill=new_hex_color)
            draw.text((i * 150 + 10, 60), new_hex_color, font=font, fill=(0, 0, 0))
            markdown_text += f"* {shade}% shade: {new_hex_color}\n"
            print_swatch(new_hex_color, f"{shade}% shade")
        except ValueError:
            print(f"Invalid shade value: {shade}")
            continue

    console = Console()
    console.print(table)

    if directory:
        os.makedirs(directory, exist_ok=True)

    image_filename = "shades.png"
    markdown_filename = "shades.md"

    custom_name = input("Enter a custom name for the files (or press Enter to use default): ")
    if custom_name:
        image_filename = f"{custom_name}.png"
        markdown_filename = f"{custom_name}.md"

    base, extension = os.path.splitext(image_filename)
    counter = 1
    image_path = os.path.join(directory, image_filename)
    markdown_path = os.path.join(directory, markdown_filename)
    while os.path.exists(image_path):
        image_filename = f"{base}_{counter}{extension}"
        markdown_filename = f"{base}_{counter}.md"
        image_path = os.path.join(directory, image_filename)
        markdown_path = os.path.join(directory, markdown_filename)
        counter += 1

    try:
        image.save(image_path)
        with open(markdown_path, "w") as f:
            f.write(markdown_text)
    except PermissionError:
        print("Permission denied. Unable to save files.")
        return

    console.print(f"Files saved as {image_path} and {markdown_path} :computer:")

def main():
    parser = argparse.ArgumentParser(description="Generate shades of a color from your hexcodes in markdown and PNG format.")
    parser.add_argument("-c", "--colors", nargs="+", help="One or more hex colors to generate shades for")
    parser.add_argument("-s", "--shades", help="List of shades to generate (comma-separated values: 20,40,60,80,100)", default="20,40,60,80,100")
    parser.add_argument("-d", "--directory", help="Specify the output directory (default: current working directory)", default=os.getcwd())
    args = parser.parse_args()

    if args.colors is None:
        parser.print_help()
        sys.exit(0)

    for color in args.colors:
        try:
            color = color.lstrip('#')  # remove leading # symbol
            if not color.startswith("#"):
                color = "#" + color
            if len(color) != 7:
                print("Error: Invalid color code. Please use a 6-digit hex code.")
                continue
            if not all(c in '0123456789ABCDEFabcdef' for c in color[1:]):
                print("Error: Invalid color code. Please use only hexadecimal digits.")
                continue
        except Exception as e:
            print(f"Error: {e}")
            continue

        shades = [int(x) for x in args.shades.split(",")]

        generate_shades(color, shades, args.directory)

if __name__ == "__main__":
    main()
    
