from .fontData import fonts

__all__ = ["fancify", "reversed_", "upsideDown", "availableFunctions"]

availableFunctions = list(fonts)
availableFunctions[availableFunctions.index("reversed")] = "reversed_"


def fancify(inputText, style):
    if style not in fonts:
        raise Exception(
            f"Style '{style}' not found. "
            f"Please use one of: { ', '.join(fonts.keys()) }"
        )

    fontInfo = fonts[style]
    font = fontInfo[1]
    fontSupported = fontInfo[0]
    if len(fontInfo) == 3:
        fontSpace = fontInfo[2]
    else:
        fontSpace = ""

    outputText = ""

    # Conversion.
    for character in inputText:
        index = None
        if character in fontSupported:
            index = fontSupported.index(character)
        if index is not None and len(font) > index:
            # If the current character is in the list of accepted characters, convert it.
            outputText += font[index]
        else:  # Otherwise, leave it as is.
            outputText += character
        if style == "blue":
            # Add spacing as requested by font
            outputText += fontSpace

    return outputText


# Register functions and add to globals

funcs = {font: eval(f"lambda input_text: fancify(input_text, {repr(font)})") \
                for font in fonts if font not in ["reversed", "upsideDown"]}
globals().update(funcs)

# Add function names to __all__
__all__ += list(funcs)

# Other functions


def reversed_(input_text):
    return "".join(reversed(fancify(input_text, "reversed")))


def upsideDown(input_text):
    return "".join(reversed(fancify(input_text, "upsideDown")))
