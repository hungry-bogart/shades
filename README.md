Here is the README file in Markdown format:

# Color Shade Generator

A Python script that generates shades of a given color and saves them to an image and a markdown file.

## Usage

To use the script, simply run it from the command line and provide the hex code of the color you want to generate shades for. You can also specify custom shades using the `-s` option.

```bash
python color_shade_generator.py <hex_color> [-s <shades>]
```

## Options

* `-s <shades>`: Specify custom shades as a comma-separated list of percentages (e.g. `10,30,50,70,90`).
* `-d`: Use default shades (20% increments) instead of custom shades.

## Example

To generate shades of the color `#FF79C6` using the default shades, run the following command:

```bash
python color_shade_generator.py "#FF79C6" -d
```

To generate shades of the color `#FF79C6` using custom shades, run the following command:

```bash
python color_shade_generator.py "#FF79C6" -s "10,30,50,70,90"
```

## Output

The script will generate an image file named `shades.png` and a markdown file named `shades.md` in the current working directory. The image file will contain the color swatches, and the markdown file will contain the hex codes for each shade.

## Requirements

* Python 3.x
* The `PIL` library is not actually used in this script, I apologize for the mistake earlier. The `colorsys` library is used instead.

## License

This script is released under the MIT License. See the LICENSE file for details.

Note: I removed the Pillow library from the requirements section, as it is not actually used in the script.
