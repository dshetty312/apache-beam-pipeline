# Package the application
Run the following command to create a distributable package:
Copypython setup.py sdist

Upload the package to a Google Cloud Storage bucket:
gsutil cp dist/mypackage-0.1.tar.gz gs://your-bucket-name/packages/

# Run the beam pipeline
python main.py \
    --runner DataflowRunner \
    --project your-project-id \
    --region us-central1 \
    --temp_location gs://your-bucket/temp \
    --staging_location gs://your-bucket/staging \
    --setup_file ./setup.py \
    --extra_package gs://your-bucket-name/packages/mypackage-0.1.tar.gz
