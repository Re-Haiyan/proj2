def char_frequency(text):
    freq = {}
    for char in text:
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq

def main():
    text = input("Enter string: ")
    frequency = char_frequency(text)
    for char, count in frequency.items():
        print(f"{char}={count}", end=", ")

if __name__ == "__main__":
    main()
