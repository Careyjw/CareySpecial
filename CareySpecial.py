import os
from time import sleep
yes=["yes","Yes","YES","Sure","y","Y"]
print("Welcome to the Carey Special.")
print("I will be walking you through some important steps.")

sleep(5)
#AVG
if(not os.path.isdir("C:\\Program Files (x86)\\AVG\\Antivirus")):
	print("I would suggest that you get AVG. Do you want to do so now?")
	if input("(yes or no)") in yes:
		print("Once finished installing please click 'scan computer' in the AVG window")
		sleep(1)
		os.chdir("C:\\Program Files (x86)\\CareySpecial\\Installers")
		os.system("AVG")
		s= input("Please type 'done' when you are finished.\n-->")
else:
	print("On AVG please click 'scan computer'")
	sleep(1)
	os.chdir("C:\\Program Files (x86)\\AVG\\Antivirus")
	os.system("AVGUI")
	s = input("Please type 'done' when you are finished.\n-->")


#malwarebytes
if(not os.path.isdir("C:\\Program Files\\Malwarebytes\\Anti-Malware")):
	print("I would suggest that you get Malwarebytes. Do you want to do so now?")
	if input("(yes or no)") in yes:
		os.chdir("C:\\Program Files (x86)\\CareySpecial\\Installers")
		os.system("Malwarebytes")
		print("Once finished installing please click 'Scan Now' in the Malwarebytes window")
		s= input("Please type 'done' when you are finished.\n-->")
else:
	print("On Malwarebytes please click 'Scan Now'")
	sleep(1)
	os.chdir("C:\\Program Files\\Malwarebytes\\Anti-Malware")
	os.system("mbam")
	s = input("Please type 'done' when you are finished.\n-->")

#diskClean
os.chdir("C:\\WINDOWS\\system32")
os.system("cleanmgr")
print("On disk Cleanup check the recycle bin, temporary files, dowloaded program files, temporary internet files. Then click OK.\n Press delete files on the permanently delete files popup")
s = input("Please type done when you are finished")

#defrag
os.chdir("C:\\WINDOWS\\system32")
os.system("dfrgui")
print("On Optimize Drives please click 'Optimize'")
s = input("Please type 'done' when you are finished.\n-->")

print("Thank you for running the Carey Special. Have a great day!")
sleep(5)