# import caesar_cipher
intermediate = ""
with open('intermediate.txt', 'r') as f:
    intermediate = f.read()

def BinaryToDecimal(binary):
        
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)   

intermediate = intermediate.replace('sword', '0')
intermediate = intermediate.replace('knife', '1')

str_data =' '
  
for i in range(0, len(intermediate), 7):
    temp_data = int(intermediate[i:i + 7])
    
    decimal_data = BinaryToDecimal(temp_data)

    str_data = str_data + chr(decimal_data)
  

print("The Binary value after string conversion is:", str_data)

# brute force caesar cipher function
def caesar_cipher(string, shift):
    cipher = ''
    for char in string:
        if char.isalpha():
            if char.isupper():
                cipher += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                cipher += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher += char
    return cipher

# call caesar cipher function
print("The decoded string is:", caesar_cipher(str_data, 1000))