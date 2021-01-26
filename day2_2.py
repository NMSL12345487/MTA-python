import random
ans = random.randint(1,100)
while True:
    guess = int(input("guess number?"))
    if ans==guess:
        print("終於猜到了你搞得我心好累")
    elif ans >= int(guess):
        print("猜得太小了")
    elif ans <= int(guess):
        print("猜得太大了!")
    else:
        print("你是文盲嗎????")