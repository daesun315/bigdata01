#file = open("ticket.txt", "w")
with open("ticket.txt", "r") as file:
    print(int(file.read()) + 1)
file.close()