#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p python3Packages.aocd

print([sum(sorted([(sum([int(f) for f in n.split("\n") if f != ""])) for n in __import__("aocd").get_data(day=1, year=2022).split("\n\n")])[::-1][:version]) for version in [1, 3]])
