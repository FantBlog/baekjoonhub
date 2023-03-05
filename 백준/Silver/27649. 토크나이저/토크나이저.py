arr = list(input().replace('<',' < ')\
    .replace('>',' > ')\
    .replace('&&',' && ')\
    .replace('||',' || ')\
    .replace('(',' ( ')\
    .replace(')',' ) ').split())
print(*arr)