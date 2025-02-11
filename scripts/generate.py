from pathlib import Path
import csv

from jinja2 import Environment, FileSystemLoader, select_autoescape


def python_name(name: str) -> str:
    """Generate a valid python variable name."""
    return name.replace(" ", "_")


def python_class_name(name: str) -> str:
    """Generate a valid python variable name."""
    return name.replace(" ", "")


def float_or_none(value: str) -> float | None:
    """Calculate a float value or none."""
    if value == "":
        return None
    return float(value)


root = Path.cwd()
scripts_path = Path(__file__).parent

env = Environment(
    loader=FileSystemLoader(str(scripts_path / "templates")),
    autoescape=select_autoescape(),
)
env.globals.update(
    python_name=python_name,
    python_class_name=python_class_name,
    float_or_none=float_or_none,
)
template = env.get_template("wpmtemplate.jinja")

modbus_files = {
    "System Values": root / "api/wpm_system_values.csv",
    "Energy System Information": root / "api/wpm_energy_system_information.csv",
}

register_blocks = {}

for name, modbus_file in modbus_files.items():
    with modbus_file.open("r") as f:
        reader = csv.reader(f)
        data = list(reader)

    api_data = data[1:]
    register_blocks[name] = api_data


generated_content = template.render(registers=register_blocks, heatpump_type="Wpm")

generated_path = root / "src/python_stiebel_eltron/wpm.py"

with generated_path.open("w") as f:
    f.write(generated_content)

print("Done!")
