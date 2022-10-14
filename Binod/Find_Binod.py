import os
dir_contents= os.listdir()
# print(dir_contents)
nBinod = 0
def isBinod(filename):
    with open(filename, 'r') as f:
        filecontent = f.read()
    if 'binod' in filecontent.lower():
        return True
        n+=1
    else:
        return False


for item in dir_contents :
    if item.endswith('txt'):
        print (f'\nDetecting_Binod_in_{item}')
        flag = isBinod(item)
        if flag:
            print(f'Binod_found_in_{item}')
            nBinod += 1
        else :
            print(f'Binod_is_not_found_in_{item}')
        
print("\n****Find_Binod_Summary****")
print(f'{nBinod} files found with Binod into it!!!')
