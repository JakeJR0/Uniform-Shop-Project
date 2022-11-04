"""

This is the section that allows the user to select what items a user wants to order

"""
import pandas as pd
from datetime import datetime, date
import re

# This opens Data.csv and stores its contents as a usable dataframe
def csv_read():
    """
    This opens the Data.csv and stores its contents as a usable dataframe
    """
    df = pd.read_csv("Data.csv")
    df.set_index("School")
    # df variavle is the dataframe that will be called on during the program
    return df


# The choose function checks if what the user selected is actually an availible item
def choose(choice, availible):
    """
    The choose functoin checks if what the user selected is actually an availble item
    """
    choice = choice.lower()
    # If the user choice is not in the list of availible schools, you'll have to choose schools again until it is
    while choice not in availible:
        choice = input(
            "\nWe don't have any records of that. Did you request correctly? Try typing again.  "
        ).lower()
        # This little section here is pretty much an easter egg, take the program's instruction litteraly, and it'll question your input.
        if choice == "again":
            choice = input("I...  didn't mean it like that ").lower()
    return str.title(choice)


def school_menu():
    """
    Function that allows you to select the school that the uniform will be ordered from
    """
    df = csv_read()

    print("Welcome to the uniform creation service!")
    print(
        "\nWe support these 6 schools:\nPrimary Schools A-D, Secondary School A and Secondary School B "
    )
    print(
        "Once a school has been selected, you can add multiple items from that school into your order.\n"
    )

    school_choice = input("Please type in what school you would like a uniform for ")
    # This takes the names of the schools from the database and makes it the list of names you can choose to search for. This means that if the number of schools were to change, the availbile search terms will change with it.
    availible_schools = []
    for i in df.index:
        if (
            df.loc[i, "School"].lower() not in availible_schools
            and df.loc[i, "School"] not in availible_schools
        ):
            toAppend = str(df.loc[i, "School"])
            availible_schools.append(toAppend.lower())

    availible_schools_backup = [
        "primary school a",
        "primary school b",
        "primary school c",
        "primary school d",
        "secondary school a",
        "secondary school b",
    ]
    try:
        school_to_show = choose(school_choice, availible_schools)
    except:
        print(
            "\nThere seems to be an issue with our database. As a result, our availible schools may be affected."
        )
        school_to_show = choose(school_choice, availible_schoolsBackup)

    find_schools(df, school_to_show)


def find_schools(df, school_to_show):
    """
    After it has been verified by the first instance of the choose function, This function finds the dataframe records whose school matches what the user chose
    """
    print("\nHere are the results: \n")
    filter = []
    try:
        for i in df.index:
            if df.iloc[i]["School"] == school_to_show:
                print(df.iloc[i], "\n" + "-_" * 25 + "\n")
                filter.append(df.iloc[i])
    except:
        print(
            "Looks like something's gone wrong. Maybe you asked for something we don't support. You should restart and try searching again."
        )

    print("Here are the availible items for " + school_to_show + ":\n\n")
    # Calls the function to specifically display the items, category and prices for said items
    selectable = display_items(school_to_show, df)
    order_choice(df, school_to_show, selectable)


# This loops through the Dataframe and only dispays the Type name, category and price of each entery that is in the school you chose  (uncleaned)
def display_items(school_to_show, df):
    selectable = []
    for i in df.index:
        if df.loc[i, "School"] == school_to_show:
            if df.loc[i, "Category"] == "Both":
                print(
                    " ."
                    + str(df.loc[i, "Type"])
                    + " for all genders . "
                    + "£"
                    + str(df.loc[i, "Price"])
                    + "\n"
                )
            else:
                print(
                    " ."
                    + str(df.loc[i, "Type"])
                    + " for "
                    + str(df.loc[i, "Category"])
                    + " . £"
                    + str(round(df.loc[i, "Price"], 2))
                    + "\n"
                )
            # This adds only the type name to a list of items that will be selectable later in the program
            selectable.append(str(df.loc[i, "Type"]).lower())
    return selectable



def order_choice(df, school_to_show, selectable):
    """
    This function has the user decide what to add to their order
    """
    recipt_list = ["Your recipt:"]
    total_cost = 0.0
    # The 'loop_count' variable will count how many itmes an item has been added to the list. We can add this number to the recipt as an order number
    loop_count = 0
    keep_going = 1
    # The 'keep_going' variable is one that detertmines your menuchoice. It's named this way it is because it has the ablility to stop this menu
    while keep_going != 3:
        if keep_going == 1:
            # The 3 lines below will advise the user to scroll up to see the availible items every three loops of the user adding items
            if loop_count % 3 == 0 and loop_count != 0:
                print("\nHere are the availible items again, no need to scroll:\n")
                display_items(school_to_show, df)

            item_choice = input(
                "\nWhat type of item are you looking for? If you don't want anything, then type nothing. "
            )
            item_choice = str.title(item_choice)
            # The item will only go through the adding process if the user did not input nothing or 'nothing'. If they did, the adding process is ignored
            if item_choice != "Nothing" and item_choice != "":
                # We need to call the choice function to make sure that the item we asked for is availbile in the school - different schools have different items
                type_to_show = choose(item_choice, selectable)
                # This finds the price of the item selected
                school = df.loc[df.School == school_to_show]
                school = school.loc[school.Type == type_to_show]
                gender = ""
                for i in school.index:
                    price = school.loc[i, "Price"]
                    if gender == "":
                        gender = school.loc[i, "Category"]
                    # If there is a version of the same item for different categories, you will be asked to decide which version of the item you want
                    # Currently Bugged
                dupes = school.duplicated(subset="Type")
                done = False
                for i in dupes:
                    if i == True and done == False:
                        gender = input(
                            "\nThis item is different depending on if it's for boys or girls. Please type either boys or girls to decide which type you want. "
                        )
                        gender = str.title(gender)
                        while gender != "Boys" and gender != "Girls":
                            gender = input("\nPlease type either boys or girls. ")
                            gender = str.title(gender)
                        done = True

                # This adds the price found into the recipt and tells it to you.
                print("\nThat's £" + str(price) + ". It's been added to your recipt")
                total_cost += price
                print("Your total cost is now £" + str(total_cost))
                loop_count += 1

                # These lines set both the now variable and the date variable. 'now' is set to the current time, and the line below the 'now' assignment formats it to Hours:Minutes:Seconds
                order_date = date.today()
                now = datetime.now()
                order_time = now.strftime("%H:%M:%S")
                recipt = ""
                recipt = f"Order number: {loop_count} - Date: {order_date} - Time: {order_time} - School: {str.title(school_to_show)}  - You ordered {str.title(type_to_show)} - Category: {gender} - Price: £{price}"
                recipt_list.append(str(recipt))
            else:
                print("\nOkay, we'll take you to the recipt menu, then.")

        # This is a query asking what you want to do next
        carry_on = False
        while carry_on == False:
            try:
                keep_going = int(
                    input(
                        "\nWhat would you like to do next?\n\n1.Add an item\n2.Remove an item\n3.Stop adding items\n4.See the recipt\nPlease type a number to select. "
                    )
                )
                carry_on = True
            except:
                keep_going = print("Please enter a number. It must be between 1 and 4.")
                carry_on = False

        if keep_going > 4 or keep_going < 1:
            while keep_going > 4 or keep_going < 1:
                try:
                    keep_going = int(input("\nPlease enter a number between 1 and 4 "))
                except:
                    keep_going = 0

        if keep_going == 2:
            # The 2nd option in keep_going allows the user to delete an item from the list
            if recipt_list != ["Your recipt:"]:
                print("Before deciding what to remove, here is the recipt:\n")
                for i in recipt_list:
                    print(i)
                try:
                    to_del = int(
                        input(
                            "\nPlease enter the order number of the order you'd like to remove: (Enter -1 to cancel) "
                        )
                    )
                except:
                    to_del = int(input("Please make sure you input a number! "))
                if to_del != -1:
                    try:
                        # This will find the final number of the recipt entry you wish to delete, (which is always the price) and removes it from the final cost.
                        found_price = [
                            float(found_price)
                            for found_price in re.findall(
                                r"-?\d+\.?\d*", recipt_list[to_del]
                            )
                        ]
                        print(recipt_list[to_del])
                        total_cost = total_cost - found_price[len(found_price) - 1]
                        recipt_list[to_del] = "Item removed"

                        print("\nIt has been removed")
                        print("Your total cost is now £" + str(total_cost))
                    except:
                        print(
                            "\nSomething went wrong when trying to delete that item. \nIs your choice of",
                            to_del,
                            "actually an entry in the list? \nPlease try again. ",
                        )
                else:
                    print("\nAlright. We'll skip the deletion")

            else:
                print(
                    "\nThat will be a problem, considering the fact the recipt is empty: there's nothing to remove!"
                )
            # If the user decides to delete the 0th entry in the recipt (Which is an introduction), these 2 lines below will add it back.
            if "Your recipt" not in recipt_list:
                recipt_list[0] = "Your recipt:"

        if keep_going == 3:
            # If you select to stop adding, the program will ask you here if you're sure.
            keep_going = input("\nAre you sure you want to stop adding? Y/N ")
            while (
                keep_going.lower() != "yes"
                and keep_going.lower() != "y"
                and keep_going.lower() != "no"
                and keep_going.lower() != "n"
            ):
                # If you don't answer either yes or no, you'll be asked to input it again
                keep_going = input("\nPlease answer either yes or no. ")
            if keep_going.lower() == "no" or keep_going.lower() == "n":
                keep_going = 1
            elif keep_going.lower() == "yes" or keep_going.lower() == "y":
                keep_going = 3

        if keep_going == 4:
            # This prints the current recipt list, so you can make adjustments
            if recipt_list != ["Your recipt:"]:
                print("\nHere's your recipt so far:\n")
                for i in recipt_list:
                    print(i)
            else:
                print("\nThe recipt is squeaky clean. Nothing to see here!")

    # This final section opens a txt file and stores the recipt contents into it
    if recipt_list != ["Your recipt:"]:
        final = open("recipt.txt", "a")
        print("Your final recipt:\n")
        for i in recipt_list:
            final.write(i)
            final.write("")
            print(i)
        final.write("Total price: £" + str(total_cost))
        print("Total price: £" + str(total_cost))
        final.write("\n\n")
        final.close()
        print(
            "\nThis has been saved to a file. Thank you for using the ordering service!"
        )
    else:
        print(
            "Even though you didn't get anything, we're glad you came.\nThanks for using the service!"
        )


# This can be tested by running the main script
if __name__ == "__main__":
    school_menu()
