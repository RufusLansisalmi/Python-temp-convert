def main():
    while True:
        print_menu()
        choice = get_menu_choice()
        if choice == 1:
            # placeholder: actual work is done by stringlab.main
            print("Kontrollera om en text är palindrom (väljs i huvudprogrammet).")
        elif choice == 3:
            print("Extrahera initialer (väljs i huvudprogrammet).")
        elif choice == 2:
            print("Avslutar programmet. Hej då!")
            break
        else:
            print("Ogiltigt val. Försök igen.")

def print_menu():
    print("Palindromkontroll:")
    print("1. Kontrollera text")
    print("3. Extrahera initialer")
    print("4. Kontrollera lösenord")
    print("2. Avsluta")

def get_menu_choice():
    try:
        choice = int(input("Ange ditt val: "))
        return choice
    except ValueError:
        print("Ogiltig inmatning. Ange ett nummer.")
        return 0
