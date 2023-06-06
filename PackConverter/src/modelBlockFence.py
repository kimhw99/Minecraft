import os
import shutil
import json
import copy
    
# south
def south(uvSide, a):
    for i in range(0, a):
        j = copy.deepcopy(uvSide[i])
        j['from'][0], j['to'][0] = j['to'][0], j['from'][0]
        j['from'][2], j['to'][2] = 16-j['from'][2], 16-j['to'][2]
        #print(j)
        uvSide.append(j)

    return uvSide


# east
def east(uvSide, a):
    for i in range(0, a):
        j = copy.deepcopy(uvSide[i])

        x = 16-j['to'][2]
        y = j['from'][0]
        z = 16-j['from'][2]
        w = j['to'][0]

        j['from'][0], j['from'][2], j['to'][0], j['to'][2] = x, y, z, w

        key = []
        pair = []
        
        for i in ['north', 'south', 'east', 'west']:
            if i in j['faces']:
                key.append(j['faces'].pop(i))
                pair.append(i)
        
        print(pair)
        
        for i in range(0, len(pair)):
            if pair[i] == 'north':
                pair[i] = 'west'
            elif pair[i] == 'east':
                pair[i] = 'north'
            elif pair[i] =='south':
                pair[i] = 'east'
            elif pair[i] == 'west':
                pair[i] = 'south'

        for i in range(0, len(pair)):
            j['faces'][pair[i]] = key[i]
            
        uvSide.append(j)
    
    return uvSide

# west
def west(uvSide, a):
    for i in range(0, a):
        j = copy.deepcopy(uvSide[i])
        j['from'][0], j['from'][2], j['to'][0], j['to'][2] = j['from'][2], j['from'][0], j['to'][2], j['to'][0]

        key = []
        pair = []
        
        for i in ['north', 'south', 'east', 'west']:
            if i in j['faces']:
                key.append(j['faces'].pop(i))
                pair.append(i)
        
        print(pair)
        
        for i in range(0, len(pair)):
            if pair[i] == 'north':
                pair[i] = 'east'
            elif pair[i] == 'east':
                pair[i] = 'south'
            elif pair[i] =='south':
                pair[i] = 'west'
            elif pair[i] == 'west':
                pair[i] = 'north'

        for i in range(0, len(pair)):
            j['faces'][pair[i]] = key[i]
            
        uvSide.append(j)
        
    return uvSide

# post
def post2(post, uvSide):
    f = open(post)
    dataPost = json.load(f)
    f.close
        
    dataPost2 = copy.deepcopy(dataPost)
    
    global blocksToAdd
    global blocksToReference
    global fence
    
    if 'elements' in dataPost:
        for i in dataPost['elements']:
            for j in i['faces']:
                i['faces'][j]['texture'] =  i['faces'][j]['texture']+'_post'
                
        uvPost = dataPost['elements']
    else:
        if fence == 'fence':
            dataPost['elements'] = [
            {   "from": [ 6, 0, 6 ],
                "to": [ 10, 16, 10 ],
                "faces": {
                    "down":  { "uv": [ 6, 6, 10, 10 ], "texture": '#' + list(dataPost['textures'])[0]+ "_post", "cullface": "down" },
                    "up":    { "uv": [ 6, 6, 10, 10 ], "texture": '#' + list(dataPost['textures'])[0]+ "_post", "cullface": "up"   },
                    "north": { "uv": [ 6, 0, 10, 16 ], "texture": '#' + list(dataPost['textures'])[0]+ "_post"},
                    "south": { "uv": [ 6, 0, 10, 16 ], "texture": '#' + list(dataPost['textures'])[0]+ "_post"},
                    "west":  { "uv": [ 6, 0, 10, 16 ], "texture": '#' + list(dataPost['textures'])[0]+ "_post"},
                    "east":  { "uv": [ 6, 0, 10, 16 ], "texture": '#' + list(dataPost['textures'])[0]+ "_post"}
                }}]
            uvPost = dataPost['elements']

        elif fence == 'wall':
            dataPost['elements'] = [
            {   "from": [ 4, 0, 4 ],
                "to": [ 12, 16, 12 ],
                "faces": {
                    "down":  { "uv": [ 4, 4, 12, 12 ], "texture": '#' + list(dataPost['textures'])[0]+ "_post", "cullface": "down" },
                    "up":    { "uv": [ 4, 4, 12, 12 ], "texture": '#' + list(dataPost['textures'])[0]+ "_post", "cullface": "up"   },
                    "north": { "uv": [ 4, 0, 12, 16 ], "texture": '#' + list(dataPost['textures'])[0]+ "_post"},
                    "south": { "uv": [ 4, 0, 12, 16 ], "texture": '#' + list(dataPost['textures'])[0]+ "_post"},
                    "west":  { "uv": [ 4, 0, 12, 16 ], "texture": '#' + list(dataPost['textures'])[0]+ "_post"},
                    "east":  { "uv": [ 4, 0, 12, 16 ], "texture": '#' + list(dataPost['textures'])[0]+ "_post"}
                }}]
            uvPost = dataPost['elements']

    for i in dataPost['textures']:
        blocksToReference.append((dataPost['textures'][i]).replace("blocks/",""))
        blocksToAdd.append((dataPost['textures'][i]).replace("blocks/","") + "_post")
        
        dataPost['textures'][i] = dataPost['textures'][i] + "_post"
        dataSide['textures'][i+'_post'] = dataPost['textures'][i]

    dataSide['textures']['particle'] = dataPost['textures'][list(dataPost['textures'])[0]] # particles

    print(dataPost2)

    if 'textures' in dataPost2:
        if 'elements' in dataPost2:
            dataPost2['textures']['particle'] = dataPost['textures'][list(dataPost['textures'])[0]] # particles
            json_object = json.dumps(dataPost2, indent=4)
            
            with open(post, "w") as outfile:
                outfile.write(json_object)
                
            outfile.close()


    a = len(uvPost)
    #print(a)
    
    for i in range(0, a):
        j = copy.deepcopy(uvPost[i])
        uvSide.append(j)
        
    return uvSide



def updateFences(post, side):

    global blocksToAdd
    global blocksToReference
    global dataSide
    global fence
    
    f = open(side)
    dataSide = json.load(f)
    f.close

    if 'elements' in dataSide:
        uvSide = dataSide['elements']

    else:
        if fence == "wall":
            uvSide = [
        {   "from": [ 5, 0, 0 ],
            "to": [ 11, 14, 8 ],
            "faces": {
                "down":  { "texture": "#wall", "cullface": "down" },
                "up":    { "texture": "#wall" },
                "north": { "texture": "#wall", "cullface": "north" },
                "west":  { "texture": "#wall" },
                "east":  { "texture": "#wall" }
            }}]
            
        elif fence == 'fence':
                uvSide = [
        {   "from": [ 7, 12, 0 ],
            "to": [ 9, 15, 9 ],
            "faces": {
                "down":  { "uv": [ 7, 0, 9, 9 ], "texture": "#texture" },
                "up":    { "uv": [ 7, 0, 9, 9 ], "texture": "#texture" },
                "north": { "uv": [ 7, 1, 9, 4 ], "texture": "#texture", "cullface": "north" },
                "west":  { "uv": [ 0, 1, 9, 4 ], "texture": "#texture" },
                "east":  { "uv": [ 0, 1, 9, 4 ], "texture": "#texture" }
            },
            "__comment": "top bar"
        },
        {   "from": [ 7, 6, 0 ],
            "to": [ 9, 9, 9 ],
            "faces": {
                "down":  { "uv": [ 7, 0, 9,  9 ], "texture": "#texture" },
                "up":    { "uv": [ 7, 0, 9,  9 ], "texture": "#texture" },
                "north": { "uv": [ 7, 7, 9, 10 ], "texture": "#texture", "cullface": "north" },
                "west":  { "uv": [ 0, 7, 9, 10 ], "texture": "#texture" },
                "east":  { "uv": [ 0, 7, 9, 10 ], "texture": "#texture" }
            }}]
        
    uvSide2 = copy.deepcopy(uvSide)
    uvSide3 = copy.deepcopy(uvSide)
    a = len(uvSide)
    
    # export (n)
    uvSide = post2(post, uvSide)

    dataSide['elements'] = uvSide
    if 'parent' in dataSide:
        dataSide.pop('parent')
    json_object = json.dumps(dataSide, indent=4)
    
    with open(material + "_" + fence +'_n.json', "w") as outfile:
        outfile.write(json_object)
    outfile.close()
    
    # export (ns wall)
    if fence == 'wall':
        print("--")
        uvSide3 = south(uvSide3, a)

        dataSide['elements'] = uvSide3
        if 'parent' in dataSide:
            dataSide.pop('parent')
        json_object = json.dumps(dataSide, indent=4)
        
        with open(material + "_" + fence +'_ns.json', "w") as outfile:
            outfile.write(json_object)
        outfile.close()
    
    # export (ns) (ns_above)
    uvSide = south(uvSide, a)

    dataSide['elements'] = uvSide
    if 'parent' in dataSide:
        dataSide.pop('parent')
    json_object = json.dumps(dataSide, indent=4)

    if fence == 'fence':
        with open(material + "_" + fence +'_ns.json', "w") as outfile:
            outfile.write(json_object)
        outfile.close()

    elif fence == 'wall':
        with open(material + "_" + fence +'_ns_above.json', "w") as outfile:
            outfile.write(json_object)
        outfile.close()

    # export (ne)
    uvSide2 = post2(post, uvSide2)
    uvSide2 = east(uvSide2, a)

    dataSide['elements'] = uvSide2
    if 'parent' in dataSide:
        dataSide.pop('parent')
    json_object = json.dumps(dataSide, indent=4)

    with open(material + "_" + fence +'_ne.json', "w") as outfile:
        outfile.write(json_object)
    outfile.close()

    # export (nse)
    uvSide = east(uvSide, a)

    dataSide['elements'] = uvSide
    if 'parent' in dataSide:
        dataSide.pop('parent')
    json_object = json.dumps(dataSide, indent=4)

    with open(material + "_" + fence +'_nse.json', "w") as outfile:
        outfile.write(json_object)
    outfile.close()
     
    # export (nsew)
    uvSide = west(uvSide, a)

    dataSide['elements'] = uvSide
    if 'parent' in dataSide:
        dataSide.pop('parent')
    json_object = json.dumps(dataSide, indent=4)

    with open(material + "_" + fence +'_nsew.json', "w") as outfile:
        outfile.write(json_object)
    outfile.close()


# blocks
blocksToAdd = []
blocksToReference = []

# prereq
materials = ['oak', 'birch', 'spruce', 'jungle', 'dark_oak', 'acacia', 'nether_brick']
fence = 'fence' # fence / wall


for material in materials:
    post = material + "_" + fence + "_post.json"
    side = material + "_" + fence + "_side.json"

    if (os.path.isfile(post) is True) and (os.path.isfile(side) is True):
        if os.path.isfile(material + "_" + fence + '_nsew.json') is False:
            updateFences(post, side)

materials = ['cobblestone', 'mossy_cobblestone']
fence = 'wall' # fence / wall

for material in materials:
    post = material + "_" + fence + "_post.json"
    side = material + "_" + fence + "_side.json"

    if (os.path.isfile(post) is True) and (os.path.isfile(side) is True):
        print(material + "_" + fence + '_nsew.json')
        if os.path.isfile(material + "_" + fence + '_nsew.json') is False:
            #if material == 'mossy_cobblestone':
                #material = 'mossy'
                
            updateFences(post, side)

#Rename Mossy Cobblestone -> Mossy
moss = ['_nsew', '_ns', '_ne', '_nse', 'ns_above', '_n', '_post']

for i in moss:
    if os.path.exists('mossy_cobblestone_wall' + i + '.json'):
        os.replace('mossy_cobblestone_wall' + i + '.json', 'mossy_wall' + i + '.json')

# add textures


#"from": [7.5, 13, 1], "to": [8.5, 15, 7],

#"from": [9, 13, 7.5], "to": [15, 15, 8.5],




