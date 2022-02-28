import csv

# Read file
file = open("vi_data_autogc_1997_2019_region.csv", 'r')

groups = {} 

# Read in lines
print("reading...")
i = 0
c = 0
for line in file.readlines():
    print("reading line,", i, c)
    original = line
    line_data = line.split(",")
    site_code = line_data[0]
    compound = line_data[1]

    # Only allow certain compounds
    if compound == "\"43218\"" or compound == "\"45201\"":

        
        # Sort by group
        if site_code in groups:
            groups[site_code].append(original)
        else:
            groups[site_code] = [original]

        c += 1
    
    i += 1


# Write to files
for code, lines in groups.items():
    print("writing code", code)
    with open(code + ".csv", "w", newline="",) as out_file:
        out_file.writelines(lines)

