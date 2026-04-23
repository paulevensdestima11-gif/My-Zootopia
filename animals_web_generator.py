import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

# 1. Load JSON data
animals_data = load_data("animals_data.json")

# 2. Build HTML output
output = ""

for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations")
    animal_type = animal.get("type")

    output += '<li class="cards__item">\n'

    if name:
        output += f"Name: {name}<br/>\n"
    if diet:
        output += f"Diet: {diet}<br/>\n"
    if locations and len(locations) > 0:
        output += f"Location: {locations[0]}<br/>\n"
    if animal_type:
        output += f"Type: {animal_type}<br/>\n"

    output += '</li>\n'

# 3. Load HTML template
with open("animals_template.html", "r", encoding="utf-8") as file:
    template = file.read()

# 4. Inject generated HTML into template
new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

# 5. Write final HTML file
with open("animals.html", "w", encoding="utf-8") as file:
    file.write(new_html)