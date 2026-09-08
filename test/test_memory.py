import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from modules.memory import *

create_database()

save_memory("name", "Abhinav")

print("My name is:", get_memory("name"))