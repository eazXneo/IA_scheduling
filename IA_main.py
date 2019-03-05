# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/
# citation provided in IA documentation
# only framework used. Code for program SOLELY devised by me (student)


# importing the tkinter GUI library
from tkinter import *
import tkinter as tk
# import operating system dependent functionality library
import os
# import data serialisation library
import pickle


LARGE_FONT = ("Verdana", 13)
# setting font for the program

# opening file to store / retrieve data from
saved_data = open("/Users/19andrusz_l/Desktop/IA/user_data", "r+")

profile_exists = False
# checking if file is empty
profile_exits = False
file_status = os.stat("/Users/19andrusz_l/Desktop/IA/user_data").st_size
if file_status == 0:
    file_empty = True
    profile_exits = False
    print("File IS empty")
elif file_status != 0:
    file_empty = False
    profile_exits = True
    print("File is NOT empty")
    print("profile DOES exist")


# the data structures (lists) that contain the data inputed by user
subjectList = [] # list containing subjects (as StringVar)
subjectNames = [] # list containing subjct names (as string)
preference_list = [0] # list contatining user liking for a subject
# (every element's index corresponds to the subeject's index in subject lists)
preference_points_list = [0] # list contatining INTEGER!!! user liking for a subject


# create a subject class to have a central place for objects (subjects) to be created (unlike at the moment)
class Subject:
    global preference_list

    # when new subject object is added, set the name and add this name to subjectNames
    def __init__(self, name):
        self.name = name
        print("Subject", name, "added.")
        subjectList.append(self)
        subjectNames.append(name)

# debug statement for whether profile exists
if file_empty == True:
        profile_exists = True
        print("profile_exists:", profile_exists)


# function that adds subjects inputed by user to the task dropdown menu to be selected from.
def addSubject():
    global subjectNames

    # For entry field 1 (HL1):
    Subject(str(newSubject.get())) # creates object in class Subject
    subjectNames = []

    # clearing the menu in the TASKS window in order to then add all the subjects in order.
    subjectMenu.children["menu"].delete(0, "end")
    for s in subjectList:
        subjectNames.append(s.name)
        subjectMenu.children["menu"].add_command(label=s.name,
                                                              command=lambda sub=s.name: selectedSubject.set(sub))
    # sets default subject to the first subject in list.
    selectedSubject.set(subjectNames[0])

    # adds the corresponding liking for a subjct to the preference list.
    preference_list.append(p1.get())

    # process repeats for the next 5 subjects.

    # For entry field 2 (HL2):
    Subject(str(newSubject2.get()))
    subjectNames = []

    subjectMenu.children["menu"].delete(0, "end")
    for s in subjectList:
        subjectNames.append(s.name)
        subjectMenu.children["menu"].add_command(label=s.name,
                                                              command=lambda sub=s.name: selectedSubject.set(sub))
    selectedSubject.set(subjectNames[0])

    preference_list.append(p2.get())

    # For entry field 3 (HL3):
    Subject(str(newSubject3.get()))
    subjectNames = []

    subjectMenu.children["menu"].delete(0, "end")
    for s in subjectList:
        subjectNames.append(s.name)
        subjectMenu.children["menu"].add_command(label=s.name,
                                                              command=lambda sub=s.name: selectedSubject.set(sub))
    selectedSubject.set(subjectNames[0])

    preference_list.append(p3.get())

    # For entry field 4 (SL1):
    Subject(str(newSubject4.get()))
    subjectNames = []

    subjectMenu.children["menu"].delete(0, "end")
    for s in subjectList:
        subjectNames.append(s.name)
        subjectMenu.children["menu"].add_command(label=s.name,
                                                              command=lambda sub=s.name: selectedSubject.set(sub))
    selectedSubject.set(subjectNames[0])

    preference_list.append(p4.get())

    # For entry field 5 (SL2):
    Subject(str(newSubject5.get()))
    subjectNames = []

    subjectMenu.children["menu"].delete(0, "end")
    for s in subjectList:
        subjectNames.append(s.name)
        subjectMenu.children["menu"].add_command(label=s.name,
                                                              command=lambda sub=s.name: selectedSubject.set(sub))
    selectedSubject.set(subjectNames[0])

    preference_list.append(p5.get())

    # For entry field 6 (SL3):
    Subject(str(newSubject6.get()))
    subjectNames = []

    subjectMenu.children["menu"].delete(0, "end")
    for s in subjectList:
        subjectNames.append(s.name)
        subjectMenu.children["menu"].add_command(label=s.name,
                                                              command=lambda sub=s.name: selectedSubject.set(sub))
    selectedSubject.set(subjectNames[0])

    preference_list.append(p6.get())

    profile_exists = True
    # updating profile exists.

    # calls function to convert strings "like", "indifferent" and "dislike" into integers representing weighting
    # in final calculations
    add_preference(preference_list)


# this function convert strings "like", "indifferent" and "dislike" into integers representing weighting
def add_preference(pref_list_strings):
    global preference_points_list
    preference_points_list = [0] # for TOK
    global pref_points
    pref_points = 1 # do not know whether this variable is of any use to my program. Keep it for the moment.

    # creating weighting
    for i in range(0, 6):
        pref_in_string = pref_list_strings[i+1]
        if pref_in_string == "dislike":
            pref_points = 0
            preference_points_list.append(0)
        elif pref_in_string == "indifferent":
            preference_points_list.append(1)
        elif pref_in_string == "like":
            pref_points = 2
            preference_points_list.append(2)

    return preference_points_list

# automatically adds TOK to subjectList and subjectNames.
if file_empty:
    Subject("TOK")
    # is the below necessary?
    profile_exists = True


taskList = [] # tasklist holds the tkinter variables associated with a certain task
tasksAll = [] # taskALl is the actual data structure holding strings and integers to be 
              # then arranged into the most efficient order to be done.
task_list = []     # placed here to be global, also so that I don't lose overview of 
                    # what should be pickled and what shouldn't.  
                    # Holds all details for every task.
week_overview = []  # also placed to be global. Holds the list displayed in week.


class Task:
    # task class
    global week_overview

    # when new task object is added, set the name and add this task to taskList and tasksAll
    def __init__(self, name):
        self.name = name
        taskList.append(self)
        tasksAll.append(name)


# this function creates the week overview by obtaining the tasks from tasksAll and sorting them according to the
# calculated score.
def create_week():
    global week_overview
    # this is the default list with 20 slots available. 
    # Will be updated in this function for the WEEK window.
    week_overview = [["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "empty", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0],
                     ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0],
                     ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0],
                     ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0]]
    #  [["subject", "description", "days until due", "length", "total score"]]

    print("task_list in create_week:", task_list)
    tasks_unordered = task_list # task_list is updated when task is added
    number_of_tasks = len(tasks_unordered)

    for i in range(0, number_of_tasks):
        week_overview.pop(19)
        week_overview.insert(0, tasks_unordered[i]) # tasks are added to week_overview list

    # function defines which part of each element in the list of one task
    # (["subject", "description", "days until due", "length", "total score"])
    def takeSecond(elem):
        return elem[4]
    # sorting the week from highest priority score to lowest.
    week_overview.sort(key=takeSecond, reverse=True)

    return week_overview


# function that adds the tasks to week_overview.
def addTask():

    # creates task object form Task class
    Task(str(newTask.get()))
    # calls create_week() function that returns week_overview that is sorted
    final_week = create_week()
    # updates listbox in WEEK
    listbox.delete(0, END)
    for j in range (0, len(final_week)):
        listbox.insert(END, [str(final_week[j][0]), "---", str(final_week[j][1]), "---", final_week[j][4]])
        # the above adds the subject, description and priority score to the week overview.
    # sets first task as default value.
    selectedTask.set(tasksAll[0])

    print("a task has been added.")

# creates subject placeholder until user adds tasks.
Task("Subject")


# --- start of GUI classes.

class SeaofBTCapp(tk.Tk):
    # this is the main class for the program

    def get_page(self, page_class):
        return self.frames[page_class]

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        # layout for the main window

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # window configuration

        self.frames = {}

        for F in (StartPage, PageOneProfile, PageTwoTasks, PageThreeWeek):
            frame = F(container, self)
            frame.pack(fill=X, padx=100)
            # for all pages, layout stays the same

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            # frame visual configuration

        self.show_frame(StartPage)
        # StartPage opens straight away

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    # This is the StartPage class

    def retrieveData(self):
        print("file empty:", file_empty)

        if file_empty == False:
            profile_exists = True

            # if file empty, all of the user data is loaded from file user_data:
            with open("/Users/19andrusz_l/Desktop/IA/user_data","rb") as f:
                # load 1
                global preference_list
                preference_list = pickle.load(f)
                print("pickled preference_list:", preference_list)
                # load 2
                global subjectList
                subjectList = pickle.load(f)
                print("pickled subjectList:", subjectList)
                # load 3
                global subjectNames
                subjectNames = pickle.load(f)
                print("pickled subjectNames:", subjectNames)
                # load 4
                global taskList
                taskList = pickle.load(f)
                print("pickled taskList:", taskList)
                # load 5
                global tasksAll
                tasksAll = pickle.load(f)
                print("pickled tasksAll:", tasksAll)
                # load 6
                global week_overview
                week_overview = pickle.load(f)
                print("pickled week_overview:", week_overview)
                # load 7
                global task_list
                task_list = pickle.load(f)
                print("pickled task_list:", task_list)
                # load 8
                global preference_points_list
                preference_points_list = pickle.load(f)
                print("pickled preference_points_list:", preference_points_list)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.retrieveData()
        # calls function to load serialised data.

        # label with intro message
        label = tk.Label(self, text="Start Page"
                                    "\nHello, welcome to your main menu. Please select an option.", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label_last = tk.Label(self, text="Below you can save and download your data", 
                                    font=LARGE_FONT)
        label_last.pack(pady=10, padx=10)

        # creating the save and 'download' buttons
        def save_data():
            file_empty = False
            print("save button pressed. File empty:", file_empty)
            # changes state of button depending on whether data is being saved or loaded
            download_button.config(state=NORMAL)
            save_button.config(state=DISABLED)

            # data being pickled (serialised):
            with open("/Users/19andrusz_l/Desktop/IA/user_data","wb") as f:
                # pickle 1
                pickle.dump(preference_list, f)
                # pickle 2
                pickle.dump(subjectList, f)
                # pickle 3
                pickle.dump(subjectNames, f)
                # pickle 4
                pickle.dump(taskList, f)
                # pickle 5
                pickle.dump(tasksAll, f)
                # pickle 6
                pickle.dump(week_overview, f)
                # pickle 7
                pickle.dump(task_list, f)
                # pickle 8
                pickle.dump(preference_points_list, f)

        def update_save_button():
            # again updating the state of the buttons:
            download_button.config(state=DISABLED)
            save_button.config(state=NORMAL)

        # creating the save and 'download' buttons:
        save_button = tk.Button(self, text='SAVE ALL', command=save_data)
        save_button.pack()
        download_button = tk.Button(self, text='DOWNLOAD DATA', command=update_save_button)
        download_button.pack()

        # makes sure that the right buttons are disabled and active when program starts:
        if file_empty == True:
            save_button.config(state=NORMAL)
            download_button.config(state=DISABLED)
        elif file_empty == False:
            save_button.config(state=DISABLED)
            download_button.config(state=NORMAL)

        # buttons to other pages:
        button3 = tk.Button(self, text="View WEEK / edit TASKS",
                            command=lambda: controller.show_frame(PageThreeWeek))
        button3.pack(fill=X, side=BOTTOM)
        button2 = tk.Button(self, text="Add TASK",
                            command=lambda: controller.show_frame(PageTwoTasks))
        button2.pack(fill=X, side=BOTTOM)
        button1 = tk.Button(self, text="Add PROFILE",
                            command=lambda: controller.show_frame(PageOneProfile))
        button1.pack(fill=X, side=BOTTOM)


class PageOneProfile(tk.Frame):
    # Profile class

    # possible options of user preference for a subject
    user_pref = ["dislike", "indifferent", "like"]

    # function to create input options for user for HL1
    def build_hl_one(self):
        label3 = tk.Label(self, text="Enter HL 1:", font=LARGE_FONT)
        label3.grid(row=2, column=0)

        # entry field for new subject
        global newSubject
        newSubject = StringVar(self)
        newEntry1 = Entry(self, textvariable=newSubject)
        newEntry1.grid(row=2, column=1)

        # user preference dropdown menu
        global p1
        p1 = StringVar(self)
        p1.set("indifferent") # default value
        user_pref = self.user_pref
        w1 = OptionMenu(self, p1, user_pref[0], user_pref[1], user_pref[2])
        w1.grid(row=2, column=2)

        return p1

        # the remaining functions for the subject and preference follow the same logic

    # function to create input options for user for HL2
    def build_hl_two(self):
        label4 = tk.Label(self, text="Enter HL 2:", font=LARGE_FONT)
        label4.grid(row=3, column=0)

        global newSubject2
        newSubject2 = StringVar(self)
        newEntry2 = Entry(self, textvariable=newSubject2)
        newEntry2.grid(row=3, column=1)

        global p2
        p2 = StringVar(self)
        p2.set("indifferent")
        user_pref = self.user_pref
        w2 = OptionMenu(self, p2, user_pref[0], user_pref[1], user_pref[2])
        w2.grid(row=3, column=2)

        return newSubject2

    # function to create input options for user for HL3
    def build_hl_three(self):
        label4 = tk.Label(self, text="Enter HL 3:", font=LARGE_FONT)
        label4.grid(row=4, column=0)

        global newSubject3
        newSubject3 = StringVar(self)
        newEntry2 = Entry(self, textvariable=newSubject3)
        newEntry2.grid(row=4, column=1)

        global p3
        p3 = StringVar(self)
        p3.set("indifferent")
        user_pref = self.user_pref
        w2 = OptionMenu(self, p3, user_pref[0], user_pref[1], user_pref[2])
        w2.grid(row=4, column=2)

        return newSubject3

    # function to create input options for user for SL1
    def build_sl_one(self):
        label3 = tk.Label(self, text="Enter SL 1:", font=LARGE_FONT)
        label3.grid(row=5, column=0)

        global newSubject4
        newSubject4 = StringVar(self)
        newEntry1 = Entry(self, textvariable=newSubject4)
        newEntry1.grid(row=5, column=1)

        global p4
        p4 = StringVar(self)
        p4.set("indifferent")
        user_pref = self.user_pref
        w1 = OptionMenu(self, p4, user_pref[0], user_pref[1], user_pref[2])
        w1.grid(row=5, column=2)

        return newSubject4

    # function to create input options for user for SL2
    def build_sl_two(self):
        label4 = tk.Label(self, text="Enter SL 2:", font=LARGE_FONT)
        label4.grid(row=6, column=0)

        global newSubject5
        newSubject5 = StringVar(self)
        newEntry2 = Entry(self, textvariable=newSubject5)
        newEntry2.grid(row=6, column=1)

        global p5
        p5 = StringVar(self)
        p5.set("indifferent")
        user_pref = self.user_pref
        w2 = OptionMenu(self, p5, user_pref[0], user_pref[1], user_pref[2])
        w2.grid(row=6, column=2)

        return newSubject5

    # function to create input options for user for SL3
    def build_sl_three(self):
        label4 = tk.Label(self, text="Enter SL 3:", font=LARGE_FONT)
        label4.grid(row=7, column=0)

        global newSubject6
        newSubject6 = StringVar(self)
        newEntry2 = Entry(self, textvariable=newSubject6)
        newEntry2.grid(row=7, column=1)

        global p6
        p6 = StringVar(self)
        p6.set("indifferent")
        user_pref = self.user_pref
        w2 = OptionMenu(self, p6, user_pref[0], user_pref[1], user_pref[2])
        w2.grid(row=7, column=2)

        return newSubject6

    # GUI config function
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="---PROFILE---", font=LARGE_FONT)
        label1.grid(row=0, column=1)
        label2 = tk.Label(self, text="Enter all of your subjects and how much you like/dislike them:\n"
                                     "It is strongly suggested that you use all options "
                                     "(\"like\", \"indifferent\", \"dislike\")\n", font=LARGE_FONT)
        label2.grid(row=1, column=1)

        # calls for functions to create entry options for user
        self.build_hl_one()
        self.build_hl_two()
        self.build_hl_three()
        self.build_sl_one()
        self.build_sl_two()
        self.build_sl_three()

        label9 = tk.Label(self, text="ToK will be automatically added.", font=LARGE_FONT)
        label9.grid(row=8, column=1)

        # this button saves profile
        button_add_profile = Button(self, text="SAVE PROFILE", command=addSubject)
        button_add_profile.grid(row=9, column=1)

        button2 = tk.Button(self, text="View/edit TASKS",
                            command=lambda: controller.show_frame(PageTwoTasks))
        button2.grid(row=10, column=1)

        button3 = tk.Button(self, text="View WEEK",
                            command=lambda: controller.show_frame(PageThreeWeek))
        button3.grid(row=11, column=1)
        button1 = tk.Button(self, text="Back to HOME",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=12, column=1)


class PageTwoTasks(tk.Frame):
    # Tasks class

    global task_list

    # default list with empty slots
    task_list = [["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0],
                 ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0],
                 ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0],
                 ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0], ["empty", "", 0, 0, 0]]

    # this function actually stores the task to be used for week overview.
    # also calculates the priority score for each task
    def create_task(self, subject, description, deadline, duration):
        global preference_points_list
        # tasks saved as: ["subject", "description", "days until due", "length", "total score"], etc]

        # calculating points from subject level
        # also extracting what subject is being looked at so as to extract the pref info later
        element_in_pref_list = 0
        if subject == subjectNames[0]:
            s_level_points = 0
            element_in_pref_list = 0
        elif subject == subjectNames[1] or subject == subjectNames[2] or subject == subjectNames[3]:
            s_level_points = 2
            if subject == subjectNames[1]:
                element_in_pref_list = 1
            elif subject == subjectNames[2]:
                element_in_pref_list = 2
            elif subject == subjectNames[3]:
                element_in_pref_list = 2
        elif subject == subjectNames[4] or subject == subjectNames[5] or subject == subjectNames[6]:
            s_level_points = 1
            if subject == subjectNames[4]:
                element_in_pref_list = 4
            elif subject == subjectNames[5]:
                element_in_pref_list = 5
            elif subject == subjectNames[6]:
                element_in_pref_list = 6

        # preference points (int) taken from preference_points_list using index from above depending on subject
        s_pref_points = preference_points_list[element_in_pref_list]

        # calculate points based on days until due:
        deadline = int(deadline)
        deadline_points = 0
        if deadline == 1:
            deadline_points = 2
        elif deadline <= 3 and deadline > 1:
            deadline_points = 1
        elif deadline > 3:
            deadline_points = 0.5
        # create int out of str duration.
        hours = int(duration[0])
        minutes = int(duration[2:])
        duration_dec = (hours + (minutes / 60))
        # calculate points based on task duration:
        t_duration_points = 0
        if duration_dec >= 3:
            t_duration_points = 2
        elif duration_dec >= 1 and duration_dec < 3:
            t_duration_points = 1
        elif duration_dec < 1:
            t_duration_points = 0

        # calculates score based on client feedback in how important the various factors are
        score = 3 * deadline_points + 3 * t_duration_points + s_pref_points + 2 * s_level_points
        
        # adds score to task_list
        task_list.pop(19)
        task_list.insert(0, [subject, description, deadline, duration, score])

    # creates the dropdown menu in TASKS if there are subjects saved
    def dropdown_after_pickle(self):
        print("here is subjectNames:", subjectNames)

        # creating stringVar and setting it to the first subject in subjectNames
        global selectedSubject
        selectedSubject = StringVar(self)
        selectedSubject.set(subjectNames[0]) # default value

        # creates subject menu using list subjectNames
        global subjectMenu
        subjectMenu = OptionMenu(self, selectedSubject, *subjectNames)
        subjectMenu.pack(fill=X)

        return selectedSubject

    # creates the dropdown menu in TASKS if there are no subjects saved
    def create_subject_dropdown_for_tasks(self):

        print("here is subjectNames:", subjectNames)
        # this creates the dropdown menu for subjects in TASKS
        label3 = tk.Label(self, text="Choose subject:", font=LARGE_FONT)
        label3.pack(pady=10, padx=10, anchor=W)
        # creating a dropdown option for the subject of the new task

        global selectedSubject
        selectedSubject = StringVar(self)
        selectedSubject.set(subjectNames[0]) # default value

        # creates subject menu using list subjectNames
        global subjectMenu
        subjectMenu = OptionMenu(self, selectedSubject, *subjectNames)
        subjectMenu.pack(fill=X)

        return selectedSubject

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="---TASKS---", font=LARGE_FONT)
        label1.pack(pady=10, padx=10)
        label2 = tk.Label(self, text="Complete these steps to add task:\n", font=LARGE_FONT)
        label2.pack(pady=10, padx=10)

        label3 = tk.Label(self, text="Subject:\n", font=LARGE_FONT)
        label3.pack(pady=10, padx=10, anchor=W)

        # creating subject dropdown menu
        if file_empty == False:
            self.dropdown_after_pickle()
        elif file_empty == True:
            self.create_subject_dropdown_for_tasks()

        label4 = tk.Label(self, text="Description:", font=LARGE_FONT)
        label4.pack(pady=10, padx=10, anchor=W)

        # creating a text entry box for the new task
        global newTask
        newTask = StringVar()
        e = Entry(self, textvariable=newTask)
        e.pack(fill=X)
        e.delete(0, END)
        e.insert(0, "...")

        # creating option menu for 'days until due'
        label5 = tk.Label(self, text="Days left until due:", font=LARGE_FONT)
        label5.pack(pady=10, padx=10, anchor=W)
        # choose days until due
        v = StringVar(self)
        v.set(1)  # default value
        l = [1, 2, 3, 4, 5, 6, 7]
        w = OptionMenu(self, v, str(l[0]), str(l[1]), str(l[2]), str(l[3]), str(l[4]), str(l[5]), str(l[6]))
        w.pack(fill=X)

        # creates option menu for task duration
        label6 = tk.Label(self, text="Duration of task:", font=LARGE_FONT)
        label6.pack(pady=10, padx=10, anchor=W)
        # choose task duration
        vd = StringVar(self)
        vd.set("0:10")  # default value
        time_list = ["0:10", "0:20", "0:30", "0:40", "0:50", "1:00", "1:10", "1:20", "1:30", "1:40", "1:50", "2:00",
                     "2:10", "2:20", "2:30", "2:40", "2:50", "3:00", "3:10", "3:20", "3:30", "3:40", "3:50", "4:00"]
        w = OptionMenu(self, vd, time_list[0], time_list[1], time_list[2], time_list[3], time_list[4], time_list[5],
                       time_list[6], time_list[7], time_list[8], time_list[9], time_list[10], time_list[11],
                       time_list[12], time_list[13], time_list[14], time_list[15], time_list[16], time_list[17],
                       time_list[18], time_list[19], time_list[20], time_list[21], time_list[22], time_list[23])
        w.pack(fill=X)

        # this function obtains the information from the user to be used in create_task().
        # needs to be here to retrieve data but can't actually create the task because function within window function.
        # therefore only retireves variables and 'shares' them with function create_task() that is a function of the class.
        # then I can easily use these in creating the week overview. "Easily".
        def confirm_new_task():
            # disables task button if 20 tasks already exist
            if task_list[-1][4] != 0:
                button_add_task.config(state=DISABLED)
                print("button disabled because limit reached")
                label6 = tk.Label(self,
                                  text="Limit of 20 tasks reached. Please delete some tasks before adding new ones.",
                                  font=LARGE_FONT)
                label6.pack(pady=10, padx=10, anchor=W)

            # obtaining task details
            task_subject = selectedSubject.get()
            task_description = e.get()
            task_deadline = v.get()
            task_duration = vd.get()

            # calls function to create task and add to the list
            PageTwoTasks.create_task(self, task_subject, task_description, task_deadline, task_duration)

        # this button adds a new task
        global button_add_task
        button_add_task = Button(self, text="ADD TASK", command=confirm_new_task)
        button_add_task.pack()

        button1 = tk.Button(self, text="Back to HOME",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(fill=X, side=BOTTOM)

        button2 = tk.Button(self, text="View PROFILE",
                            command=lambda: controller.show_frame(PageOneProfile))
        button2.pack(fill=X, side=BOTTOM)

        button3 = tk.Button(self, text="View WEEK",
                            command=lambda: controller.show_frame(PageThreeWeek))
        button3.pack(fill=X, side=BOTTOM)


class PageThreeWeek(tk.Frame):
    # Week class

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = tk.Label(self, text="--- WEEK OVERVIEW ---", font=LARGE_FONT)
        label1.pack(pady=10, padx=10)
        label2 = tk.Label(self, text="This is your week:", font=LARGE_FONT)
        label2.pack(pady=10, padx=10)
        label3 = tk.Label(self, text="TASKS IN ORDER GO HERE!!!", font=LARGE_FONT)
        label3.pack(pady=10, padx=10)
        label4 = tk.Label(self, text="Week overview can be found below.\n"
                                     "(scroll to reach the end)", font=LARGE_FONT)
        label4.pack(pady=10, padx=10)

        # refresh week:
        global refresh_week_button
        refresh_week_button = tk.Button(self, text="REFRESH WEEK!",
                            command=addTask)
        refresh_week_button.pack()

        # below ?
        global selectedTask
        selectedTask = StringVar()
        selectedTask.set(tasksAll[0])

        # This list box gives the week overview.
        global listbox
        listbox = Listbox(self)
        listbox.pack(fill=BOTH, expand=1)
        listbox.insert(END, "WEEK OVERVIEW PLACEHOLDER!!!")

        # function to delete a task from list:
        def delete_task():
            # try is needed because might be deleting a placeholder and that isn't
            # an element in tasksAll or taskList.
            try:
                # obtaining the element in Listbox
                lb = listbox
                task_to_delete = lb.get(ANCHOR)

                # obtaining index of selected task
                index = lb.get(0, "end").index(task_to_delete)
                print("task selected to delete:", task_to_delete)
                print("at index:", index)

                # might not be important anymore... (turining tuple into list)
                task_to_delete = list(task_to_delete)
                print("type:", type(task_to_delete))

                # deleting element in Listbox
                lb.delete(ANCHOR)

                # default placeholder: ["empty", "", 0, 0, 0]
                # trying to delete this element from ALL data structures.
                try:
                    taskList.pop(index)
                except IndexError:
                    print("this task was added this run and was not saved")
                tasksAll.pop(index)
                week_overview.pop(index)
                week_overview.append(["empty", "", 0, 0, 0])
                task_list.pop(index)
                task_list.append(["empty", "", 0, 0, 0])
                print("length of tasksAll", len(tasksAll))
                print("task list:", task_list)
                print("length of week_overview:", len(week_overview))
                print("week o ...", week_overview[-1][2])
                if week_overview[-1][2] == 0:
                    button_add_task.config(state=NORMAL)
                    print("normal state")
            except ValueError:
                print("trying to delete nothing. Pass")

        delete_task_from_week = Button(self, text="Delete task",
                   command=delete_task)
        delete_task_from_week.pack()

        # these are the menu buttons
        button1 = tk.Button(self, text="Back to HOME",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(fill=X, side=BOTTOM)

        button2 = tk.Button(self, text="View PROFILE",
                            command=lambda: controller.show_frame(PageOneProfile))
        button2.pack(fill=X, side=BOTTOM)

        button3 = tk.Button(self, text="View/edit TASKS",
                            command=lambda: controller.show_frame(PageTwoTasks))
        button3.pack(fill=X, side=BOTTOM)


# runs application from main class
app = SeaofBTCapp()
# app name:
app.title("IB Organisation App")
# runs application
app.mainloop()