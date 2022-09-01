# Task Manager

Download git repo and run install.sh from install folder.

Example:
```bash

root@DESKTOP-UHBGVLH:~/bd#
 [0/1 35.4] 🦁 tm -h
usage: tm [-h] [-a ADD] [-t TITLE] [-c COMPLETE] [--clear [CLEAR [CLEAR ...]]] [-f FAILED] [-u UNKNOWN] [-d DELETE] [-r RUNNING] [--summary [SUMMARY [SUMMARY ...]]] [--notes NOTES] [--sn SN]

Welcome to Task Manager

optional arguments:
  -h, --help            show this help message and exit
  -a ADD, --add ADD     Add Task, ex. 'Finish this @ development @ 34.5 will take 1st as task, 2nd as title and 3rd as deadline'
  -t TITLE, --title TITLE
                        Add Title
  -c COMPLETE, --complete COMPLETE
                        Mark Completed
  --clear [CLEAR [CLEAR ...]]
                        Delete all tasks
  -f FAILED, --failed FAILED
                        Mark failed
  -u UNKNOWN, --unknown UNKNOWN
                        Mark unknown or undecided
  -d DELETE, --delete DELETE
                        Delete Task
  -r RUNNING, --running RUNNING
                        Mark Running
  --summary [SUMMARY [SUMMARY ...]]
                        Get details of completed/total tasks
  --notes NOTES         Add notes to task file
  --sn SN               Show note content

```