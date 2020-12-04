import ast, re

with open("day4.txt") as f:
    passports = f.read().split("\n\n")

passports = [ast.literal_eval("{'" + x.replace("\n", " ").replace(" ", "', '").replace(":", "':'") + "'}") for x in passports]

# "cid" is optional
allFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

validPassports = 0
validFieldPassports = 0

for pasp in passports:
	if all(elem in pasp.keys() for elem in allFields):
		validPassports += 1
		if not (len(pasp["byr"]) == 4 and 2002 >= int(pasp["byr"]) >= 1920):
			continue
		if not (len(pasp["iyr"]) == 4 and 2020 >= int(pasp["iyr"]) >= 2010):
			continue
		if not (len(pasp["eyr"]) == 4 and 2030 >= int(pasp["eyr"]) >= 2020):
			continue
		if not re.search(r"^((?:1[5-8][0-9]|19[0-3]){1}cm|(?:59|6[0-9]|7[0-6]){1}in)$", pasp["hgt"]):
			continue
		if not re.search(r"^#(?:[0-9a-fA-F]{6})$", pasp["hcl"]):
			continue
		if not pasp["ecl"] in eyeColors:
			continue
		if not len(pasp["pid"]) == 9:
			continue

		validFieldPassports += 1

print("Valid passports: {}".format(validPassports))
print("Valid fields passports: {}".format(validFieldPassports))