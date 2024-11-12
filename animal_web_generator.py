import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_animal_info(data):
    output = ''
    for animal in data:
        output += f"<li class='cards__item'>\n"
        output += f"    <h2 class='card__title'>Name: {animal['name']}</h2>\n"
        if 'diet' in animal['characteristics']:
            output += f"    <p class='card__text'>Diet: {animal['characteristics']['diet']}</p>\n"
        if animal['locations']:
            output += f"    <p class='card__text'>Location: {animal['locations'][0]}</p>\n"  # Nur den ersten Standort
        if 'type' in animal['characteristics']:
            output += f"    <p class='card__text'>Type: {animal['characteristics']['type']}</p>\n"
        output += "</li>\n"
    return output


animals_data = load_data('animals_data.json')
animal_info = generate_animal_info(animals_data)

with open('animals_template.html', 'r') as file:
    template_content = file.read()

final_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info)

with open('animals.html', 'w') as file:
    file.write(final_content)

