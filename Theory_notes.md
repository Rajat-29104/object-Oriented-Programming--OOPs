# OOP Theory Notes

---

# 1. Classes and Objects

Definition:

A class is a blueprint used to create objects.

An object is an instance of a class.

Purpose:

It helps us group data and functions together.

Example:

```python
class Student:
    pass

student1 = Student()
```

---

# 2. Constructor (__init__)

Definition:

A constructor is a special method that runs automatically when an object is created.

Purpose:

It initializes object data.

Example:

```python
class Student:

    def __init__(self,name):

        self.name = name
```

---

# 3. Instance Variables

Definition:

Variables that belong to an object.

Purpose:

Store object data.

Example:

```python
self.name

self.marks
```

---

# 4. Instance Methods

Definition:

Functions created inside a class.

Purpose:

Perform operations on object data.

Example:

```python
def display(self):

    print(self.name)
```

---

# 5. Class Variables

Definition:

Variables shared by all objects.

Purpose:

Store common data.

Example:

```python
class Student:

    school = "ABC School"
```

---

# 6. Encapsulation

Definition:

Wrapping data and methods inside a class.

Purpose:

Protect data.

Example:

```python
self.__balance
```

---

# 7. Inheritance

Definition:

A child class can use properties of a parent class.

Purpose:

Code reusability.

Example:

```python
class Employee:

    pass

class Manager(Employee):

    pass
```

---

# 8. Polymorphism

Definition:

Same method gives different outputs.

Purpose:

Flexibility.

Example:

```python
start()
```

---

# 9. Abstraction

Definition:

Showing important details and hiding unnecessary implementation.

Purpose:

Reduce complexity.

Example:

```python
@abstractmethod
```

---

# 10. Method Overriding

Definition:

A child class changes a parent class method.

Purpose:

Customize behavior.

Example:

```python
def start():

    print("Car starts")
```

---

# 11. super() Function

Definition:

Used to call the parent class constructor or methods.

Purpose:

Reuse parent code.

Example:

```python
super().__init__()
```

---

# 12. Access Modifiers

## Public

Accessible everywhere.

```python
name
```

## Protected

Accessible inside class and child class.

```python
_name
```

## Private

Accessible only inside class.

```python
__name
```
