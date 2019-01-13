nvidia-docker build -t nvtfcu10 -f Dockerfile.gpu ./ --build-arg SSH_KEY="$(cat ~/.ssh/id_rsa.pub)"
