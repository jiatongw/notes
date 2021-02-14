
input = [
    "1, Laozhang, 0", 
    "2, Zhangsan, 1",
    "3, Lisi, 1",
    "4, Wangwu, 2",
    "5, Xiaoliu, 2",
    "6, GeBiLaoWang, 3",
    ]

def main(input):
    order_map={}
    level_map={}

    for item in input:
        item_list=item.split(",")
        # {'Laozhang': '1', 'Zhangsan': '2', 'Lisi': '3', 'Wangwu': '4', 'Xiaoliu': '5', 'GeBiLaoWang': '6'}
        order_map[item_list[1].strip()] = item_list[0].strip()

        # {'Laozhang': '0', 'Zhangsan': '1', 'Lisi': '1', 'Wangwu': '2', 'Xiaoliu': '2', 'GeBiLaoWang': '3'}
        level_map[item_list[1].strip()] = item_list[2].strip()
    relation_map={}

    for i in order_map:
        for j in level_map:
            if level_map[j] == order_map[i]:
                if i not in relation_map:
                    relation_map[i] = [j]
                else:
                    relation_map[i].append(j)
                    
    # {'Laozhang': ['Zhangsan', 'Lisi'], 'Zhangsan': ['Wangwu', 'Xiaoliu'], 'Lisi': ['GeBiLaoWang']}
    ceo = ""

    for i in level_map:
        if level_map[i] == "0":
            ceo = i
    dfs(relation_map, ceo, 0)


def dfs(relation_map, name, count):
    print(count * "\t" + name)
    for next_name in relation_map[name]:
        if next_name in relation_map:
            dfs(relation_map, next_name, count+1)
        else:
            print((count+1) * "\t"+next_name)

if __name__ == '__main__':
    main(input)

