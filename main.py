import os
import pandas as pd

# Load CSV data into a pandas DataFrame
data = pd.read_csv(r'/content/test_labels.csv')

# Filter only relevant classes from the CSV data
relevant_classes = ['Car', 'Pedestrian', 'Cyclist']  # Note the capitalization as per your txt file data
data = data[data['label'].isin(relevant_classes)]

# Create a dictionary where each index corresponds to a list of labels
csv_dict = data.groupby('index')['label'].apply(list).to_dict()
print(csv_dict)
# Directory where the txt files are located
txt_dir = r'/content/label_2'

# Counter for missing classes
missing_classes = 0
n=100 #number of images considered
# Create a sorted list of the txt files
txt_files = sorted(os.listdir(txt_dir))
txt_files = txt_files[:n]
# Iterate over each txt file, but only take the first "n" where "n" is the total indices in the CSV data
for filename in txt_files:
    print(filename)
    if filename.endswith('.txt'):
        # Get the index from the filename
        index = int(filename.split('.')[0])
        # Open and read the txt file
        with open(os.path.join(txt_dir, filename), 'r') as f:
            txt_classes = [line.split()[0] for line in f]  # Only take the first word on each line

        # Filter only relevant classes from the txt file
        txt_classes = [cls for cls in txt_classes if cls in relevant_classes]
        print(csv_dict)
        # If the index exists in the CSV data
        if index in csv_dict:
            print("Afef", csv_dict)
            csv_classes = csv_dict[index]
            print("A", csv_classes)
            # Check for each class in txt file
            for cls in txt_classes:
                # If the class is not in the CSV data or the count is less, increment the missing counter
                if csv_classes.count(cls) < txt_classes.count(cls):
                    missing_classes += 1
accuracy = 100-((missing_classes/n)*100)
print(f"Total missing classes: {missing_classes}")
print(f"Accuracy: {accuracy}")

