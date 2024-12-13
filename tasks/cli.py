from .storage import add_task, remote_task, get_all_tasks, mark_task_completed
from .export import save_to_file


def handle_action():
   user_input = input(f'What action do you want to take?\n'
                      '1 - add task\n'
                      '2 - remove task\n'
                      '3 - mark as done\n'
                      '4 - show all tasks\n')
   match user_input:
       case '1':
           title = input('Enter title\n')
           add_task(title)
       case '2':
           print(get_all_tasks())
           index = int(input('Choose task to remove\n'))
           remote_task(index)
       case '3':
           print(get_all_tasks())
           index = int(input('Choose task to mark as done\n'))
           mark_task_completed(index, True)
       case '4':
           print(get_all_tasks())  
       case _:
           print('Try again')


def handle_interrupt():
   user_input = input(f'\nDo you want to export tasks (y/n): ')
   if user_input == 'y':
       save_to_file(get_all_tasks(), 'export')
       return True