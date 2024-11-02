import streamlit as st 
import math

# function to calculate bmi 
def calculate_bmi(weight,height):
  return weight/((height/100)**2)
 # function to get bmi category 
def get_bmi_category(bmi):
   if bmi<16:
     return"severe thinness","#ff0000"
   elif 16<=bmi<17:
     return"moderate thinness","#ff4500"
   elif 17<=bmi <18.5:
     return "mild thinness","#ff8c00"
   
