# C-R-U-D
# C-Create, R-Read, U-update, D-Delete

task_table = """CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL, 
        completed INTEGER DEFAULT 0
     )
"""

# Create - Создание записи
insert_task = 'INSERT INTO tasks (task) VALUES (?)'


# Read - Просмотр записи
select_task = 'SELECT id, task, completed FROM tasks'

select_task_completed = 'SELECT id, task, completed FROM tasks WHERE completed = 1'

select_task_uncompleted = 'SELECT id, task, completed FROM tasks WHERE completed = 0'


# Update - Обновление записи
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'

# Delete - Удаление записи
delete_task = 'DELETE FROM tasks WHERE id = ?'
