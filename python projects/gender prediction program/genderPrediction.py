from sklearn import tree

# [height, weight, shoe size]
x = [
    [160, 52, 6],
    [165, 58, 7],
    [170, 64, 8],
    [175, 70, 9],
    [180, 77, 10],
    [185, 84, 11],
    [190, 91, 12],
    [168, 61, 7],
    [173, 68, 8],
    [178, 74, 9]
]

y = [
    "female",
    "female",
    "male",
    "male",
    "male",
    "male",
    "male",
    "female",
    "female",
    "male"
]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

def predict_gender():
    height = int(input("what is your height(cm):"))
    weight = int(input("what is your weight(kg):"))
    shoe_size = int(input("what is your shoe size(uk):"))
    new_person = [height, weight, shoe_size]

    prediction = clf.predict([new_person])

    print(prediction)

predict_gender()