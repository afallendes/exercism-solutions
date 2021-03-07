def value(colors) -> int:
    return int(''.join([ str(value_single(_)) for _ in colors[:2] ]))

def value_single(color:str) -> int:
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ].index(color)
