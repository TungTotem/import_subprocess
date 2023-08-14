import subprocess

subprocess.run(["sh", "./test.sh"]) # startet das bereits angelegte shell script
output1 = subprocess.run(["sh", "./test.sh"], capture_output=True, text=True) #speichert den Output in eine Variable
print("\n" "This is a copy of the shell output \n" "\n", output1.stdout) #gibt den Inhalt der Variable als Text aus



