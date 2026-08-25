def gridTraveler(r,c,mapp):
    if (r,c) in mapp: return mapp[(r,c)]
    if r ==1 and c == 1: return 1
    if r<1 or c<1 : return 0
    down = gridTraveler(r-1,c,mapp)
    right = gridTraveler(r,c-1,mapp)
    mapp[(r,c)] = down+right
    mapp[(c,r)] = down + right
    return mapp[(r,c)]
print(gridTraveler(18,18,{}))