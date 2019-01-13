nvidia-docker build -t nvcu10pap:latest -f Dockerfile.gpu ./ --build-arg SSH_KEY="$(cat ~/.ssh/id_rsa.pub)"
