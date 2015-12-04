import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_preview()
    camera.xposure_compensation = 2
    camera.exposure_mode = 'spotlight'
    camera.meter_mode = 'matrix'
    camera.vflip = 'true'
    # camera.image_effect = 'film'
    # Give the camera some time to adjust to conditions
    time.sleep(30)
    # camera.capture('foo.jpg')
    camera.stop_preview()
