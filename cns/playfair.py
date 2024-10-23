def create_matrix(key):
    # Prepare the key by removing duplicates and spaces
    key = key.replace(" ", "").upper()
    matrix = []
    seen = set()

    for char in key:
        if char not in seen:
            if char == 'J':  # Replace 'J' with 'I'
                char = 'I'
            matrix.append(char)
            seen.add(char)

    # Add remaining letters to the matrix
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in seen:
            matrix.append(char)

    # Convert list to 5x5 matrix
    matrix_5x5 = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix_5x5

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None  # Return None if the character is not found

def encode_playfair(plaintext, key):
    matrix = create_matrix(key)
    plaintext = plaintext.upper().replace(" ", "").replace("J", "I")
    
    # Prepare plaintext by creating digraphs
    prepared_text = []
    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        if i + 1 < len(plaintext):
            char2 = plaintext[i + 1]
            if char1 == char2:  # If both characters are the same, insert 'X'
                prepared_text.append(char1)
                prepared_text.append('X')
                i += 1
            else:
                prepared_text.append(char1)
                prepared_text.append(char2)
                i += 2
        else:
            prepared_text.append(char1)
            prepared_text.append('X')  # Append 'X' if there's an odd character
            i += 1

    # Encode the digraphs
    ciphertext = []
    for i in range(0, len(prepared_text), 2):
        char1 = prepared_text[i]
        char2 = prepared_text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Same row
            ciphertext.append(matrix[row1][(col1 + 1) % 5])
            ciphertext.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:  # Same column
            ciphertext.append(matrix[(row1 + 1) % 5][col1])
            ciphertext.append(matrix[(row2 + 1) % 5][col2])
        else:  # Rectangle
            ciphertext.append(matrix[row1][col2])
            ciphertext.append(matrix[row2][col1])

    return ''.join(ciphertext)

def decode_playfair(ciphertext, key):
    matrix = create_matrix(key)
    ciphertext = ciphertext.upper().replace(" ", "").replace("J", "I")
    
    plaintext = []
    i = 0
    
    while i < len(ciphertext):
        char1 = ciphertext[i]
        if i + 1 < len(ciphertext):
            char2 = ciphertext[i + 1]
        else:
            char2 = 'X'  # Append 'X' if there's an odd character
        
        # Check if both characters are valid
        if find_position(matrix, char1) is None or find_position(matrix, char2) is None:
            print(f"Invalid characters: '{char1}' or '{char2}' not in Playfair matrix.")
            return
        
        i += 2
        
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        
        if row1 == row2:  # Same row
            plaintext.append(matrix[row1][(col1 - 1) % 5])
            plaintext.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Same column
            plaintext.append(matrix[(row1 - 1) % 5][col1])
            plaintext.append(matrix[(row2 - 1) % 5][col2])
        else:  # Rectangle
            plaintext.append(matrix[row1][col2])
            plaintext.append(matrix[row2][col1])
    
    return ''.join(plaintext)

# User Input
mode = input("Do you want to encode or decode? (e/d): ").lower()
key = input("Enter the key: ")
if mode == 'e':
    plaintext = input("Enter the plaintext: ")
    ciphertext = encode_playfair(plaintext, key)
    print("Ciphertext:", ciphertext)
elif mode == 'd':
    ciphertext = input("Enter the ciphertext: ")
    decoded_message = decode_playfair(ciphertext, key)
    if decoded_message:
        print("Decoded message:", decoded_message)
else:
    print("Invalid mode selected. Please choose 'e' for encode or 'd' for decode.")
