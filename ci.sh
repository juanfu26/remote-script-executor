# Create the builder instance to use
docker buildx create --use

# BUILD multiarch image with BAKE
COMMAND="docker buildx bake --push"
echo $COMMAND
eval $COMMAND