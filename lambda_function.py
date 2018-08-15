from __future__ import print_function
from  job_to_event_map  import evnt_to_jobs
import json
import boto3
import logging

def lambda_handler(event, context):
     logger = logging.getLogger()
     logger.setLevel(logging.INFO)
     logger.info('Initialise   aws batch client')
     batch = boto3.client('batch')
     logger.info("Received event: \n" + json.dumps(event, indent=2))
     logger.info('Log group name \n'+context.log_group_name)
     logger.info('Log Stream Name \n'+ context.log_stream_name)
     # Get parameters for the SubmitJob call
     eid=event['Eventid']
     #get jobcfg  Dictionary Object from eventID passed in event
     jobcfg=evnt_to_jobs(eid)
     jobName = jobcfg['jobName']
     jobQueue = jobcfg['jobQueue']
     jobDefinition = jobcfg['jobDefinition']
    # containerOverrides and parameters are optional
     if event.get('containerOverrides'):
         containerOverrides = event['containerOverrides']
     else:
         containerOverrides = {}
     if event.get('parameters'):
         parameters = event['parameters']
     else:
         parameters = {}
         logger.info("Invoking Batch Submit Command with values\n" )
         logger.info("jobQueue="+jobQueue+ "\tjobName="+jobName+"\t jobDefinition="+jobDefinition )

     try:
        # Submit a Batch Job
        response = batch.submit_job(jobQueue=jobQueue, jobName=jobName, jobDefinition=jobDefinition,
                                    containerOverrides=containerOverrides, parameters=parameters)
        # Log response from AWS Batch
        logger.info("Response: " + json.dumps(response, indent=2))
        # Return the jobId
        jobId = response['jobId']
        return {
           'jobId': jobId
        }
     except Exception as e:
        print(e)
        message = 'Error submitting Batch Job'
        logger.error(message)
        raise Exception(message)

     return s
