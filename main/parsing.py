import re

# Compiled regex for parsing

translation = re.compile(r'(?P<lang>[A-Za-z ]+):(?P<text>.+);')
pronunciation = re.compile(r'pronounced \[.+\];')

spelling1 = re.compile(r'[a-z]+\-[A-Z]+')
spelling2 = re.compile(r'[A-Z]+\-[a-z]+')

markup = re.compile(r'\{.+\}')


def parse_description(text):
    """ Parses descriptions to remove special notation. """

    text = remove_with_RE(text, translation)
    text = remove_with_RE(text, pronunciation)
    text = remove_with_RE(text, spelling1)
    text = remove_with_RE(text, spelling2)
    text = remove_with_RE(text, markup)

    text = parse_punctuation(text, '.')
    text = parse_punctuation(text, ',')
    text = parse_punctuation(text, ';')
    text = parse_punctuation(text, ':')

    text = parse_parenthesis(text)

    return text.replace("  ", " ")


def remove_with_RE(text, compiled_re):
    """ Removes text that matches a given regex. """

    match = compiled_re.search(text)

    if match:
        text = text.replace(match.group(0), "")

    return text


def parse_punctuation(text: str, punct: str):
    """ Ensures that a punctuation marks are properly formatted;
    they have a space after and not before. """

    punct_re = re.compile(r'(?P<punct>\%s)\w' % punct)

    # Add space after punctuation mark.
    match = punct_re.search(text)

    while match:
        text = text[:match.end("punct")] + " " + text[match.end("punct"):]
        match = punct_re.search(text)

    # Remove space before punctuation mark.
    text = text.replace(" " + punct, punct)

    return text

def parse_parenthesis(text: str):
    """ Ensures parenthesis are properly parsed. """
    cases = [("(;", "("), ("(,", "("), ("( ", "("), (" )", ")")]

    for case in cases:
        text = text.replace(case[0], case[1])

    return text
