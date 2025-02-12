def shorten_text(text, max_length=64):
    return text[:max_length] + "..." if len(text) > max_length else text


if __name__ == '__main__':
    pass
