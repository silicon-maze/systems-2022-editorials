import base64

given_input = "8437385373703739737382373883731163731163739" \
            "037385373863734837388373483736637310237386373" \
            "1223737037311737310037371373863731213738837350" \
            "37382373108373983736837370373573736137361" \

numbers = given_input.split("373")
base64string = ''.join(list(map(lambda e : chr(int(e)), numbers)))

base64bytes = base64string.encode("ascii")

string_bytes = base64.b64decode(base64bytes)
text = string_bytes.decode("ascii")
print(text)
