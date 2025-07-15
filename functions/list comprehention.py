#list Comprehension check "a" present within the list element
nm = ["anusha", "sanchayan", "parthib", "tanbi", "soumodip"]
newlist = [x for x in nm if "a" in x]
print(newlist)