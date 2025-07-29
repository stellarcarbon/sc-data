import sys
from pathlib import Path

template_path = Path(sys.argv[1])
output_path = Path(sys.argv[2])
variables = dict(arg.split("=", 1) for arg in sys.argv[3:])

template = template_path.read_text()
output = template.format(**variables)
output_path.write_text(output)
