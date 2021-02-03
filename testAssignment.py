from factors import *
from fractionsAssignment import *
import time, sys, random

"""
The followig are unit test functions. They userandom geerated numbers and process them as prime factors or fractions and compare results computed in other ways. The test methodolgy is decribed in each unit test procedure
"""

def unittest_factors():
  for j in range(0,100):
    """
    Test find_prime_factors by ensuring that the product method of the factors object returns the original number being factorised.
    """
    i = random.randrange(1, 600, 1)
    k = find_prime_factors(i)
    try:
      assert k.product() == i
    except AssertionError:
      print(i,k.product())
  print('find_prime_factors unit test complete')

  for i in range(0,100):
    """
    Test find_hcf_factors by ensuring that the hcf divides both the original numbers and the numbers resulting from that division hacf a hcf of one.
    """
    j = random.randrange(1, 600, 1)
    k = random.randrange(1, 600, 1)
    l = find_hcf(j, k)
    l = l.product()
    try:
      assert j % l == 0
      assert k % l == 0
      assert find_hcf(j // l, k // l).product() == 1
    except AssertionError:
      print(j,k,l,j // l, k // l)
  print('hcf unit test complete')

  for i in range(0,100):
    """
    Test find_lcm_factors by ensuring that the lcm is divisible by each of two randomly generated numbers, and the remainder of the lcm when didvide by the hcf is the product of the remainders of the original two numbers when divided by the hcf.
    """
    j =random.randrange(1, 600, 1)
    k =random.randrange(1, 600, 1)
    l = find_lcm(j,k)
    m = find_hcf(j,k).product()
    try:
      assert l%j == 0
      assert l%k == 0
      assert l//m == j//m * k//m
    except AssertionError:
      print(j,k,l.product())
  print('lcm unit test complete')

def unittest_fractions():
  """
  Test fractions object by generating two random fractions and doing addition, subraction multiplication and division on the two fractions
  The results provided by the num method of the fraction is compared with the result of doing the operation in python using floating point data objects.
  To take into account rounding error in the floating operations, the absolute value of the difference between the two numbers is checked to be below an arbitrary difference.
  """
  difference = .00001
  for i in range(0,5):
    print(f'start test {i}')
    j = random.randrange(1, 600, 1)
    l = random.randrange(1, 600, 1)
    m = random.randrange(1, 600, 1)
    n = random.randrange(1, 600, 1)
    f1= fraction(j,l)
    f2= fraction(m,n)

    #########################
    #
    # Test Fraction Addition
    #
    #########################

    f3 = f1 + f2
    print(f1,'+',f2,'=',f3)

    ###################################################
    # Write the assert statement to test the above operation
    ###################################################

    try:
      assert abs(abs(1)-abs(1)) < difference
    except AssertionError:
      print('fail addition test {i}', f1, f2, f3, f3.num(), (j/l)+(m/n))

    #########################
    #
    # Test Fraction Subtraction
    #
    #########################
    
    f3 = f1 - f2
    print(f1,'-',f2,'=',f3)

    ###################################################
    # Write the assert statement to test the above operation
    ###################################################

    try:
      assert abs(abs(1)-abs(1)) < difference
    except AssertionError:
      print('fail addition test {i}', f1, f2, f3, f3.num(), (j/l)-(m/n))


    #########################
    #
    # Test Fraction Multiplication
    #
    #########################
    
    f3 = f1 * f2
    print(f1,'x',f2,'=',f3)

    ###################################################
    # Write the assert statement to test the above operation
    ###################################################

    try:
      assert abs(abs(1)-abs(1)) < difference
    except AssertionError:
      print('fail multiplication test {i}', f1, f2, f3, f3.num(), (j/l)*(m/n))
    
    #########################
    #
    # Test Fraction Division
    #
    #########################
    
    f3 = f1 / f2
    print(f1,'/',f2,'=',f3)

    ###################################################
    # Write the assert statement to test the above operation
    ###################################################

    try:
      assert abs(abs(1)-abs(1)) < difference
    except AssertionError:
      print('fail division test {i}', f1, f2, f3, f3.num(), (j/l)/(m/n))
  print('fractions unit test complete')