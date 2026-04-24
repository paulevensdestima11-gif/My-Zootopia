import json
import os
import webbrowser


def load_data(file_path):
    """Load JSON data from file"""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def serialize_animal(animal):
    """Convert one animal into required text format"""

    characteristics = animal.get("characteristics", {})

    name = animal.get("name")
    diet = characteristics.get("diet")
    locations = animal.get("locations")
    animal_type = characteristics.get("type")

    output = ""

    # First line: name only (NO "Name:")
    if name:
        output += f"{name}\n"

    # Required fields
    if diet:
        output += f"Diet: {diet}\n"

    if locations:
        output += f"Location: {' and '.join(locations)}\n"

    if animal_type:
        output += f"Type: {animal_type}\n"

    output += "\n"

    return output


def build_output(data):
    """Build full output for all animals"""
    return "".join(serialize_animal(animal) for animal in data)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    json_path = os.path.join(base_dir, "animals_data.json")
    template_path = os.path.join(base_dir, "animals_template.html")
    output_path = os.path.join(base_dir, "animals.html")

    # Load JSON data
    data = load_data(json_path)

    # Build formatted text
    animals_text = build_output(data)

    # Load HTML template
    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    # Replace placeholder
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_text)

    # Debug (optional, can remove later)
    print(final_html[:300])

    # Write final HTML file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(final_html)

    print("Generated:", output_path)

    # Open in browser
    webbrowser.open(f"file://{output_path}")


if __name__ == "__main__":
    main()