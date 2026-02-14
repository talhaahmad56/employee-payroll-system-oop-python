Employee Payroll System (Python OOP)

A menu-driven Employee Payroll System built using Python Object-Oriented Programming concepts.
This project demonstrates inheritance, method overriding, polymorphism, and clean class design.

 Project Objective

To practice and demonstrate:

Object-Oriented Programming in Python

Inheritance using parent and child classes

Use of super() to reuse parent logic

Method overriding

Runtime polymorphism

Command-line interface (CLI) programs

 OOP Concepts Used

Encapsulation

Inheritance

Method Overriding

Polymorphism

super()

__str__()

 Class Structure
🔹 Employee (Parent Class)

Attributes

emp_id

name

base_salary

Methods

calculate_salary()

__str__()

 Manager (Child Class)

Inherits from Employee

Additional Attribute

bonus

Overridden Logic

Salary = base salary + bonus

 Developer (Child Class)

Inherits from Employee

Additional Attribute

overtime_hours

Overridden Logic

Salary = base salary + (overtime_hours × 5000)

 Features

Add Manager or Developer

Calculate salaries dynamically

Polymorphic salary calculation

Menu-driven CLI

Clean and readable output
