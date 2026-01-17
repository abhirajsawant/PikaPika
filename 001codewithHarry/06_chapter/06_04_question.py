spam1="lot of money"
spam2="buy now"
spam3="subscribe"
spam4="click this"

mail = input("write/paste the mail: ")

if(spam1 in mail or spam2 in mail or spam3 in mail or spam4 in mail):
    print("spammmmmmmm")

else:print("not a spam")