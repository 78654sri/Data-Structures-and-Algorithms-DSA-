def circle_passing(n):
    circle=set()
    member = 0
    count = 0

    while member not in circle:
        circle.add(member)
        count += 1
        member = (member + 2) % n

    if count == n:
        return True
    else:
        return False

result=circle_passing(5)
print(result)