import basic

while True:
    text = input('Diamond > ')
    result, error = basic.run('<stdin>', text)

    if error: print(error.as_string())
    elif result: print(repr(result))