for _ in range(int(input())):
    drink = {}
    for _ in range(int(input())):
        school, amount = input().split()
        drink[school] = int(amount)
    print(max(drink, key=drink.get))
