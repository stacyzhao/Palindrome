import re
# checks if word is a palindrome. returns true or false
def remove_special_character(text):
    # user_input = input ("enter some words to check if its a palindrome: ")
    clean_text = re.sub("[^A-Za-z]+", "", text)
    clean_text = clean_text.lower()
    return clean_text

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

def main():
    user_input = input("enter some words to check if its a palindrome: ")
    clean_text = remove_special_character(user_input)
    print(clean_text)
    if is_palindrome(clean_text):
        print ("palindrome is true")
    else:
        print ("palindrome is false")

if __name__ == '__main__':
    main()
