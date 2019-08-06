"""
Learn about bytes
Bytes are similar to str type, but they are a sequence of
bytes instead of Unicode code points.

Use for raw binary data, fixed-width, single byte

Use the bytes() constructor
"""

d = b'data'
print(d, type(d))

info = b'some bytes here'
#Split the bytes using split() method for bytes
print(info.split())

#Ecoding Alt+162 = o'
message = "Vamos al zoológico"
print(message)
data = message.encode("utf-8")
print (data)
#decoding
new_message = data.decode("utf-8")
print(new_message)