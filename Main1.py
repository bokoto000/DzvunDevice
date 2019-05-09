import picamera
import subprocess
from PIL import Image
from bluetooth_con import bluetooth_mac,bluetooth_connection
from sound_board import play
from hardware_interface import button_setup,button

blueMac=bluetooth_mac.get_bluetooth_mac()

subprocess.call(['sudo', 'hciconfig', 'hci0', 'piscan'])

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.rotation=180;

button_setup.setup_button(play, camera, button)
bluetooth_connection.start_bluetooth_con()


#message = input("Press enter to quit\n\n") # Run until someone presses enter
