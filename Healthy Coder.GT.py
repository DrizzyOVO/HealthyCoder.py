# from pygame import mixer
# from datetime import datetime
# from time import time
#
#
# def musiconloop(file, stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#
#     while True:
#         a = input("Enter here")
#         if a == stopper:
#             mixer.music.stop()
#             break
#         else:
#             print("Enter according to the info given")
#
# def log(msg):
#     with open("HealthyCoderGT.txt", "a") as op:
#         op.write(f"{msg} {datetime.now()}\n")
#
# if __name__=='__main__':
#     ini_water = time()
#     ini_eyes = time()
#     ini_exercise = time()
#     watime = 3600
#     eytime = 1800
#     extime = 2700
#     totwa = 0
#     totey = 0
#     totex = 0
#
#     while True:
#
#         if time() - ini_water > watime:
#             print("Water drinking time, drink 0.4Ls for maintaining good health, type 'drank' to stop")
#             musiconloop("Water.mp3.mp3", "drank")
#             log("Drank 0.4ls Water at ")
#             ini_water = time()
#             totwa = totwa + 1
#             if totwa == 8:
#                 break
#
#         elif time() - ini_eyes > eytime:
#             print("Water drinking time, type 'eyedone' to stop")
#             musiconloop('Eyes.mp3.mp3', 'eyedone')
#             log("Eyes relaxed at ")
#             ini_eyes = time()
#             totey = totey + 1
#             if totey == 16:
#                 break
#
#         elif time() - ini_exercise > extime:
#             print("Water drinking time, type 'exed' to stop")
#             musiconloop('Exercise.mp3.mp3', 'exed')
#             log("Warmup at ")
#             ini_exercise = time()
#             totex = totex + 1
#             if totex == 10:
#                 break



