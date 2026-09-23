STONE_TO_KG = 6.35029
POUND_TO_KG = 0.453592
KG_TO_STONE = 1 / STONE_TO_KG
INCH_TO_CM = 2.54


def stones_pounds_to_kg(stones, pounds):
    return stones * STONE_TO_KG + pounds * POUND_TO_KG


def kg_to_stones_pounds(kg):
    total_stones = kg * KG_TO_STONE
    stones = int(total_stones)
    pounds = (total_stones - stones) * 14
    return stones, pounds


def stones_pounds_to_kg_prompt():
    stones = float(input("Stones: "))
    pounds = float(input("Pounds: "))
    kg = stones_pounds_to_kg(stones, pounds)
    print(f"{stones} st {pounds} lb = {kg:.2f} kg")


def kg_to_stones_pounds_prompt():
    kg = float(input("Kilograms: "))
    stones, pounds = kg_to_stones_pounds(kg)
    print(f"{kg} kg = {stones} st {pounds:.2f} lb")


def stones_pounds_to_pounds(stones, pounds):
    return stones * 14 + pounds


def stones_pounds_to_pounds_prompt():
    stones = float(input("Stones: "))
    pounds = float(input("Pounds: "))
    total_pounds = stones_pounds_to_pounds(stones, pounds)
    print(f"{stones} st {pounds} lb = {total_pounds:.2f} lb")


def feet_inches_to_cm(feet, inches):
    return (feet * 12 + inches) * INCH_TO_CM


def feet_inches_to_cm_prompt():
    feet = float(input("Feet: "))
    inches = float(input("Inches: "))
    cm = feet_inches_to_cm(feet, inches)
    print(f"{feet} ft {inches} in = {cm:.2f} cm")


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_celsius_prompt():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} F = {celsius:.2f} C")


CONVERSIONS = {
    "1": ("Stones and pounds to kilograms", stones_pounds_to_kg_prompt),
    "2": ("Kilograms to stones and pounds", kg_to_stones_pounds_prompt),
    "3": ("Stones and pounds to pounds", stones_pounds_to_pounds_prompt),
    "4": ("Feet and inches to centimeters", feet_inches_to_cm_prompt),
    "5": ("Fahrenheit to Celsius", fahrenheit_to_celsius_prompt),
}


def main():
    print("Select a conversion:")
    for key, (label, _) in CONVERSIONS.items():
        print(f"{key}. {label}")
    choice = input("Choice: ").strip()

    conversion = CONVERSIONS.get(choice)
    if conversion is None:
        print("Invalid choice")
        return

    _, prompt_func = conversion
    prompt_func()


if __name__ == "__main__":
    main()
