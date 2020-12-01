



def list_comp1(input_data):
    """
    make this into a list comprehension

    example:
    >> list_comp1([1,0,90,40])
    >> [0,0,1,1]
    """
    transformed_data = [0 if 0<=i<10 else 1 for i in input_data]

    
    return transformed_data

            