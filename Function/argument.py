# Area of Circle = PI*Radius*Radius
def Area(Radius,PI=3.14):
    print('Radius:',Radius)
    print('PI value:',PI)
    Result = PI*Radius*Radius
    return Result

def main():
    # positional arugment
    Output_01 = Area(10,12)
    print('Area of circle:',Output_01)
    #first arugument is positonal and second is default
    Output_01 = Area(10)
    print('Area of circle:',Output_01)

    #Keyword Arugument
    Output_02 = Area(PI=3,Radius=12)
    print('Area of circle:',Output_02)
    #keyword argument and second is default
    Output_02 = Area(Radius=12)
    print('Area of circle:',Output_02)

if __name__ == "__main__":
    main()