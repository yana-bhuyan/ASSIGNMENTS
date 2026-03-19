try:
    # Writing city data
    with open("city.txt", "w") as f:
        f.write("Dehradun 5.78 308.20\n")
        f.write("Delhi 190 1484\n")
        f.write("Mumbai 124 603\n")
        f.write("Chandigarh 11 114\n")
        f.write("Jaipur 30 467\n")

    # Reading city data
    with open("city.txt", "r") as f:
        total_area = 0

        for line in f:
            city, pop, area = line.strip().split()
            pop = float(pop)
            area = float(area)

            print(f"{city} - Population: {pop} Lakhs, Area: {area}")

            if pop > 10:
                print(city, "has population > 10 lakhs")

            total_area += area

    print("Total Area:", total_area)

except Exception as e:
    print("Error:", e)