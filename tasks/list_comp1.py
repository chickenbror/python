



def list_comp1(input_data):
    """
    make this into a list comprehension

    example:
    >> list_comp1([1,0,90,40])
    >> [0,0,1,1]
    """
    transformed_data = [0 if 0<=i<10 else 1 for i in input_data]

    # for i in input_data:

    #     if i >= 0:  #Append nothing if i<0

    #         if i < 10:
    #             transformed_data.append(0) #If 0<=i<10
    #         else:
    #             transformed_data.append(1) #If i>10
    
    return transformed_data

if __name__ == "__main__":
    
    print(list_comp1([1,0,90,40,-1]))
