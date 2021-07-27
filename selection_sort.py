'''
概念: 反覆從未排序的數列中取出最小的元素
'''
if __name__=='__main__':
    # input_data = [55, 23, 87, 62, 16]
    input_data = [16, 25, 39, 27, 12, 8, 45, 63]
    print(f'original data: {input_data}')
    for i in range(0, len(input_data)):
        for j in range(i , len(input_data)):
            if input_data[i] > input_data[j]:
                input_data[i], input_data[j] = input_data[j], input_data[i]
        print(f' sort times: {i}, current list: {input_data}')
    print(f'ans is: {input_data}')