import fiftyone as fo
import fiftyone.brain as fob
import fiftyone.zoo as foz

import os

path = "data/coco-2017"

try:
    os.mkdir("data")
except Exception as e:
    pass

coco_dataset = foz.load_zoo_dataset(
    "coco-2017", 
    split="validation",
    dataset_dir=path
)
coco_dataset.persistent = True

model = foz.load_zoo_model("clip-vit-base32-torch")

coco_dataset.apply_model(model)

# Index ground truth objects by similarity
try:
    object_index = fob.compute_similarity(
    coco_dataset,
    patches_field="ground_truth",
    model="clip-vit-base32-torch",
    brain_key="gt_sim",
)
except Exception as e:
    pass



if __name__ == "__main__":
    # View summary info about the dataset
    session = fo.launch_app(coco_dataset)

    # Convert to patches view
    patches = coco_dataset.to_patches("ground_truth")

    # Perform a text query
    query = "Wild animals"
    view = patches.sort_by_similarity(query, k=25, brain_key="gt_sim")

    # Apply to the session
    session.view = view

    session.wait()
