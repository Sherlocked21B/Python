import subprocess
from pynput.keyboard import Key , Controller , KeyCode
password = '1234567890'
cmd='ls'
command = "sudo nano /etc/resolv.conf".split()
subprocess.call("echo {} | sudo -S {}".format(password , cmd), shell=True)
keyboard=Controller()
# moving the curser down 
keyboard.press(Key.ctrl.value)
keyboard.press('j')
keyboard.release('j')
keyboard.release(Key.ctrl.value)
# deleting the content
keyboard.press(Key.ctrl.value)
keyboard.press('k')
keyboard.release('k')
keyboard.release(Key.ctrl.value)
keyboard.type("nameserver 1.1.1.1")
# exiting the window
keyboard.press(Key.ctrl.value)
keyboard.press('x')
keyboard.release('x')
keyboard.release(Key.ctrl.value)
# saving the content 
keyboard.press('y')
for i in range(2):
    keyboard.press(Key.enter.value)
    keyboard.release(Key.enter.value)
subprocess.run(command)

