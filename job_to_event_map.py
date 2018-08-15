def zero():
        jd={
        "jobName": "job1",
        "jobQueue": "arn:aws:batch:us-east-1:ACCT:job-queue/yourjobqueue",
        "jobDefinition": "arn:aws:batch:us-east-1:ACCT:job-definition/jobdef"
       }

        return jd
def one():
        jd={
        "jobName": "Job2",
        "jobQueue": "arn:aws:batch:us-east-1:ACCT:job-queue/yourjobqueue",
        "jobDefinition": "arn:aws:batch:us-east-1:ACCT:job-definition/jobdef"
       }

        return jd

def two():
        jd={
        "jobName": "Job3",
        "jobQueue": "arn:aws:batch:us-east-1:ACCT:job-queue/yourjobqueue",
        "jobDefinition": "arn:aws:batch:us-east-1:ACCT:job-definition/jobdef"
       }
def three():
        jd={
        "jobName": "Job4",
        "jobQueue": "arn:aws:batch:us-east-1:ACCT:job-queue/yourjobqueue",
        "jobDefinition": "arn:aws:batch:us-east-1:ACCT:job-definition/jobdef"
       }
        return jd

switcher = {
        0: zero,
        1: one,
        2: two,
        3:three
    }

print(' Test the Switch mapping ')
def evnt_to_jobs(eid):
    # Get the function from switcher dictionary
    func = switcher.get(eid, "nothing")
    # Execute the function
    return func()
