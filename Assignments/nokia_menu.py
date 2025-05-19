menu_loop = 1

while menu_loop == 1:
    print(" MAIN MENU ")
    print("1. Phone book")
    print("2. Messages")
    print("3. Call register")
    print("4. Tones")
    print("5. Settings")
    print("6. Call divert")
    print("7. Games")
    print("8. Calculator")
    print("9. Reminders")
    print("10. Clock")
    print("11. Profiles")
    print("12. SIM services")
    
    choice = input("Pick a main option: ")

    if choice == "1":  
        print("\n Phone book ")
        print("1. Search")
        print("2. Service Nos.")
        print("3. Add name")
        print("4. Erase")
        print("5. Edit")
        print("6. Assign tone")
        print("7. Send b’card")
        print("8. Options")
        print("  1. Type of view")
        print("  2. Memory status")
        print("9. Speed dials")
        print("10. Voice tags")
       
        sub_choice = input("select: ")
        if sub_choice == "1":
            print("Searching contacts... Search for a name!")
        elif sub_choice == "2":
            print("Showing service numbers")
        elif sub_choice == "3":
            print("Adding a new name, nice!")
        elif sub_choice == "4":
            print("Erase all contact")
        elif sub_choice == "5":
            print("Edit a name")
        elif sub_choice == "6":
            print("set a tone for a contact!")
        elif sub_choice == "7":
            print("Sending a business card")
        elif sub_choice == "8":
            sub_sub = input("View type (1) or Memory (2)? ")
            if sub_sub == "1":
                print("Changing view type...")
            elif sub_sub == "2":
                print("Checking memory status...")
        elif sub_choice == "9":
            print("Setting up speed dials!")
        elif sub_choice == "10":
            print("Setting voice tags, sweet!")
        elif sub_choice == "":
            print("invalid option!")  # Note: This might need a logic fix

    elif choice == "2":  
        print("\n Messages ")
        print("1. Write messages")
        print("2. Inbox")
        print("3. Outbox")
        print("4. Picture messages")
        print("5. Templates")
        print("6. Smiley")
        print("7. Message settings")
        print("  1. Set 1")
        print("    1. Message centre number")
        print("    2. Messages sent as")
        print("    3. Message validity")
        print("  2. Common")
        print("    1. Delivery reports")
        print("    2. Reply via same centre")
        print("    3. Character support")
   
        sub_choice = input("Pick a sub-option or Enter 0 to back: ")
        if sub_choice == "1":
            print("Writing a message, let’s go!")
        elif sub_choice == "2":
            print("Checking inbox, any texts?")
        elif sub_choice == "3":
            print("Looking at outbox...")
        elif sub_choice == "4":
            print("Sending a pic message!")
        elif sub_choice == "5":
            print("Using a template, easy!")
        elif sub_choice == "6":
            print("Adding a smiley!")
        elif sub_choice == "7":
            sub_sub = input("Set 1 (1) or Common (2)? ")
            if sub_sub == "1":
                sub_sub2 = input("Centre (1), Sent as (2), or Validity (3)? ")
                if sub_sub2 == "1":
                    print("Setting message centre number...")
                elif sub_sub2 == "2":
                    print("Choosing how messages are sent...")
                elif sub_sub2 == "3":
                    print("Setting message validity...")
            elif sub_sub == "2":
                sub_sub2 = input("Delivery (1), Reply (2), or Character (3)? ")
                if sub_sub2 == "1":
                    print("Toggling delivery reports...")
                elif sub_sub2 == "2":
                    print("Setting reply via same centre...")
                elif sub_sub2 == "3":
                    print("Adjusting character support...")
        elif sub_choice == "":
            print("Back to main menu!")
        else:
            print("invalid choce fam!")

    elif choice == "3": 
        print("\n Call register ")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialled numbers")
        print("4. Erase recent call lists")
        print("5. Show call duration")
        print("  1. Last call duration")
        print("  2. All calls’ duration")
        print("  3. Received calls’ duration")
        print("  4. Dialled calls’ duration")
        print("  5. Clear timers")
        print("6. Show call costs")
        print("  1. Last call cost")
        print("  2. All calls’ cost")
        print("  3. Clear counters")
        print("7. Call cost settings")
        print("  1. Call cost limit")
        print("  2. Show costs in")
        print("  3. Prepaid credit")
       
        sub_choice = input("Pick an option or Enter 0 to back: ")
        if sub_choice == "1":
            print("Showing missed calls...")
        elif sub_choice == "2":
            print("Checking received calls...")
        elif sub_choice == "3":
            print("Looking at dialled numbers...")
        elif sub_choice == "4":
            print("Erasing call lists, done!")
        elif sub_choice == "5":
            sub_sub = input("Last (1), All (2), Received (3), Dialled (4), or Clear (5)? ")
            if sub_sub == "1":
                print("Showing last call duration...")
            elif sub_sub == "2":
                print("Total call duration")
            elif sub_sub == "3":
                print("Received calls duration...")
            elif sub_sub == "4":
                print("Dialled calls duration...")
            elif sub_sub == "5":
                print("Clearing timers, reset")
        elif sub_choice == "6":
            sub_sub = input("Last (1), All (2), or Clear (3)? ")
            if sub_sub == "1":
                print("Last call cost, check it!")
            elif sub_sub == "2":
                print("All calls cost, big spender!")
            elif sub_sub == "3":
                print("Clearing cost counters...")
        elif sub_choice == "7":
            sub_sub = input("Limit (1), Show (2), or Credit (3)? ")
            if sub_sub == "1":
                print("Setting call cost limit...")
            elif sub_sub == "2":
                print("Showing costs in your currency...")
            elif sub_sub == "3":
                print("Checking prepaid credit...")
        elif sub_choice == "":
            print("Back to main menu!")
        else:
            print("invalid choce fam!")

    elif choice == "4":  
        print("\n Tones ")
        print("1. Ringing tone")
        print("2. Ringing volume")
        print("3. Incoming call alert")
        print("4. Composer")
        print("5. Message alert tone")
        print("6. Keypad tones")
        print("7. Warning and game tones")
        print("8. Vibrating alert")
        print("9. Screen saver")
        
        sub_choice = input("Pick an option or Enter to back: ")
        if sub_choice == "1":
            print("Picking a ringing tone, nice!")
        elif sub_choice == "2":
            print("Adjusting ringing volume...")
        elif sub_choice == "3":
            print("Setting incoming call alert...")
        elif sub_choice == "4":
            print("Composing a tone, get creative!")
        elif sub_choice == "5":
            print("Choosing message alert tone...")
        elif sub_choice == "6":
            print("Toggling keypad tones...")
        elif sub_choice == "7":
            print("Setting warning/game tones...")
        elif sub_choice == "8":
            print("Turning on vibrating alert...")
        elif sub_choice == "9":
            print("Setting up screen saver...")
        elif sub_choice == "":
            print("Back to main menu!")
        else:
            print("invalid choce fam!")

    elif choice == "5": 
        print("\n Settings ")
        print("1. Call settings")
        print("  1. Automatic redial")
        print("  2. Speed dialling")
        print("  3. Call waiting options")
        print("  4. Own number sending")
        print("  5. Phone line in use")
        print("  6. Automatic answer")
        print("2. Phone settings")
        print("  1. Language")
        print("  2. Cell info display")
        print("  3. Welcome note")
        print("  4. Network selection")
        print("  5. Lights")
        print("  6. Confirm SIM service actions")
        print("3. Security settings")
        print("  1. PIN code request")
        print("  2. Call barring service")
        print("  3. Fixed dialling")
        print("  4. Closed user group")
        print("  5. Phone security")
        print("  6. Change access codes")
        print("4. Restore factory settings")
        
        sub_choice = input("selcet an or Enter to back: ")
        if sub_choice == "1":
            sub_sub = input("Redial (1), Speed (2), Waiting (3), Own num (4), Line (5), Auto (6)? ")
            if sub_sub == "1":
                print("Turning on auto redial...")
            elif sub_sub == "2":
                print("Setting up speed dial...")
            elif sub_sub == "3":
                print("Adjusting call waiting...")
            elif sub_sub == "4":
                print("Sending own number...")
            elif sub_sub == "5":
                print("Switching phone line...")
            elif sub_sub == "6":
                print("Setting auto answer...")
        elif sub_choice == "2":
            sub_sub = input("Language (1), Cell info (2), Welcome (3), Network (4), Lights (5), Confirm (6)? ")
            if sub_sub == "1":
                print("Choosing language...")
            elif sub_sub == "2":
                print("Toggling cell info...")
            elif sub_sub == "3":
                print("Setting welcome note...")
            elif sub_sub == "4":
                print("Picking network...")
            elif sub_sub == "5":
                print("Adjusting lights...")
            elif sub_sub == "6":
                print("Confirming SIM actions...")
        elif sub_choice == "3":
            sub_sub = input("PIN (1), Barring (2), Fixed (3), Closed (4), Security (5), Codes (6)? ")
            if sub_sub == "1":
                print("Setting PIN code...")
            elif sub_sub == "2":
                print("Barring calls...")
            elif sub_sub == "3":
                print("Fixing dialling...")
            elif sub_sub == "4":
                print("Setting closed user group...")
            elif sub_sub == "5":
                print("Locking phone security...")
            elif sub_sub == "6":
                print("Changing access codes...")
        elif sub_choice == "4":
            print("Restoring factory settings, here we go!")
        elif sub_choice == "":
            print("Back to main menu!")
        else:
            print("Pick 1-4 or hit Enter, man!")

    elif choice == "6":  
        print("\n Call divert ")
        print("Setting up call divert options...")
        input("Hit Enter to go back: ")
        print("Back to main menu!")

    elif choice == "7":  
        print("\n Games ")
        print("Playing some Nokia games, good times!")
        input("Hit Enter to go back: ")
        print("Back to main menu!")

    elif choice == "8":  
        print("\n Calculator ")
        print("lets do some calculations")
        input("Hit Enter to go back: ")
        print("Back to main menu!")

    elif choice == "9": 
        print("\n Reminders ")
        print("Setting a reminder, don’t forget!")
        input("Hit Enter to go back: ")
        print("Back to main menu!")

    elif choice == "10":  
        print("\n Clock ")
        print("1. Alarm clock")
        print("2. Clock settings")
        print("  1. Date setting")
        print("  2. Stopwatches")
        print("  3. Countdown timer")
        print("  4. Auto update of date and time")
        sub_choice = input("select an option or Enter to back: ")
        if sub_choice == "1":
            print("Setting an alarm, wake up!")
        elif sub_choice == "2":
            sub_sub = input("Date (1), Stopwatch (2), Timer (3), or Auto (4)? ")
            if sub_sub == "1":
                print("Setting the date...")
            elif sub_sub == "2":
                print("Starting a stopwatch...")
            elif sub_sub == "3":
                print("Setting a countdown timer...")
            elif sub_sub == "4":
                print("Auto updating date/time...")
        elif sub_choice == "":
            print("Back to main menu!")
        else:
            print("invalid choce fam!")

    elif choice == "11":  
        print("\n Profiles ")
        print("Switching profiles, personalize it!")
        input("Hit Enter to go back: ")
        print("Back to main menu!")

    elif choice == "12":  
        print("\n SIM services ")
        print("Accessing SIM stuff...")
       
        sub_choice = input("Hit Enter to exit or anything else to back: ")
        if sub_choice == "":
            print("Exiting Nokia menu, see ya!")
            menu_loop = 0  
        else:
            print("Yo invalid choce fam!")

    print("")