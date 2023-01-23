#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  File: Hull.py

#  Description: This program prints the vertices of the convex hull starting at the 
#  extreme left point and going clockwise around the convex hull. It also prints the area of the convex hull.

#  Student Name: Gaytri Vasal

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 02/14/2022

#  Date Last Modified: 02/18/2022
    
import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  return ((p.x * q.y) + (q.x * r.y) + (r.x * p.y) - (p.y * q.x) - (q.y * r.x) - (r.y * p.x))

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  # create empty list to store vertices in upper hull
  upper_hull = []

  # append first two points in sorted list to upper hull
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])

  # traverse all elements of list from third point to last point
  for i in range(2, len(sorted_points)):

      # append the point being traversed to upper_hull
      upper_hull.append(sorted_points[i])
                 
      while ((len(upper_hull) >= 3) and (det(upper_hull[len(upper_hull) - 3], upper_hull[len(upper_hull) - 2], upper_hull[len(upper_hull) - 1]) > 0)):
          # delete the middle point among the last three points, provided that upper_hull has a length of 3 or greater and the last three points do not turn right
          upper_hull.pop(len(upper_hull) - 2)

  # create empty list to store vertices in lower hull
  lower_hull = []

  # append last two points in sorted list to lower hull
  lower_hull.append(sorted_points[len(sorted_points) - 1])
  lower_hull.append(sorted_points[len(sorted_points) - 2])

  # traverse all elements of list, starting from third to last point and ending at first point
  for i in range(len(sorted_points) - 3, -1, -1):

      # append the point being traversed to lower_hull
      lower_hull.append(sorted_points[i])

      while ((len(lower_hull) >= 3) and (det(lower_hull[len(lower_hull) - 3], lower_hull[len(lower_hull) - 2], lower_hull[len(lower_hull) - 1]) > 0)):
          # delete the middle point among the last three points, provided that lower_hull has a length of 3 or greater and the last three points do not turn right
          lower_hull.pop(len(lower_hull) - 2)

  # remove first and last points from lower_hull to prevent duplication of points from upper_hull
  lower_hull.pop(len(lower_hull) - 1)
  lower_hull.pop(0)
  
 

  # append lower_hull to upper_hull to compute the vertices of convex hull
  convex_hull = upper_hull + lower_hull

  return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):

  # compute first part of determinant, denoted by the following formula: x1 * y2 + x2 * y3 + ... + xn * y1
  firstpart = 0
  for i in range(0, len(convex_poly)):
      # once i reaches n, yi+1 is out of bounds; sets yi+1 to y1
      if i+1 == len(convex_poly):
          firstpart += convex_poly[i].x * convex_poly[0].y
      else:
          firstpart += convex_poly[i].x * convex_poly[i+1].y
      

  # compute second part of determinant, represented by the following formula: - y1 * x2 - y2 * x3 - ... - yn * x1
  secondpart = 0
  for i in range(0, len(convex_poly)):
      # once i reaches n, xi+1 is out of bounds; sets xi+1 to x1
      if i+1 == len(convex_poly):
          secondpart += convex_poly[i].y * convex_poly[0].x
      else:
          secondpart += convex_poly[i].y * convex_poly[i+1].x

 

  # combine parts to find value of determinant
  determinant = firstpart - secondpart 

  # calculate and return area
  return (1/2) * abs(determinant)

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  assert (det(Point(0,0), Point(1, 1), Point(2, 2))) == 0
  assert (det(Point(1, 2), Point(8, 3), Point(45, 46))) == 264
  
  assert (area_poly([Point(0,0), Point(0, 6), Point(6, 0)])) == 18.0
  assert (area_poly([Point(0, 0), Point(0, 45), Point(0, 60), Point(1, 1), Point(1, 36), Point(2, 0), Point(3, 34)])) == 14.5
  
  convexhull = convex_hull([Point(0, 0), Point(1, 1), Point(2, 2)])
  convex_hull1 = []
  for element in convexhull:
      convex_hull1.append(str(element))
  assert(convex_hull1) == ['(0, 0)', '(1, 1)', '(2, 2)', '(1, 1)']
  
  convexhull = convex_hull([Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 2), Point(2, 3)])
  convex_hull2 = []
  for element in convexhull:
      convex_hull2.append(str(element))
  assert (convex_hull2) == ['(0, 0)', '(0, 1)', '(0, 2)', '(2, 3)']
  
  convexhull = convex_hull([Point(0, 1), Point(0, 20), Point(1, 3), Point(2, 11), Point(3, 3)])
  convex_hull3 = []
  for element in convexhull:
      convex_hull3.append(str(element))
  assert (convex_hull3) == ['(0, 1)', '(0, 20)', '(2, 11)', '(3, 3)']
     
  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)

  '''
  # print the sorted list of Point objects
  for p in sorted_points:
    print (str(p))
  '''

  # get the convex hull
  convexhull = convex_hull (sorted_points)

  # run your test cases
  test_cases()

  # print your results to standard output
  # print(test_cases())
  
  
  # print the convex hull
  print("Convex Hull")
  for element in convexhull:
    print(str(element))

  # get the area of the convex hull
  area = area_poly(convexhull)

  # print the area of the convex hull
  print()
  print("Area of Convex Hull = " + str(area))

if __name__ == "__main__":
  main()



