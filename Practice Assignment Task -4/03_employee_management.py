# Program: Employee Management

# Demonstrate Inheritance

class Employee:

    def work(self):

        print("Employee is working")


class Manager(Employee):

    def manage(self):

        print("Manager is managing the team")


manager1 = Manager()

manager1.work()

manager1.manage()


# Sample Output

'''
Employee is working

Manager is managing the team
'''