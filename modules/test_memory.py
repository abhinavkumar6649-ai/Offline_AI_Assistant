import sys
import os

# Ensure modules can be imported directly or via package structure
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.memory import create_database, save_memory, get_memory

create_database()

save_memory(
    "name",
    "Abhinav"
)
name = get_memory("name")

print("My name is :", name)
