from factors import *


class fraction:
  """
  A class to create fractions and do arithmatic with them

  fractions will be represented as tuples of integers.
  If the fraction is negative the sign will be reained in the denominator

  Methods

  1 Simplify
  2 Add
  3 Multiply
  4 Divide
  5 raise to a power (integer powers only)

  """
  def __init__ (self,numerator,denominator=1):
    """
    This is the init method to create a fraction. It takes a numerator and a denominator, determines the sign by dividing the product of the numerator and denominator by the absolute value of that product, ans then stores this data.
    The sign will be stored in the numerator 
    """
    self.debug = False
    if (self.debug): print(f'enter fraction.__init__ with {numerator}, {denominator}')
    sign = int(numerator * denominator / abs(numerator * denominator))
    if (self.debug): print(f'enter sign is {sign}')
    self.value=(sign * abs(numerator),abs(denominator))
    self.simplify()

  def equivalent (self, factor):
    """
    This methods makes an equivalent fraction by multiplying numerator and denominator by the same number
    """
    if (self.debug): print(f'enter fraction.equivalent {factor}')
    return (self.value[0] * factor, self.value[1]* factor)

  def simplify (self):
    """
    This methods simplifies a fraction by dividing numerator and denominator by their hoighest common factor
    """
    if (self.debug): print(f'enter fraction.simplify')
    hcf = find_hcf(self.value[0], self.value[1])
    self.value = (self.value[0] // hcf.product(), self.value[1] // hcf.product())
    return

  def num (self):
    """
    returns a floating point value for the fraction
    """
    return self.value[0]/self.value[1]

  def __add__ (self, other):
    """
    This method adds two fraction objects and returns a third object. 
    It finds the lcm of the two denominators and uses this to find a factor to make equivalent fractions of the same denominator. 
    The numerators are then added 
    Finally the fraction is simplified if possible
    """
    if (self.debug): print(f'enter fraction.__add__ with {other}')
    lcm = find_lcm(self.value[1], other.value[1])
    if (self.debug): print(f'{int(lcm/self.value[1])} {self.value}')
    f1 = self.equivalent(int(lcm/self.value[1]))
    f2 = other.equivalent(int(lcm/other.value[1]))
    f3 =  fraction(f1[0]+f2[0], lcm)
    if (self.debug): print(f'{f3}, {self}, {other}')
    return f3

  def __sub__ (self,other):
    """
    This method subtracts two fraction objects by negating the second and adding
    """
    if (self.debug): print(f'enter fraction.__sub__ with {other}')
    f2 = fraction(-1*other.value[0],other.value[1])
    f3 = self.__add__(f2)
    return f3

  def __mul__ (self,other):
    """
    This method multiplies two fraction objects and returns a third object. 
    Numberators and denominators are multiplied. 
    The result is then simplified
    """
    if (self.debug): print(f'enter fraction.__mul__ with {other}')
    f3 = fraction(self.value[0]*other.value[0],self.value[1]*other.value[1])
    if (self.debug): print(f3, self, other)
    f3.simplify()
    return f3


  def __truediv__ (self,other):
    """
    This method divides this fraction objectsby another and returns a third object. 
    The numberator and denominator of this fraction are multiplied by the denominator and numerator of the other fraction respectivley
    The result is then simplified
    Final
    """
    if (self.debug): print(f'enter fraction.__mul__ with {other}')
    f3 = fraction(self.value[0]*other.value[1],self.value[1]*other.value[0])
    if (self.debug): print(f3, self, other)
    return f3


  def __str__ (self):
    """
    This method returns a string version of the fraction in the format
    n|d. eg 3|5 for three fifths 1|4 for a quarter
    """
    return f'"{self.value[0]}|{self.value[1]}"'