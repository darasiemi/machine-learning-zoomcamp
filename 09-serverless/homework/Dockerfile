# FROM agrigorev/model-2025-hairstyle:v1 AS modelbase

# FROM agrigorev/model-2025-hairstyle:v1
# RUN pip install onnxruntime keras-image-helper

# WORKDIR /code
# COPY --from=modelbase ./hair_classifier_empty.onnx /code/hair_classifier_empty.onnx

# COPY lambda_function.py ./

# CMD ["lambda_function.lambda_handler"]

FROM agrigorev/model-2025-hairstyle:v1

# Install extra Python packages
RUN pip install --no-cache-dir onnxruntime pillow numpy

# The model file hair_classifier_empty.onnx is already in the
# current WORKDIR of this image – no need to copy it.

# Add your lambda handler code
COPY lambda_function.py .

# Lambda entrypoint
CMD ["lambda_function.lambda_handler"]
