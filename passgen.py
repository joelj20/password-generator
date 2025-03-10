import argparse
import random
import string

def generate_password(length=8, use_digits=True, use_symbols=False):
    characters = string.ascii_letters
    
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "⚠️ Error: Cannot generate password without characters"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Password generator")
    parser.add_argument("-l", "--length", type=int, default=8, 
                      help="Password length (default: 8)")
    parser.add_argument("-d", "--digits", action="store_false",
                      help="Exclude numbers")
    parser.add_argument("-s", "--symbols", action="store_true",
                      help="Include special characters")
    
    args = parser.parse_args()
    
    password = generate_password(
        length=args.length,
        use_digits=args.digits,
        use_symbols=args.symbols
    )
    
    print(f"🔒 Your password: {password}")

if __name__ == "__main__":
    main()
