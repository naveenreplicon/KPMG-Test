#!/usr/bin/python3

users = [{"name": "john", "age": "27"}, {"name": "meg", "age": "23"}]
print(' '.join(x["age"] for x in users))