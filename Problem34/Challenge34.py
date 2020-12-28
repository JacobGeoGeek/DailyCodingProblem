def find_palindrome(word: str, numberOfletters: int = 1) -> str:
    if word == word[::-1]:
        return word

    position: int = numberOfletters * -1
    sub_word: str = word[position:]

    new_word: str = sub_word[::-1] + word

    if new_word == new_word[::-1]:
        return new_word

    numberOfletters += 1
    return find_palindrome(word, numberOfletters)


if __name__ == "__main__":
    print(find_palindrome("race") == "ecarace")
    print(find_palindrome("google") == "elgoogle")
