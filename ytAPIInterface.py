# -*- coding: utf-8 -*-

# Sample Python code for youtube.liveBroadcasts.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import pickle
import datetime
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
#'2022-5-10T00:00:00.000Z'
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
def deleteLive(credentials,id):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_246499621476-2gqk0ubjch8stn32p9rnnlkgieqo6bds.apps.googleusercontent.com.json"

    
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    request = youtube.liveBroadcasts().delete(
        id=id
    )
    response = request.execute()

    return(response)

def updateLive(credentials,id,privicy):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_246499621476-2gqk0ubjch8stn32p9rnnlkgieqo6bds.apps.googleusercontent.com.json"

    
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    request = youtube.liveBroadcasts().update(
        part = "status",
        body = {
          "status": {
                "privacyStatus": privicy
            },
          "id": id
        }
    )
    response = request.execute()

    return(response)
    
def scheduleLive(title,scheduledStartTime,scheduledEndTime, privicySetting, desc, credentials):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_246499621476-2gqk0ubjch8stn32p9rnnlkgieqo6bds.apps.googleusercontent.com.json"

    
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.liveBroadcasts().insert(
        body={
            "snippet": {
                "description": desc,
                "title": title,
                "scheduledStartTime": scheduledStartTime,
                "scheduledEndTime": scheduledEndTime
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
                "privacyStatus": privicySetting
            }
        },
        part="snippet,contentDetails,status"
    )
    response = request.execute()
    return response
    #print(response)

if __name__ == '__main__':
    scheduleLive("teststream",'2022-04-24T30:16:46-07:00','2022-5-11T00:00:00.000Z',"unlisted","testDesc")
                             