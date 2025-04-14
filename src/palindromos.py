

def is_palindrome(palabra):

    palabra = palabra.lower().replace(" ", "").replace(",", "").replace(":", "").replace(";", "").replace("!", "").replace("?", "").replace(".", "")
    palabra = palabra.replace("-", "").replace("_", "").replace("'", "").replace('"', "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace("<", "").replace(">", "").replace("/", "").replace("\\", "")

    if palindromo == palabra:
        print(f"La palabra {palabra} es un palíndromo")
        return True
    else:
        print(f"La palabra {palabra} no es un palíndromo")
        return False

def main():

    palabra = input("Introduce una palabra:")
    is_palindrome(palabra)
    
if __name__ == "__main__":
    main()