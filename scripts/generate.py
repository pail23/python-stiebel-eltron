"""Generate python files to access the stiebel eltron heat pumps."""

from pathlib import Path
import csv

from jinja2 import Environment, FileSystemLoader, Template, select_autoescape


def python_name(name: str, suffix: str = "") -> str:
    """Generate a valid python variable name."""
    if suffix == "":
        result = name
    else:
        result = name + "_" + suffix
    return result.replace(" ", "_")


def python_class_name(name: str) -> str:
    """Generate a valid python variable name."""
    return name.replace(" ", "")


def float_or_none(value: str) -> float | None:
    """Calculate a float value or none."""
    if value == "":
        return None
    return float(value)


def get_base_address(registers: list) -> int:
    """Get the base address from a register block."""
    result = 35000
    for register in registers:
        result = min(result, int(register[0]))
    return result - 1


def generate_heatpump(
    root_path: Path, template: Template, modbus_files: dict, heatpump_type: str
):
    """Generate the python file for a heat pump."""
    register_blocks = []

    for name, modbus_file in modbus_files.items():
        with modbus_file.open("r") as f:
            reader = csv.reader(f)
            data = list(reader)

        api_data = data[1:]
        register_blocks.append(
            {
                "name": name,
                "count": len(api_data),
                "base_address": get_base_address(api_data),
                "register_block": api_data,
            }
        )

    generated_content = template.render(
        registers=register_blocks, heatpump_type=heatpump_type
    )

    generated_path = root_path / f"src/python_stiebel_eltron/{heatpump_type.lower()}.py"

    with generated_path.open("w") as f:
        f.write(generated_content)


def main() -> None:
    """Generate the python files."""
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

    wpm_template = env.get_template("wpmtemplate.jinja")
    wpm_modbus_files = {
        "System Values": root / "api/wpm_system_values.csv",
        "Energy System Information": root / "api/wpm_energy_system_information.csv",
    }
    generate_heatpump(root, wpm_template, wpm_modbus_files, "Wpm")

    lwz_template = env.get_template("lwztemplate.jinja")
    lwz_modbus_files = {
        "System Values": root / "api/lwz_system_values.csv",
    }
    generate_heatpump(root, lwz_template, lwz_modbus_files, "Lwz")


if __name__ == "__main__":
    main()
    print("Done!")
