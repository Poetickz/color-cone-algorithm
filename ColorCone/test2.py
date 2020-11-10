from ColorCone import ColorCone

import joblib

model = joblib.load('ColorCone/model-x7.pkl')

algoritm = ColorCone(model, 1.3, 0.5)

rgb_example = (239,126,115)

print(algoritm.modify_rgb(rgb_example))