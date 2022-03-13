def run():
    #this is the way to add lists
    list_1 = [1, 2, 3, 4, 5]
    list_2 = ['a', '*', 3, 'hola']
    new_list = [list_1 + list_2]
    print(new_list)
    
    #this is the way to add dictionaries but consider when you use de same key the dictinary is not going to work, it'll give give you the second resul with the same key
    #example
    #dic_1 = {
    #    1:'llave 1', #here your are going to get an error 
    #    2:'llave 2', #just the second dic is goiing to work
    #    3:'llave 3'  #cause the firts one have the sema key.
    #}
    #dic_2 = {
    #    1:'a',
    #    2:'b',
    #    3:'c'
    #}
    dic_1 = {
        11:'llave 1',
        21:'llave 2',
        31:'llave 3'
    }
    dic_2 = {
        1:'a',
        2:'b',
        3:'c'
    }
    new_dict = dic_2 | dic_1
    print(new_dict)


if __name__ == '__main__':
    run()