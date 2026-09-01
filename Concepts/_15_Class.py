"""
ANNOTATED OOP EXAMPLE
Every line is labeled with the OOP term it demonstrates.
Read top to bottom — this is meant to be a walkthrough, not just working code.
"""

# ---------------------------------------------------------
# CLASS DEFINITION
# ---------------------------------------------------------
class Employee:                        # 'Employee' is a CLASS -> a blueprint for objects
    """A class representing an Employee."""

    # CLASS ATTRIBUTE (a.k.a. class variable)
    # Belongs to the CLASS itself, shared by ALL objects (instances) of this class.
    # Not tied to any one instance unless overridden.
    company_name = "Acme Corp"

    raise_percentage = 1.05            # another CLASS ATTRIBUTE, shared default value

    # ---------------------------------------------------------
    # CONSTRUCTOR / INITIALIZER
    # ---------------------------------------------------------
    def __init__(self, name, salary):
        # '__init__' is the INITIALIZER (often loosely called the "constructor").
        # It runs automatically right after a new OBJECT is created.

        # 'self' refers to THE SPECIFIC OBJECT being created/operated on.
        # It is the first PARAMETER of every instance method, passed automatically
        # by Python — you never pass it manually when calling the method.

        # 'name' and 'salary' are PARAMETERS — variables that receive the values
        # (called ARGUMENTS) passed in when the object is created.

        self.name = name               # 'self.name' is an INSTANCE ATTRIBUTE
                                        # (a.k.a. instance variable) — unique to THIS object.
        self.salary = salary           # another INSTANCE ATTRIBUTE, unique per object.

        self._id_number = id(self)     # leading underscore '_' = PROTECTED ATTRIBUTE
                                        # (a convention meaning "internal use," not enforced by Python).

        self.__ssn = "XXX-XX-XXXX"     # leading double underscore '__' = PRIVATE ATTRIBUTE
                                        # Python performs NAME MANGLING on this:
                                        # internally becomes '_Employee__ssn'.

    # ---------------------------------------------------------
    # INSTANCE METHOD
    # ---------------------------------------------------------
    def give_raise(self):
        # This is an INSTANCE METHOD — a function defined inside a class that
        # operates on a specific object's data via 'self'.
        self.salary = self.salary * self.raise_percentage   # reading a CLASS ATTRIBUTE
                                                              # through 'self' (allowed, falls back to class if
                                                              # no instance attribute of that name exists)
        return self.salary             # RETURN VALUE sent back to whoever called the method

    def describe(self):
        # Another INSTANCE METHOD. Uses INSTANCE ATTRIBUTES to build a string.
        return f"{self.name} earns {self.salary} at {Employee.company_name}"
        # 'Employee.company_name' accesses the CLASS ATTRIBUTE directly via the CLASS NAME.

    # ---------------------------------------------------------
    # CLASS METHOD
    # ---------------------------------------------------------
    @classmethod                       # DECORATOR marking the method below as a CLASS METHOD
    def set_raise_percentage(cls, new_percentage):
        # 'cls' refers to THE CLASS ITSELF (not an instance).
        # Used to read/modify CLASS-level state, shared by all objects.
        cls.raise_percentage = new_percentage

    @classmethod
    def from_string(cls, employee_str):
        # ALTERNATE CONSTRUCTOR pattern: builds and returns a new OBJECT
        # from a differently-formatted input (a common CLASS METHOD use case).
        name, salary = employee_str.split("-")
        return cls(name, int(salary))  # 'cls(...)' calls Employee(...) to create a new OBJECT

    # ---------------------------------------------------------
    # STATIC METHOD
    # ---------------------------------------------------------
    @staticmethod                      # DECORATOR marking the method below as a STATIC METHOD
    def is_valid_salary(amount):
        # No 'self' or 'cls' — a STATIC METHOD doesn't touch instance or class state.
        # It's just a regular function grouped inside the class because it's
        # logically related to Employee.
        return amount > 0

    # ---------------------------------------------------------
    # DUNDER / MAGIC METHODS (double-underscore methods)
    # ---------------------------------------------------------
    def __str__(self):
        # Called automatically by print(obj) or str(obj).
        # Meant to be a READABLE description for end users.
        return f"Employee({self.name})"

    def __repr__(self):
        # Called by repr(obj), and used as fallback for print() if __str__ missing.
        # Meant to be an UNAMBIGUOUS description, useful for debugging.
        return f"Employee(name={self.name!r}, salary={self.salary!r})"

    def __eq__(self, other):
        # OPERATOR OVERLOADING: defines what '==' means for two Employee OBJECTS.
        # 'other' is a PARAMETER representing the second object being compared.
        return self.salary == other.salary


# ---------------------------------------------------------
# INHERITANCE
# ---------------------------------------------------------
class Manager(Employee):               # 'Manager' is a SUBCLASS (child class)
                                        # 'Employee' in parentheses is the SUPERCLASS (parent/base class)
                                        # This models an IS-A relationship: a Manager IS AN Employee.

    def __init__(self, name, salary, team_size):
        # SUPER() CALL: invokes the PARENT class's __init__ to reuse its logic
        # instead of duplicating 'self.name = name' etc.
        super().__init__(name, salary)

        self.team_size = team_size     # an INSTANCE ATTRIBUTE specific to Manager only

    def describe(self):
        # METHOD OVERRIDING: Manager provides its OWN version of 'describe',
        # replacing the one inherited from Employee. This is POLYMORPHISM —
        # the same method name behaves differently depending on the OBJECT'S class.
        base_description = super().describe()   # calling the PARENT's version too
        return f"{base_description}, manages {self.team_size} people"


# ---------------------------------------------------------
# COMPOSITION (an alternative to inheritance: "HAS-A" relationship)
# ---------------------------------------------------------
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []            # will HOLD other OBJECTS (composition)

    def add_employee(self, employee):
        # 'employee' PARAMETER here is expected to be an OBJECT of type Employee.
        self.employees.append(employee)


# ===========================================================
# USING THE CLASSES: creating and working with OBJECTS
# ===========================================================

# INSTANTIATION: calling the class like a function creates a new OBJECT (INSTANCE).
emp1 = Employee("Asha", 50000)          # 'emp1' is an OBJECT / INSTANCE of class Employee
emp2 = Employee("Ravi", 60000)          # 'emp2' is a DIFFERENT OBJECT, independent state

# ATTRIBUTE ACCESS: dot notation reads an object's ATTRIBUTE
print(emp1.name)                        # -> "Asha"   (INSTANCE ATTRIBUTE)
print(Employee.company_name)            # -> "Acme Corp"   (CLASS ATTRIBUTE, accessed via class)

# METHOD CALL: dot notation + parentheses invokes a METHOD on an object
print(emp1.describe())                  # 'self' is auto-filled with 'emp1' behind the scenes
print(emp1.give_raise())                # mutates emp1's own salary, doesn't touch emp2

# CLASS METHOD CALL: changes shared state for ALL objects (since it modifies the CLASS ATTRIBUTE)
Employee.set_raise_percentage(1.10)

# ALTERNATE CONSTRUCTOR usage
emp3 = Employee.from_string("Meera-45000")   # emp3 is a new OBJECT built via the classmethod

# STATIC METHOD CALL: doesn't need an object at all, called directly on the class
print(Employee.is_valid_salary(50000))       # -> True

# INHERITANCE in action
mgr1 = Manager("Kabir", 90000, 5)       # 'mgr1' is an OBJECT of the SUBCLASS Manager
print(mgr1.describe())                  # runs Manager's OVERRIDDEN describe(), which also calls the parent's

# isinstance() checks OBJECT-CLASS relationships, respecting INHERITANCE
print(isinstance(mgr1, Manager))        # -> True  (direct class match)
print(isinstance(mgr1, Employee))       # -> True  (Manager IS-A Employee, inheritance respected)
print(isinstance(mgr1, Department))     # -> False (unrelated class)

# DUNDER METHODS in action
print(emp1)                             # -> calls __str__ automatically  => "Employee(Asha)"
print(repr(emp1))                       # -> calls __repr__ automatically
print(emp1 == emp2)                     # -> calls __eq__ automatically, compares salaries

# COMPOSITION in action
eng_dept = Department("Engineering")    # 'eng_dept' is an OBJECT of class Department
eng_dept.add_employee(emp1)             # passing an OBJECT (emp1) as an ARGUMENT
eng_dept.add_employee(mgr1)             # Department HAS Employees, rather than BEING one
print([str(e) for e in eng_dept.employees])