if __name__ == '__main__':
    # input_data = [55, 23, 87, 62, 16]
    input_data = [16, 25, 39, 27, 12, 8, 45, 63]
    print(f'original data: {input_data}')
    for i in range(len(input_data), -1, -1):
        for j in range(i):
            if j +1 < len(input_data) and input_data[j] > input_data[j+1]: 
                # switch
                input_data[j], input_data[j+1] = input_data[j+1], input_data[j]
        print(f'sort times: {len(input_data)-i}, value turns to: {input_data}')