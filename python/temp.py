a1 = [1,1,1,1,1,1,1]
a2 = [2,2,2,2,2,2]
a3 = [3,3,3,6,9]
a4 = [a1,a2,a3]
gem = []
participated = []
for i,array in enumerate(a4):
    if i==0:
        for j, val in enumerate(a4[0]):
            gem.append(val)
            participated.append(1)
    else:
        for placevalue in range(len(array)):
            if i == 1:
                print(len(gem) - 1 - (len(array) - 1 -placevalue))
            gem[len(gem) - 1 - (len(array) - 1 -placevalue)] += array[placevalue]
            participated[len(gem) - 1 - (len(array) - 1 -placevalue)] = participated[len(gem) - 1 - (len(array) - 1 -placevalue)] + 1

for i in range(len(gem)):
    gem[i] = gem[i] / participated[i]