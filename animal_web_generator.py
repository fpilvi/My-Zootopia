import json


def load_data(file_path):
    """
    Loads data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: A list of dictionaries containing animal data.

    Raises:
        FileNotFoundError: If the file is not found.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    try:
        with open(file_path, "r") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON file.")
        raise


def generate_animal_info(data):
    """
    Generates an HTML string for animal information cards.

    Args:
        data (list): A list of dictionaries containing animal data.

    Returns:
        str: HTML content for the animal cards.
    """
    output = ''
    for animal in data:
        output += "<li class='cards__item'>\n"
        output += f"    <h2 class='card__title'>Name: {animal['name']}</h2>\n"
        if 'diet' in animal['characteristics']:
            output += f"    <p class='card__text'>Diet: {animal['characteristics']['diet']}</p>\n"
        if animal.get('locations'):
            output += f"    <p class='card__text'>Location: {animal['locations'][0]}</p>\n"  # First location
        if 'type' in animal['characteristics']:
            output += f"    <p class='card__text'>Type: {animal['characteristics']['type']}</p>\n"
        output += "</li>\n"
    return output


def generate_html(data_file, template_file, output_file):
    """
    Reads animal data and a template file to generate an HTML output file.

    Args:
        data_file (str): Path to the JSON data file.
        template_file (str): Path to the HTML template file.
        output_file (str): Path to the generated HTML output file.

    Raises:
        FileNotFoundError: If any input file is missing.
    """
    try:
        # Load the animal data
        animals_data = load_data(data_file)

        # Generate animal info HTML
        animal_info = generate_animal_info(animals_data)

        # Read the template file
        with open(template_file, 'r') as file:
            template_content = file.read()

        # Replace the placeholder with generated content
        final_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info)

        # Write to the output file
        with open(output_file, 'w') as file:
            file.write(final_content)

        print(f"HTML file successfully generated: {output_file}")

    except FileNotFoundError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
