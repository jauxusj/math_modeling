import sys, os

print(os.getcwd())

os.system("echo hi!")
# os.system('C:/Users/inf3-3/AppData/Local/Programs/Python/Python311/python.exe "c:/Users/inf3-3/Documents/GitHub/math_modeling/lec_5_sys&os.py"')

print("Python version is:", sys.version)
print(sys.path)
print(sys.platform)

print(dir(sys))