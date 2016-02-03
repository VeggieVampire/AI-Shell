import aiml
import commands
import subprocess
#import ~/I2C-1602-LCD/print.py
 
k = aiml.Kernel()
 
# load the aiml file
k.learn("aiml/*.aiml")
 
# set a constant
k.setBotPredicate("name", "Hal9k")
 
while True:
    input = raw_input("You: ")
    response = k.respond(input)
    # print out on the shell
    print response
    # and as speech
    subprocess.Popen("~/I2C-1602-LCD/print.py " + response, shell=True)
	#os.system("~/I2C-1602-LCD/print.py test1 test2")
	#os.system("script2.py 1")
	#print commands.getoutput("/usr/bin/espeak -v en+f4 -p 99 -s 160 \"" + response + "\"")
