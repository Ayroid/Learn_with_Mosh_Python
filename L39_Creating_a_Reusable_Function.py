# Converting the emoji programs to functions

def emoji_converter(message):
    words=message.split(" ")
    emojis = {":)":"😊",":(":"🙁",":|":"😐",":/":"😕"}
    output = ""
    for i in words:
        output +=emojis.get(i,i) + " "
    return output

message = input("> ")
answer = emoji_converter(message)
print(answer)
