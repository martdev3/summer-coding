from datetime import datetime

def main():
    name = input("What is your name? ")
    favLang = input("What is your favorite programming language? ")
    now = datetime.now().strftime("%A, %B %d at %I:%M %p")
    daysUntilEndOfSummer = daysUntilDate(2026, 9, 1)
    print(f"Hi {name}, you started your summer coding on {now} with {favLang}.")

    if daysUntilEndOfSummer < 30:
        print(f"There are {daysUntilEndOfSummer} days left until the end of summer. Get READY!")
    else:
        print(f"There are {daysUntilEndOfSummer} days left until the end of summer. Keep coding and have fun!")

def daysUntilDate(year,month, day):
    today = datetime.now()
    futureDate = datetime(year, month, day)
    delta = futureDate - today
    return delta.days

if __name__ == "__main__":    
    main()