import csv
import random
import re

class Bank:
    """
        Class that represent a bank, simulating create of accounts, deposits and withdraw.

        Attributes:
            email (str): Email of user.
            n_account (str): Number of account.
            password (str): Password of account.
            _balance (float): balance of account.
        """
    def __init__(self, email, n_account='12345678', password='11qq11', balance=0):
        """
            Initializes one object Bank with email, number of account, password and initial balance.
        """
        self.email = email
        self.n_account = n_account
        self.password = password
        self._balance = balance

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        match = re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if match:
            self._email = email
        else:
            raise ValueError('Invalid Email')

    @property
    def n_account(self):
        return self._n_account

    @n_account.setter
    def n_account(self, n_account):
        if len(str(n_account)) != 8:
            raise ValueError("Invalid account, it's number valid is 8")

        if not str(n_account).isnumeric():
            raise ValueError("Invalid account, words isn't accept")

        self._n_account = n_account

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if str(password).isnumeric() or str(password).isalpha():
            raise ValueError('This password have number and words')
        if len(password) != 6:
            raise ValueError('This password have 6 elements')
        self._password = password



    @classmethod
    def create(cls):
        """
               Create a new account.

               Solicit email, generate one number of account random and define one password.

               Returns:
                   Bank: One new object of class Bank.
               """
        email = input('Write your best email: ')
        with open('accounts.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == email:
                    raise AttributeError('This email has registered')
        nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        num_account = ''.join(map(str, random.choices(nums, k=8)))
        psswrd = input('Password: ')
        password = input('Confirm: ')
        while password != psswrd:
            print('Password incorrect!')
            psswrd = input('Password: ')
            password = input('Confirm: ')

        return cls(email, num_account, password)

    def check(self):
        """
        Checks if a account exist and permit deposit or withdraw.
        """
        with open('accounts.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            rows = []
            new_row = []
            for row in reader:
                if self.email in row:
                    print('This account has exist')
                    r = input('You want a deposit here? (D) or a withdraw(W)? ')
                    while r.upper() not in 'DW':
                        r = input('You want a deposit here?(D) or a withdraw(W)? ')
                    if r.upper() == 'D':
                        value = float(input('Value: '))
                        balance = float(row[3])
                        dep = value + balance
                        self.deposit(dep)
                        new_row = [self.email, row[1], self.password, self._balance]
                    if r.upper() == 'W':
                        value = float(input('Value: '))
                        balance = float(row[3])
                        if value > balance:
                            raise ValueError('Balance insufficient')
                        dep = value - balance
                        self.withdraw(dep)
                        new_row = [self.email, row[1], self.password, self._balance]
                else:
                    rows.append(row)

                if new_row:
                    rows.append(new_row)
        with open('accounts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)


    def append(self):
        """
        Add one account in database (CSV file), deleting duplicates.

        Update balance.
        """
        with open('accounts.csv', "r", newline="", encoding="utf-8") as csvfile:
            reader = list(csv.reader(csvfile))
            header = reader[0]
            rows = reader[1:]

        new_list = []
        balance = 0

        for row in rows:
            if str(self.n_account) == row[0]:
                balance = float(row[3])
            else:
                new_list.append(row)

        with open('accounts.csv', "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(new_list)

        with open('accounts.csv', "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([self.email, self.n_account, self.password, self._balance + balance])

    def deposit(self, n):
        """
            Add one value in balance of account.

            Args:
                n (float): Amount to be deposited.
        """
        self._balance += n

    def withdraw(self, n):
        """
                Realize one withdraw in account, subtracting one value of balance.

                Args:
                    n (float): Amount to be drawn.
                """
        self._balance -= n
