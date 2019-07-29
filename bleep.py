from cs50 import get_string
from sys import argv


def main():

    if len(argv) != 2 :
         print("Not valid")
         return 1

    msg= input("what message would you like to censor ?:")
    ban_file = argv[1]
    ban = set()

    txt = open(ban_file,"r+")

    for line in txt:
        ban.add(line.strip())

    msg_word = msg.split()
    censor_word = ""

    for word in msg_word:
        if word.lower() in ban:
            censor_word += ('*'*len(word))+ ""
        else :
            censor_word += (word)+ ""

    print(""+censor_word.strip())

    txt.close()


if __name__ == "__main__":
    main()
