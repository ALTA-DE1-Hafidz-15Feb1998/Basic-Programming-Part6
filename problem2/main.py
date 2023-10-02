def caesar(offset, input_str):
    result = ""

    for char in input_str:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char.lower())
            shifted_code = ((char_code - ord('a') + offset) % 26) + ord('a')
            shifted_char = chr(shifted_code)
            if is_upper:
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char

    return result

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl