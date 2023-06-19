import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
import glob
from PIL import Image
import skimage.io as io
import skimage.transform as trans
from keras.models import *
import scipy.ndimage

def get_frames(video_path, dst_path):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error opening video file")
        return
        
    # Get some video properties
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Create the output directory if it doesn't exist
    os.makedirs(dst_path, exist_ok=True)
    
    # Loop through all frames
    for frame_index in range(frame_count):
        # Read the next frame from the video
        ret, frame = cap.read()

        if not ret:
            print(f"Error reading frame {frame_index}")
            continue

        # Save the frame as an image
        frame_path = os.path.join(dst_path, f"frame_{frame_index:04d}.jpg")
        cv2.imwrite(frame_path, frame)

    # Release the video file and close any open windows
    cap.release()
    cv2.destroyAllWindows()
    
def get_results_from_video(video_path, model_path):
    model = load_model(model_path)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    video_name = os.path.basename(video_path)
    video_name = video_name.split(".")[0]

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        exit()

    i = 0
    a = 0        
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        i += 1
        a += 1
        
        width, height = frame.shape[1], frame.shape[0]
        # If the frame was not read correctly or end of video is reached, break the loop
        if not ret:
            break
        
        if i == 10:
            i=0
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resize_frame = trans.resize(gray, (128, 128))
            gray = gray / 255
            img = trans.resize(gray,(128, 128, 1))
            
            print("imgshape:", img.shape)
            # Perform segmentation
            segmented_image = model.predict(np.expand_dims(img, axis=0))
            segmented_image = np.squeeze(segmented_image)  # Remove the batch dimension if present
            print("segmentedshape:", segmented_image.shape)
            print("segmenteddtype", segmented_image.dtype)
            #mask = np.where(segmented_image > 0.3, 255, 0).astype(np.float64)
            
            print(resize_frame.dtype)
            #print(mask.dtype)
            crop = np.zeros(segmented_image.shape)
            print("cropshape1:", crop.shape)
            
            for ix, x in enumerate(segmented_image):
                for iy, y in enumerate(x):
                    if y > 0.3:
                        crop[ix, iy] = img[ix, iy]
            
            cv2.imshow("crop", crop)         
            cv2.imshow("Segmented", segmented_image)
            cv2.imshow("Frame", resize_frame)

            os.makedirs("./result_frames/"+video_name+"/crop/", exist_ok=True)
            os.makedirs("./result_frames/"+video_name+"/segmented/", exist_ok=True)
            os.makedirs("./result_frames/"+video_name+"/resize/", exist_ok=True)
            
            cv2.imwrite("./result_frames/"+video_name+"/crop/" + str(a) + ".jpg", crop)        
            cv2.imwrite("./result_frames/"+video_name+"/segmented/" + str(a) + ".jpg", segmented_image)
            cv2.imwrite("./result_frames/"+video_name+"/resize/" + str(a) + ".jpg", resize_frame)

        # Wait for 'q' key to be pressed to exit
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the video capture object and close any open windows
    cap.release()
    cv2.destroyAllWindows()
    
    
def get_result_from_image(model_path, image_path):
    model = load_model(model_path)
    
    img = cv2.imread(image_path)    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resize_frame = trans.resize(gray, (128, 128))
    gray = gray / 255
    img = trans.resize(gray,(128, 128, 1))
    
    print("imgshape:", img.shape)
    # Perform segmentation
    segmented_image = model.predict(np.expand_dims(img, axis=0))
    segmented_image = np.squeeze(segmented_image)  # Remove the batch dimension if present
    print("segmentedshape:", segmented_image.shape)
    print("segmenteddtype", segmented_image.dtype)
    #mask = np.where(segmented_image > 0.3, 255, 0).astype(np.float64)
    
    print(resize_frame.dtype)
    #print(mask.dtype)
    crop = np.zeros(segmented_image.shape)
    print("cropshape1:", crop.shape)
    
    for ix, x in enumerate(segmented_image):
        for iy, y in enumerate(x):
            if y > 0.3:
                crop[ix, iy] = img[ix, iy]
    
    cv2.imshow("crop", crop)         
    cv2.imshow("Segmented", segmented_image)
    cv2.imshow("Frame", resize_frame)

    os.makedirs("./result_frames/"+image_path+"/crop/", exist_ok=True)
    os.makedirs("./result_frames/"+image_path+"/segmented/", exist_ok=True)
    os.makedirs("./result_frames/"+image_path+"/resize/", exist_ok=True)
    
    cv2.imwrite("./result_frames/"+image_path+"/crop/" + str(a) + ".jpg", crop)        
    cv2.imwrite("./result_frames/"+image_path+"/segmented/" + str(a) + ".jpg", segmented_image)
    cv2.imwrite("./result_frames/"+image_path+"/resize/" + str(a) + ".jpg", resize_frame)
    
    
# Test_videos klasöründeki tüm videların tüm karelerini ilgili klasöre kaydeder.
'''
get_frames("./test_videos/CIMG9438.AVI", "./video_frames/video1/")
get_frames("./test_videos/DASHCAMCropped.mp4", "./video_frames/video2/")
get_frames("./test_videos/Pothole.mp4", "./video_frames/video3/")
get_frames("./test_videos/potholes-dashcam.mp4", "./video_frames/video4/")
'''    

# Modele video eklemeye yarar
# model_path olarak eğitilmiş modellerden birini seçebilirsiniz
# video_path olarak istedğiniz farklı bir video yolu girebilirsiniz
get_results_from_video(model_path="./trained_models/model128amagenyok.h5", video_path="./test_videos/CIMG9438.AVI")


# Modele tek bir resim yükler ve sonucu döndürür
# model_path olarak eğitilmiş modellerden birini seçebilirsiniz
# image_path olarak istedğiniz farklı bir resim yolu girebilirsiniz
'''
get_result_from_image(model_path="./trained_models/model128amagenyok.h5", image_path="./test_images/1.jpg")
'''

