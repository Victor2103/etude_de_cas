import fiftyone.zoo as foz

downloaded_datasets = foz.list_downloaded_zoo_datasets("data")
print(downloaded_datasets)