import numpy as np


class Box:
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z

class BoxClassifier:
    def __init__(self, box_types, max_relative_deviation):
        self.box_types = box_types
        self.max_relative_deviation = max_relative_deviation

    def classify(self, box):
        dimensions_box = [box.x, box.y, box.z]
        dimensions_box.sort()
        err_min = float('inf')
        min_err_type = None
        for box_type in self.box_types:
            dimensions_type = [box_type.x, box_type.y, box_type.z]
            dimensions_type.sort()
            err_x = abs(dimensions_box[0] - dimensions_type[0]) / dimensions_type[0]
            err_y = abs(dimensions_box[1] - dimensions_type[1]) / dimensions_type[1]
            err_z = abs(dimensions_box[2] - dimensions_type[2]) / dimensions_type[2]
            err = np.array([err_x, err_y, err_z])

            if err_x > self.max_relative_deviation: continue
            if err_y > self.max_relative_deviation: continue
            if err_z > self.max_relative_deviation: continue

            if np.linalg.norm(err) < err_min: err_min = err
            min_err_type = box_type

        return min_err_type

class BoxReader:

    def __init__(self, separator):
        self.separator = separator

    def read_from_file(self, path):
        boxes = []
        with open(path) as file:
            lines = file.readlines()
        for line in lines:
            parts = line.split(self.separator)
            boxes.append(Box(parts[0], int(parts[1]), int(parts[2]), int(parts[3])))
        return boxes