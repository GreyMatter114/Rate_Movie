import subprocess
n=int(input("Enter: \n1 to train\n2 to test"))
if(n==1):
	subprocess.call([r'train.bat'])
elif(n==2):
	subprocess.call([r'test.bat'])
else:
	print("Invalid Input")