if [ ! -f tests/docker_compose.yaml ]; then
    cp tests/docker_compose.example.yaml tests/docker_compose.yaml
fi

docker-compose -f tests/docker_compose.yaml up -d --no-deps --build