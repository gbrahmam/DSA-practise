for _ in range(int(input())):
    burger,soda,combo = [int(x) for x in input().split()]
    if burger<combo and soda<combo:
        print((burger+soda)-combo)