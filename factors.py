debug = False

class factors:
  """
  A class to  hold factors of a rational number in index format
  """
  def __init__(self):
    """
    create a dictionary to hold the factors in index form.
    The index will represent the base. 
    The element will reprsent the index
    """
    self.debug = False
    if (self.debug): print("factors.__init__ entered")
    self.primes={}
    if (self.debug): print("factors.__init__ ended")
    return


  def add(self, base, index=1):
    """
    Add a factor by inrementing the index
    If no index is given assume 1.
    Check if the base is already in the dictionary and if so add the index to the existing disctionary Value. 
    Otherwise create a new base.
    """
    if (self.debug): print("factors.add entered")
    if (base in self.primes.keys()):
      self.primes[base] += index
    else:
      self.primes[base] = index
    if (self.debug): print("factors.add ended")
    return

  def product(self):
    """
    return the product of the prime factors
    """
    if (self.debug): print("factors.product entered")
    product = 1
    for i,j in self.primes.items():
      product *= i**j
    if (self.debug):print ('product is {product}')
    if (self.debug): print("factors.product ended")
    return product


  def __str__(self):
    """
    This method returns a string version of the fraction in the format
    """
    factor_string = 'start factor list\n'
    for i, j in self.primes.items():
      factor_string += str(i) + ' ** ' + str(j) + '\n'
    factor_string += 'end factor list\n'
    if (self.debug): print("factors.__str__ ended")
    return factor_string


def find_prime_factors(num):
  """
  finds the prime factors of a number and returns it as a factors object 
  """
  global debug
  if debug:print(f'start find_prime_factors3 with {num}')
  primes = factors()
  for i in range(2,abs(num)):
    if debug:print(f'i = {i}')
    if (num % i == 0):
      primes = find_prime_factors(int(num/i))
      if debug:print(f'now store prime factor i = {i} to primes')
      if debug:print(primes)
      primes.add(i)
      if debug:print (f'return with {num}')
      return primes
  primes.add(num)
  if debug:print(primes)
  if debug:print (f'return with {num}')
  return primes


def find_hcf(num1,num2):
  """
  finds the hcf of two numbers and returns it as a factors object 
  """
  global debug
  if debug:print(f'start find_hcf with {num1} and {num2}')
  hcf = factors()
  num1 = find_prime_factors(num1)
  num2 = find_prime_factors(num2)
  for i,j in num1.primes.items():
    if (i in num2.primes.keys()):
      hcf.add(i, min(j, num2.primes[i]))
  if debug:print('hcf ended with', hcf)
  return hcf

def find_lcm(num1,num2):
  """
  finds the lcm of a number and returns it as an integer 
  """
  global debug
  if debug:print(f'start find_lcm with {num1} and {num2}')
  hcf = find_hcf(num1, num2)
  lcm = num1 * num2 / hcf.product()
  if debug:print('lcm ended with', int(lcm))
  return int(lcm)
  