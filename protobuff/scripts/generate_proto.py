# protobuff/scripts/generate_proto.py
import subprocess
from pathlib import Path


def create_proto_files():
    # Get the project root directory
    project_root = Path(__file__).parent.parent.parent
    proto_dir = project_root / "proto"
    output_dir = project_root / "protobuff" / "generated"

    # Create the output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create __init__.py in the generated directory
    (output_dir / "__init__.py").touch()

    # Generate the protobuf files
    proto_files = list(proto_dir.glob("*.proto"))
    for proto_file in proto_files:
        cmd = [
            "protoc",
            f"--python_out={output_dir}",
            f"-I{proto_dir}",
            str(proto_file)
        ]
        subprocess.run(cmd, check=True)
        print(f"Generated Python code for {proto_file.name}")


if __name__ == "__main__":
    create_proto_files()