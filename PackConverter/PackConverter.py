import glob, os
from zipfile import ZipFile
import shutil

main2 = os.getcwd()

file = input("enter name > ")


if os.path.isdir(file): # directory
    filename = file
    shutil.copytree(filename, 'PackConverter/' + "#convertedPack - " + filename)

elif os.path.exists(file+'.zip'): #.zip file (input only name)
        
    file = file + '.zip'
    filename = file[:-4]

    print(file)

    with ZipFile(file, 'r') as zObject:
        zObject.extractall(path='PackConverter/' + "#convertedPack - " + filename)

elif os.path.exists(file) and file[-4:] == '.zip': #.zip file (input + .zip)
        
    file = file
    filename = file[:-4]

    print(file)

    with ZipFile(file, 'r') as zObject:
        zObject.extractall(path='PackConverter/' + "#convertedPack - "  + filename)

os.chdir('PackConverter/')

if os.path.exists("#convertedPack - " + filename + '/pack.mcmeta'):
    with open("main.py") as f:
        exec(f.read())
    f.close()

    # pack format = 1
    mcmeta = open("#convertedPack - " + filename + '/pack.mcmeta')
    mcmetaRead = mcmeta.read()
    mcmetaRead = mcmetaRead.replace('\n','')
    
    data = json.loads(mcmetaRead)
    data['pack']['pack_format'] = 1
    json_object = json.dumps(data, indent=4)
    
    mcmeta.close()

    with open("#convertedPack - " + filename + '/pack.mcmeta', "w") as outfile:
        outfile.write(json_object)
    outfile.close()  

    # zip file
    os.chdir(main2)
    shutil.make_archive(filename+' - Converted', 'zip', 'PackConverter/' + "#convertedPack - " + filename)
    print("conversion complete")

else:
    os.chdir(main2)
    print("pack format is invalid")

# - folder

# - zip
