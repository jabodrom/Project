import os

for f in os.listdir("/Users/Полина_2/Downloads"):
    print(f)

print(os.getcwd())

os.chdir("/Users/Полина_2/Downloads")
print(os.getcwd())

print(os.getenv("HOMEPATH","it is Windows"))
print(os.getcwd())
my_home = os.getenv("HOMEPATH")
for f in os.listdir(my_home):
    print(f)

os.chdir(my_home)
for f in os.listdir("Dropbox"):
    print(f)

