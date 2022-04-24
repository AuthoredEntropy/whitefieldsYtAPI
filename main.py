import tkinter as tk
import tkinter.font as tkFont
import datetime
import tkbuilder as tkb
from tkinter.messagebox import askyesno
import ytAPIInterface as yt
import json
import os
import pickle
import datetime
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request
def returnConfig():
    with open('./userConfig.json') as f:
        data = json.load(f)
        return data
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
userConfig = returnConfig()
client_secrets_file = "client_secret_246499621476-2gqk0ubjch8stn32p9rnnlkgieqo6bds.apps.googleusercontent.com.json"

credentials = None
if( os.path.exists('token.pickle')):
    print("Loading Credentials From File")
    with open('token.pickle', 'rb') as token:
        credentials = pickle.load(token)
        
# If there are no valid credentials available, then either refresh the token or log in.
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        print('Refreshing Access Token...')
        credentials.refresh(Request())
    else:
        print('Fetching New Tokens...')
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            'client_secret_246499621476-2gqk0ubjch8stn32p9rnnlkgieqo6bds.apps.googleusercontent.com.json',
            scopes=["https://www.googleapis.com/auth/youtube.force-ssl"]
        )

        flow.run_local_server(port=8080, prompt='consent',
                              authorization_prompt_message='')
        credentials = flow.credentials

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as f:
            print('Saving Credentials for Future Use...')
            pickle.dump(credentials, f)
            
def main():
    root = tk.Tk()
    root.title("White Field's Church Youtube Interface")
    root.geometry("850x500")
    assembleGUI(root)
    root.mainloop()
    
def setText(e,text):
    e.delete(0,"end")
    e.insert(0,text)
    return
def createTitle(service,title):
    for x in range(2):
        for i in range(len(userConfig['whiteFieldsAltNames'])):
            if(x == 0):
                serviceTitle  = title + "- First Service -"
                if(service == 2):
                    serviceTitle =  title + "- Second Service -"
            else:
                serviceTitle  = title + "- 1st Service -"
                if(service == 2):
                    serviceTitle =  title + "- 2nd Service -"
            combinedTitle = serviceTitle + userConfig['whiteFieldsAltNames'][i]
            if(len(combinedTitle) <= 100):
                return combinedTitle
    if(len(serviceTitle) <= 100):
        return serviceTitle
    elif(len(title) <= 100):
        return title
    else:
        return title[:99]
def formatTime(time):
    today = (datetime.datetime.now(datetime.timezone.utc).isoformat())[:19]+"-07:00"
    finalDate = today[:10] + "T" + time + today[16:]
    return finalDate

def scheduleLiveStreams(data):
    baseTitle = data[0]
    description = data[1]
    privicy = data[2]
    start1 = formatTime(data[3])
    start2 = formatTime(data[4])
    end1 = formatTime(data[5])
    end2 = formatTime(data[6])
    title1 = createTitle(1,baseTitle)
    title2 = createTitle(2,baseTitle)
    print(start1)
    print(end1)
    res1 = yt.scheduleLive(title1,start1,end1,privicy,description,credentials)
    res2 = yt.scheduleLive(title2,start2,end2,privicy,description,credentials)
    with open('responses.pickle', 'wb') as f:
            print('Saving Stream IDs...')
            pickle.dump([res1,res2], f)
            
def loadDefaultValues(end1,end2,start1,start2,privicy,title,desc):
    setText(title,userConfig["defaultTitle"])
    desc.delete(1.0,"end")
    desc.insert(1.0,userConfig["defaultDescription"])
    setText(start1,userConfig['defaultFirstServiceStartTime'])
    setText(start2,userConfig['defaultSecondServiceStartTime'])
    setText(end1,userConfig['defaultFirstServiceEndTime'])
    setText(end2,userConfig['defaultSecondServiceEndTime'])
    setText(privicy,userConfig['defaultPrivacySetting'])
    
def publicizeStreams():
    resArr =None
    with open('responses.pickle', 'rb') as res:
        resArr = pickle.load(res)
    id1 = resArr[0]["id"]
    id2 = resArr[1]["id"]
    yt.updateLive(credentials,id1,"public")
    yt.updateLive(credentials,id2,"public")
    
def unlistStreams():
    resArr =None
    with open('responses.pickle', 'rb') as res:
        resArr = pickle.load(res)
    id1 = resArr[0]["id"]
    id2 = resArr[1]["id"]
    yt.updateLive(credentials,id1,"unlisted")
    yt.updateLive(credentials,id2,"unlisted")

def privateStreams():
    resArr =None
    with open('responses.pickle', 'rb') as res:
        resArr = pickle.load(res)
    id1 = resArr[0]["id"]
    id2 = resArr[1]["id"]
    yt.updateLive(credentials,id1,"private")
    yt.updateLive(credentials,id2,"private")
    
def deleteStreams():
    resArr =None
    with open('responses.pickle', 'rb') as res:
        resArr = pickle.load(res)
    id1 = resArr[0]["id"]
    id2 = resArr[1]["id"]
    answer = askyesno(title='confirmation',
                    message='Are you sure that you want to delete both streams permanently?')
    if answer:
        yt.deleteLive(credentials,id1)
        yt.deleteLive(credentials,id2)
def logout():
    os.remove("token.pickle")
    exit(0)
def assembleGUI(root):
    frame = tk.Frame(root)
    spacerl = tkb.addHorizontalSpacer(frame,10)
    spacerr = tkb.addHorizontalSpacer(frame,10,"right")
    btnFrame = tk.Frame(frame)
    inputFrame =tk.Frame(frame)
    tkb.addHorizontalSpacer(inputFrame,10,"right")
    btnFrame.pack(side="left",anchor="n")
    spacerh2 = tkb.addVerticalSpacer(btnFrame,5)
    spacerl2 = tkb.addHorizontalSpacer(frame,10)
    inputFrame.pack(side="left",anchor="n")
    spacerh = tkb.addVerticalSpacer(inputFrame,5)
    btnFrame2 = tk.Frame(frame,width=300,height=300)
    btnFrame2.pack_propagate(0)
    btnFrame2.pack(side="left")
    spacerh4 = tkb.addVerticalSpacer(btnFrame2,5)
    monoFont = tkFont.Font(family="DejaVu Sans Mono", size=16, weight="bold")
    descriptionFrame = tk.Frame(inputFrame)
    descriptionTextField = tk.Text(descriptionFrame,width=30,height=6)
    titleFrame = tk.Frame(inputFrame,pady=5)
    titleLabel = tkb.addLabel(titleFrame,"titleFrame","Title:",5,side="left")
    titleInput =tkb.addInput(titleFrame,False,40,26,False)
    privicy = ["public","unlisted","private"]
    privicyFrame = tk.Frame(inputFrame,pady=5)
    privicyLabel = tkb.addLabel(privicyFrame,"titleFrame","Visibility Settings:",5,side="left")
    privicyDropBox =tkb.addDropDown(privicyFrame,"visiblity",privicy,20)
    time = userConfig["allowedTimes"]
    startTimeFrame = tk.Frame(inputFrame,pady=5)
    startTimeLabel = tkb.addLabel(startTimeFrame,"titleFrame","1st service start time:",5,side="left")
    startTimeDropBox =tkb.addDropDown(startTimeFrame,"startTime",time,20)
    startTime2Frame = tk.Frame(inputFrame,pady=5)
    startTime2Label = tkb.addLabel(startTime2Frame,"titleFrame","2nd service start time:",5,side="left")
    startTime2DropBox =tkb.addDropDown(startTime2Frame,"start2Time",time,20)
    endTimeFrame = tk.Frame(inputFrame,pady=5)
    endTimeLabel = tkb.addLabel(endTimeFrame,"titleFrame","1st service end time:",5,side="left")
    endTimeDropBox =tkb.addDropDown(endTimeFrame,"endtime1",time,20)
    endTime2Frame = tk.Frame(inputFrame,pady=5)
    endTime2Label = tkb.addLabel(endTime2Frame,"titleFrame","2nd service end time:",5,side="left")
    endTime2DropBox =tkb.addDropDown(endTime2Frame,"endtime2",time,20)
    createLiveBtn = tk.Button(btnFrame,width=25,height=3,text="schedule live streams")
    createLiveBtn.pack(side="top",anchor="w")
    publicLiveBtn = tk.Button(btnFrame,width=25,height=3,text="publicize live streams",command=publicizeStreams)
    publicLiveBtn.pack(side="top",anchor="w")
    unlistLiveBtn = tk.Button(btnFrame,width=25,height=3,text="un-list live streams", command=unlistStreams)
    unlistLiveBtn.pack(side="top",anchor="w")
    privateLiveBtn = tk.Button(btnFrame,width=25,height=3,text="private live streams", command=privateStreams)
    privateLiveBtn.pack(side="top",anchor="w")
    deleteLiveBtn = tk.Button(btnFrame,width=25,height=3,text="delete live streams", command=deleteStreams)
    deleteLiveBtn.pack(side="top",anchor="w")
    spacerh3 = tkb.addVerticalSpacer(btnFrame,5)
    autoLiveBtn = tk.Button(btnFrame,width=25,height=3,text="Logout", command=logout)
    autoLiveBtn.pack(side="top",anchor="w")
    titleFrame.pack(side="top",anchor="w")
    descriptionFrame.pack(side="top",anchor="w")
    startTimeFrame.pack(side="top",anchor="w")
    startTime2Frame.pack(side="top",anchor="w")
    endTimeFrame.pack(side="top",anchor="w")
    endTime2Frame.pack(side="top",anchor="w")
    privicyFrame.pack(side="top",anchor="w")
    descriptionLabel = tkb.addLabel(descriptionFrame,"Description","Description:",0,side="left")
    descriptionTextField.pack(side="left")
    createLiveBtn.config(command=lambda: scheduleLiveStreams([titleInput.get(),descriptionTextField.get("1.0","end"),privicyDropBox.get(),startTimeDropBox.get(),startTime2DropBox.get(),endTimeDropBox.get(),endTime2DropBox.get()]))
    frame.pack(side="left",anchor="n")
    loadDefaultValues(endTimeDropBox,endTime2DropBox,startTimeDropBox,startTime2DropBox,privicyDropBox,titleInput,descriptionTextField)
    


if __name__ == '__main__':
    main()
    