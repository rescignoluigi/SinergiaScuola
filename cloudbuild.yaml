serviceAccount: "projects/sinergiascuola-backend-v2/serviceAccounts/sinergia-backend@sinergiascuola-backend-v2.iam.gserviceaccount.com"

options:
  logging: CLOUD_LOGGING_ONLY
  defaultLogsBucketBehavior: REGIONAL_USER_OWNED_BUCKET

steps:
  - name: "gcr.io/cloud-builders/docker"
    dir: "."
    args:
      - "build"
      - "-t"
      - "europe-west8-docker.pkg.dev/sinergiascuola-backend-v2/backend/backend-image:$COMMIT_SHA"
      - "-f"
      - "Dockerfile"
      - "."

images:
  - "europe-west8-docker.pkg.dev/sinergiascuola-backend-v2/backend/backend-image:$COMMIT_SHA"
