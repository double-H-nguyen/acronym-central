def main():
    while True:
        user_input = input("Type in an acronym/abbreviation: \n")
        user_input = user_input.lower()

        if (user_input == "mon"):
            print("Monday")
        elif (user_input == "tue"):
            print("Tuesday")
        elif (user_input == "wed"):
            print("Wednesday")
        elif (user_input == "thurs"):
            print("Thursday")
        elif (user_input == "fri"):
            print("Friday")
        elif (user_input == "lol"):
            print("Laugh Out Loud")
        else:
            print("That acronym does not exist")

        user_input = input(
            "Do you want to search another acronym? Type 'no' to exit program or enter anything to continue: ")
        if (user_input.lower() == 'no'):
            break

    print('Thanks for using Acronym Central!')

if __name__ == "__main__":
    main()
