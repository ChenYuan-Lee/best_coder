from networkx import Graph, connected_components
from pandas import read_csv
import numpy as np

bank_df = read_csv("bank_accounts.csv", dtype = {"userid": str, "bank_account": str})
cc_df = read_csv("credit_cards.csv", dtype = {"userid": str, "credit_card": str})
device_df = read_csv("devices.csv", dtype = {"userid": str, "device": str})

all_users = set(bank_df.userid.tolist() + cc_df.userid.tolist() + bank_df.userid.tolist())

graph = Graph()
graph.add_nodes_from(all_users)

for name, group in bank_df.groupby("bank_account"):
    ids = group.userid.tolist()
    if len(ids) > 1:
        anchor = ids[0]
        rest = ids[1:]
        edges_to_add = [(anchor, other) for other in rest]
        graph.add_edges_from(edges_to_add)

for name, group in cc_df.groupby("credit_card"):
    ids = group.userid.tolist()
    if len(ids) > 1:
        anchor = ids[0]
        rest = ids[1:]
        edges_to_add = [(anchor, other) for other in rest]
        graph.add_edges_from(edges_to_add)

for name, group in device_df.groupby("device"):
    ids = group.userid.tolist()
    if len(ids) > 1:
        anchor = ids[0]
        rest = ids[1:]
        edges_to_add = [(anchor, other) for other in rest]
        graph.add_edges_from(edges_to_add)

fraud_dict = {}
for uuid, user_ids in enumerate(connected_components(graph)):
    for user_id in user_ids:
        fraud_dict[user_id] = uuid


def main_fn(order):
    uuid1 = fraud_dict.get(order.buyer_userid, None)
    uuid2 = fraud_dict.get(order.seller_userid, None)
    if uuid1 == uuid2:
        if uuid1 is None or uuid2 is None:
            return 0
        else:
            return 1
    else:
        return 0


order_df = read_csv("orders.csv", dtype = {"orderid": int, "buyer_userid": str, "seller_userid": str})
order_df["is_fraud"] = order_df.apply(main_fn, axis = 1)
order_df[["orderid", "is_fraud"]].to_csv("results2.csv", index = False)
print(order_df)
