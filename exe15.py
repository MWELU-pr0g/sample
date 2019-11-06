from sys import argv

script,filename=argv

text=open(filename)

print("here's your file %r:")%(filename)
print(text.read)

print("the filename again:")
file_again=input('>')

text_again=open(file_again)

print(text_again.read)
