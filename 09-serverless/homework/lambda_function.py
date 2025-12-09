from io import BytesIO
from urllib import request

from PIL import Image
import numpy as np
import onnxruntime as ort

IMAGENET_MEAN = np.array([0.485, 0.456, 0.406], dtype="float32")
IMAGENET_STD  = np.array([0.229, 0.224, 0.225], dtype="float32")

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def preprocess_image(url):
    """
    image_bytes: raw bytes of an image (e.g. from requests.get(url).content)
    returns: numpy array of shape (1, 3, 200, 200) ready for model input
    """

    # 1) Load and convert to RGB
    img = download_image(url)

    # 2) Resize to 200x200  (same as transforms.Resize((200, 200)))
    img = prepare_image(img, (200,200))

    # 3) To "tensor": HWC float32 in [0,1]
    x = np.asarray(img, dtype="float32") / 255.0  # shape (200, 200, 3)

    # 4) Normalize with ImageNet mean/std (channel-wise, broadcast on last dim)
    x = (x - IMAGENET_MEAN) / IMAGENET_STD       # still (200, 200, 3)

    # 5) Channels-first (C, H, W) like torch.Tensor
    x = np.transpose(x, (2, 0, 1))               # (3, 200, 200)

    # 6) Add batch dimension: (1, 3, 200, 200)
    x = np.expand_dims(x, axis=0)

    return x

# preprocessor = create_preprocessor(preprocess_pytorch, target_size=(224, 224))


session = ort.InferenceSession(
    "hair_classifier_empty.onnx", providers=["CPUExecutionProvider"]
)
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name



def predict(url):
    X = preprocess_image(url)
    result = session.run([output_name], {input_name: X})
    float_prediction = result[0][0].tolist()
    return float_prediction


def lambda_handler(event, context):
    url = event["url"]
    result = predict(url)
    return result

if __name__ == "__main__":
    url = "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"
    pred = predict(url)
    print(pred)
    # print(x)