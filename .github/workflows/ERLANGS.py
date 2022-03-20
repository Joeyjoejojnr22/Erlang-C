import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def factorial(value):
    a=1
    for i in reversed(range(int(value))):
        a*=i
    if a==0:
        return 1
    else:
        return a

def erlangs(
    no_calls=100,#number of calls
    in_a_period_of_hours=0.5,#timeframe to normalise to one hour
    AHT_in_secs=180,#average handling time
    Required_service_level=0.80,#target service level system will auto graph the 
    Target_Answer_Time=20,#target time in seconds to answer, will be 60 for us
    Max_occupancy=0.85,#target occupancy, occupancy greater than 85% risks burn out as it requires staff to always be availaible
    shrinkage=0.3):#peole on break, holiday etc

    def factorial(value):
        a=1
        for i in range(int(value)):
            a=(i+1)*a
        if a==0:
            return 1
        else:
            return a
    def series(A,N):

        test=0
        for i in range(int(N)):
            FACT=factorial(i)
            POW=(A**i)
            
            test+=POW/FACT
            #print(test)
        return test

    no_calls/=in_a_period_of_hours#normallised per hour
    call_minutes=no_calls*(AHT_in_secs/60)#work out time
    call_intensity=call_minutes/60#erlangs in hour#
    A=call_intensity
    N=call_intensity+1

    SLA_per_person=[0]*int(N)
    total_staff=[]
    for i in range(int(N)):
        total_staff.append(i+1)
        

    probable_wait=0
    service_level=0
    average_speed_of_answer=0

    occupancy_over_time=[0]*int(N)
    immediate_answer_over_time=[0]*int(N)
    average_speed_of_answer_time=[0]*int(N)
    probable_wait_over_time=[0]*int(N)
    minimium_staff=[0]*int(N)

    AHT_impact=[]
    AHT_Service=[]
    

    while service_level < Required_service_level:
        N_FACTORIAL=factorial(N)
        A_POWER_n=A**N
        X=((A_POWER_n)/N_FACTORIAL)
        X*=N/(N-A)
        Y=series(A,N)
        
        probable_wait=X/(Y+X)

        service_level=1-(probable_wait*(2.71828**-((N-A)*(Target_Answer_Time/AHT_in_secs))))
        average_speed_of_answer=(probable_wait*AHT_in_secs)/(N-call_intensity)

        immediate_answer=(1-probable_wait)*100#percentage of calls answered immediately

        occupancy=(call_intensity/A)*100

        No_agents_required=N/(1-shrinkage)

        Min_agents=A+1

        SLA_per_person.append(service_level*100)

        N+=1

        total_staff.append(No_agents_required)

        occupancy_over_time.append(occupancy)
        immediate_answer_over_time.append(immediate_answer)
        average_speed_of_answer_time.append(average_speed_of_answer)
        probable_wait_over_time.append(probable_wait)
        minimium_staff.append(N)


    return (Min_agents,No_agents_required,occupancy,immediate_answer,average_speed_of_answer,probable_wait,
            minimium_staff,
            occupancy_over_time,
            immediate_answer_over_time,
            average_speed_of_answer_time,
            probable_wait_over_time,
            total_staff,
            SLA_per_person)


def erlangs_AHT(
    no_calls=100,#number of calls
    in_a_period_of_hours=0.5,#timeframe to normalise to one hour
    AHT_in_secs=180,#average handling time
    Required_service_level=0.80,#target service level system will auto graph the 
    Target_Answer_Time=20,#target time in seconds to answer, will be 60 for us
    Max_occupancy=0.85,#target occupancy, occupancy greater than 85% risks burn out as it requires staff to always be availaible
    shrinkage=0.3):#peole on break, holiday etc

    def factorial(value):
        a=1
        for i in range(int(value)):
            a=(i+1)*a
        if a==0:
            return 1
        else:
            return a
    def series(A,N):

        test=0
        for i in range(int(N)):
            FACT=factorial(i)
            POW=(A**i)
            
            test+=POW/FACT
            #print(test)
        return test

    no_calls/=in_a_period_of_hours#normallised per hour
    call_minutes=no_calls*(AHT_in_secs/60)#work out time
    call_intensity=call_minutes/60#erlangs in hour#
    A=call_intensity
    N=call_intensity+1

    SLA_per_person=[0]*int(N)
    total_staff=[]
    minimium_staff=[]
    for i in range(int(N)):
        minimium_staff.append(i+1)
        total_staff.append(i/(1-shrinkage))

    probable_wait=0
    service_level=0
    average_speed_of_answer=0

    occupancy_over_time=[0]*int(N)
    immediate_answer_over_time=[0]*int(N)
    average_speed_of_answer_time=[0]*int(N)
    probable_wait_over_time=[0]*int(N)
    

    AHT_impact=[]
    AHT_Service=[]
    

    while AHT_in_secs < Required_service_level:
        N_FACTORIAL=factorial(N)
        A_POWER_n=A**N
        X=((A_POWER_n)/N_FACTORIAL)
        X*=N/(N-A)
        Y=series(A,N)

        call_minutes=no_calls*(AHT_in_secs/60)#work out time
        
        probable_wait=X/(Y+X)

        service_level=1-(probable_wait*(2.71828**-((N-A)*(Target_Answer_Time/AHT_in_secs))))
        average_speed_of_answer=(probable_wait*AHT_in_secs)/(N-call_intensity)

        immediate_answer=(1-probable_wait)*100#percentage of calls answered immediately

        occupancy=(call_intensity/A)*100

        No_agents_required=N/(1-shrinkage)

        Min_agents=A+1

        AHT_impact.append(service_level*100)
        AHT_Service.append(AHT_in_secs)

        N+=1
        AHT_in_secs-=1




    return (AHT_Service,AHT_impact)

lisp=[]

for i in range(5):
    response=erlangs(
        no_calls=9389,#number of calls
        in_a_period_of_hours=112,#timeframe to normalise to one hour
        AHT_in_secs=463,#average handling time
        Required_service_level=(0.70+(i*0.05)),#target service level system will auto graph the 
        Target_Answer_Time=60,#target time in seconds to answer, will be 60 for us
        Max_occupancy=0.85,#target occupancy, occupancy greater than 85% risks burn out as it requires staff to always be availaible
        shrinkage=0.4
        )#peole on break, holiday etc
    print("*"*50)
    print("No AGENTS REQUIRED")
    print(response[1]*14)
    print("Percentage immediate answer")
    print(response[3])
    print("Average Speed Of Answer")
    print(response[4])
    print("Probable Wait")
    print(response[5])



datum={}
datum['SLA']=response[-1]
datum["staff count"]=response[-2]
datum["Probable Wait"]=response[-3]
datum["Average Speed Of Answer"]=response[-4]
datum["Immediate Answer"]=response[-5]
datum["Occupancy"]=response[-6]
datum["Minimium Staff"]=response[-7]
df = pd.DataFrame (datum)
sns.set_context("poster")
sns.relplot(data=df, x='staff count', y='SLA', kind='line')
plt.savefig('C:\\Data\\graphs\\ERLANGS\\ERLANGS_STAFF_REQUIREMENT_SLA.png')
plt.close()
sns.relplot(data=df, x='staff count', y='Probable Wait', kind='line')
plt.savefig('C:\\Data\\graphs\\ERLANGS\\ERLANGS_PROBABLE_WAIT_STAFF.png')
plt.close()
sns.relplot(data=df, x='staff count', y='Average Speed Of Answer', kind='line')
plt.savefig('C:\\Data\\graphs\\ERLANGS\\ERLANGS_AVG_SPEED_OF_ANSWER.png')
plt.close()
sns.relplot(data=df, x='staff count', y='Immediate Answer', kind='line')
plt.savefig('C:\\Data\\graphs\\ERLANGS\\IMMEDIATE_ANSWER_STAFF.png')
plt.close()
sns.relplot(data=df, x='Occupancy', y='SLA', kind='line')
plt.savefig('C:\\Data\\graphs\\ERLANGS\\OCCUPANCY_SLA.png')
plt.close()
sns.relplot(data=df, x='Minimium Staff', y='SLA', kind='line')
plt.savefig('C:\\Data\\graphs\\ERLANGS\\ERLANGS_MIN_STAFF_SLA.png')
plt.close()




        
    
