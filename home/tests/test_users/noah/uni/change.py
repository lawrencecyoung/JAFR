tasks_file = open('original_tasks.md', "r")
tasks_content = tasks_file.read()
search = f"25"
replacement = f"27"
tasks_content = tasks_content.replace(search, replacement)
tasks_file = open('original_tasks.md', "w")
tasks_file.write(tasks_content)
