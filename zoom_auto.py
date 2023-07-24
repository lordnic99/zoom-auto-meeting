import subprocess
import csv
import pyautogui
import time
import pyperclip

is_zoom_started     = False
zoom_exe_path       = "C:\\Users\\HOANG\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
zoom_data_path      = "C:\\Users\\HOANG\\Desktop\\room_info.csv"
zoom_join_png       = "C:\\Users\\HOANG\\Desktop\\zoom_join.png"
zoom_meeting_join   = "C:\\Users\\HOANG\\Desktop\\zoom_meeting_join.png"
zoom_meeting_join2  = "C:\\Users\\HOANG\\Desktop\\zoom_meeting_join_2.png"

def start_zoom(zoom_exe_path):
    subprocess.Popen(zoom_exe_path)
    is_zoom_started = True
    
def get_zoom_info(data_file):
    with open(data_file) as f:
        csv_f = csv.reader(f)
        csv_f = list(csv_f)
        return csv_f[0][0], csv_f[0][1]
    
def pyautogui_click_on(png_sample):
    pyautogui.click(png_sample)
    time.sleep(5)
    
def copy_and_paste(data):
    pyperclip.copy(data)
    pyautogui.hotkey("ctrl","v")
    time.sleep(5)
    
if __name__ == "__main__":
    start_zoom(zoom_exe_path)
    if is_zoom_started:
        print("INFO: Zoom is started!")
    
    print("INFO: Waiting for Zoom start completely!")
    time.sleep(15)
    id, password = get_zoom_info(zoom_data_path)
    print(f"INFO: id = {id}, password = {password}")
    
    pyautogui_click_on(zoom_join_png)
    print("INFO: Join meeting button was clicked!")
    copy_and_paste(id)
    pyautogui_click_on(zoom_meeting_join)
    
    copy_and_paste(password)
    pyautogui_click_on(zoom_meeting_join2)
    print("INFO: All working are done completely!")
    
    