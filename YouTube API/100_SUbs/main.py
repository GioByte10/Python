# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import time

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)


    request = youtube.channels().list(
        part="statistics",
        id="UCyzE4BoCBWV9lTgeujvk8_w"
    )
    response = request.execute()
    subscriberCount = int(response["items"][0]["statistics"]["subscriberCount"])
    print("Gracias por " + str(subscriberCount) + " suscriptores!")

    request = youtube.subscriptions().list(
        part="subscriberSnippet",
        maxResults=100,
        mySubscribers=True
    )
    response = request.execute()
    publicSubscribers = response['pageInfo']['totalResults']

    for i in range(publicSubscribers):
        print(str(i + 1) + "  Gracias " + response['items'][i]['subscriberSnippet']['title'])
        time.sleep(0.4)

    for i in range(subscriberCount - publicSubscribers):
        print(str(i + 1 + publicSubscribers) + " Gracias anonimo")
        time.sleep(0.1)





if __name__ == "__main__":
    main()
