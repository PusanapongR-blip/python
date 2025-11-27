from cryptography.fernet import Fernet

def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)

# write_key()
def load_key():
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  return key

def view():
  with open("passwords.txt", "r") as f:
    for line in f.readlines():
      data = line.rstrip()
      user, password = data.split("|")
      print(f"User: {user} | Password: {fer.decrypt(password.encode()).decode()}")

def add():
    user = input("Enter the username: ")
    password = input("Enter the password: ")

    with open("passwords.txt", "a") as f:
      f.write(f"{user}|{fer.encrypt(password.encode()).decode()}\n")
    print("Password added successfully!")
  

key = load_key()
fer = Fernet(key)



while True:
  mode = input("Would you like to 'view' your passwords or 'add' a new password? (type q to quit): ").lower()
  if mode == "view":
      view()
  elif mode == "add":
      add()
  elif mode == "q":
      break
  else:
      print("Invalid mode selected.")

