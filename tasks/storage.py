from typing import List, Tuple


_DB = []


#[{'title': 'TODO1', 'completed': True}]


def add_task(title: str) -> None:
  _DB.append({
     'title': title,
     'completed': False
  })


def remote_task(index:int) -> None:
  _DB.pop(index)


def mark_task_completed(index:int, completed: bool) -> None:
  _DB[index]['completed'] = completed


def get_all_tasks() -> List[Tuple[int, str, bool]]:
  return [(i, task['title'], task['completed']) for i, task in enumerate(_DB)]