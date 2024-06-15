In this exercise, you will create a program that reads words from the user until the user enters a blank line. After the user enters a blank line your program should display each word entered by the user exactly once. The words should be displayed in the same order that they were first entered. For example, if the user enters:

first

second

first

third

second

then your program should display:

first

second

third






unique_words = set()
ordered_words = []
while True:
    word = input().strip()
    if not word:
        break
    if word not in unique_words:
        unique_words.add(word)
        ordered_words.append(word)
for word in ordered_words:
    print(word)

