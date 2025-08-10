# Assignment 1: Television Class 

## Overview
This project demonstrates **Object-Oriented Programming (OOP)** in Python by designing:
- A `Television` class
- A `SmartTelevision` subclass (inherits from `Television`)

Key OOP concepts:
- **Encapsulation**
- **Inheritance**
- **Abstraction**
- **Polymorphism**

---

## Class Structure

### **Television**
**Attributes**
- `brand` (string): Brand name of the TV
- `size` (integer): Size in inches
- `is_smart` (boolean): Whether the TV is smart or regular

**Methods**
- `turn_on()` → Turns the TV ON
- `turn_off()` → Turns the TV OFF
- `display_info()` → Displays brand, size, and type

---

### **SmartTelevision** (Inherits from `Television`)
**Extra Attribute**
- `streaming_apps` (list): Installed streaming apps

**Extra Method**
- `open_app(app_name)` → Opens an app if installed, otherwise shows an error message

---

## Example Code
```python
tv2 = SmartTelevision("Samsung", 55, True, ["Netflix", "YouTube", "Hulu"])
tv2.turn_on()
tv2.display_info()
tv2.open_app("Netflix")
tv2.open_app("Disney+")
tv2.turn_off()
```


---

# Activity 2: Polymorphism Challenge – Animals

## Overview
This program demonstrates **Polymorphism** in Python OOP.

Multiple classes (`Cat` and `Horse`) share the same method name `move()` but implement it differently.

---

## Class Structure

### **Animal** (Base Class)
**Method**
- `move()` → Placeholder method to be overridden.

---

### **Cat** (Inherits from `Animal`)
**Method**
- `move()` → Prints `"The cat walks silently."`

---

### **Horse** (Inherits from `Animal`)
**Method**
- `move()` → Prints `"The horse gallops swiftly."`

---

## Example Code
```python
animals = [Cat(), Horse()]
for animal in animals:
    animal.move()
```

This repository has two Python OOP files:

- **Assignment 1**: Television Class with inheritance.
- **Activity 2**: Polymorphism with Animals.

---

##  How to access this project

### Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/Wendy-Okoth/PLPPythonWeek5.git
cd PLPPythonWeek5

Assignment 1: Television Class
Run the assignment1.py script:

python assignment1.py
This will launch the demonstration of the Television and SmartTelevision classes—showing how to turn the TV on/off, display info, and open streaming apps.

Activity 2: Polymorphism Challenge – Animals
Run the activity2.py script:

python activity2.py
This demonstrates polymorphism with the Cat and Horse classes, each defining its own version of the move() method.


