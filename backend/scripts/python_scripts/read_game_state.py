import zlib
from lua_to_json import convert_save_to_json


def read_save_file(filename, output_file):
    with open(filename, "rb") as f:
        compressed_data = f.read()

    decompressed = zlib.decompress(compressed_data, wbits=-zlib.MAX_WBITS)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(decompressed.decode("utf-8"))
        read_game_state(output_file)


def read_game_state(save_file_path: str) -> dict:
    return convert_save_to_json(save_file_path)


if __name__ == "__main__":
    # Example usage
    save_data = read_game_state("../save_state.lua")
    print(f"Current state: {save_data['STATE']}")


# def format_lua_table(text, indent_size=4):
#     # Remove 'return ' from the start if present
#     if text.startswith("return "):
#         text = text[7:]

#     depth = 0
#     formatted = []
#     current_line = ""
#     in_string = False
#     string_char = None

#     def add_line():
#         if current_line.strip():
#             formatted.append(" " * (depth * indent_size) + current_line.strip())

#     for char in text:
#         if char in "\"'":
#             if not in_string:
#                 in_string = True
#                 string_char = char
#             elif string_char == char:
#                 in_string = False
#             current_line += char
#         elif in_string:
#             current_line += char
#         elif char in "{[":
#             add_line()
#             if current_line.strip():
#                 formatted.append(
#                     " " * (depth * indent_size) + current_line.strip() + char
#                 )
#             else:
#                 formatted.append(" " * (depth * indent_size) + char)
#             depth += 1
#             current_line = ""
#         elif char in "}]":
#             add_line()
#             depth -= 1
#             current_line = char
#         elif char == ",":
#             current_line += char
#             add_line()
#             current_line = ""
#         elif char == "=":
#             current_line += " = "
#         else:
#             current_line += char

#     add_line()
#     return "\n".join(formatted)


# # Usage:
# def format_and_save(input_file, output_file):
#     with open(input_file, "r", encoding="utf-8") as f:
#         content = f.read()

#     # Format the content
#     formatted_content = format_lua_table(content)

#     # Write to new file
#     with open(output_file, "w", encoding="utf-8") as f:
#         f.write(formatted_content)


# # read_save_file(
# #     "../../../../../../c/Users/Maljik/AppData/Roaming/Balatro/1/save.jkr",
# #     "save_state.lua",
# # )


# Use it like this:
# format_and_save("save_state.txt", "formatted_save.txt")
