from Functions_and_Declarations import *
from sklearn.model_selection import train_test_split

DATA_PATH = os.path.join('COMMAND_DATA')
commands = np.array(['forward', 'left', 'right','stop'])
num_data = 30


label_map = {label:num for num, label in enumerate(commands)}


data, labels = [], []

for command in commands:
    for c in range(num_data):
        res = np.load(os.path.join(DATA_PATH, command, "{}.npy".format(c)))
        data.append(res)
        #labels.append(label_map[command])
        labels.append(command)

x = np.array(data)
#y = keras.utils.to_categorical(labels).astype(int)
y = labels



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)
print(x_train)
print(y_train)