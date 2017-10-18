def checkPalindrome(word):
    '''
    This program checks if a word or sentence is a palindrome.

    A palindrome is a word or statement that reads the same in reverse
    :param word: This parameter is a string of words or sentence to be checked.
    :return: The function doesn't have a return value.
    '''
    if word == word[::-1]:
        print('Word is a palindrome')
    else:
        print('Word is not a palindrome')


checkPalindrome('sms')
checkPalindrome('ayak')
