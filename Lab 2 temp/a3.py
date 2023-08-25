def main():
    with open("sample.txt", "w") as file:
        file.write("NALLAMILLI NAGA VENKATA REDDY\n")
        file.write("Hello WORLD.\n")
        file.write("Line\n")
        file.write("Advacnced programming\n")
        file.write("Fifth line\n")
        file.write("testing.\n")
        file.write("seven.\n")
    lines = []
    with open("sample.txt", "r") as file:
        lines = file.readlines()

    line_data_dict = {}
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        line_length = len(line)
        line_data_dict[line_number] = [line, line_length]

    print("Dictionary with line numbers as keys and [string, length] as values:")
    print(line_data_dict)

    letter_frequency_dict = {}
    for line in lines:
        for char in line:
            if char.isalpha():
                char_lower = char.lower()
                if char_lower in letter_frequency_dict:
                    letter_frequency_dict[char_lower] += 1
                else:
                    letter_frequency_dict[char_lower] = 1

    print("\nDictionary with letter frequencies:")
    print(letter_frequency_dict)

if __name__ == "__main__":
    main()