import zlib
from lua_to_json import convert_save_to_json


def read_meta_file(filename, output_file):
    with open(filename, "rb") as f:
        compressed_data = f.read()

    decompressed = zlib.decompress(compressed_data, wbits=-zlib.MAX_WBITS)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(decompressed.decode("utf-8"))
        read_meta_state(output_file)


def read_meta_state(save_file_path: str) -> dict:
    return convert_save_to_json(save_file_path)


if __name__ == "__main__":
    # Example usage
    read_meta_file(
        "/mnt/c/Users/Maljik/AppData/Roaming/Balatro/settings.jkr",
        "../save_states/meta_state.lua",
    )
    # meta_data = read_meta_state("../meta_state.lua")
    # print(f"Current meta: {meta_data}")
