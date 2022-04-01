import tkinter as tk
import tkinter.font as tkFont
import tkbuilder as tkb
def main():
    root = tk.Tk()
    root.title("White Field's Church Youtube Interface")
    root.geometry("750x750")
    assembleGUI(root)
    root.mainloop()

def scheduleLiveStreams(data):
    print(data)

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
    time = ["6:00am","6:30am","7:00am","7:30am","8:00am","8:30am","9:00am","9:30am","10:00am","10:30am","11:00am","11:30am","12:00am","12:30am","1:00pm","1:30pm"]
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
    publicLiveBtn = tk.Button(btnFrame,width=25,height=3,text="publicize live stream(s)")
    publicLiveBtn.pack(side="top",anchor="w")
    updateLiveBtn = tk.Button(btnFrame,width=25,height=3,text="update live stream(s)")
    updateLiveBtn.pack(side="top",anchor="w")
    spacerh3 = tkb.addVerticalSpacer(btnFrame,5)
    autoLiveBtn = tk.Button(btnFrame,width=25,height=3,text="Auto Publicize Streams: Off")
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
    createLiveBtn.config(command=lambda: scheduleLiveStreams([titleInput.get(),descriptionTextField.get("1.0","end")]))
    frame.pack(side="left",anchor="n")
    
    


if __name__ == '__main__':
    main()
    