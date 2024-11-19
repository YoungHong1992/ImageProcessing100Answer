import cv2
import gradio as gr


def swapChannel(img: cv2.Mat) -> cv2.Mat:
    b, g, r = cv2.split(img)  # OpenCV中图像通道是BGR排布，计算机显示时是RGB排布
    return cv2.merge([r, g, b])  # OpenCV获取到色彩通道后，交换R/B通道即可


if __name__ == "__main__":
    with gr.Blocks() as demo:
        gr.Markdown("""
        # 读取图像，然后将RGB通道替换成BGR通道(交换R/B通道)
        """)
        in_img = gr.Image()
        out_img = gr.Image()
        btn = gr.Button("转换")
        btn.click(swapChannel, inputs=in_img, outputs=out_img)
    demo.launch(share=False)
