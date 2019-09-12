from itertools import starmap
from PyQt5.QtWidgets import QLabel

meta_object = QLabel.staticMetaObject
itr = map(lambda index: meta_object.property(index),
          range(0, meta_object.propertyCount()))
for prop in itr:
    print(prop.name())
