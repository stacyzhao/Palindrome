import re

def remove_special_character(text):
    clean_text = re.sub("[^A-Za-z]+", "", text)
    clean_text = clean_text.lower()
    return clean_text

def is_palindrome(text):
    clean_text = remove_special_character(text)

    if len(clean_text) == 0 or len(clean_text) == 1:
        return False
    elif len(clean_text) < 4:
        if clean_text[0] == clean_text[-1]:
            return True
        else:
            return False
    else:
        if clean_text[0] == clean_text[-1]:
            return is_palindrome(clean_text[1:-1])
        return False

def main():
    user_input = input("Check if your word is a palindrome!: ")
    if is_palindrome(user_input):
        print ("Your word is a palindrome!")
    else:
        print ("Your word is not a palindrome :(")

if __name__ == '__main__':
    main()
