def pounds_to_kg(pounds):
    return pounds * 0.453592

def feet_to_cm(feet):
    return feet * 30.48

if __name__ == '__main__':
    weight_lbs = float(input("Enter weight in pounds (lbs): "))
    height_ft = float(input("Enter height in feet (ft): "))

    weight_kg = pounds_to_kg(weight_lbs)
    height_cm = feet_to_cm(height_ft)

    print(f"Weight in kilograms: {weight_kg:.2f} kg")
    print(f"Height in centimeters: {height_cm:.2f} cm")
