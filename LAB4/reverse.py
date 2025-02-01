def reverse_file_content(input_file, output_file):
    try:
        # Open the input file and read its content
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Reverse the content
        reversed_content = content[::-1]

        # Write the reversed content to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(reversed_content)

        print(f"Reversed content has been saved to {output_file}")
    
    except FileNotFoundError:
        print("Error: The input file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_filename = "input.txt"
output_filename = "output.txt"

reverse_file_content(input_filename, output_filename)
