import fiftyone as fo

import os
import requests
import tarfile

url = "http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz"
path = 'data/food.tar.gz'

try:
    os.mkdir("data")
except Exception as e:
    print(e)

try:
    os.system('bash scripts/food_data.sh')
except Exception as e:
    print(e)

"""# Create the first datasetdataset
food_dataset = fo.Dataset.from_dir(
    dataset_dir="data/food-101/images",
    dataset_type=fo.types.ImageClassificationDirectoryTree,
    name="Food Dataset",
)
food_dataset.persistent = True"""