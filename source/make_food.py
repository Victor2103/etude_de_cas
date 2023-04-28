import fiftyone as fo

import os
import requests
import tarfile

url = "http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz"
path = 'data/food.tar.gz'
 
try:
    os.mkdir("data")
    req = requests.get(url, stream=True)
    if req.status_code == 200:
        with open(path, 'wb') as f:
            f.write(req.raw.read())
    tar  = tarfile.open(path)
    tar.extractall('data')
    tar.close

except Exception as e:
    print(e)

"""# Create the first datasetdataset
food_dataset = fo.Dataset.from_dir(
    dataset_dir="data/food-101/images",
    dataset_type=fo.types.ImageClassificationDirectoryTree,
    name="Food Dataset",
)
food_dataset.persistent = True"""