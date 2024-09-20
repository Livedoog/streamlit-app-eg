#import modules
import streamlit as steam

#class defination
class Buttons:
    def __init__(self,button_name):
        if steam.button(f"Button Number {button_name}"):
            st=int(button_name)**2
            steam.toast(st)
            self.calc(st)
    def calc(self,num):
        if num%2==0:
            steam.balloons()
        else:
            steam.snow()   
 
#Function defination
def squarenums():
    for i in range(5):
        Buttons(i)
def reverse():
    steam.header(".Reversing the String.")
    name=steam.text_input("Enter the text to be reversed: ")
    steam.title(f"The reversed String: {name[::-1]}")
#Function calling

reverse()
        