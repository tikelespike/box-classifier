from box_classifier import *

if __name__ == '__main__':
    box1 = Box("tall", 1, 9, 1)
    box2 = Box("wide", 3, 1, 3)
    box_types = [box1, box2]
    classifier = BoxClassifier(box_types, 0.15)
    boxes = [Box("kinda wide box", 2.9, 1.1, 3.08), Box("kinda tall box", 1.01, 8.8, 0.9), Box("weird cubic box", 5, 5, 5)]
    for box in boxes:
        result_type = classifier.classify(box)
        if result_type is None:
            print(box.id + " could not be classified")
        else:
            print(box.id + " classified as " + result_type.id)