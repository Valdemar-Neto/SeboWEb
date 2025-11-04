import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))  # Adiciona a raiz do projeto

from app.main import app
import json

with open("docs/openapi.json", "w", encoding="utf-8") as f:
    json.dump(app.openapi(), f, indent=2, ensure_ascii=False)

