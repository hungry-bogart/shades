# Shades

A Python script that generates shades of a given hex color value and saves them to an image and a markdown file.

## Usage

To use the script, simply run it from the command line and provide the hex code of the color you want to generate shades for.

```bash
$ python shades.py
usage: shades.py [-h] [-c COLORS [COLORS ...]] [-s SHADES] [-d DIRECTORY]

Generate shades of a color from your hexcodes in markdown and PNG format.

options:
  -h, --help            show this help message and exit
  -c COLORS [COLORS ...], --colors COLORS [COLORS ...]
                        One or more hex colors to generate shades for
  -s SHADES, --shades SHADES
                        List of shades to generate (default: 20, 40, 60, 80, 100)
  -d DIRECTORY, --directory DIRECTORY
                        Specify the output directory (default: current working directory)
```

## Output

The script will generate an image file named `shades.png` and a markdown file named `shades.md` in the current working directory.

You can change the names of directories and filenames if you follow the prompts.

The image file will contain the color swatches and the markdown file will contain the hex codes for each shade.

You can use the directory flag if you'd like to save your files somewhere specific.

## Requirements

* Python 3.x
* Rich
* Pillow

## Installation

To install the script, run the following command:

This will install on your system directly into the current directory.

Clone the repository:

```git clone https://github.com/hungry-bogart/shades.git```

Enter the directory:

```cd shades```

Install the requirements:

```pip -r requirements.txt```

## Using a Virtual Environment (preferred)

To use the script in a virtual environment, run the following command:
Change "myenv" to the name of your virtual environment. It could be something like shades-env.

Create a virtual environment:
```python -m venv myenv```

Activate the virtual environment:
```source myenv/bin/activate```

Install the requirements:
```pip install -r requirements.txt```

---

### Uninstall the script

>Clean up the virtual environment: This is one benefit of virtual environments. You don't have to worry about conflicting packages. Also, if you just want to try the script, it's easy to remove a virtual environment when you are done.

**Deactivate the virtual environment**
```deactivate```

Remove the virtual environment:
```rm -rf myenv```

Done!
  
>This version tested on Linux (Arch) 09/26/24

If you test on other systems, please let me know if you have successes or issues.

### License

This script is released under the MIT License. See the LICENSE file for details.
