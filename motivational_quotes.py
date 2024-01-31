import random

class MotivationalQuotes:
    def __init__(self):
        self.quotes = [
            "Believe you can and you're halfway there. -Theodore Roosevelt",
            "The only way to do great work is to love what you do. -Steve Jobs",
            "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
            "It always seems impossible until it's done. -Nelson Mandela",
            "Your time is limited, don't waste it living someone else's life. -Steve Jobs",
            "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. -Christian D. Larson",
            "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
            "The only limit to our realization of tomorrow will be our doubts of today. -Franklin D. Roosevelt",
            "Success is not final, failure is not fatal: It is the courage to continue that counts. -Winston Churchill",
            "The only person you are destined to become is the person you decide to be. -Ralph Waldo Emerson",
            "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
            "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. -Roy T. Bennett",
            "Do not wait to strike till the iron is hot, but make it hot by striking. -William Butler Yeats",
            "It's not about how hard you hit. It's about how hard you can get hit and keep moving forward. -Rocky Balboa",
            "The only way to achieve the impossible is to believe it is possible. -Charles Kingsleigh"
        ]

    def print_random_quote(self):
        random_quote = random.choice(self.quotes)
        print(random_quote)

if __name__ == "__main__":
    motivational_quotes = MotivationalQuotes()
    motivational_quotes.print_random_quote()
