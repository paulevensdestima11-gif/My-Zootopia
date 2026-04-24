import json
import os
import webbrowser


def load_data(file_path):
    """Load JSON data from file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def build_html(animals_data):
    """Generate HTML list items from JSON"""
    output = ""

    for animal in animals_data:
        name = animal.get("name")
        characteristics = animal.get("characteristics", {})

        diet = characteristics.get("diet")
        animal_type = characteristics.get("type")
        locations = animal.get("locations")

        output += '<li class="cards__item">\n'

        # Title
        if name:
            output += f'  <div class="card__title">{name}</div>\n'

        # Text block
        output += '  <p class="card__text">\n'

        if diet:
            output += f'      <strong>Diet:</strong> {diet}<br/>\n'

        if locations:
            location_text = " and ".join(locations)
            output += f'      <strong>Location:</strong> {location_text}<br/>\n'

        if animal_type:
            output += f'      <strong>Type:</strong> {animal_type.capitalize()}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

    return output


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # File paths (robust, no guessing)
    json_path = os.path.join(base_dir, "animals_data.json")
    template_path = os.path.join(base_dir, "animals_template.html")
    output_path = os.path.join(base_dir, "animals.html")

    # Load data
    animals_data = load_data(json_path)

    # Generate HTML
    cards_html = build_html(animals_data)

    # Load template
    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    # Inject content
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", cards_html)

    # Write final HTML
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(final_html)

    print("HTML generated successfully:", output_path)

    # Open in browser
    webbrowser.open(f"file://{output_path}")


if __name__ == "__main__":
    main()