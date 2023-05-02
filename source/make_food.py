import fiftyone as fo

import os

path = 'data/food-101'

if not(os.path.exists(path)):
    os.system('bash scripts/food_data.sh')

# Create the food dataset
food_dataset = fo.Dataset.from_dir(
    dataset_dir="data/food-101/images",
    dataset_type=fo.types.ImageClassificationDirectoryTree,
    name="Food Dataset",
)
food_dataset.persistent = True

"""from PIL import Image
import requests

from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(text=["a photo of a cat", "a photo of a dog"], images=image, return_tensors="pt", padding=True)

outputs = model(**inputs)
logits_per_image = outputs.logits_per_image # this is the image-text similarity score
probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities"""
