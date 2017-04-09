from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

genres_nothot = np.loadtxt("../data/single_num_genre_tags.txt")

na_train = np.array(np.loadtxt("../data/batches/batch_1.txt"), dtype="float32")
na_test = np.array(np.loadtxt("../data/batches/batch_24.txt"), dtype="float32")

for i in range(2, 24):
    data = np.loadtxt(("../data/batches/batch_%(i)s.txt" % locals()))
    na_train = np.concatenate((na_train, data))

for i in range(25, 29):
    data = np.loadtxt(("../data/batches/batch_%(i)s.txt" % locals()))
    na_test = np.concatenate((na_test, data))

labels_train_nothot = np.array(genres_nothot[0:len(na_train)], dtype="int32")
labels_test_nothot = np.array(genres_nothot[len(na_train):], dtype="int32")


features_array =  [
0.05600731687037498,
0.06860986452054794,
3.0910964165216144,
0.1464611496056862,
0.16041940411523675,
0.4823313304954637,
0.00038081079227547627,
0.08411186696900982,
-17.81654097826876,
0.961004497413283,
-0.4969442856661338,
0.22623577305620765,
-0.154838770667418,
0.39734218592114084,
0.17525510965939067,
-0.13625194085456405,
-0.16359257482213624,
0.25959169233729434,
0.028287531452625466,
0.01919373622327452,
-0.12439255337475205,
0.0006933685570485762,
0.0007047895515870522,
0.001610680530202902,
0.0007269830308656564,
0.0008636884447262516,
0.0013598017380908808,
0.001871933838338538,
0.0011466639091088596,
0.0010855837180873903,
0.0008803270631170333,
0.0011715181762012937,
0.0009376727801765112,
0.0009901428809023433,
0.015110266529133196,
0.02900165641919676,
0.1978362479743389,
0.02552527648596338,
0.013365259415870634,
0.2037349105031198,
0.00021645954014460958,
0.02881738031889408,
0.6838349914594682,
0.4220689536938029,
0.6508458482481436,
0.45920941830211,
0.25325567232932555,
0.26066485493560027,
0.20321988673400324,
0.23027628737560055,
0.1615056281605721,
0.41795934584132116,
0.3703279886361258,
0.3187872574994319,
0.2706605272321142,
0.000844972772091594,
0.0007536150124379257,
0.0013993978777177222,
0.0005989441916388648,
0.0008823715618789572,
0.00136692656094431,
0.0020175030904995344,
0.0014281726676987243,
0.0011074197836130316,
0.0004852168654119002,
0.0023022246781709576,
0.0018490094498212937,
0.000780926749810205,
199.99999999999997
]

single_song_features = np.array(features_array, dtype='int32')

print (len(na_train))
print (len(labels_train_nothot))
print (len(na_test))
print (len(labels_test_nothot))

classifications = []

for i in range(0, 20):
    clf = RandomForestClassifier(n_jobs=2)
    clf.fit(na_train, labels_train_nothot)
    preds = clf.predict(single_song_features)
    print("hellloooooooooooooo")
    print (preds)
    print("hellloooooooooooooo")
    classifications.append(preds[0])

print (classifications)

# print (pd.crosstab(labels_test_nothot, preds, rownames=['actual'], colnames=['preds']))
