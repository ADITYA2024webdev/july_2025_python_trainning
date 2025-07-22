
a=input("text:")
from datetime import datetime


current_datetime = datetime.now()


filename=str(current_datetime).replace(":","_")




with open(str(filename)+".txt", "w") as file:
    file.write(a)

print(f"File '{filename}' has been created.")


