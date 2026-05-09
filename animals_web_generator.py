import json
import os
import webbrowser


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def serialize_animal(animal):
    characteristics = animal.get("characteristics", {})

    name = animal.get("name")
    diet = characteristics.get("diet")
    locations = animal.get("locations")
    animal_type = characteristics.get("type")

    output = ""

    if name:
        output += f"<li class='cards__item'><div class='card__title'>{name}</div>"

    output += "<div class='card__text'>"

    if diet:
        output += f"Diet: {diet}<br>"

    if locations:
        output += f"Location: {' and '.join(locations)}<br>"

    if animal_type:
        output += f"Type: {animal_type}<br>"

    output += "</div></li>"

    return output


def build_output(data):
    return "".join(serialize_animal(animal) for animal in data)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    json_path = os.path.join(base_dir, "animals_data.json")
    template_path = os.path.join(base_dir, "animals_template.html")
    output_path = os.path.join(base_dir, "animals.html")

    data = load_data(json_path)

    animals_text = build_output(data)

    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_text)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(final_html)

    webbrowser.open(f"file://{output_path}")


if __name__ == "__main__":
    main()
