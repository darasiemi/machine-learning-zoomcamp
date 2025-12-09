# FROM public.ecr.aws/lambda/python:3.13
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# COPY pyproject.toml uv.lock ./
# RUN uv pip install --system -r <(uv export --format requirements-txt)

# COPY lambda_function.py model.bin ./

# CMD ["lambda_function.lambda_handler"]

# Use AWS Lambda Python runtime
FROM public.ecr.aws/lambda/python:3.12

# Optional: add uv for dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /var/task

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN uv export --format=requirements-txt --no-hashes -o requirements.txt \
 && python -m pip install --no-cache-dir -r requirements.txt -t .

# Copy your code and model
COPY lambda_function.py model.bin ./

# ✅ Explicitly set handler and environment
ENV _HANDLER=lambda_function.lambda_handler
CMD ["lambda_function.lambda_handler"]
