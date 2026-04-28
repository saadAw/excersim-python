palette = [
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
]

restistances = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}


def resistor_label(colors):

    if len(colors) == 1:
        return "0 ohms"

    wert = 0

    if len(colors) == 4:
        wert = (
            palette.index(colors[0]) * 10 + palette.index(colors[1])
        ) * 10 ** palette.index(colors[2])

    if len(colors) == 5:
        wert = (
            palette.index(colors[0]) * 100
            + palette.index(colors[1]) * 10
            + palette.index(colors[2])
        ) * 10 ** palette.index(colors[3])

    einheiten = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    einheiten_index = 0

    while wert // 1000 > 0 and wert > 0:
        wert = wert / 1000
        einheiten_index += 1

    if wert%1 == 0:
        wert = int(wert)

    return f"{wert} {einheiten[einheiten_index]} ±{restistances[colors[-1]]}"
