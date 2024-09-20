import random
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number) 

def play_game():
    print("Welcome to the FizzBuzz Game!")
    print("Let's play! I'll give you a number, and you guess the FizzBuzz word.")

    for _ in range(5):
        number =random.randint(1, 100)
        print(f"\nWhat's the FizzBuzz for {number}?")
        user_guess = input("Your guess: ").strip().lower() 

        correct_answer = fizz_buzz(number).lower() 

        if user_guess == correct_answer:
            print("You got it right! Well done!")
        else:
            print(f"the correct FizzBuzz is: {fizz_buzz(number)}")

    print("\nThanks for playing!")
play_game()
       
        
    
    

    




    
   
    



    