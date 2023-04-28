import fiftyone as fo
import fiftyone.zoo as foz

coco_dataset = foz.load_zoo_dataset(
    "coco-2017", 
    split="validation"
)
coco_dataset.persistent = True

if __name__ == "__main__":
    # View summary info about the dataset
    session = fo.launch_app(coco_dataset)
    session.wait()
