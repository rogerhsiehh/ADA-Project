from PIL import Image
import torch
import pandas as pd
import os

class CarDDDataset(torch.utils.data.Dataset):
    def __init__(self, csv_file, image_dir, class_label_mapping, transform=None):
        """
        Args:
            csv_file (str): Path to the CSV file containing image paths and labels.
            image_dir (str): Directory where images are stored.
            class_label_mapping (dict): Mapping of label numbers to class descriptions.
            transform (callable, optional): Optional transform to apply to images.
        """
        self.data = pd.read_csv(csv_file)
        self.image_dir = image_dir
        self.class_label_mapping = class_label_mapping
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        # Get the image file path and labels
        image_id = self.data.iloc[idx]['image_id']
        image_path = os.path.join(self.image_dir, image_id)  # Construct full image path
        multi_label_vector = eval(self.data.iloc[idx]['multi_label_vector'])  # List of binary values

        # Load the image as a PIL object
        image = Image.open(image_path).convert("RGB")

        # Apply transformations if specified
        if self.transform:
            image = self.transform(image)

        # Get the string class names for active labels
        active_labels = [self.class_label_mapping[i + 1] for i, val in enumerate(multi_label_vector) if val == 1]

        # Return the structured data
        return {
            "image": image,  # PIL Image or transformed tensor
            "image_file_path": image_path,
            "labels": torch.tensor(multi_label_vector, dtype=torch.float),  # Multi-label tensor
            "active_label_names": active_labels  # List of active class names
        }