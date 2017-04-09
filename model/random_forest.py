



######
########
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

genres_nothot = np.loadtxt("../data/single_num_genre_tags.txt")

na_train = np.array(np.loadtxt("../data/batches/batch_1.txt"), dtype="float32")
na_test = np.array(np.loadtxt("../data/batches/batch_24.txt"), dtype="float32")

for i in range(2, 24):
    data = np.loadtxt(f"../data/batches/batch_{i}.txt")
    na_train = np.concatenate((na_train, data))

for i in range(25, 29):
    data = np.loadtxt(f"../data/batches/batch_{i}.txt")
    na_test = np.concatenate((na_test, data))

labels_train_nothot = np.array(genres_nothot[0:len(na_train)], dtype="int32")
labels_test_nothot = np.array(genres_nothot[len(na_train):], dtype="int32")

print (len(na_train))
print (len(labels_train_nothot))
print (len(na_test))
print (len(labels_test_nothot))

clf = RandomForestClassifier(n_jobs=2)

clf.fit(na_train, labels_train_nothot)

preds = clf.predict(na_test)
print (pd.crosstab(labels_test_nothot, preds, rownames=['actual'], colnames=['preds']))
