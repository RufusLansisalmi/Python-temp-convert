from stringutils import normalize
from menu import print_menu, get_menu_choice


def is_palindrome(text: str) -> bool:
    cleaned = normalize(text)
    return cleaned == cleaned[::-1]


def main() -> None:
    
    while True:
        print_menu()
        choice = get_menu_choice()
        match choice:
            case 1:
                text = input("Ange text att kontrollera: ")
                result = is_palindrome(text)
                if result:
                    print(f"'{text}' är ett palindrom.")
                else:
                    print(f"'{text}' är inte ett palindrom.")
            case 3:
                name = input("Ange ett fullständigt namn: ")
                initials = extract_initials(name)
                print(f"Initialer: {initials}")
            case 4:
                pwd = input("Ange lösenord att kontrollera: ")
                try:
                    length = int(input("Minsta längd (enter för standard 8): ") or 8)
                except ValueError:
                    length = 8
                mixed = input("Kräv både stora och små bokstäver? (j/n, enter för j): ")
                mixed_case = (mixed.strip().lower() != 'n') if mixed else True
                punct = input("Kräv skiljetecken? (j/n, enter för j): ")
                punctuation = (punct.strip().lower() != 'n') if punct else True
                ok = check_password(pwd, length=length, mixed_case=mixed_case, punctuation=punctuation)
                print("Lösenordet är säkert." if ok else "Lösenordet är inte säkert.")
            case 2:
                print("Avslutar programmet. Hej då!")
                break
            case _:
                print("Ogiltigt val. Försök igen.")





def extract_initials(name: str) -> str:
    
    if not name:
        return ""

    particles = {"af", "av", "de", "von"}
    parts = name.split()
    initials = []
    for part in parts:
        cleaned = part.strip()
        if not cleaned:
            continue
        key = cleaned.lower()
        if key in particles:
            initials.append(key[0] + ".")
        else:
            initials.append(cleaned[0].upper() + ".")

    return "".join(initials)




def check_password(password: str,
                   length: int = 8,
                   mixed_case: bool = True,
                   punctuation: bool = True) -> bool:
    
    import string

    if not isinstance(password, str):
        return False

    if len(password) < length:
        return False

    if mixed_case:
        has_upper = any(ch.isupper() for ch in password)
        has_lower = any(ch.islower() for ch in password)
        if not (has_upper and has_lower):
            return False

    if punctuation:
        if not any(ch in string.punctuation for ch in password):
            return False

    return True

if __name__ == "__main__":
    main()