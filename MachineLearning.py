#First program in Python and first Machine learning try
#Is there sun or no
from pip._vendor.distlib.compat import raw_input
from sklearn import tree

features = [[7,0], [8,1], [9,1], [6,0]] #0 = AM || #1 = PM
labels = [1, 1, 0, 0]  #1 = Sun || #0 = No Sun

clf = tree.DecisionTreeClassifier()
cld = clf.fit(features, labels)

hour = raw_input ("Cual es la hora?\n")
meridian = raw_input ("AM or PM?\n")

if meridian == "AM" or "Am" or "am":
    meridian = 0

elif meridian == "PM" or "Pm" or "pm":
    meridian = 1

else:
    print "Not a correct Format"

prediccion = cld.predict ([[hour, meridian]])       

if prediccion == 1:
    print "There is sun"

else:
    print "There is no sun"  

