import random
import string
import pyperclip

def password_strength(password):
    length = len(password)
    strength = 0
    criteria = [
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password)
    ]
    strength += sum(criteria)
    
    if length >= 12:
        strength += 1

    levels = {
        1: "😐 Weak",
        2: "😬 Fair",
        3: "🙂 Good",
        4: "💪 Strong",
        5: "🔥 Very Strong"
    }
    return levels.get(strength, "Unknown")

def display_banner():
    print(r"""
╔══════════════════════════════════════╗
║ 🔐  WELCOME TO THE PASSWORD WIZARD  🔐 ║
╚══════════════════════════════════════╝
     A Magical Way to Secure Your Keys
""")

def generate_password(length, upper, lower, digits, symbols):
    char_pool = ''
    if upper: char_pool += string.ascii_uppercase
    if lower: char_pool += string.ascii_lowercase
    if digits: char_pool += string.digits
    if symbols: char_pool += string.punctuation

    if not char_pool:
        return None

    return ''.join(random.choice(char_pool) for _ in range(length))

def suggest_passphrase():
    words = ['wizard', 'phoenix', 'galaxy', 'quantum', 'dragon', 'nebula', 'matrix', 'puzzle']
    return '-'.join(random.choices(words, k=4))

def main():
    display_banner()
    try:
        length = int(input("🔢 Enter desired password length (min 6): "))
        if length < 6:
            print("❗ Password too short. Minimum is 6.")
            return

        print("\nSelect components for your password:")
        upper = input("Include UPPERCASE letters? (y/n): ").strip().lower() == 'y'
        lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
        symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, upper, lower, digits, symbols)
        if not password:
            print("⚠️  No character types selected. Try again!")
            return

        print("\n✨ Generated Password:")
        print(f"🔐 {password}")
        print(f"📈 Strength: {password_strength(password)}")

        copy_choice = input("\n📋 Copy to clipboard? (y/n): ").strip().lower()
        if copy_choice == 'y':
            pyperclip.copy(password)
            print("✅ Password copied to clipboard!")

        extra = input("\n🪄 Want a secure passphrase instead? (y/n): ").strip().lower()
        if extra == 'y':
            phrase = suggest_passphrase()
            print(f"\n🔑 Suggested Passphrase: {phrase}")

        print("\n🎉 Done! Stay safe out there in the digital world 🛡️")
    
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
