# -*- coding: utf-8 -*-

# Sample Python code for youtube.liveBroadcasts.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import datetime
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_246499621476-2gqk0ubjch8stn32p9rnnlkgieqo6bds.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)


    start = datetime.datetime.now().isoformat()
    print(start)
    end = datetime.datetime.now().isoformat()
    print(end)
    request = youtube.liveBroadcasts().insert(
        body={
            "snippet": {
                "title": "Test broadcast",
                "scheduledStartTime": '2022-5-9T00:00:00.000Z',
                "scheduledEndTime": '2022-5-10T00:00:00.000Z'
            },
            "contentDetails": {
                "enableClosedCaptions": True,
                "enableContentEncryption": True,
                "enableDvr": True,
                "enableEmbed": True,
                "recordFromStart": True,
                "startWithSlate": True
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        part="snippet,contentDetails,status"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()