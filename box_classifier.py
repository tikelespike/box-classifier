import numpy as np


class Box:
    def __init__(self, describing_id, x, y, z, weight=1):
        self.id = describing_id
        self.x = x
        self.y = y
        self.z = z
        self.weight = weight

class BoxClassifier:
    def __init__(self, box_types, max_relative_deviation, use_weight):
        self.box_types = box_types
        self.max_relative_deviation = max_relative_deviation
        self.use_weight = use_weight

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
            err_w = abs(box.weight - box_type.weight) / box_type.weight
            err = np.array([err_x, err_y, err_z, err_w]) if self.use_weight else np.array([err_x, err_y, err_z])

            if err_x > self.max_relative_deviation: continue
            if err_y > self.max_relative_deviation: continue
            if err_z > self.max_relative_deviation: continue
            if err_w > self.max_relative_deviation and self.use_weight: continue

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
            box = Box(parts[0], int(parts[1]), int(parts[2]), int(parts[3]))
            if len(parts) > 4: box.weight = int(parts[4])
            boxes.append(box)
        return boxes
