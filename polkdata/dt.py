from sklearn import tree
import os
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
os.system("dot -Tpdf iris.dot > iris.pdf")
