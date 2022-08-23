def main(s):
    """
    A variable of type str is given. make sure all letters are lowercase.
    Args:
        s: str
    Returns:
        bool: answer
    """
    x = s.lower() == s
    
    return x
print(main('codeschool'))