import re


def extract_jokers_list(content):
    # Find the jokers list in the content
    jokers_match = re.search(r"jokers\s*=\s*\[(.*?)\]", content, re.DOTALL)
    if not jokers_match:
        raise ValueError("Could not find jokers list in file")
    return jokers_match.group(0), jokers_match.group(1)


def extract_name(joker_str):
    # Using a simple regex to find content between name=" and the next "
    match = re.search(r'name="([^"]+)"', joker_str)
    return match.group(1) if match else ""


def sort_jokers(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    # Get the full jokers list and its content
    full_list, jokers_content = extract_jokers_list(content)

    # Split into individual Joker entries
    jokers = []
    current_joker = []
    for line in jokers_content.split("\n"):
        if line.strip().startswith("Joker("):
            if current_joker:
                jokers.append("\n".join(current_joker))
            current_joker = [line]
        elif line.strip():
            current_joker.append(line)
    if current_joker:
        jokers.append("\n".join(current_joker))

    # Sort by name
    sorted_jokers = sorted(jokers, key=extract_name)

    # Create new content
    new_list = "jokers = [\n" + ",\n".join(sorted_jokers) + "\n]"

    # Replace in original content
    new_content = content.replace(full_list, new_list)

    with open(file_path, "w") as f:
        f.write(new_content)


if __name__ == "__main__":
    file_path = "../../app/seed/joker_list.py"  # Replace with your file path
    sort_jokers(file_path)
