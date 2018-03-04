#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The purpose of this program is to calculate how many times bigger the Alaskan district
is from an average Wisconsin district

Background:

    Wisconsin has eight congressional districts covering its land area of 169,790 
    square kilometers, while Alaska has just one district for its 1,717,856 square 
    kilometers. Write a program which determines how many times bigger than the average 
    Wisconsin district that Alaskan district is. 
"""

wisconsin_land_area = 169790
wisconsin_numberOf_districts = 8

alaska_average_district_size = 1717856
   
def find_average_district_size(land_area,numberOf_districts):
    global average_district_size #make variable global to exist outside of function
    average_district_size = land_area / numberOf_districts

    
find_average_district_size(wisconsin_land_area,wisconsin_numberOf_districts)


def compare_district_size_ratio(avg_district1_size, avg_district2_size):
    global numberOf_times_bigger
    numberOf_times_bigger = avg_district2_size / avg_district1_size
    
    
compare_district_size_ratio (average_district_size, alaska_average_district_size)   

print("The Alaskan district is approximately",'{0:.2f}'.format(numberOf_times_bigger),
      'times bigger than an average Wisconsin district.')