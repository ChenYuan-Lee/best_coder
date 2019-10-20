from pandas import read_csv
from nltk.stem import PorterStemmer

import re

ps = PorterStemmer()

kw_df = read_csv("kw_list.csv", index_col = "Group")
kw_map = {}
kw2_list = []
kw3_list = []
for id, kw_str in kw_df.itertuples():
    for kw in kw_str.split(", "):
        kw_comp = kw.split(" ")
        if len(kw_comp) == 1:
            stemmed_kw = ps.stem(kw)
        elif len(kw_comp) == 2:
            stemmed_kw = re.sub("\-", "", " ".join([ps.stem(word) for word in kw_comp]))
            kw2_list.append(stemmed_kw)
        else:
            stemmed_kw = re.sub("\-", "", " ".join([ps.stem(word) for word in kw_comp]))
            kw3_list.append(stemmed_kw)
        kw_map["".join(stemmed_kw.split(" "))] = id
print(kw_map)
print(kw2_list)
print(kw3_list)


def stem_fn(name_str):
    regex = re.compile('[^a-zA-Z \']')
    regexed_str = regex.sub(' ', name_str)
    return " ".join([ps.stem(word) for word in regexed_str.split(" ")]).strip()


def main(name_str):
    results = set()
    for kw in kw3_list:
        name_str = name_str.replace(kw, "".join(kw.split(" ")))
    for kw in kw2_list:
        name_str = name_str.replace(kw, "".join(kw.split(" ")))
    for i in name_str.split(" "):
        id = kw_map.get(i)
        if id is not None:
            results.add(id)
    return sorted(list(results))

data = read_csv("data.csv", index_col = "index")
data.name = data.name.str.lower()
data.name = data.name.transform(stem_fn)
data.name = data.name.transform(main)
print(data.to_csv("results.csv"))