import random
import time

sample = [2, 10, 16, 18, 22, 44, 50]

def main():
    #winning_ticket = input("winning ticket separated by , (len 7): ").split(",")
    winning_ticket = sample.copy()
    while len(winning_ticket) != 7:
        winning_ticket = list(input("winning ticket separated by , (len 7): "))
    winning_ticket.sort()
    print("Winning ticket: ", winning_ticket)
    drawn_ticket = []
    tries = 0
    while get_matches(winning_ticket, drawn_ticket) != 7:
        drawn_ticket = draw()
        print("drawn ", tries, ": ", drawn_ticket, ", macthed ", get_matches(winning_ticket, drawn_ticket))
        tries = tries + 1
    print("Won, tried ", tries, " times")

def draw():
    pool = list(range(1, 51))
    # 7 numbers
    draw_set = []
    for i in range(0, 7):
        random.seed(time.time())
        drawnNumber = random.choice(pool)
        pool.remove(drawnNumber)
        draw_set.append(drawnNumber)
        #time.sleep(0.1)
    draw_set.sort()
    return draw_set

def get_matches(winning_ticket, drawn_ticket):
    return len(set(winning_ticket) & set(drawn_ticket))

if __name__ == "__main__":
    main()