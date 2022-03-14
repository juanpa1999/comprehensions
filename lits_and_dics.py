def run():
    
    list_inside_dic = [
        {"1": "a"},
        {"2": "b"},
        {"3": "c"},
        {"4": "d"}
    ]
    dic_inside_list = {
        "number": [26, 27, 28, 29],
        "digist": ["*", "/", "-"]
    }

    for value in list_inside_dic:
        print(value)



if __name__ == '__main__':
    run()