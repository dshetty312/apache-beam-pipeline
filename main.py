import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

# Import our custom package
from mypackage.processor import process_data

class CustomOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_value_provider_argument('--input', default='gs://your-bucket/input.txt')
        parser.add_value_provider_argument('--output', default='gs://your-bucket/output.txt')

def run():
    pipeline_options = PipelineOptions()
    custom_options = pipeline_options.view_as(CustomOptions)

    p = beam.Pipeline(options=pipeline_options)

    (p
     | 'ReadInput' >> beam.io.ReadFromText(custom_options.input)
     | 'ProcessData' >> beam.Map(process_data)
     | 'WriteOutput' >> beam.io.WriteToText(custom_options.output)
    )

    result = p.run()
    result.wait_until_finish()

if __name__ == '__main__':
    run()
