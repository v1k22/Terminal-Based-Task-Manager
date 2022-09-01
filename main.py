from const import *
from cal import *
import task
import sys
from pathlib import Path

import argparse

N_args = None

def run(args):

    Path("/etc/bd").mkdir(parents=True, exist_ok=True)

    task.data = {}

    if N_args == 1:
        task.display()

    if args.add != None:
        task.add_task(args.add)

    if args.clear != None:
        task.delete_data()

    if args.complete != None:
        task.mark(args.complete, 'c')

    if args.failed != None:
        task.mark(args.failed, 'f')

    if args.unknown != None:
        task.mark(args.unknown, 'u')

    if args.running != None:
        task.mark(args.running, 'r')

    if args.delete != None:
        task.delete_task(args.delete)

    if args.summary != None:
        task.task_summary()

    if args.notes != None:
        task.add_notes(args.notes)

    if args.sn != None:
        task.add_show_notes(args.sn)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Welcome to Task Manager')
    parser.add_argument('-a','--add', help="Add Task, ex. 'Finish this @ development @ 34.5 will take 1st as task, 2nd as title and 3rd as deadline' ", required=False, type=str)
    parser.add_argument('-t','--title', help='Add Title', required=False)
    parser.add_argument('-c','--complete', help='Mark Completed', required=False)
    parser.add_argument('--clear', nargs = '*', help='Delete all tasks', required=False)
    parser.add_argument('-f','--failed', help='Mark failed', required=False)
    parser.add_argument('-u','--unknown', help='Mark unknown or undecided', required=False)
    parser.add_argument('-d','--delete', help='Delete Task', required=False)
    parser.add_argument('-r','--running', help='Mark Running', required=False)
    parser.add_argument('--summary', nargs = '*' ,help='Get details of completed/total tasks', required=False)
    parser.add_argument('--notes', help='Add notes to task file', required=False)
    parser.add_argument('--sn', help='Show note content', required=False)


    args = parser.parse_args()

    N_args = len(sys.argv)

    run(args)