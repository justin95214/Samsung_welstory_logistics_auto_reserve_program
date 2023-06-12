import os
import datetime

def getfiles(dirpath,folder):
    filelist = [s for s in os.listdir(dirpath)
        if os.path.isfile(os.path.join(dirpath, s))]
    filelist.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)),reverse=True)
    print(filelist)
    recent_file = filelist[0]
    os.rename(dirpath+"\\"+recent_file,dirpath+"\\"+folder +"_"+ str(datetime.date.today())+".xlsx")


#folder = 'Order_Manage_Per_client_order_details_schedule'
#getfiles(os.getcwd()+"\\"+ folder,folder)

