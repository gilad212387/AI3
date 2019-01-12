
import classifier
from hw3_utils import load_data
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Perceptron


arr = [1,2,3,4,5]



# experiment 1
examples, labels, test = load_data()
data = []
data.append(examples)
data.append(labels)
classifier.split_crosscheck_groups(data, 2)

tree_classifier = classifier.sklearn_factory_wrapper(DecisionTreeClassifier(criterion='entropy'))
accuracy, error = classifier.evaluate(tree_classifier, 2)
print("%.2f, %.2f" % (accuracy, error))

# experiment 2
perceptron = classifier.sklearn_factory_wrapper(Perceptron())
accuracy, error = classifier.evaluate(perceptron, 2)
print("%.2f, %.2f" % (accuracy, error))
