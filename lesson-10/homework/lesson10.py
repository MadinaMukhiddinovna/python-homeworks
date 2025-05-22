from datetime import datetime
class Task:
    def __init__(self, title, description, due_date, status=False):
        self.title = title
        self.description = description
        self.due_date = due_date  #example "2025-05-20"
        self.status = status  # False , True 

    def mark_complete(self):
        self.status = True

    def __str__(self):
        status = "Done" if self.status else "Pending"
        return f"{self.title} | Due: {self.due_date} | Status: {status}\n  Description: {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            return True
        return False

    def list_all_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def list_incomplete_tasks(self):
        for i, task in enumerate(self.tasks):
            if not task.status:
                print(f"{i}. {task}")

def main_todo():
    todo = ToDoList()
    while True:
        print("\nToDo List Menu:")
        print("1. Add task")
        print("2. Mark task complete")
        print("3. List all tasks")
        print("4. List incomplete tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            todo.add_task(Task(title, description, due_date))
            print("Task added.")
        elif choice == '2':
            todo.list_all_tasks()
            idx = int(input("Enter task number to mark complete: "))
            if todo.mark_task_complete(idx):
                print("Task marked as complete.")
            else:
                print("Invalid task number.")
        elif choice == '3':
            todo.list_all_tasks()
        elif choice == '4':
            todo.list_incomplete_tasks()
        elif choice == '5':
            print("Exiting ToDo List.")
            break
        else:
            print("Invalid option, try again.")
# main_todo()
        
         class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        for i, post in enumerate(self.posts):
            print(f"{i}. {post}")

    def list_posts_by_author(self, author):
        found = False
        for post in self.posts:
            if post.author.lower() == author.lower():
                print(post)
                found = True
        if not found:
            print("No posts found by this author.")

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]
            return True
        return False

    def edit_post(self, index, title=None, content=None, author=None):
        if 0 <= index < len(self.posts):
            if title:
                self.posts[index].title = title
            if content:
                self.posts[index].content = content
            if author:
                self.posts[index].author = author
            return True
        return False

    def latest_posts(self, count=5):
        for post in self.posts[-count:]:
            print(post)

def main_blog():
    blog = Blog()
    while True:
        print("\nBlog Menu:")
        print("1. Add post")
        print("2. List all posts")
        print("3. List posts by author")
        print("4. Delete a post")
        print("5. Edit a post")
        print("6. Show latest posts")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
            print("Post added.")
        elif choice == '2':
            blog.list_all_posts()
        elif choice == '3':
            author = input("Enter author name: ")
            blog.list_posts_by_author(author)
        elif choice == '4':
            blog.list_all_posts()
            idx = int(input("Enter post number to delete: "))
            if blog.delete_post(idx):
                print("Post deleted.")
            else:
                print("Invalid post number.")
        elif choice == '5':
            blog.list_all_posts()
            idx = int(input("Enter post number to edit: "))
            title = input("New title (leave blank to keep): ")
            content = input("New content (leave blank to keep): ")
            author = input("New author (leave blank to keep): ")
            if blog.edit_post(idx, title or None, content or None, author or None):
                print("Post updated.")
            else:
                print("Invalid post number.")
        elif choice == '6':
            blog.latest_posts()
        elif choice == '7':
            print("Exiting Blog.")
            break
        else:
            print("Invalid option, try again.")
# main_blog()

              class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account {self.account_number} | Holder: {self.holder_name} | Balance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.balance
        return None

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.deposit(amount)
        return False

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            return account.withdraw(amount)
        return False

    def transfer(self, from_acc_num, to_acc_num, amount):
        from_acc = self.accounts.get(from_acc_num)
        to_acc = self.accounts.get(to_acc_num)
        if from_acc and to_acc and from_acc.balance >= amount > 0:
            from_acc.withdraw(amount)
            to_acc.deposit(amount)
            return True
        return False

    def display_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

def main_bank():
    bank = Bank()
    while True:
        print("\nBank Menu:")
        print("1. Add account")
        print("2. Check balance")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Transfer money")
        print("6. Display account details")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            acc_num = input("Account number: ")
            name = input("Account holder name: ")
            bank.add_account(Account(acc_num, name))
            print("Account added.")
        elif choice == '2':
            acc_num = input("Account number: ")
            balance = bank.check_balance(acc_num)
            if balance is not None:
                print(f"Balance: ${balance:.2f}")
            else:
                print("Account not found.")
        elif choice == '3':
            acc_num = input("Account number: ")
            amount = float(input("Amount to deposit: "))
            if bank.deposit(acc_num, amount):
                print("Deposit successful.")
            else:
                print("Deposit failed.")
        elif choice == '4':
            acc_num = input("Account number: ")
            amount = float(input("Amount to withdraw: "))
            if bank.withdraw(acc_num, amount):
                print("Withdrawal successful.")
            else:
                print("Insufficient funds or invalid account.")
        elif choice == '5':
            from_acc = input("From account number: ")
            to_acc = input("To account number: ")
            amount = float(input("Amount to transfer: "))
            if bank.transfer(from_acc, to_acc, amount):
                print("Transfer successful.")
            else:
                print("Transfer failed. Check accounts and balance.")
        elif choice == '6':
            acc_num = input("Account number: ")
            bank.display_account(acc_num)
        elif choice == '7':
            print("Exiting Bank.")
            break
        else:
            print("Invalid option, try again.")
# main_bank()
