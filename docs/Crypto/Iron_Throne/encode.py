def strToBinary(s):
    bin_conv = []
 
    for c in s:
         
        # convert each char to
        # ASCII value
        ascii_val = ord(c)
         
        # Convert ASCII value to binary
        binary_val = bin(ascii_val)
        bin_conv.append(binary_val[2:])
         
    return (' '.join(bin_conv))
 
# Driver Code
if __name__ == '__main__':
    s = 'PfoBGhofy'

    intermediate = strToBinary(s)

    # convert all zeroes in intermediate to 'sword'
    intermediate = intermediate.replace('0', 'sword')
    intermediate = intermediate.replace('1', 'knife')
    intermediate = intermediate.replace(' ', '')
    
    # save intermediate to a file
    with open('intermediate.txt', 'w') as f:
        f.write(intermediate)