import fiftyone as fo
import fiftyone.zoo as foz
import fiftyone.brain as fob

import os

path = 'data/food-101'

if not(os.path.exists(path)):
    os.system('bash scripts/food_data.sh')

try:
    # Create the food dataset
    food_dataset = fo.Dataset.from_dir(
        dataset_dir="data/food-101/images",
        dataset_type=fo.types.ImageClassificationDirectoryTree,
        name="Food Dataset",
    )
    food_dataset.persistent = True
except:
    pass

food_dataset = fo.load_dataset('Food Dataset')

classes = os.listdir("data/food-101/images")

model = foz.load_zoo_model(
    "clip-vit-base32-torch",
    text_prompt="A photo of a",
    classes=classes
)

food_dataset.apply_model(model)

try:
    # Index ground truth objects by similarity
    object_index = fob.compute_similarity(
        food_dataset,
        patches_field="ground_truth",
        model="clip-vit-base32-torch",
        brain_key="gt_sim",
    )
except Exception as e:
    pass



if __name__ == "__main__":

    # View summary info about the dataset
    session = fo.launch_app(food_dataset)

    # Convert to patches view
    patches = food_dataset.to_patches("ground_truth")

    # Perform a text query
    query = "a fish dish"
    view = patches.sort_by_similarity(query, k=25, brain_key="gt_sim")

    # Apply to the session
    session.view = view

    session.wait()