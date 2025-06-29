print('Welcome to Smart Scheduler!')
choices = ['1','2','3','4','5']
inp = ''
exams = {}
examnum = 1

def add_exam():
    global examnum
    name = input('Exam name: ')
    date = input('Exam date: ')
    time = input('Exam time: ')
    room = input('Exam room: ')

    for exam in exams.values():
        if exam['date'] == date and exam['time'] == time:
            print('\nConflict in scheduling detected. Please choose another time and date.\n')
            return
    
    exams[examnum] = {
        'name': name,
        'date': date,
        'time': time,
        'room': room
    }

    print('\nSuccess! You will now be redirected to the menu...\n')
    examnum += 1

def print_exams():
    if not exams:
        print('\nNo exams scheduled.\n')
    else:
        print('\n---List of scheduled exams:---\n')
        for examnum, details in exams.items():
            print(f'Exam Number: {examnum}')
            print(f'    Name: {details['name']}')
            print(f'    Date: {details['date']}')
            print(f'    Time: {details['time']}')
            print(f'    Room: {details['room']}')
            print("-------------------------------\n")

def edit_exams():
    if not exams:
        print('\nNo exams scheduled.\n')
        return
    
    print_exams()

    try:
        examnum = int(input('\nEnter the number of the exam you would like to edit: '))
        if examnum not in exams:
            print('Invalid exam number.\n')
            return
    except ValueError:
        print('\nEnter the number of the exam you would like to edit: ')
        return
    
    print('\nWhich detail would you like to edit? Please input the corresponding number:')
    print('1: Name\n2: Date\n3: Time\n4: Room')
    edit_detail = input()

    if edit_detail == '1':
        new = input('Enter new exam name: ')
        exams[examnum]['name'] = new
    elif edit_detail == '2':
        new = input('Enter new exam date: ')
        exams[examnum]['date'] = new
    elif edit_detail == '3':
        new = input('Enter new exam time: ')
        exams[examnum]['time'] = new
    elif edit_detail == '4':
        new = input('Enter new exam room: ')
        exams[examnum]['room'] = new
    else:
        print("\n input. Please try again.")
        return

    print('\nExam edited successfully!')

def del_exam():
    if not exams:
        print('\nNo exams scheduled.\n')
        return
    
    print_exams()

    try:
        examnum = int(input('\nEnter the number of the exam you would like to delete: '))
        if examnum not in exams:
            print('Invalid exam number.\n')
            return
    except ValueError:
        print('\nEnter the number of the exam you would like to delete: ')
        return

    while True:
        prompt = input(f'Are you sure you want to delete exam number {examnum} with name {exams[examnum]['name']}? Please type "yes" or "no".\n').lower()
        if prompt == 'yes':
            del exams[examnum]
            print('Exam deleted successfully! You will now be redirected to the menu...\n')
            break
        elif prompt == 'no':
            print('\nDeletion cancelled.\n')
            break
        else:
            print('Invalid input. Please type "yes" or "no".')

while inp != '5':
    print('Please input the number which corresponds to your desired operation.\n')
    inp = input('1: Add a new exam\n2: View all exams\n3: Edit an exam entry\n4: Delete an exam entry\n5: Exit program\n\n')

    while inp not in choices:
        print('\nInvalid input. Please try again.')
        inp = input('1: Add a new exam\n2: View all exams\n3: Edit an exam entry\n4: Delete an exam entry\n5: Exit program\n\n')

    if inp == '1':
        add_exam()
    elif inp == '2':
        print_exams()
    elif inp == '3':
        edit_exams()
    elif inp == '4':
        del_exam()
    elif inp == '5':
        print('\nThank you!')
        exit()
