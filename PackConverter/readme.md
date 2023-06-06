**PackConverter**
-

A bunch of spaghetti code that converts 1.19 / 1.20 resource packs to a format compatible with version 1.8. This was mainly tested on PVP texture packs, so the success rate of conversion may vary, especially for packs that rely heavily on JSON models. <br /> <br /> 


**Dependencies**

- Python
- PIL
- shutil
- glob  <br /> <br />


**Steps to Use**

1. Unzip PackConverter.zip into a folder.
2. Place a resource pack of choice into the same folder. 
3. Run PackConverter.py 
4. Input the resource pack name to convert & initiate.
5. The script will output a new pack compatible with Minecraft 1.8.  <br /> <br />

**Limitations**

- Packs that rely heavily on 3D / JSON models may be buggy.
- Certain entities (Horses, Boats, Zombie Pigmen) will not convert properly as they have different entity models. 
- Some PVP packs will look different from the original because they were designed to be an overlay for the new 1.14 Jappa textures. You can download a pre-converted Jappa pack and overlay it on top to resolve this. Alternatively, you can extract the textures from the minecraft .jar file and convert it into a 1.8 pack using the PackConverter.
