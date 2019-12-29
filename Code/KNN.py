import pandas as pd
import json
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def combineData(train_range,loc_input,loc_output):
    training_input_data = None
    training_output_data = None

    for idx in range(train_range[0],train_range[1]+1):
        print idx
        temp_input = pd.read_csv(loc_input+str(idx)+".csv")
        temp_output = json.load(open(loc_output+str(idx)+".txt"))

        index_list = []
        output_pro = []

        for idx, val in enumerate(temp_output):

            if 0 in val and not(6 in val or 7 in val or 1 in val):
                output_pro.append(0)
                index_list.append(idx)
            elif 6 in val and not(0 in val or 7 in val or 1 in val):
                output_pro.append(6)
                index_list.append(idx)
            elif 7 in val and not(0 in val or 6 in val or 1 in val):
                output_pro.append(7)
                index_list.append(idx)
            elif 1 in val and  not(6 in val or 7 in val or 0 in val):
                output_pro.append(1)
                index_list.append(idx)

        try:
            training_input_data = training_input_data.append(temp_input.iloc[index_list,:2500])
            training_output_data.extend(output_pro)
        except:
            training_input_data = temp_input.iloc[index_list,:2500]
            training_output_data = output_pro

    return training_input_data,training_output_data


training_input_data = None
training_output_data = None
curr = 1

for idx in range(1,6):
    temp = [curr,curr+99]
    temp_input, temp_output = combineData(temp,"song_csv_training/input/input_data_","song_csv_training/output/output_data_")
    try:
        training_input_data = training_input_data.append(temp_input)
        training_output_data.extend(temp_output)
        print training_input_data.shape
    except:
        training_input_data = temp_input
        training_output_data = temp_output
    curr += 100


index_equal = []
count_index = {0:0,1:0,6:0,7:0}
maintain_op = []

min_count = min(training_output_data.count(0),training_output_data.count(6),training_output_data.count(7),training_output_data.count(1))

for i,val in enumerate(training_output_data):
    if count_index[val] < min_count:
        index_equal.append(i)
        maintain_op.append(val)
    count_index[val] += 1

training_input_data = training_input_data.iloc[index_equal]
training_output_data = maintain_op

test_input_data = None
test_output_data = None
curr = 1
for idx in range(1,2):
    temp = [curr,curr+99]
    temp_input, temp_output = combineData(temp,"song_csv_test/input/input_data_","song_csv_test/output/output_data_")
    try:
        test_input_data = test_input_data.append(temp_input)
        test_output_data.extend(temp_output)
    except:
        test_input_data = temp_input
        test_output_data = temp_output
    curr += 100


training_input_data = pd.DataFrame(training_input_data)
test_input_data = pd.DataFrame(test_input_data)

for i in range(1,30):

    neigh = KNeighborsClassifier(n_neighbors=i)
    neigh.fit(training_input_data,training_output_data)
    accuracy =  neigh.score(test_input_data,test_output_data)

    print "accuracy of neighbor: " + str(i) + " : " + str(accuracy)

    y_prime = neigh.predict(test_input_data)

    confusion_matrix_test = confusion_matrix(test_output_data, y_prime, labels=[0, 1, 6, 7])
    df_cm = pd.DataFrame(confusion_matrix_test, index=[idx for idx in [0, 1, 6, 7]],
                         columns=[idx for idx in [0, 1, 6, 7]])
    plt.figure(figsize=(10, 7))
    sn.heatmap(df_cm, annot=True)
    plt.savefig("Output/test_confusion_matrix_knn_"+str(i)+".pdf")