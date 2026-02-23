# Create a simple login system using files.

users_Dict = {   #empty dictionary
 
}    

def update_Dictionary():
  #updating dictionary with the information from the file

  users_Dict.clear()    # resetting the dictionary
  try:
    with open("users.txt", "r") as f:
      users_List = f.readlines()

      for user in users_List:
        line = user.strip()      #strip() --> removes whitespace from both ends.

        # skip blank lines
        if not line:  
          continue

        parts = line.split()      #split() --> splits based on whitespaces

        # skip malformed lines (more than 2 words / parts)
        if (len(parts) != 2):
          continue

        #if not then take username and password
        userName, password = parts
        
        users_Dict[userName] = password

  except FileNotFoundError:
    print("File not found!!!")

update_Dictionary()

while True:
  print("\n----- Menu -----")
  print("1. Login")
  print("2. Register")
  print("3. Exit")

  try:
    choice = int(input("Enter your choice: "))
  except ValueError:
    print("Invalid choice! Please choose a number beteen 1-3.")
    continue

  if choice == 1:
    userName = input("\nEnter your username: ")

    if userName not in users_Dict:
      print("User does not exist. Please register first.")

    else:
      password = input("Enter your password: ")
      if password != users_Dict.get(userName):
        print("Incorrect password!!!")
      else:
        print("------ Logged in successfully ------")

  # REGISTRATION
  elif choice == 2:
    userName = input("\nEnter your username: ")

    if userName not in users_Dict.keys():
      password = input("Enter your password: ")

      # adding the usename and password in the file
      with open("users.txt", "a") as f:
        f.write(userName + " " + password + "\n")
        
      update_Dictionary()

      print("------ Registration successfull -----")

    else:
      print("Username already exists. Please choose a valid username.")

  elif choice == 3:
    print("------ GoodBye ------")
    break

  else:
    print("Please choose a valid option.")

