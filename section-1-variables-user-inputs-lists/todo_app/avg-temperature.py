def calculate_avg_temp(datafile):
    with open(datafile, "r") as file:
        data = file.readlines()
    temperatures_str_list = data[1:]
    temperatures = [float(x) for x in temperatures_str_list]
    average = sum(temperatures) / len(temperatures)
    return average


avg = calculate_avg_temp("data.txt")
print(f"Average temperature is {avg}")