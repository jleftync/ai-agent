import os
from config import MAX_CHARS
from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")
print(result)
result=get_file_content("calculator", "main.py")
print(f"main.py length: {len(result)}")
print(f"main.py truncated: {'truncated' in result}")
print(result)
result=get_file_content("calculator", "pkg/calculator.py")
print(f"pkg/calculator.py length: {len(result)}")
print(f"pkg/calculator.py truncated: {'truncated' in result}")
print(result)
result=get_file_content("calculator", "/bin/cat") #(this should return an error string)
print(f"/bin/cat length: {len(result)}")
print(f"/bin/cat truncated: {'truncated' in result}")
print(result)
result=get_file_content("calculator", "pkg/does_not_exist.py") #(this should return an error string)
print(f"pkg/does_not_exist.py length: {len(result)}")
print(f"pkg/does_not_exist.py truncated: {'truncated' in result}")
print(result)
