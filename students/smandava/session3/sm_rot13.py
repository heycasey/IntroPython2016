"""Oct 16, 2016 ROT13 Exercise."""
import codecs

rot13_decode = codecs.decode("Zntargvp sebz bhgfvqr arne pbeare", 'rot_13')
print(rot13_decode)


def rot13(text):
    """Return ROT13 encoding for user input."""
    user_input = input("Enter text to encode using ROT13:")
    rot13_output = codecs.encode(user_input, 'rot_13')
    decode_text = codecs.encode(text, 'rot_13')  # for assertion
    print(rot13_output)
    return decode_text

if __name__ == '__main__':
    assert rot13('Hello World') == 'Uryyb Jbeyq'
    assert rot13('Python') == 'Clguba'
    assert rot13('ROT13') == 'EBG13'
