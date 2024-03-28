from pathlib import Path
import json
import yaml


def cleanup() -> None:
    """
    Clean up the generated templates.

    This function removes files that are not needed based on the Copier config file, and
    regularizes JSON files.
    """
    print("Cleaning up the generated templates...")

    # read the Copier config file
    copier_config = _get_copier_config()
    algorithm_name = copier_config.get("algorithm_name")

    # Remove license if no license is needed
    if (
        Path("LICENSE").exists()
        and copier_config.get("open_source_license") == "no_license"
    ):
        print("Removing LICENSE file as no license was chosen...")
        Path("LICENSE").unlink()

    # Remove partial function files if partial function is not defined
    if not copier_config.get("has_partial_function"):
        print("Removing partial function file as partial function is not defined...")
        Path(algorithm_name, "partial.py").unlink()

    # Remove central function files if central function is not defined
    if not copier_config.get("has_central_function"):
        print("Removing central function file as central function is not defined...")
        Path(algorithm_name, "central.py").unlink()

    # Ensure JSON files are regularized
    JSON_FILES = ["algorithm_store.json"]
    for json_file in JSON_FILES:
        _regularize_json_file(json_file)

    # Remove this file from the generated template
    print("Removing cleanup.py file...")
    Path("cleanup.py").unlink()


def _get_copier_config() -> dict:
    """
    Read the Copier config file and return the config as a dictionary.
    """
    try:
        with open(".copier-answers.yml", "r") as file:
            copier_config = yaml.safe_load(file)
    except FileNotFoundError:
        print("No Copier config file found. Exiting...")
        return
    except Exception as e:
        print(f"Error reading Copier config file: {e}")
        return

    return copier_config


def _regularize_json_file(json_file: str) -> None:
    """
    Regularize the JSON file by sorting the keys and formatting the file.

    Args:
        json_file (Path): Path to the JSON file.
    """
    print(f"Regularizing JSON file {json_file} spacing...")
    try:
        with open(json_file, "r") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"File {json_file} not found. Exiting...")
        return
    except Exception as e:
        print(f"Error reading file {json_file}: {e}")
        return

    try:
        with open(json_file, "w") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        print(f"Error writing to file {json_file}: {e}")
        return


if __name__ == "__main__":
    cleanup()
    # print empty line to separate output of this script to the output of the rest of
    # the copier process
    print()
