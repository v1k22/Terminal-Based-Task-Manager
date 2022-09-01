import pickle
import os
import glob
from pathlib import Path
from const import *
from cal import *

data = {}
tasks = {}

def err(msg):
    print (msg)
    exit()

def load_data():
    global data

    if os.path.isfile('/etc/bd/data.pickle'):
        with open('/etc/bd/data.pickle', 'rb') as handle:
            data = pickle.load(handle)

def get_space_n(*arg):
    N = len(arg)
    L = 0
    for i in range(N):
        L += len(arg[i])
    return L * ' '

def save_data():
    global data

    with open('/etc/bd/data.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def delete_data():
    global data

    data = {}
    save_data()

    print ('\nAll Tasks are deleted!\n')

    files = glob.glob('/etc/bd/*')
    for f in files:
        os.remove(f)

def get_task_id():
    global data

    total_tasks = 0
    for title, list_of_tasks in data.items():
        if len(list_of_tasks) >= 1:
            total_tasks += len(list_of_tasks)

    return str(total_tasks + 1)

def add_task(task_details):
    global data
    load_data()

    __task = task_details.split('@')
    if len(__task) > 3: err('require 3 arguments')

    if len(__task) != 3:
        err('pending to handle this case')
        pass

    total_tasks = len(data.keys())

    task = {}
    task['des'] = __task[0].rstrip().lstrip()
    task['due_date'] = __task[2].rstrip().lstrip()
    task['remaining_time'] = get_remaining_time(task['due_date'])
    task['parent_task'] = title = __task[1].rstrip().lstrip()
    task['id'] = get_task_id()
    task['status'] = check_box
    task['note_status'] = False

    print ('Task Title = ', task['parent_task'])
    print ('Task des = ', task['des'])
    print ('Task due date = ', task['due_date'])
    print ('Task id = ', task['id'])
    print ('Tasked Saved!!')


    if title in data.keys():
        data[title].append(task)
    else: 
        print ('adding new title')
        data[title] = []
        data[title].append(task)

    save_data()

def work_week():
    year, week, day = get_work_week()
    print ('WW = ', str(week) + '.' + str(day))

def mark(N, status):
    global data
    load_data()

    sym = check_box
    if status == 'c': sym = green_tick
    elif status == 'f': sym = red_cross
    elif status == 'u': sym = question_mark
    elif status == 'r': sym = running

    found = False
    for title, list_of_tasks in data.items():
        for task in list_of_tasks:
            if task['id'] == N:
                task['status'] = sym
                found = True

    if not found: print ('Task does not exists')
    else: print ('Status updated')
    
    save_data()

def delete_task(N):
    global data
    load_data()

    found = False
    for title, list_of_tasks in data.items():
        task_num = 0
        for task in list_of_tasks:
            if task['id'] == N:
                del list_of_tasks[task_num]
                found = True
            task_num += 1

    if not found: print ('Task does not exists')
    else: print ('Status updated')
    
    save_data()

def task_summary():
    global data
    load_data()

    total_tasks = 0
    total_completed_tasks = 0
    for title, list_of_tasks in data.items():
        if len(list_of_tasks) >= 1:
            total_tasks += len(list_of_tasks)
            for task in list_of_tasks:
                if task['status'] == green_tick:
                    total_completed_tasks += 1

    year, week, day = get_work_week()
    result = str(total_completed_tasks) + '/' + str(total_tasks) + ' ' + str(week) + '.' + str(day)
    print (result, end = '')

def add_notes(N):
    global data
    load_data()

    found = False
    # get task id
    for title, list_of_tasks in data.items():
        if len(list_of_tasks) > 0:
            for task in list_of_tasks:
                if str(task['id']) == str(N):
                    found = True

    if not found:
        print ('Invalid Task id')
        exit()

    # check directory
    if Path('/etc/bd').is_dir():
        print ('exists')
    else:
        print ('doesnt exits')
        print ('creating dir')
        Path("/etc/bd").mkdir(parents=True, exist_ok=True)

    # check if notes file exists
    command = 'vi /etc/bd/' + str(N)
    os.system(command)

    sz = os.stat('/etc/bd/' + str(N)).st_size

    for title, list_of_tasks in data.items():
        if len(list_of_tasks) > 0:
            for task in list_of_tasks:
                if str(task['id']) == str(N):
                    task['note_status'] = True
                    break

    save_data()

def add_show_notes(N):

    # check directory
    if Path('/etc/bd').is_dir():
        pass
    else:
        print ('doesnt exits bd directory')
        print ('creating dir')
        Path("/etc/bd").mkdir(parents=True, exist_ok=True)

    # check if notes file exists
    file_path = '/etc/bd/' + str(N)
    if Path(file_path).is_file():
        with open(file_path, 'r') as f:
            print(f.read())
    else:
        print ('No file/notes available')

def complete_status():
    global data
    load_data()

    total_tasks = 0
    completed_tasks = 0
    for title, list_of_tasks in data.items():
        if len(list_of_tasks) > 0:
            total_tasks += len(list_of_tasks)
            for task in list_of_tasks:
                if task['status'] == green_tick:
                    completed_tasks += 1
    
    comp_per = (100 * completed_tasks) / total_tasks
    return int(comp_per)

def display():

    global data
    load_data()

    work_week()

    total_titles = len(data.keys())

    if total_titles == 0:
        print ('0 tasks available! ')
        return 

    current_title = 1
    print (vir_line)
    for title, list_of_tasks in data.items():
        print (BOLD + OKGREEN + inside_string, title, ENDC)
        print (OKCYAN + vir_line, '\t', inside_string , 'Time Left  Due Date   Status     Task', ENDC)

        for task in list_of_tasks:
            task_des = task['des']
            due_date = task['due_date']
            task_id = task['id']
            status = task['status']
            rem_time = task['remaining_time']
            note_status = ''
            if task['note_status']: note_status = '*'

            if float(rem_time) < 0.5:
                print (FAIL + vir_line, '\t', inside_string, '[', rem_time , ']', '  ' , due_date , '\t   ' , status, '\t\t' , task_id, note_status , task_des, ENDC)
            else:
                print (vir_line, '\t', inside_string, '[', rem_time , ']', '  ' , due_date , '\t   ' , status, '\t\t' , task_id, note_status , task_des)

    comp_per = complete_status()
    end_str = end_line + ' ['
    for i in range(50):
        if i < (comp_per // 2):
            end_str += bar
        else:
            end_str += '-'
    
    end_str += '] ' + str(comp_per) + '%' + ENDC

    bar_color = OKGREEN
    if comp_per <= 25:
        bar_color = FAIL
    elif comp_per > 25 and comp_per <= 50:
        bar_color = OKCYAN
    else:
        bar_color = OKGREEN

    print (vir_line)
    print (bar_color + end_str)