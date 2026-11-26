class StringReverse:
    def __init__(self, text):
        self.__text = text

    def reverse_words(self):
        return " ".join(self.__text.split()[::-1])


sentence = input("Enter a string: ")

obj = StringReverse(sentence)

print("Reversed string:", obj.reverse_words())