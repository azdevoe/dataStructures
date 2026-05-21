def findPath(tree,target):
    if tree["val"]==target:
        return [tree["val"]]
    if len(tree["children"]) ==0:
        return []
    for node in tree["children"]:
        path =findPath(node,target)
        if path:
            return [tree['val']] + path
    return []

tree = {
    "val": 1,
    "children": [
        {"val": 2, "children": [
            {"val": 4, "children": []},
            {"val": 5, "children": []}
        ]},
        {"val": 3, "children": [
            {"val": 6, "children": []}
        ]}
    ]
}

print(findPath(tree, 5))
print(findPath(tree, 6))
print(findPath(tree, 9))