from pathlib import Path

puzzle_input_file_path = Path(__file__).with_name('example.txt')
#puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines() #can stay string 
puzzle_input_file.close()

times = puzzle_input[0].split(':')[1].split()
times = list(map(int, times))

distances = puzzle_input[1].split(':')[1].split()
distances = list(map(int, distances))

ways=[]

for i in range(len(times)):
    ways.append(0)

#attempt at binary search
# #low = 1 high = time?
# for i in range(len(times)):
#     low = 1
#     high = times[i]
#     while low <= high:
#         mid = (low + high) // 2
#         if ((times[i] - low) * low) > distances[i]:
#             # print(low)
#             ways[i]+=1
#             low+=1
#         elif (((times[i] - high) * high) < distances[i]) or ((times[i] - low) * low) > distances[i]:
#             high = mid -1 
#         elif ((times[i] - low) * low) <= distances[i]:
#             print(low)
#             low+=1

#         # elif ((times[i] - low) * low) == distances[i]:
#         #      low = mid +1 
#     print('dddddddddddddddddddddddddddddd')

for i in range(len(times)):
    ways.append(0)

for i in range(len(times)):
    for j in range(1,times[i]+1):
        if (times[i] - j) * j > distances[i]:
            ways[i]+=1
        
product = 1

for way in ways:
    product*=way
print(ways)

