import os
dir_contents= os.listdir()
# print(dir_contents)
nBinod = 0
def isBinod(filename):
    with open(filename, 'r') as f:
        filecontent = f.read()
    if 'binod' in filecontent.lower():
        return True
        n = n + 1
    else:
        return False


for item in dir_contents :
    if item.endswith('txt'):
        print (f'\nDetecting Binod in {item}')
        flag = isBinod(item)
        if flag:
            print(f'Binod found in {item}')
            nBinod += 1
        else :
            print(f'Binod is not found in {item}')
        
print("\n****Find Binod Summary****")
print(f'{nBinod} files found with Binod into it!!!')
