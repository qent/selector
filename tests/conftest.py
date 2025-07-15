import sys
from pathlib import Path

# Ensure package root is importable when tests are run without installation
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
