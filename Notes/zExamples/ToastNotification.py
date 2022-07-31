import time
from winotify import Notification, audio

toast = Notification(app_id="ToastNotification",
                     title="Title",
                     msg="Totification test",
                     duration="long",
                     icon=r"C:\Users\super\Desktop\Giovanni\Programacion\Resources\CheckmarkIcon.webp")

toast.add_actions(label="Button text", launch="https://github.com/versa-syahptr/winotify/")
toast.add_actions(label="Button text2", launch="https://github.com/versa-syahptr/winotify/")

toast.set_audio(audio.Mail, loop=False)
toast.show()
