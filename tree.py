import math 

def entropy(arr):
    s = 0
    for item in arr:
        if item != 0 and item != 1:
            s -= (item * math.log(item, 2))
    return s

def b_ent(p):
    return entropy([p, (1-p)])

def remainder(pos, neg, total_pos, total_neg):
    s = 0
    for p, n in zip(pos, neg):
        s += (p+n)/(total_pos + total_neg) * b_ent(p / (p + n))
    return s

def gain(pos, neg, total_pos, total_neg):
    return b_ent(total_pos / (total_pos + total_neg)) - remainder(pos, neg, total_pos, total_neg)

#print(gain([1, 1, 2, 2], [1, 1, 2, 2], 6, 6))
#print(gain([0, 4, 2], [2, 0, 4], 6, 6))

def build_tree(data):
    max_gain = 0
    split = 0

    features = set()
    for feature in range(len(data[0]) - 1):
        pos_values = {}
        neg_values = {}
        for train_datapoint in range(len(data)):
            if data[train_datapoint][-1] == "y":
                pos_values[data[train_datapoint][feature]] = pos_values.get(data[train_datapoint][feature], 0) + 1
            if data[train_datapoint][-1] == "n":
                neg_values[data[train_datapoint][feature]] = neg_values.get(data[train_datapoint][feature], 0) + 1

        a = []
        b = []
        for item in set(pos_values).union(set(neg_values)):
            a.append(pos_values.get(item, 0))
            b.append(neg_values.get(item, 0))
        g = gain(a, b, sum(a), sum(b))

        if g > max_gain:
            max_gain = g
            split = feature

    if max_gain != 0:
        print("Splitting on feature {}".format(split))
        #print(max_gain)
        next_iter = {}
        for item in data:
            next_iter.setdefault(item[split], []).append(item)

        for item in next_iter:
            print("Buildling tree on value {}".format(item))
            #print(next_iter[item])
            build_tree(next_iter[item])

    if max_gain == 0:
        print("At leaf node")



#Dataset taken from AI: AMA 3rd edition
data = [["y", "n", "n", "y", "s", 3, "n", "y", "f", 0, "y"],
        ["y", "n", "n", "y", "f", 1, "n", "n", "t", 30, "n"],
        ["n", "y", "n", "n", "s", 1, "n", "n", "b", 0, "y"],
        ["y", "n", "y", "y", "f", 1, "y", "n", "t", 10, "y"],
        ["y", "n", "y", "n", "f", 3, "n", "y", "f", 60, "n"],
        ["n", "y", "n", "y", "s", 2, "y", "y", "i", 0, "y"],
        ["n", "y", "n", "n", "n", 1, "y", "n", "b", 0, "n"],
        ["n", "n", "n", "y", "s", 2, "y", "y", "t", 0, "y"],
        ["n", "y", "y", "n", "f", 1, "y", "n", "b", 60, "n"],
        ["y", "y", "y", "y", "f", 3, "n", "y", "i", 10, "n"],
        ["n", "n", "n", "n", "n", 1, "n", "n", "t", 0, "n"],
        ["y" ,"y", "y", "y", "f", 1, "n", "n", "b", 30, "y"]]

build_tree(data)


        


