import re

def find_and_save_strings(html_file, output_file):
    with open(html_file, 'r') as file:
        html_content = file.read()
        
        # Find all positions of substrings having the pattern "pathogenName"
        positions = [match.start() for match in re.finditer(r'pathogenName', html_content)]
        
        # Open output file in write mode
        with open(output_file, 'w') as output:
            # Extract the strings inside "> <" and "Tax ID: " that follow these positions
            for pos in positions:
                start = html_content.find('>', pos) + 1
                end = html_content.find('<', start)
                if start != -1 and end != -1:
                    string_inside_brackets = html_content[start:end].strip()
                    tax_id_start = html_content.find('Tax ID: ', end) + len('Tax ID: ')
                    tax_id_end = html_content.find('<', tax_id_start)
                    if tax_id_start != -1 and tax_id_end != -1:
                        tax_id_string = html_content[tax_id_start:tax_id_end].strip()
                        output.write(f"{string_inside_brackets}\t{tax_id_string}\n")

def main():
    # Path to the HTML file
    html_file = '/home/icaro/Desktop/Chan_Zuckerberg_ID_Detect_&_Track_Infectious_Diseases.html'
    # Path to the output text file
    output_file = '/home/icaro/Desktop/CZ_ID_pathogen_list_2024.tsv'
    
    find_and_save_strings(html_file, output_file)

if __name__ == "__main__":
    main()