import cv2
import gradio as gr


# 将图像灰度化, 可以用OpenCV内置函数，或自己实现
def cvGrayscale(img: cv2.Mat) -> cv2.Mat:
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def selfGrayscale(img: cv2.Mat) -> cv2.Mat:
    # Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
    b, g, r = cv2.split(img)  # 读取的数值范围是[0,255]整数
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b  # 求灰度值操作后，数值变为了浮点值
    gray = gray.astype("uint8")  # 再次恢复为[0,255]整数
    return gray


if __name__ == "__main__":
    with gr.Blocks() as demo:
        gr.Markdown("""
        # 将图像灰度化
        """)
        with gr.Row():
            in_img = gr.Image()
            with gr.Column():
                out_cv = gr.Image()
                btn = gr.Button("灰度化(OpenCV内置)")
                btn.click(cvGrayscale, inputs=in_img, outputs=out_cv)
            with gr.Column():
                out_self = gr.Image()
                btn_self = gr.Button("灰度化(自行实现)")
                btn_self.click(selfGrayscale, inputs=in_img, outputs=out_self)
    demo.launch(share=False)
