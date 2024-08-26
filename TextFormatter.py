import re
import os

def remove_newlines(input_text: str) -> str:
    # Regular expression pattern to match a newline not preceded by punctuation
    pattern = r"(?<![.!?;:-])\n"

    # Replace the matched newlines with a space
    result = re.sub(pattern, " ", input_text)

    return result

def combine_hyphenated_lines(input_text: str) -> str:
    # Regular expression pattern to match a line ending with a hyphen followed by a newline
    pattern = r"(\w+)-\n(\w+)"

    # Replace the matched hyphenated lines with combined words
    result = re.sub(pattern, r"\1\2", input_text)

    return result

def remove_divider_lines(input_text: str) -> str:
    # Regular expression pattern to match lines consisting of repeated characters or underscores
    pattern = r"^(?:[-=_*]{3,}|(?:\s*[-=_])+\s*)$\n?"

    # Replace the matched divider lines with an empty string
    result = re.sub(pattern, "", input_text, flags=re.MULTILINE)

    return result

def remove_consecutive_underscores(input_text: str) -> str:
    # Regular expression pattern to match consecutive underscores
    pattern = r"_+"

    # Replace the matched consecutive underscores with an empty string
    result = re.sub(pattern, "", input_text)

    return result

def clean_text_file(file_path: str) -> None:
    # Read the text from the file
    with open(file_path, "r") as file:
        text = file.read()

    # Clean the text
    cleaned_text = remove_newlines(text).strip()
    cleaned_text = combine_hyphenated_lines(cleaned_text).strip()
    cleaned_text = remove_divider_lines(cleaned_text).strip()
    cleaned_text = remove_consecutive_underscores(cleaned_text).strip()

    # Save the cleaned text to the same file
    with open(file_path, "w") as file:
        file.write(cleaned_text)

    print(f"Cleaned text saved to {file_path}")


for f in os.listdir('/home/darshewskijadmin@consilio.com/ExperimentalLLMs/NewPhi/'):
    file_path = '/home/darshewskijadmin@consilio.com/ExperimentalLLMs/NewPhi/' + f
    clean_text_file(file_path)