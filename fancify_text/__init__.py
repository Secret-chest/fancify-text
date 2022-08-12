from fancify_text.fontData import fonts, modifiers


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


# Functions for command-line usage.


def sansSerif(input_text):
    return fancify(input_text, "sansSerif")


def bold(input_text):
    return fancify(input_text, "bold")


def italic(input_text):
    return fancify(input_text, "italic")


def boldItalic(input_text):
    return fancify(input_text, "boldItalic")


def monospaced(input_text):
    return fancify(input_text, "monospaced")


def wide(input_text):
    return fancify(input_text, "wide")


def boldSerif(input_text):
    return fancify(input_text, "boldSerif")


def italicSerif(input_text):
    return fancify(input_text, "italicSerif")


def boldItalicSerif(input_text):
    return fancify(input_text, "boldItalicSerif")


def doubleStruck(input_text):
    return fancify(input_text, "doubleStruck")


def script(input_text):
    return fancify(input_text, "script")


def fraktur(input_text):
    return fancify(input_text, "fraktur")


def boldFraktur(input_text):
    return fancify(input_text, "boldFraktur")


def blue(input_text):
    return fancify(input_text, "blue")


def squared(input_text):
    return fancify(input_text, "squared")


def circled(input_text):
    return fancify(input_text, "circled")


def smallCaps(input_text):
    return fancify(input_text, "smallCaps")


def curly(input_text):
    return fancify(input_text, "curly")


def reversed_(input_text):
    return "".join(reversed(fancify(input_text, "reversed")))


def upsideDown(input_text):
    return "".join(reversed(fancify(input_text, "upsideDown")))


def boxed(input_text):
    return fancify(input_text, "boxed")


def wiry(input_text):
    return fancify(input_text, "wiry")


def parenthesized(input_text):
    return fancify(input_text, "parenthesized")


def heavyCircled(input_text):
    return fancify(input_text, "heavyCircled")


def currency(input_text):
    return fancify(input_text, "currency")


def cool(input_text):
    return fancify(input_text, "cool")


def magic(input_text):
    return fancify(input_text, "magic")
