chars = "abcdegh"

def multiple_if_vowels(st: str) -> str:
    if st.lower() in "aeiou":
        return st*10
    return st

chars = "".join([multiple_if_vowels(char) for char in chars])
print(chars)
