import subprocess
import json
import glob
import os
import time

for x in range(20):
    with open("./iden.json") as data_file:
        data = json.load(data_file)

    with open("./iden.json", "w") as data_file:
        data["identifier"] = int(time.time())
        json.dump(data, data_file, indent=4)

    identifier = data["identifier"]
    output = "concrete_voids"
    output_merge = "concrete_voids_merged.out"

    p1 = subprocess.Popen("python -m gprMax concrete_voids.in -n 120 -gpu", shell=True)

    p1.wait()

    p2 = subprocess.Popen("python -m tools.outputfiles_merge --remove-files %s" % output, shell=True)

    p2.wait()

    p3 = subprocess.Popen("python -m tools.plot_Bscan %s Ez --save" % output_merge, shell=True)

    p3.wait()

    vtis = glob.glob('*.vti');
    for vti in vtis:
        os.remove(vti)
    print("VTIs deleted")
    img = output + '_merged.jpg'
    renamed = str(identifier) + img
    os.rename(img, renamed)


    print("Image exported")
