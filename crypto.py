def machine():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    Value = keys[-1] + keys[0:-1]

    encryptDict = dict(zip(keys, Value))
    decryptDict = dict(zip(Value, keys))

    message = input("Please enter a Password")
    mode = input("Please select an encryption mode : Encode(E) OR Decode(D) \n")

    if mode.upper() == 'E':
        newMessage = ''.join([encryptDict[letter]
                             for letter in message.lower()])

    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter]
                             for letter in message.lower()])
    else:
        print('Please enter an Valid choice, Decrypt(D) OR Encrypt(E)')

    return newMessage


print(machine())