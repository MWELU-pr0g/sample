# from os import ssample.txt as f0

# print(os.listdir(home))
try:
    with open('sample.txt','r') as f:
	f_contents=f.read()

except Exception:
	text='none'

print(f_contents)