from prefect.infrastructure.container import DockerContainer

# alternative to creating DockerContainer block in the UI
docker_block = DockerContainer(
    image = "discdiver/prefect:zoom",
    image_pull_policy = 'ALWAYS',
    auto_remove = True,
)

docker_block.save('zoom1', overwrite=True)