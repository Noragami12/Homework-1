import math

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def calculator():
    # Переменная для хранения текущего результата
    accumulator = None
    
    print(f"{Colors.CYAN}--- 🧮 Calculator with Memory (Accumulator) ---{Colors.RESET}")
    print("Commands: +, -, *, /, ^, exp, sqrt")
    print("Special: 'reset' to start over, 'exit' to quit")

    while True:
        try:
            # Если в памяти уже есть число, показываем его
            if accumulator is not None:
                print(f"\n{Colors.YELLOW}Current value: {accumulator}{Colors.RESET}")
                op = input(f"{Colors.CYAN}Operation with this value (or reset/exit): {Colors.RESET}").strip().lower()
                num1 = accumulator
            else:
                print(f"\n{Colors.YELLOW}Memory is empty.{Colors.RESET}")
                op = input(f"{Colors.CYAN}Choose operation (or exit): {Colors.RESET}").strip().lower()
                if op in ('exit', 'reset'): 
                    if op == 'exit': break
                    accumulator = None; continue
                num1 = float(input("Enter first number: "))

            if op == 'exit':
                print("Goodbye! 👋")
                break
            
            if op == 'reset':
                accumulator = None
                print(f"{Colors.YELLOW}Memory cleared!{Colors.RESET}")
                continue

            # Операции с одним числом
            if op == 'sqrt':
                if num1 < 0:
                    print(f"{Colors.RED}Error: Negative sqrt!{Colors.RESET}")
                else:
                    accumulator = math.sqrt(num1)
            
            elif op == 'exp':
                accumulator = math.exp(num1)

            # Операции со вторым числом
            elif op in ('+', '-', '*', '/', '^'):
                num2 = float(input("Enter next number: "))
                
                if op == '+': accumulator = num1 + num2
                elif op == '-': accumulator = num1 - num2
                elif op == '*': accumulator = num1 * num2
                elif op == '/':
                    if num2 == 0:
                        print(f"{Colors.RED}Error: Division by zero!{Colors.RESET}")
                        continue
                    accumulator = num1 / num2
                elif op == '^':
                    accumulator = math.pow(num1, num2)
            
            else:
                print(f"{Colors.RED}Unknown operation!{Colors.RESET}")
                continue

            print(f"{Colors.GREEN}New result: {accumulator}{Colors.RESET}")

        except ValueError:
            print(f"{Colors.RED}Invalid input! Enter a number.{Colors.RESET}")
        except OverflowError:
            print(f"{Colors.RED}Error: Number too large!{Colors.RESET}")

if __name__ == "__main__":
    calculator()
