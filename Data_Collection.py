from setuptools import Command
from Functions_and_Declarations import *



command = 'stop'
initial_rep = 0
repititions = 30
folder_name = 'COMMAND_DATA'
prep_time = 20

data_collection(command, initial_rep, repititions, folder_name, prep_time)
cap.release()
cv2.destroyAllWindows()
