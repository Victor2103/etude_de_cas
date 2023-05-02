import fiftyone as fo

coco_dataset = fo.load_dataset('COCO Dataset')

if __name__ == "__main__":
    # View summary info about the dataset
    session = fo.launch_app(coco_dataset)
    session.wait()
