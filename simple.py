import tempfile
import streamlit as st
import cv2
import numpy as np


def main():
    st.set_page_config(page_title="Video")
    # define side bar and upload all types of images only
    st.sidebar.title("Student images with name")
    st.sidebar.markdown("Upload images of students")
    uploaded_file = st.sidebar.file_uploader(
        "Choose a file", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        # convert the file to an opencv image.
        file_bytes = np.asarray(
            bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        # Now do something with the image! For example, let's display it:
        st.image(opencv_image, channels="BGR")

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

            # display image
            st.image(filename, channels="BGR")

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


global cap
cap = cv2.VideoCapture(2)

if __name__ == "__main__":

    main()
