# Write Python programs to perform operations on dictionaries and sets, including 
# sorting, merging, frequency counting, and identifying common or unique elements.

keys = input("Enter Keys : ").split()
values = list(map(int, input("Enter Values : ").split()))
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print("\nDictionary : ", d)
values_list = list(d.values())
values_list.sort()
sorted_d = {}
for i in values_list:
    for k in d:
        if d[k] == i and k not in sorted_d:
            sorted_d[k] = d[k]
print("\nSorted Dictionary : ", sorted_d)

keys2 = input("\nEnter Keys for second dictionary : ").split()
values2 = list(map(int, input("Enter Values for second dictionary : ").split()))
d2 = {}
for i in range(len(keys2)):
    d2[keys2[i]] = values2[i]
merged = d.copy()
merged.update(d2)
print("Merged Dictionary : ", merged)

text = input("\nEnter a word : ")
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("Frequency Count : ", freq)

set1 = set(map(int, input("\nEnter elements for first set : ").split()))
set2 = set(map(int, input("Enter elements for second set : ").split()))
print("Common Elements : ", set1.intersection(set2))
print("Unique Elements : ", set1.difference(set2))