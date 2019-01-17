def pal():
    word = input("check word: ").replace(" ", "").lower()
    if word == word[::-1]:
        return "yes"
    return "no"
if name == 'main':
    print(pal())
