import base64

# the string from the file meta data is base64 encoded
# decode it
base64_message = 'YidceGIyXHhiZVx4YTVceGJhXHg4NFx4ODhceDlhXHhiM1x4YjNceGEwXHg4YVx4YTBceDliXHhjZlx4YTBceGIxXHhiMFx4YTBceDhjXHg5Mlx4OGJceDk4XHhhMFx4OTVceGNmXHg5MVx4YTBceDhjXHhiMVx4Y2ZceDg4XHg4Mic='
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)

# take this message and store it in another variable 
# i could not find a way to convert this message directly from str to bytes
# hence had to manually copy paste it in the next line

cipher_text = b'\xb2\xbe\xa5\xba\x84\x88\x9a\xb3\xb3\xa0\x8a\xa0\x9b\xcf\xa0\xb1\xb0\xa0\x8c\x92\x8b\x98\xa0\x95\xcf\x91\xa0\x8c\xb1\xcf\x88\x82'

for key in range(256):
    print(bytes([b^key for b in cipher_text]))