# To work with files & directory we can use the pathlib module
# **To be covered later**

from pathlib import Path

path = Path("packageex")
for file in path.glob("*.py"):
    print(file)