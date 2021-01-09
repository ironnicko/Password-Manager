import pickle
import os
import random
from cryptography.fernet import Fernet


class drop:
    def __init__(self, no, purp, password, key):
        self.no = no
        self.purp = purp
        self.password = password
        self.key = key

    def __repr__(self):
        return self.password.decode()


class main:

    def __init__(self):
        self.filename = "passwords.bin"
        self.load()

    def load(self):
        try:
            with open(self.filename, 'rb') as file:
                self._accounts = pickle.load(file)
        except:
            self._accounts = []

    def save(self):
        for i in os.listdir():
            if self.filename == i:
                os.remove(self.filename)
        with open(self.filename, 'wb') as file:
            pickle.dump(self._accounts, file)

    def add_account(self, no, p=None, pas=None):
        purp = p or input("Purpose: ")
        password = pas or input('Enter the password')
        key = Fernet.generate_key()
        password = Fernet(key).encrypt(str.encode(password))
        account = drop(no, purp, password, key)
        self._accounts.append(account)
        self.save()

    def display(self, no=None):
        if no:
            for i in self._accounts:
                if no == i.no:
                    print(
                        f'Password: {Fernet(i.key).decrypt(i.password).decode()}')
        else:
            for i in self._accounts:
                print(i)

    def update(self, no):
        for i in self._accounts:
            if input("Warning!\nOnce you press \'y\', you're old data will forever be gone.\nDo you want to continue?[y/n]").lower() == 'y':
                if i.no == no:
                    password = Fernet(i.key).decrypt(i.password).decode()
                    self.delete(no)
                    no = int(input("Enter new Roll no:"))
                    purp = input("Enter new purpose:")
                    self.add_account(no, purp, password)
                    i.no = no
                    i.purp = purp
            self.save()

    def delete(self, no=None):
        for pos, i in enumerate(self._accounts):
            if no:
                if i.no == no:
                    confirm = input("Are you sure? (Y/N):\t").upper()
                    if confirm == 'Y':
                        del self._accounts[pos]
                        self.save()
                        print("successfully deleted")
                else:
                    print("account does not exist")
            else:
                for i in os.listdir():
                    if i == self.filename:
                        os.remove(self.filename)


def menu():
    while True:
        choice = input(
            '1.Create\n2.Read\n3.Update\n4.Delete\n5.Display all\n6.Delete All\n0.Exit\n')
        accounts = main()
        if choice == '1':
            no = int(input('Enter Roll no.:\t'))
            accounts.add_account(no)
        elif choice == '2':
            no = int(input('Enter Roll no:\t'))
            accounts.display(no)
        elif choice == '3':
            no = int(input("Enter Roll no:\t"))
            accounts.update(no)
        elif choice == '4':
            no = int(input("Enter Roll no:\t"))
            accounts.delete(no)
        elif choice == '5':
            accounts.display()
        elif choice == '6':
            accounts.delete()
        elif choice == '0':
            break


if __name__ == '__main__':
    menu()
