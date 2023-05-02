import os

import fiftyone.zoo as foz

try:
    os.mkdir("data")
except Exception as e:
    print(e)

coco_dataset = foz.load_zoo_dataset(
    "coco-2017", 
    split="validation",
    dataset_name="COCO dataset",
    dataset_dir="data"
)
coco_dataset.persistent = True