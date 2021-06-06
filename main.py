def main():
    user_input = input("Type in an acronym: \n")
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
    else:
        print("That acronym does not exist")


if __name__ == "__main__":
    main()
