people_list = [[i for i in range(1,15)]]
def people(floor, hosu):

    if len(people_list) != floor+1:
        for chuga in range(len(people_list),floor+1):
            people_list.append([sum(people_list[chuga-1][:i]) for i in range(1,15)])

    return sum(people_list[floor-1][:hosu])
        

T = int(input())

for test_case in range(1,T+1):
    floor = int(input())
    hosu = int(input())
    print(people(floor , hosu))