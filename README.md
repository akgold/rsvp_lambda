# A small function to run on AWS lambda to allow RSVPs to a google doc

Makes use of the [gspread](https://github.com/burnash/gspread) API.

In order to authorize google sheets, follow [these instructions](http://gspread.readthedocs.io/en/latest/oauth2.html) to get json of API key. Then save as credentials.json in root directory of app. 

Make sure to use service account keys rather than OauthClientIDs or API Keys.

In order to run, you'll need to follow these steps:

In directory with script:
```
pip install gspread -t .
pip install oauth2client -t .
```

Zip the file using 
`zip -r deploy.zip *`

Upload zip file to lambda.
