# Определяем цвета (ANSI escape codes)
class Colors:
    GREEN = '\033[92m'   # Зеленый (хорошее настроение)
    YELLOW = '\033[93m'  # Желтый (нейтральное)
    RED = '\033[91m'     # Красный (грустное)
    CYAN = '\033[96m'    # Голубой (для ИИ)
    RESET = '\033[0m'    # Сброс цвета к стандартному

def start_dialogue():
    print(f"{Colors.CYAN}--- English Dialogue Starter ---{Colors.RESET}\n")
    
    # Приветствие ИИ
    print(f"{Colors.CYAN}AI: Hello! How are you today? 👋{Colors.RESET}")
    print("Options:")
    print("1 - I'm doing great! 😊")
    print("2 - I'm feeling a bit sad. 😔")
    print("3 - I'm just okay. 😐")
    
    choice = input("\nYour choice (1/2/3): ")

    # Реакция на ответ
    if choice == "1":
        print(f"\nUser: {Colors.GREEN}I'm doing great! 😊{Colors.RESET}")
        print(f"{Colors.CYAN}AI: That's wonderful! Energy levels are high today! 🚀{Colors.RESET}")
    
    elif choice == "2":
        print(f"\nUser: {Colors.RED}I'm feeling a bit sad. 😔{Colors.RESET}")
        print(f"{Colors.CYAN}AI: I'm sorry to hear that. Sending you a virtual hug! 🫂{Colors.RESET}")
        print(f"{Colors.CYAN}AI: Remember, it's okay to have bad days.{Colors.RESET}")
    
    elif choice == "3":
        print(f"\nUser: {Colors.YELLOW}I'm just okay. 😐{Colors.RESET}")
        print(f"{Colors.CYAN}AI: A calm day is a good day too. ☁️{Colors.RESET}")
        print(f"{Colors.CYAN}AI: Anything interesting on your mind?{Colors.RESET}")
    
    else:
        print(f"\n{Colors.RED}AI: System error... just kidding! But I don't know that option. 🤖{Colors.RESET}")

if __name__ == "__main__":
    start_dialogue()
