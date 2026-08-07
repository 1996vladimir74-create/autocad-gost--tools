SCALES = [

    "1:1",
    "2:1",
    "5:1",
    "10:1",

    "1:2",
    "1:5",
    "1:10",
    "1:20",
    "1:50"

]


def get_scale(scale):

    if scale in SCALES:

        return scale


    return "1:1"