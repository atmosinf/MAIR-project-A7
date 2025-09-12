import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

from baseline_inform import BaselineInform
from baseline_rulebased import BaselineRuleBased

# Path to 'dialog_acts.dat' file
file_path = "data/dialog_acts.dat"

# List for feature and target
labels = []
sentences = []

# Open file
with open(file_path) as f:
    for line in f:
        # Remove unwanted spaces and characters (like '\n'), convert string to lower case, split the act from the dialog and store as lists in list
        prepped_line = line.strip().lower().split(" ", maxsplit=1)
        labels.append(prepped_line[0])
        sentences.append(prepped_line[1])

def predict_data():
    # Split dataset into train- and testset
    _, x_test, _, y_test = train_test_split(sentences, labels, random_state=42, test_size=0.15)

    baseInform = BaselineInform()
    baseInform_res = baseInform.predict(x_test)

    baseRuleBased = BaselineRuleBased()
    baseRuleBased_res = baseRuleBased.predict(x_test)

    print("accuracy score baseInform:", accuracy_score(y_test, baseInform_res))
    # print(confusion_matrix(y_test, baseInform_res))
    ConfusionMatrixDisplay.from_predictions(y_test, baseInform_res)
    plt.xticks(rotation=90, fontsize=8)
    plt.show()

    print("accuracy score baseRuleBased:", accuracy_score(y_test, baseRuleBased_res))
    # print(confusion_matrix(y_test, baseRuleBased_res))
    ConfusionMatrixDisplay.from_predictions(y_test, baseRuleBased_res)
    plt.xticks(rotation=90, fontsize=8)
    plt.show()

def test_models():
    ...

def start_up_ui():
    print("You're running my code! What is it you want to do?")
    print("If you want me to classify the 'dialog_acts.dat' file, type 'file'.")
    print("Or if you want me to classify one of your utterances, type 'try me'.")
    print("If you want to stop this script, type 'exit'.")

    user_input = input("What is it going to be?: ")

    if user_input not in ['file', 'try me', 'exit']:
        print('You put in an incorrect input, try again!')
        user_input = input("What is it going to be?: ")
    
    if user_input == 'file':
        print('Okay, you want me to show my skills, here you go!')
        predict_data()
    elif user_input == 'try me':
        print('You want to test my skills!')
        ...
    else:
        print("You're shutting me down...")
        exit

start_up_ui()


"""
    TODO:
    DONE - split dataset into train- and testset
    DONE - Create first baseline model (always classify as majority class (inform))
    DONE - Create second baseline model based on rules (start simple and add if necessary) at least 0.8 (80%) accuracy
    - Add feature for the user to input a new utterance and classify that utterance 
"""
