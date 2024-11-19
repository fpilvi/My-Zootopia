# main.py
from animal_web_generator import generate_animal_info, load_data

def main():
    # Datei laden
    data = load_data('animals_data.json')
    # HTML-Content generieren
    animal_info = generate_animal_info(data)
    # Template lesen und ersetzen
    with open('animals_template.html', 'r') as template_file:
        template = template_file.read()
    final_content = template.replace('__REPLACE_ANIMALS_INFO__', animal_info)
    # Ausgabe schreiben
    with open('animals.html', 'w') as output_file:
        output_file.write(final_content)
    print("HTML-Datei erfolgreich erstellt!")

if __name__ == "__main__":
    main()