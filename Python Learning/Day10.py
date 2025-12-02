# Dated:- 01/12/2025/Monday

# Public, Protected and Private

class PublicExample:
    def __init__(self):
        self.public_variable = "This is public"
    # public method 
    def public_method(self):
        return "This is public method"

obj = PublicExample()
print(obj.public_variable)
print(obj.public_method())

# ----------------------------------------------
class ProtectedExample:
    # protected variable
    def __init__(self):
        self._protected_variable = "This is procted variable"
    # procted method
    def _protected_method(self):
        return "This is protected method"

obj = ProtectedExample()
print(obj._protected_variable)
print(obj._protected_method())

# -----------------------------------------------------
class PrivateExample:
    # pricate variable
    def __init__(self):
        self.__private_variable = "This is private variable"
    # private method
    def __private_method(self):
        return "This is private method"

obj = PrivateExample()
print(obj.__private_variable)
print(obj.__private_method())

# ------------------------------------------------------

class EncapsulationWithProperties:
    def __init__(self):
        # Private attribute
        self._value = 0

    # Getter property
    @property
    def value(self):
        return self._value

    # Setter property
    @value.setter
    def value(self, new_value):
        if new_value >= 0:
            self._value = new_value
        else:
            print("Value must be non-negative. Setting to 0.")

# Creating an instance of the class
obj = EncapsulationWithProperties()
