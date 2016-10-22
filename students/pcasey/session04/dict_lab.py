#!/usr/bin/env python3

if __name__ == "__main__":

    lab = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

    print(lab)

    lab.pop("cake")

    print(lab)

    lab["fruit"] = "Mango"

    print(lab)

    print(lab.keys())

    print(lab.values())

    print("cake" in lab)

    print("Mango" in lab.values())

    lab = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

    for k, v in lab.items():
        newlab = {}
        newlab[k] = v.count("t")

    print(newlab)
