# fortune.py

def main():
    # Personal details
    name = "Mohit Gupta"
    admission_number = "21JE0569"

    # Welcome message
    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮")

    # Get user mood
    mood = input(
        "How are you feeling today? (happy/sad/neutral): ").strip().lower()

    # Mood-based fortune
    if mood == "happy":
        print(
            f"✨ Your fortune: Great things await you, {name.split()[0]}! Keep smiling. ✨")
    elif mood == "sad":
        print("✨ Your fortune: Every storm passes—sunshine is on the way. ✨")
    elif mood == "neutral":
        print("✨ Your fortune: A small surprise will brighten your day soon. ✨")
    else:
        print("✨ I couldn't understand your mood, but something good is coming your way! ✨")


if __name__ == "__main__":
    main()
    