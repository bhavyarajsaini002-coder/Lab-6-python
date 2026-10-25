n = int(input())

winning_distance = -1
runner_up_distance = -1

for i in range(n):
    distance = int(input())

    if distance > winning_distance:
        runner_up_distance = winning_distance
        winning_distance = distance

    elif distance > runner_up_distance and distance != winning_distance:
        runner_up_distance = distance

print(winning_distance)
print(runner_up_distance)