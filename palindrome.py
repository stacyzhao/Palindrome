def is_palindrome(text):
    if len(text) == 0 or len(text) == 1:
        return False
    elif len(text) < 4:
        if text[0] == text[-1]:
            return True
        else:
            return False
    else:
        if text[0] == text[-1]:
            return is_palindrome(text[1:-1])
        return False
