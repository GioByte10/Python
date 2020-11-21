#First program in Python and first Machine learning try
#Is there sun or no

from sklearn import tree

features = [[7], [20], [21], [6]] #0 = AM || #1 = PM
labels = [1, 1, 0, 0]  #1 = Sun || #0 = No Sun

clf = tree.DecisionTreeClassifier()
cld = clf.fit(features, labels)

while True:
    hour = raw_input ("Cual es la hora?\n")
    meridian = raw_input ("AM or PM?\n")

    if meridian == "AM" or "Am" or "am":
        hour = hour
    
    elif meridian == "PM" or "Pm" or "pm":
        hour = hour + 12

    else:
        print "Not a correct Format"

    prediccion = cld.predict ([[hour]])       

    if hour != -1 or meridian != -1:
        break    

    if prediccion == 1:
        print "There is sun"

    else:
        print "There is no sun"          


