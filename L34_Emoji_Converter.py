message = input("> ")
words = message.split(" ")
emojis = {":)":"😊",":(":"🙁",":|":"😐",":/":"😕"}

for i in words:
    if i in emojis:
        print(emojis[i]+" ",end="")
    else:
        print(i+" ",end="")