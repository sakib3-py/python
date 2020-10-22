import getpass
def sign_up():
    user_name = input("")
    passwrd = getpass.getpass("")
    
    email = input("")
    phone_num =len(input(""))

    while True:
        if len(passwrd) < 9  :
            print("password should be at least 8 characters long:)")
            passwrd = getpass.getpass()
        elif len(passwrd) >=  8:
            break
        
    server_store = {
        "name":user_name,
        "password":passwrd,
        "Email":email,
        "phone":phone_num
    }
    print("You have successfully signedup.Now pls login")
    while True:
        user_id = input("Enter your user id: ")
        passkey= input("Enter your password: ")
        if user_id == server_store["name"] and passkey == server_store["password"]:
            print(f"welcome {user_id}! A new journey begins.")
            print("1.reset password")
            print("2.logout")
            user_input = input("")
            if user_input == "reset password":
                new_pass = getpass.getpass()
                server_store["password"] = new_pass
                print("your password has been reset")
            elif user_input == "logout":
                print("You have successfully logged out.")
            else:
                print("Thanks for staying with us")
                break
                

            
        elif user_id != server_store["name"] or passkey !=server_store["password"]:
            print("User name or password is incorrect,please try again")
sign_up()
            




