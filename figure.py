import os
import time


class Figure:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.scad_path = self.base_path+"/generated_openscad/"+str(time.time())[:-3]+".scad"
        scad_file = file(self.scad_path, "w")
        scad_preface = file(self.base_path+"/scad_preface.txt")
        for each in scad_preface:
            scad_file.write(each)
        scad_preface.close()
        scad_file.close()
        self.points = []
        self.lines = {}

    def line(self, (x1, y1, z1), (x2, y2, z2), width=1, end1="round", end2="round"):
        p1 = [x1, y1, z1]
        p2 = [x2, y2, z2]
        width=float(width)
        scad_file = file(self.scad_path, "a")
        scad_file.write("line(" + str(p1) + "," + str(p2) + ", diameter=" + str(width) + ");\n")
        if end1 == "round":
            scad_file.write("translate(" + str(p1) + ") sphere(" + str(width/2) + ");\n")
        if end2 == "round":
            scad_file.write("translate(" + str(p2) + ") sphere(" + str(width/2) + ");\n")
        scad_file.close()
        if p1 not in self.points:
            self.points.append(p1)
            self.lines[len(self.points)-1] = []
        if p2 not in self.points:
            self.points.append(p2)
            self.lines[len(self.points)-1] = []
        self.lines[self.points.index(p1)].append({"point":self.points.index(p2),"width":width})

    def get_openscad_path(self):
        saved = file(self.base_path+"/openscad_path.txt").read().rstrip()
        if saved == "":
            print "Looking for the openscad installation. Write the correct path into " + self.base_path+"/openscad_path.txt"
        else:
            return saved

    def generate_stl(self):
        print("generating...")
        openscad_path = self.get_openscad_path()
        print openscad_path + " " + self.scad_path
        os.system(openscad_path + " " + self.scad_path)