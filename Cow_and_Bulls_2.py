print("""       Welcome to Cows and Bulls game.
      
First person will enter a 4-digit number. And the other person will guess the number with hints.
      
Hints :-
Cows - It means how many correct digits are in your number.
Bulls - It means how many correct digits are in correct position.""")

no = "2345"

while True :
    n = str(int(input("Enter number : ")))
    c = b = 0

    if n != no :
        for i in n :
            if i in no :
                c += 1

        for i in range(0,len(no)) :
            if n[i] == no[i] :
                b += 1
        
        print(f"Cows = {c}   Bulls = {b}")
    else :
        print("You have guess the number.")
        break