#dictionary
thisdict = {
  "brand": "Ford",
  "model": "example",
  "year": 1964
}

print(thisdict)

#can we add
thisdict["color"]="pink"
#operaions in dictionaries
print(thisdict.keys())
print(thisdict.values())
print(thisdict.pop("year"))
print(thisdict.popitem())#it will remove last item in the dictinary
mydict=thisdict.copy()#copy form one dictionary to another dictionary
print(mydict)
