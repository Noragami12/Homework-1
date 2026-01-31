import random

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'

def guess_the_number():
    print(f"{Colors.MAGENTA}--- 🎲 Guess the Number Game 🎲 ---{Colors.RESET}")
    
    while True:
        print(f"\nSelect Difficulty Level:")
        print("1. Easy (1-10)")
        print("2. Medium (1-50)")
        print("3. Hard (1-100)")
        print("Type 'exit' to quit")
        
        choice = input(f"{Colors.CYAN}Your choice: {Colors.RESET}").strip().lower()
        
        if choice == 'exit':
            print("Thanks for playing! 👋")
            break
            
        # Настройка диапазона в зависимости от уровня
        if choice == "1":
            limit = 10
        elif choice == "2":
            limit = 50
        elif choice == "3":
            limit = 100
        else:
            print(f"{Colors.RED}Invalid choice! Please pick 1, 2, or 3.{Colors.RESET}")
            continue

        secret_number = random.randint(1, limit)
        attempts = 0
        print(f"\n{Colors.YELLOW}I've picked a number between 1 and {limit}. Try to guess it!{Colors.RESET}")

        # Основной цикл угадывания
        while True:
            try:
                guess = input(f"Enter your guess: ")
                
                # Позволяем выйти в меню в любой момент
                if guess.lower() == 'menu':
                    break
                
                guess = int(guess)
                attempts += 1

                if guess < secret_number:
                    print(f"{Colors.CYAN}Higher! ⬆️{Colors.RESET}")
                elif guess > secret_number:
                    print(f"{Colors.CYAN}Lower! ⬇️{Colors.RESET}")
                else:
                    print(f"\n{Colors.GREEN}🎉 CONGRATULATIONS! 🎉{Colors.RESET}")
                    print(f"You guessed the number {secret_number} in {attempts} attempts!")
                    break
                    
            except ValueError:
                print(f"{Colors.RED}Please enter a valid number or 'menu' to go back.{Colors.RESET}")

        # Спрашиваем, хочет ли пользователь сыграть еще раз
        play_again = input(f"\nPlay another level? (yes/no): ").strip().lower()
        if play_again != 'yes' and play_again != 'y':
            print("See you next time!")
            break

if __name__ == "__main__":
    guess_the_number()
