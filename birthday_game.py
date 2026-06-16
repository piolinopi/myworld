#!/usr/bin/env python3
"""
🎂 BIRTHDAY CELEBRATION GAME 🎂
A fun interactive game to celebrate birthdays!
"""

import random
import time
from typing import List, Tuple

class BirthdayGame:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.celebrations = [
            "🎉 Awesome!",
            "🎊 Fantastic!",
            "🎈 Great job!",
            "🎁 Excellent!",
            "✨ Amazing!",
            "🌟 Outstanding!"
        ]
        
    def print_banner(self, text: str):
        """Print a festive banner"""
        width = len(text) + 4
        print("\n" + "🎂" * (width // 2))
        print(f"  {text}")
        print("🎂" * (width // 2) + "\n")
    
    def game_intro(self):
        """Display game introduction"""
        self.print_banner("🎉 Happy B'Day 18th 🎉")
        print("🎂assiiikk!! udah tuaa aja lwuh, aku punya hadiah🎉")
        print("Eiittss sebelum itu pilih mode game dulu:")
        print("\nChoose your game mode:")
        print("1. 👀Quiz awal mula (Tanya jawab)")
        print("2. Tebak gambar🖼 (Potongan Gambar)")
        print("3. ✨Memory Game (Kenangan yang membekas)")
        print("4. Birthday Countdown🎁 (Jangan di buka (sebenernya gpp sih:v))")
        return input("\nSelect mode (1-4): ").strip()
    
    def 👀Quiz_awal_mula(self):
        """Play 👀Quiz awal mula"""
        print("\n" + "=" * 40)
        print("👀Quiz awal mula")
        print("=" * 40 + "\n")
        
        questions = [
            {
                "question": "Kalau ulang tahunmu di rayain, kamu bakal ngapain?",
                "options": ["A) Balik tidur", "B) pura - pura ga tau", "C) ikut ngerayain ", "D) sikap biasa"],
                "answer": "C"
            },
            {
                "question": "How many candles are typically on a birthday cake?",
                "options": ["A) 100", "B) 1", "C) Your age", "D) 13"],
                "answer": "C"
            },
            {
                "question": "What's the most common birthday song?",
                "options": ["A) Happy Birthday", "B) Birthday Cake", "C) Celebrate", "D) Party On"],
                "answer": "A"
            },
            {
                "question": "What is a common birthday gift?",
                "options": ["A) Homework", "B) Soap", "C) Present", "D) Vegetables"],
                "answer": "C"
            },
            {
                "question": "How often do you have a birthday?",
                "options": ["A) Every month", "B) Once a year", "C) Every 4 years", "D) Never"],
                "answer": "B"
            }
        ]
        
        correct = 0
        for i, q in enumerate(questions, 1):
            print(f"Question {i}/5: {q['question']}")
            for option in q['options']:
                print(f"  {option}")
            
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            
            if answer == q['answer']:
                print("✅ Assyyiikk bener nich")
                correct += 1
                self.score += 10
            else: answer == q['answer']:
                print("✅ Yaahhooo!!")
                correct += 1
                self.score += 10
            else: answer == q['answer']:
                print("✅ Lagi bang! nambah teruss")
                correct += 1
                self.score += 10
            else:
                print(f"❌ Hayoo mencet yang mana😒 {q['answer']}")
            print()
            else:
                print(f"❌ Jawab yang bener😒 {q['answer']}")
            print()
            else:
                print(f"❌ Jangan asal jawab😒 {q['answer']}")
            print()
        
        print(f"\n📊 Results: {correct}/5 correct!")
        print(f"Points earned: {correct * 10}")
        print(f"Total score: {self.score}")
    
    def number_guessing(self):
        """Guess the mystery number"""
        print("\n" + "=" * 40)
        print("🔢 NUMBER GUESSING MODE")
        print("=" * 40 + "\n")
        
        secret = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        
        print("I'm thinking of a number between 1 and 100...")
        print(f"You have {max_attempts} attempts!\n")
        
        while attempts < max_attempts:
            try:
                guess = int(input("Guess a number: "))
                attempts += 1
                
                if guess == secret:
                    points = max(50 - attempts * 5, 10)
                    self.score += points
                    print(f"\n🎉 You got it! The number was {secret}!")
                    print(f"You guessed in {attempts} attempts!")
                    print(f"Points earned: {points}")
                    print(f"Total score: {self.score}\n")
                    return
                elif guess < secret:
                    print(f"📈 The number is higher! ({max_attempts - attempts} attempts left)\n")
                elif guess > secret:
                    print(f"📉 The number is lower! ({max_attempts - attempts} attempts left)\n")
            except ValueError:
                print("Please enter a valid number!\n")
        
        print(f"❌ Game Over! The number was {secret}")
        print(f"Final score: {self.score}\n")
    
    def memory_game(self):
        """Memory sequence game"""
        print("\n" + "=" * 40)
        print("🧠 MEMORY GAME")
        print("=" * 40 + "\n")
        
        sequence = []
        level = 1
        
        while True:
            # Add new number to sequence
            sequence.append(random.randint(1, 4))
            
            print(f"🎯 Level {level}")
            print(f"Watch the sequence: {' '.join(map(str, sequence))}")
            time.sleep(2)
            print("\033[H\033[J")  # Clear screen
            
            # Get user input
            user_sequence = []
            print(f"Repeat the sequence (separated by spaces):")
            try:
                user_sequence = list(map(int, input().split()))
            except ValueError:
                print("❌ Invalid input! Game Over!")
                print(f"You reached level {level}")
                print(f"Points earned: {level * 20}")
                self.score += level * 20
                print(f"Total score: {self.score}\n")
                return
            
            if user_sequence == sequence:
                print(f"✅ Correct!")
                self.score += 20
                level += 1
                time.sleep(1)
            else:
                print(f"❌ Wrong! The sequence was: {' '.join(map(str, sequence))}")
                print(f"You reached level {level}")
                print(f"Points earned: {level * 20}")
                self.score += level * 20
                print(f"Total score: {self.score}\n")
                return
    
    def birthday_countdown(self):
        """Birthday bomb defusing game"""
        print("\n" + "=" * 40)
        print("💣 BIRTHDAY BOMB DEFUSAL")
        print("=" * 40 + "\n")
        
        print("⚠️  A birthday surprise is about to explode!")
        print("Answer math questions to defuse it!\n")
        
        problems = [
            {"equation": "5 + 3", "answer": 8},
            {"equation": "12 - 7", "answer": 5},
            {"equation": "6 × 4", "answer": 24},
            {"equation": "20 ÷ 4", "answer": 5},
            {"equation": "3² + 4", "answer": 13},
        ]
        
        for i, problem in enumerate(problems, 1):
            print(f"⏱️  Problem {i}/5")
            try:
                answer = int(input(f"Solve: {problem['equation']} = "))
                if answer == problem['answer']:
                    print("✅ Correct! Wire defused!\n")
                    self.score += 15
                else:
                    print(f"❌ Wrong! The answer is {problem['answer']}\n")
            except ValueError:
                print("❌ Invalid input!\n")
        
        print("🎉 BOMB DEFUSED! Birthday Saved!")
        print(f"Total score: {self.score}\n")
    
    def run(self):
        """Main game loop"""
        while True:
            mode = self.game_intro()
            
            if mode == "1":
                self.trivia_mode()
            elif mode == "2":
                self.number_guessing()
            elif mode == "3":
                self.memory_game()
            elif mode == "4":
                self.birthday_countdown()
            else:
                print("Invalid mode selected!")
                continue
            
            # Ask to play again
            play_again = input("Play another round? (yes/no): ").strip().lower()
            if play_again != "yes" and play_again != "y":
                break
        
        self.print_banner(f"🎂 FINAL SCORE: {self.score} 🎂")
        print("Thanks for playing! Have an amazing birthday! 🎉")


if __name__ == "__main__":
    game = BirthdayGame()
    game.run()
