FROM python:3.13-alpine@sha256:bb2c06f24622d10187d0884b5b0a66426a9c8511c344492ed61b5d382bd6018c

LABEL maintainer="gautrot"
LABEL description="Image Python 3.13 sous Alpine Linux"
LABEL version=1.0.0
LABEL authors="gautrot"

WORKDIR /app

RUN apk add --no-cache make

COPY . .
RUN make init

CMD ["make", "run"]
