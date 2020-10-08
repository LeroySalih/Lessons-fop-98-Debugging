

def main():
    bank = 100
    choice = input("How much to withdraw?")
    choice = int(choice)

    if (choice > bank):
        choice = bank

    print("Giving you ", choice, "SAR")
    bank = bank + choice
    print("You have ", bank, "SAR remaining.")
    
if __name__ == "__main__":
    main()
    