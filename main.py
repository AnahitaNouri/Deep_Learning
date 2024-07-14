import config as c
from train import train
from utils import load_datasets, make_dataloaders
import time
from datetime import timedelta

def format_time(seconds):
    return str(timedelta(seconds=int(seconds)))

def train_all_classes():
    total_start_time = time.time()
    class_times = {}

    for class_name in c.class_names:
        print(f"Starting training on class: {class_name}")
        class_start_time = time.time()
        
        try:
            # Load datasets for the current class
            train_set, test_set = load_datasets(c.dataset_path, class_name)
            
            # Create dataloaders for the current class
            train_loader, test_loader = make_dataloaders(train_set, test_set)
            
            # Train the model on the current class
            model = train(train_loader, test_loader, class_name)
            
            class_duration = time.time() - class_start_time
            class_times[class_name] = class_duration

            print(f"Completed training for class: {class_name}")
            print(f"Time taken for {class_name}: {format_time(class_duration)}")
            print()

        except Exception as e:
            print(f"An error occurred while training class {class_name}: {str(e)}")
            print(f"Skipping class {class_name} and moving to the next one.")
            print()
            continue

    total_duration = time.time() - total_start_time

    print("Finished training all classes.")
    print(f"Total training time: {format_time(total_duration)}")
    print("\nTraining time for each class:")
    for class_name, duration in class_times.items():
        print(f"{class_name}: {format_time(duration)}")

if __name__ == "__main__":
    train_all_classes()