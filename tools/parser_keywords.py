from mylib.items import Keywords, db


file = open('C:/Users/Administrator/Desktop/jiaju.txt', 'r', encoding='utf-8')

arg = []
for line in file:
    temp_array = line.strip().split('    ')
    if len(temp_array) < 6:
        continue
    data = {
        'keyword': temp_array[0],
        'type': 'child',
        'pc_index': temp_array[2],
        'bd_index': temp_array[3],
        'pc_search': temp_array[4],
        'bd_search': temp_array[5],
        'bd_site': temp_array[6],
        'opt_index': temp_array[7],
    }
    arg.append(data)
    print(data)
    if len(arg) == 10:
        try:
            with db.atomic():
                Keywords.replace_many(arg).execute()
                # print(arg)
        except Exception as e:
            print(e)
            continue
        arg = []
        print('-------------------------')

try:
    with db.atomic():
        Keywords.replace_many(arg).execute()
        # print(arg)
except Exception as e:
    print(e)
print('all done')
