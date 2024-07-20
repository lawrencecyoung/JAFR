import os
import sys
import json
import datetime

def main():
    def split_passwd(filename):
        passwd_file = open(filename, "r")
        passwd_content = passwd_file.readlines()
        users = []
        for i in passwd_content:
            x = i.split(':')    #<username>:<password>:<user ID>:<group ID>:<user ID info>:<home directory>:<default shell>
            users.append(x)
        return users

    def date_today(date_string):
        try:
            input_date = datetime.datetime.strptime(date_string, "%d/%m/%y")
            today = datetime.datetime.now().date()
            if input_date.date() == today:
                return True
            else:
                return False
        except ValueError:
            return False

    def next_n_days(date_string, n):
        try:
            input_date = datetime.datetime.strptime(date_string, "%d/%m/%y")
            today = datetime.datetime.now().date()
            n_days_from_now = today + datetime.timedelta(days=n)
            if today < input_date.date() <= n_days_from_now:
                return True
            else:
                return False
        except ValueError:
            return False

    def separate_tasks_file(filename):
        tasks_file = open(filename, "r")
        tasks_content = tasks_file.readlines()
        tasks = []
        for i in tasks_content:
            tasks.append(i)
        tasks_split = []
        date_format = '%d/%m/%y'
        for i in tasks:
            try:
                pairs = []
                x = i.split('Due:')
                x[0] = x[0].strip()
                if x[0].startswith('-'):
                    pairs.append(x[0].strip('- '))
                    y = x[1].strip().split(' ', 1)
                    datetime.datetime.strptime(y[0], date_format)
                    pairs.append(y[0].strip())
                    pairs.append(y[1].strip())
                    tasks_split.append(pairs)
            except:
                pass
        return tasks_split


    def separate_meetings_file(filename):
        meetings_file = open(filename, "r")
        meetings_content = meetings_file.readlines()
        meetings = []
        for i in meetings_content:
            meetings.append(i)
        meeting_split = []
        for i in meetings:
            try:
                pairs = []
                x = i.split('Scheduled:')
                x[0] = x[0].strip()
                if x[0].startswith('-'):
                    pairs.append(x[0].strip('- '))
                    y = x[1].strip().split(' ', 1)
                    date_format = '%d/%m/%y'
                    time_format = '%H:%M'
                    try:
                        datetime.datetime.strptime(y[1], date_format)
                        datetime.datetime.strptime(y[0], time_format)
                        pairs.append(y[0].strip())
                        pairs.append(y[1].strip())
                        meeting_split.append(pairs)
                    except ValueError:
                        pass
            except:
                pass
        return meeting_split

    def completing_tasks(filename):
        tasks = separate_tasks_file(filename)
        incomplete_tasks = []
        for i in tasks:
            if i[2] == 'not complete':
                incomplete_tasks.append(i)     
        if incomplete_tasks == []:
            print("No tasks to complete!")
            return

        print("Which task(s) would you like to mark as completed?")
        
        counter = 1
        for i in incomplete_tasks:
            if i[2] == 'not complete':
                print(f"{counter}. {i[0]} by {i[1]}")
                counter+=1


        valid = False
        while valid == False:
            task_choice = input().strip().split()
            try:
                for i in range(len(task_choice)):
                    task_choice[i] = int(task_choice[i])
                set_choice = sorted(set(task_choice))

                i = 0
                for idx in set_choice:
                    if idx >= counter or idx < 1:
                        print('Invalid choice of tasks')
                        break
                    if i == len(set_choice)-1:
                        valid = True
                    i+=1
            except:
                print("Invalid choice of tasks")
        
        marked_tasks = []
        for idx in set_choice:
            marked_tasks.append(incomplete_tasks[idx-1])

        if valid==True:
            tasks_file = open(filename, "r")
            tasks_content = tasks_file.read()
            for i in marked_tasks:
                search = f"{i[0]} Due: {i[1]} {i[2]}"
                replacement = f"{i[0]} Due: {i[1]} complete"
                tasks_content = tasks_content.replace(search, replacement, 1)
            tasks_file = open(filename, "w")
            tasks_file.write(tasks_content)

        print("Marked as complete.")
        
        
    def add_meeting(filename):
        meeting_desc = input("Please enter a meeting description:\n")
        while True:
            
            if "Scheduled:" in meeting_desc:
                print("Invalid meeting description")
            elif meeting_desc.strip() == '':
                print("Invalid meeting description")
            else:
                break
            meeting_desc = input()

        x = False
        while x == False:
            try:
                date = input("Please enter a date:\n")
                input_date = datetime.datetime.strptime(date, "%d/%m/%y")
                x = True
            except:
                x = False
        x = False
        while x == False:
            try:
                time = input("Please enter a time:\n")
                input_time = datetime.datetime.strptime(time, "%H:%M")
                x = True
            except:
                x = False

        combined = f"- {meeting_desc} Scheduled: {time} {date}\n"
        lines_to_add = ['\n##### added by you\n', combined]
        meetings_file = open(filename, "a")
        meetings_file.writelines(lines_to_add)
        meetings_file.close()
        print(f"Ok, I have added {meeting_desc} on {date} at {time}.")
        
        x = False
        while x == False:
            share = input("Would you like to share this meeting? [y/n]: ")
            if share == 'y' or share == 'n':
                x = True
        
        if share == 'n':
            return None
        elif share == 'y':
            return combined #Use this function to prompt share afterwards

    def change_master_directory(password_file):
        path = input("Which directory would you like Jafr to use?\n")
        home_directory = os.path.expanduser('~')
        user_setting_file = open(f'{home_directory}/.jafr/user-settings.json', 'r')
        data = json.load(user_setting_file)
        data["master"] = path
        user_setting_file = open(f'{home_directory}/.jafr/user-settings.json', 'w')
        json.dump(data, user_setting_file)
        print(f"Master directory changed to {path}.")

    def share(passwd_file, user, content, t_or_m):
        if t_or_m == 't':
            file_type = 'tasks'
        elif t_or_m == 'm':
            file_type = 'meetings'
        
        print('Who would you like to share with?')
        users = split_passwd(passwd_file)
        user_id_list = []
        for i in users:
            if i[0]!=user:
                print(i[2], i[0])
                user_id_list.append(i[2])

        while True:
            chosen_users = input()
            chosen_users = chosen_users.split()
            for i in range(len(chosen_users)):
                if chosen_users[i] not in user_id_list:
                    break
            else:
                break
            print("Invalid user ID entered")

        home_dir_list = [] 
        for chosen in chosen_users:
            for i in users:
                if i[2] == chosen:
                    home_dir_list.append(i[5])
        for home_directory in home_dir_list:
            try:
                user_setting_file = open(f'{home_directory}/.jafr/user-settings.json', 'r')
                x = json.load(user_setting_file)
                filename = x['master']+'/'+file_type+'.md'
                if os.path.exists(filename) == False:
                    print("Jafr's chosen master directory does not exist.", file=sys.stderr)
                    return
            except:
                print("Jafr's chosen master directory does not exist.", file=sys.stderr)
                return

            lines_to_add = [f'\n##### shared by {user}\n', content]
            meetings_file = open(filename, "a")
            meetings_file.writelines(lines_to_add)
            meetings_file.close()
        
        if t_or_m == 't':
            print("Task shared.")
        elif t_or_m == 'm':
            print("Meeting shared.")


    def task_share(passwd_file, task_file, user):
        tasks = separate_tasks_file(task_file)
        print("Which task would you like to share?")
        i = 0
        while i < len(tasks):
            print(f"{i+1}. {tasks[i][0]} by {tasks[i][1]}")
            i+=1

        while True:
            task_choice = input()
            try:
                task_choice = int(task_choice)
                if task_choice > 0 and task_choice <= len(tasks):
                    break
                else:
                    print('Invalid Task Number')
            except:
                print('Invalid Task Number')
                True
        task_chosen = tasks[task_choice-1]
        content = f"- {task_chosen[0]} Due: {task_chosen[1]} {task_chosen[2]}\n"
        share(passwd_file, user, content, 't')
        
    def meeting_share(passwd_file, meeting_file, user):
        meetings = separate_meetings_file(meeting_file)
        print("Which meeting would you like to share?")
        i = 0
        while i < len(meetings):
            print(f"{i+1}. {meetings[i][0]} on {meetings[i][2]} at {meetings[i][1]}")
            i+=1
        if i == 0:
            print("No meetings to share.")
            return

        while True:
            meeting_choice = input()
            try:
                meeting_choice = int(meeting_choice)
                if meeting_choice > 0 and meeting_choice <= len(meetings):
                    break
                else:
                    print('Invalid Meeting Number')
            except:
                print('Invalid Meeting Number')
                continue
        meeting_chosen = meetings[meeting_choice-1]
        content = f"- {meeting_chosen[0]} Scheduled: {meeting_chosen[1]} {meeting_chosen[2]}\n"
        share(passwd_file, user, content, 'm')
        

    password_file = sys.argv[1]


    username = os.environ.get('USER')
    home_directory = os.path.expanduser('~')
    user_setting_file = open(f'{home_directory}/.jafr/user-settings.json', 'r')
    data = json.load(user_setting_file)
    path = data["master"]

    if not os.path.exists(path):
        print("Jafr's chosen master directory does not exist.", file=sys.stderr)
        sys.exit(0)

    Tasks_File =  path + '/tasks.md'
    Meetings_File = path + '/meetings.md'

    if os.path.exists(Tasks_File) and os.path.exists(Meetings_File):
        pass
    else:
        print('Missing tasks.md or meetings.md file.', file=sys.stderr)
        sys.exit(0)


    tasks = separate_tasks_file(Tasks_File)
    print("Just a friendly reminder! You have these tasks to finish today.")
    for i in tasks:
        if date_today(i[1]) and i[2] == 'not complete':
            print('-', i[0])
    print("\nThese tasks need to be finished in the next three days!")
    for i in tasks:
        if next_n_days(i[1], 3) and i[2] == 'not complete':
            print('-', i[0], 'by', i[1])
    meetings = separate_meetings_file(Meetings_File)
    print("\nYou have the following meetings today!")
    for i in meetings:
        if date_today(i[2]):
            print('-',i[0],'at',i[1])
    print("\nYou have the following meetings scheduled over the next week!")
    for i in meetings:
        if next_n_days(i[2], 7):
            print('-',i[0],'on',i[2],'at',i[1])

    print()
    y = False
    while y == False:
        print("What would you like to do?")
        print('''1. Complete tasks
2. Add a new meeting.
3. Share a task.
4. Share a meeting.
5. Change Jafr's master directory.
6. Exit''')

        x = False
        while x == False:
            try:
                choice = int(input())
                if 1 <= choice <= 5:
                    x = True
                elif choice == 6:
                    break
            except:
                x = False

        if choice == 1:
            completing_tasks(Tasks_File)
        elif choice == 2:
            x = add_meeting(Meetings_File)
            if x:
                share(password_file, username, x, 'm')
        elif choice == 3:
            task_share(password_file, Tasks_File, username)
        elif choice == 4:
            meeting_share(password_file, Meetings_File, username)
        elif choice == 5:
            change_master_directory(password_file) 
        elif choice == 6:
            y = True

if __name__ == '__main__':
    main()
