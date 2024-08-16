#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

server.indexed_dataset()

try:
    server.get_hyper_index('1', 100)
except AssertionError as e:
    print("AssertionError raised:", e)

try:
    server.get_hyper_index(-1, 100)
except AssertionError as e:
    print("AssertionError raised:", e)

try:
    server.get_hyper_index(100000, 100)
except AssertionError as e:
    print("AssertionError raised:", e)


index = 3
page_size = 2

print("Nb items:", len(server._Server__indexed_dataset))

# 1- request first index
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next index
print(server.get_hyper_index(res.get('next_index'), page_size))

# 3- remove the first index
del server._Server__indexed_dataset[res.get('index')]
print("Nb items:", len(server._Server__indexed_dataset))

# 4- request again the initial index -> the first data retreives is not the same as the first request
print(server.get_hyper_index(index, page_size))

# 5- request again initial next index -> same data page as the request 2-
print(server.get_hyper_index(res.get('next_index'), page_size))
