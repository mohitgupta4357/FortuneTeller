# fortune.py

import datetime
import random

def colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def get_fortune(mood, name):
    fortunes = {
        "happy": [
            f"Great things await you, {name}! Keep shining 🌞",
            f"Your joy is contagious, {name}—spread it around! 🎉",
            "Today, the universe dances with you! 💃",
            f"You're glowing, {name}—and the world notices ✨"
        ],
        "sad": [
            f"Every storm passes, {name}—sunshine is on the way 🌦️",
            "You’re stronger than you think 🌈",
            f"This is just a chapter, {name}, not your whole story 📖",
            f"Even the moon has its phases, {name}. Brighter days are near 🌙"
        ],
        "neutral": [
            "A small surprise will brighten your day soon 🎁",
            f"Stay open, {name}—magic hides in the ordinary ✨",
            "Balance is your superpower today ⚖️",
            f"An unexpected message is headed your way, {name} 📬"
        ],
        "unknown": [
            f"Something good is coming your way, {name} 🌠",
            f"The future is mysterious, {name}—but always full of potential 🔮",
            f"Destiny favors the curious, {name} 👁️"
        ]
    }
    return random.choice(fortunes.get(mood, fortunes["unknown"]))

def mood_emoji(mood):
    return {
        "happy": "😄",
        "sad": "😢",
        "neutral": "😐"
    }.get(mood, "🌀")

def main():
    name = "Mohit Gupta"
    first_name = name.split()[0]
    admission_number = "21JE0569"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(colored(f"\n🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮", "1;35"))
    print(colored(f"🕒 {current_time}\n", "1;30"))

    while True:
        mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

        if mood not in ["happy", "sad", "neutral"]:
            print(colored("⚠️ I didn’t quite get that mood, but I’ll read your fortune anyway!", "1;33"))
            mood = "unknown"

        fortune = get_fortune(mood, first_name)
        emoji = mood_emoji(mood)

        print(colored(f"\n{emoji} Your fortune: {fortune}", "1;36"))

        retry = input(colored("\nWould you like another fortune? (yes/no): ", "1;32")).strip().lower()
        if retry != "yes":
            print(colored(f"\n🔚 Thanks for visiting the Fortune Teller, {first_name}. Stay awesome! ✌️", "1;35"))
            break

if __name__ == "__main__":
    main()
