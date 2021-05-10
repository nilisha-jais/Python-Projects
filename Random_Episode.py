import os
import random

p='C:\\Users\\LENOVO\\Videos\\Captures'
os.chdir(p)
file_name=random.choice(os.listdir())
print(file_name)
print("Enjoy!!")
os.popen(file_name,'r')