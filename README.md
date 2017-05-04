# A small function to run on AWS lambda to allow RSVPs to a google doc

In order to run, you'll need to follow these steps:

In directory with script:
pip install gspread, oauth2client -t .

Make config file consisting of
```
keys = "googlesheetsapikey"
```

Zip file and deploy to lambda.
