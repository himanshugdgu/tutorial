import streamlit as st
import cv2
import tempfile
import os

def main():
    # Set page title
    st.set_page_config(page_title="Camera Video", page_icon="📹")
    # Set app title
    st.title("Camera Video")
    
    # Check if camera permission is granted
    if st.button("Check Camera Permission"):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            st.warning("Unable to access camera.")
        else:
            st.success("Camera permission granted.")
        cap.release()
    
    # Create a list of camera devices
    devices = []
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            devices.append(i)
        cap.release()
    
    # Check if there are any camera devices available
    if not devices:
        st.warning("No camera devices found.")
        return
    
    # Select camera device
    device = st.selectbox("Select camera device", devices)
    
    # Open camera
    cap = cv2.VideoCapture(device)
    
    # Check if camera is opened
    if not cap.isOpened():
        st.warning("Unable to access camera.")
        return
    
    # Create a button to capture image
    if st.button("Capture Image"):
        # Capture image
        ret, frame = cap.read()
        
        # Check if image is captured
        if not ret:
            st.warning("Unable to capture image.")
            return
        
        # Create a temporary file to store image
        with tempfile.NamedTemporaryFile(delete=False) as f:
            filename = f.name + ".jpg"
            cv2.imwrite(filename, frame)
            st.success("Image captured.")
        
        # Display last captured image
        if os.path.exists(filename):
            st.image(filename, use_column_width=True)
    
    # Create a loop to show video stream
    video = st.empty()
    while True:
        # Read frame from camera
        ret, frame = cap.read()
        
        # Check if frame is read
        if not ret:
            st.warning("Unable to read frame.")
            break
        
        # Convert frame to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Display frame
        video.image(frame, channels="RGB")
    
    # Release camera
    cap.release()

if __name__ == "__main__":
    main()
