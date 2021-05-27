

while __name__ == "__main__":
    response = ""
    msg = input("-->")
    pmsg = msg.lower() # to turn everything input to lowercase

    if 'hi' in msg or 'hello' in msg or 'hy' in msg or 'howdy' in msg:
        response += " hi."
    if 'how' in msg and 'are' in msg and 'you' in msg:
        response += " I am fine."
    if 'i' in msg and 'love' in msg and 'you' in msg:
        response += " Let's just be friends."
    
    print(response)
    
