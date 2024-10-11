import cv2
import gradio as gr


def swapChannel(img: cv2.Mat) -> cv2.Mat:
    b, g, r = cv2.split(img)
    return cv2.merge([r, g, b])


def runGr():
    gr_instance = gr.Interface(swapChannel, gr.Image(), gr.Image())
    gr_instance.launch(share=True)
