#Created by: Alireza Teimoori
#Created on: 19 Sep 2017
#Created for: ICS3UR-1
#Lesson: Unit 1-01
#This program show schools and their mascots (3 Buttons)


import ui


def mother_teresa_touch_up_inside(sender):
    # displays Mother Teresa and its mascot
    view['school_name_label'].text = 'Mother Teresa HS'
    view['mascot_label'].text = 'Titans'

def st_joe_touch_up_inside(sender):
    # displays St. Joe and its mascot
    view['school_name_label'].text = 'St. Joe HS'
    view['mascot_label'].text = 'Jaguars'

def st_mark_touch_up_inside(sender):
    # display St. Mark and its macot
    view['school_name_label'].text = 'St. Mark HS'
    view['mascot_label'].text = 'Lions'

view = ui.load_view()
view.present('sheet')
