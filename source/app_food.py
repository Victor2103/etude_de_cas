import fiftyone as fo

food_dataset = fo.load_dataset('Food Dataset')

if __name__ == "__main__":
    # View summary info about the dataset
    session = fo.launch_app(food_dataset)
    session.wait()