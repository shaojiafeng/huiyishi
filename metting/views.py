from django.shortcuts import render
from metting import models
from django.http import JsonResponse
import json



# Create your views here.
def login(request):
    if request.method=="GET":
        return render(request,"login.html")
def index(request):
    if request.method=="GET":
        meeting_scheduled_list=models.Meeting_scheduled.time_choice
        # metting_Rom=models.Meeting_scheduled.objects.all()
        return render(request,"index.html",{"meeting_scheduled_list":meeting_scheduled_list})
def booking(request):
    if request.method == 'GET':
        response={'status':True,'msg':None,'data':None}
        try:
            import datetime
            current_date=datetime.datetime.now().date()
            choice_date=request.GET.get("choice_date")
            choice_date = datetime.datetime.strptime(choice_date, '%Y-%m-%d').date()
            if choice_date<current_date:
                raise Exception("日期必须大于等于当前时间")
            # 获取预订信息
            '这一天会议室所有的预订信息'
            booking_list=models.Meeting_scheduled.objects.filter(date=choice_date)
            booking_dict={}
            for item in booking_list:
                if item.metting_id not in booking_dict:
                    booking_dict[item.metting_id]={item.time_quantum:{"username":item.user.username,"user_id":item.user_id}}
                else:
                    booking_dict[item.metting_id][item.time_quantum]={"username":item.user.username,"user_id":item.user_id}
            mettingRom_list=models.MettingRom.objects.all()
            data=[]
            for mettingRom in mettingRom_list:
                tr=[]
                tr.append({"text":mettingRom.caption,"attrs":{}})
                for time in models.Meeting_scheduled.time_choice:
                    if mettingRom.id in booking_dict and time[0] in booking_dict[mettingRom.id]:
                        td={"text":booking_dict[mettingRom.id][time[0]]["username"],"attrs":{"mettingRom_id":mettingRom.id,"time_id":time[0],'class':'chosen'}}
                    else:
                        td={"text":"","attrs":{"mettingRom_id":mettingRom.id,"time_id":time[0]}}
                    tr.append(td)
                data.append(tr)
            response["data"]=data
        except Exception as e:
            response["status"]=False
            response["msg"]=str(e)
        return JsonResponse(response)
