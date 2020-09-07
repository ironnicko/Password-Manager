import pickle, os, random

class Student:

    def __init__(self, roll, name, password):
        self.roll = roll
        self.name = name
        self.password = password

    def __str__(self):
        return 'Name:%5s\nPassword:%4s'%(self.name, self.password)

class Students:

    def __init__(self):
        self.filename = 'passwords.dat'
        self.load()

    def load(self):
        try:
            with open(self.filename, 'rb') as f:
                self._accounts = pickle.load(f)
        except:
            self._accounts = []

    def exist(self, roll):
        if self._accounts:
            for b in self._accounts:
                if b.roll == roll:
                    return True
        return False

    def save(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)
        with open(self.filename, 'wb') as f:
            pickle.dump(self._accounts, f)

    def search(self, roll):
        for pos, b in enumerate(self._accounts):
            if b.roll == roll:
                return pos, b
        return 0, None


    def add_account(self, roll):
        name = input("Purpose: ")
        password = input('Enter the password')
        account = Student(roll, name, password)
        self._accounts.append(account)
        self.save()

    def display(self, roll):
        if self.exist(roll):
            pos, account = self.search(roll)
            print(account)
        else:
            print("account does not exist")

    def display_all(self):
        for i in self._accounts:
            print(i)

    def update(self, roll):
        if self.exist(roll):
            pos, account = self.search(roll)
            print(account)
            name = input('Name:\n')
            self._accounts[pos].description = name
            self.save()
            print("successfully updated")
        else:
            print( "account does not exist")

    def delete(self, roll):
        if self.exist(roll):
            pos, account = self.search(roll)
            print(account)
            confirm = input("Are you sure? (Y/N):\t").upper()
            if confirm == 'Y':
                del self._accounts[pos]
                self.save()
                print("successfully deleted")
        else:
            print("account does not exist")


def menu():
    while True:
        choice = int(input('1.Create\n2.Read\n3.Update\n4.Delete\n5.Display all\n0.Exit\n'))
        accounts = Students()
        if choice == 1:
            roll = int(input('Enter the roll no.:\t'))
            accounts.add_account(roll)
        elif choice == 2:
            roll = int(input('Enter roll:\t'))
            accounts.display(roll)
        elif choice == 3:
            roll = int(input("Enter roll:\t"))
            accounts.update(roll)
        elif choice == 4:
            roll = int(input("Enter roll:\t"))
            accounts.delete(roll)
        elif choice == 5:
            accounts.display_all()
        elif choice == 0:
            break

if __name__ == '__main__':
    menu()