def isPalindrome(sentence):
    return sentence.lower() == sentence[::-1].lower()

sentence = input("Digite uma palavra: ")

if isPalindrome(sentence):
    print(f'{sentence} é um palindromo.')
else:
    print(f'{sentence} não é um palindromo.')
