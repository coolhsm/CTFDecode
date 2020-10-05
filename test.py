import base64
find_decode = lambda d , data : eval(f'base64.{d}({data})')
print(find_decode)
def decode(data):

  for i in dir(base64):
    if i[3:] == 'decode':
      try:
        decode_data = find_decode(i,data)
        chars = decode_data if all(chr(x).isalpha() or chr(x).isspace() for x in decode_data)else None
        if chars != None :
          return f'Decoded String is: {chars.decode("utf-8")}\nEncrypet was used is: {i:3}'
      except:
        pass

#_______________ Test _________________

print(decode(b'NM&qnZy;B1a%^M')) #output : Hello World , b85
print(decode(b'48656C6C6F20576F726C64'))#output : Hello World , b16
print(decode(b'SGVsbG8gV29ybGQ='))#output : Hello World , b64
print(decode(b'JBSWY3DPEBLW64TMMQ======'))#output : Hello World , b32