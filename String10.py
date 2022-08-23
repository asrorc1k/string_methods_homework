def main(s):
    """
    A string containing the letter "x" is given. Find the index of the letter "x" in this variable.
    Args:
        s: str
    Returns:
        str: answer
    """
    idx = s.find('x,')
    return idx
print(main('Bexruz'))