''' 
You are given a list of rectangles represented by min and max x and y coordinates. 
Compute whether or not a pair of rectangles overlap each other. If one rectangle completely cover another. 
it is considered overlapping

Example:

{
    "top_left" : (1, 4), 
    "dimensions" : (3, 3) # width , height 
}, 
{
    "top_left" : (-1, 3), 
    "dimensions" : (2, 1)
}, 
{
    "top_left" : (0, 5), 
    "dimensions" : (4, 3)
}
it returns True, because the first and the third angle overlap 
'''

dict1 = {"top_left": (1, 4), "dimensions": (3, 3)}
dict2 = {"top_left": (-1, 3), "dimensions": (2, 1)}
dict3 = {"top_left": (0, 5), "dimensions": (4, 3)}

'''
Calculate through the list of rectangle one by one to get the coordinates (TL and BR) of the rectangle.
To check if the rectangle overlap:
    - Two rectangles overlap if and only if one rectangle TL corner is to the left of the other rectangle BR corner(x-axis) AND
        one rectangle's TL corner is above the other rectangle BR corner (y-axis)
If any pair of the rectangle satisfies the conditions above return true, else false.
'''

def is_overlapping(rectangles):
    def check_overlap(rect1, rect2):
        rect1_tl = (rect1["top_left"][0], rect1["top_left"][1])
        rect1_br = (rect1["top_left"][0] + rect1["dimensions"][0], rect1["top_left"][1] - rect1["dimensions"][1])
        rect2_tl = (rect2["top_left"][0], rect2["top_left"][1])
        rect2_br = (rect2["top_left"][0] + rect2["dimensions"][0], rect2["top_left"][1] - rect2["dimensions"][1])

        x_overlap = not (rect1_br[0] < rect2_tl[0] or rect2_br[0] < rect1_tl[0])
        y_overlap = not (rect1_br[1] > rect2_tl[1] or rect2_br[1] > rect1_tl[1])

        return x_overlap and y_overlap

    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if check_overlap(rectangles[i], rectangles[j]):
                return True

    return False

# Example usage
rectangles = [
    {
        "top_left": (1, 4),
        "dimensions": (3, 3)
    },
    {
        "top_left": (-1, 3),
        "dimensions": (2, 1)
    },
    {
        "top_left": (0, 5),
        "dimensions": (4, 3)
    }
]

result = is_overlapping(rectangles)
print(result)

