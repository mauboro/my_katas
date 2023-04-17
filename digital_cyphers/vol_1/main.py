def encode(message, key):
    message = [ord(m) - 96 for m in message]
    for i in range(len(message)):
        message[i] += int(str(key)[i % len(str(key))])
    return message
