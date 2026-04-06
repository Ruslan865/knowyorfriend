# main.py
# Professional skeleton for KnovYourFrend app

from modules.camera import Camera
from modules.overlay import Overlay
from modules.audio import AudioPlayer

def main():
    print("KnovYourFrend app started!")

    # Kamera sistemi
    cam = Camera()
    cam.start_preview()

    # Overlay sistemi (GIF)
    ov = Overlay()

    # Audio sistemi
    au = AudioPlayer()

    # App loop
    try:
        while True:
            # Kamera frame al
            frame = cam.get_frame()

            # GIF overlay yoxla
            ov.update(frame)

            # Audio yoxla / oynat
            au.update()

            # Burada GUI və ya Kivy event loop ilə birləşdirilə bilər
            # Hələ minimal skeleton, funksionallığı sonradan əlavə edəcəyik

    except KeyboardInterrupt:
        print("App stopped by user")

if __name__ == "__main__":
    main()
