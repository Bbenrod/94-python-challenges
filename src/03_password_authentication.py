import getpass

# A password authentication system is a system that is used for the identification of a user. Think of it like a login screen that you see while logging in to your Facebook account. It asks for your email or a username and then it asks for your password. If you have entered the correct password then it verifies you as the real user.


def run():
    users = [
        {"username": "Kato", "password": "1234"},
        {"username": "Pastel", "password": "pretty_cat"},
        {"username": "Bombon", "password": "pretty_dog"},
    ]

    username = input("TYPE YOUR USERNAME:\t")

    exist_username = any(user['username'] == username for user in users)

    if exist_username:
        user_password = ""
        for user in users:
            if (user['username'] == username):
                user_password = user["password"]

        password = getpass.getpass("TYPE YOUR PASSWORD:\t")

        while (user_password != password):
            password = getpass.getpass("TYPE YOUR PASSWORD AGAIN:\t")

        print("VERIFIED USER.")
    else:
        print("INVALID USER.")


if __name__ == "__main__":
    run()
