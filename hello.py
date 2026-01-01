name = ""
while name == "":
   name = input("Wie heißt Du?")  
   if name == "": 
            print("Hmm;Es scheint, als ob Du keinen Namen eingegeben hast.\nBitte sag mir Deinen Namen (ich verrate ihn auch nicht)")
   continue

age = ""

while True:
       age = input("Wie alt bist Du?")
       if age.isdigit():
           age = int(age)
           break
       else:
        print("Bitte gib eine gültige Zahl ein\nDu kannst hier auch unter 18 rein:)")

print("Willkommen bei hello.py,", name,"\nDu bist", age,"Jahre alt!")
