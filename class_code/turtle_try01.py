#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:31:24 2022

@author: dieter
"""

import turtle                # import the turtle

turtle.clearscreen()

n_corners = 20
      
my_turtle = turtle.Turtle()    # make a variable called my_turtle
my_turtle.shape('turtle')       # set the shape of the robot to ‘turtle’

for i in range(n_corners):

    my_turtle.forward(20)
    my_turtle.right(360/n_corners)
