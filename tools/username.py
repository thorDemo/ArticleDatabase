from mylib.items import UserName


# usernames = UserName.select(UserName.name).order_by(UserName.id).limit(20)

# for it in usernames:
#     print(it.name)

file1 = open('C:/Users/Administrator/Desktop/username.txt', 'r', encoding='utf-8')
temp = ''
for line in file1:
    if 'person' in line:
        temp = line.strip()
    else:
        temp += line.strip()

    print(temp)
