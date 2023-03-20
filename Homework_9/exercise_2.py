class Math:

   def __init__(self, a:int, b:int):
      self.a = a
      self.b = b

   def addition(self):
    return self.a+self.b 

   def multiplication(self):
    return self.a*self.b 
    

   def division(self):
    return self.a/self.b 

   def subtraction(self):
    return self.a-self.b 

calc = Math(2,5)

print("Answer addition:", calc.addition())
print("Answer multiplication:", calc.multiplication())
print("Answer division:", calc.division())
print("Answer subtraction:", calc.subtraction())