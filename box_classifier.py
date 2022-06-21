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
        dimensionsBox = [box.x, box.y, box.z]
        dimensionsBox.sort()
        errMin = float('inf')
        minErrType = None
        for box_type in self.box_types:
            dimensionsType = [box_type.x, box_type.y, box_type.z]
            dimensionsType.sort()
            errX = abs(dimensionsBox[0] - dimensionsType[0]) / dimensionsType[0]
            errY = abs(dimensionsBox[1] - dimensionsType[1]) / dimensionsType[1]
            errZ = abs(dimensionsBox[2] - dimensionsType[2]) / dimensionsType[2]
            err = np.array([errX, errY, errZ])

            if errX > self.max_relative_deviation: continue
            if errY > self.max_relative_deviation: continue
            if errZ > self.max_relative_deviation: continue

            if np.linalg.norm(err) < errMin: errMin = err
            minErrType = box_type

        return minErrType
