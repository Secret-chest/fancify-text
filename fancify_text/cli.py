import argparse
from . import functions


def fancify_cmd():
    parser = argparse.ArgumentParser(
        description="Convert text to unicode font"
    )

    parser.add_argument(
        "font",
        help="Font to use. Use 'all' - to print text with using all fonts"
    )
    parser.add_argument(
        "input_text",
        help="The text to convert"
    )

    args = parser.parse_args()

    # If font is all, then print text in all available fonts
    if args.font.lower() == "all":
        for f in functions.availableFunctions:
            print(f, '-', getattr(functions, f)(args.input_text))
        
        return

    # Replace "reversed" with "reversed_"
    if args.font == "reversed":
        args.font = "reversed_"

    # Check if font is available
    if args.font not in functions.availableFunctions:
        print(f'Font "{args.font}" not found')
        return

    print(getattr(functions, args.font)(args.input_text))
