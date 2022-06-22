from box_classifier import *

if __name__ == '__main__':
    # box_types = [Box("tall", 100, 900, 100), Box("wide", 300, 100, 300, 200)]
    box_types = BoxReader(',').read_from_file('demoboxes.txt')

    allowed_deviation = 0.15
    classifier = BoxClassifier(box_types, allowed_deviation, use_weight=False)

    boxes = [Box("kinda wide box", 290, 110, 308), Box("kinda tall box", 101, 880, 90), Box("weird cubic box", 500, 500, 500)]
    for box in boxes:
        result_type = classifier.classify(box)
        if result_type is None:
            print(box.id + " could not be classified")
        else:
            print(box.id + " classified as " + result_type.id)
