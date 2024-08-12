python main.py \
    --runner DataflowRunner \
    --project your-project-id \
    --region us-central1 \
    --temp_location gs://your-bucket/temp \
    --staging_location gs://your-bucket/staging \
    --setup_file ./setup.py \
    --extra_package gs://your-bucket-name/packages/mypackage-0.1.tar.gz
