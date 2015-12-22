import pandas as pd
import math
import itertools

north_pole = (90,0)
weight_limit = 1000.0

def haversine(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d
    
def bb_sort(ll): 
    ll = [[0,north_pole,10]] + ll[:] + [[0,north_pole,10]] 
    for i in range(1,len(ll) - 2):
        for k in range(i+2,i+4):
            lcopy = ll[:]
            lcopy[i:k]=ll[k-1:i-1:-1]
            if path_opt_test(ll[1:-1]) > path_opt_test(lcopy[1:-1]):
                ll = lcopy[:]
    return ll[1:-1]

def path_opt_test(llo):
    f_ = 0.0
    d_ = 0.0
    l_ = north_pole
    for i in range(len(llo)):
        d_ += haversine(l_, llo[i][1])
        f_ += d_ * llo[i][2]
        l_ = llo[i][1]
    d_ += haversine(l_, north_pole)
    f_ += d_ * 10 #sleigh weight for whole trip
    return f_

gifts = pd.read_csv("~/Downloads/santa/gifts.csv").fillna(" ")

gifts['TripId']=0
gifts['i']=0
gifts['j']=0


for n in [1.26]:
    i_ = 0
    j_ = 0
    for i in range(90,-90,int(-180/n)):
        i_ += 1
        j_ = 0
        for j in range(180,-180,int(-360/(n+0.59))):
            j_ += 1
            #cu = c.cursor()
            gifts.loc[(gifts['Latitude']>(i-180/n))&(gifts['Latitude']<i)&(gifts['Longitude']>(j-360/(n+0.59)))&(gifts['Longitude']<(j)),"i"]=i_
            gifts.loc[(gifts['Latitude']>(i-180/n))&(gifts['Latitude']<i)&(gifts['Longitude']>(j-360/(n+0.59)))&(gifts['Longitude']<(j)),"j"]=j_

    
    for limit_ in [67]:

        trips=gifts[gifts['TripId']==0]
        trips=trips.sort_values(['i','j','Longitude','Latitude'])
        trips=trips[0:limit_]
        t_ = 0
        while len(trips.GiftId)>0:
            g = []
            t_ += 1
            w_ = 0.0
            for i in range(len(trips.GiftId)):
                    if (w_ + float(trips.iloc[i,3]))<= weight_limit:
                        w_ += float(trips.iloc[i,3])
                        g.append(trips.iloc[i,0])
            gifts.loc[gifts['GiftId'].isin(g),'TripId']=t_
            trips=gifts[gifts['TripId']==0]
            trips=trips.sort_values(['i','j','Longitude','Latitude'])
            trips=trips[0:limit_]

        
        ou_ = open("submission_opt" + str(limit_) + "_" + str(n) + ".csv","w")
        ou_.write("TripId,GiftId\n")
        bm = 0.0

        for s_ in range(1,t_+1):
            trip=gifts[gifts['TripId']==s_]
            trip=trip.sort_values(['Latitude','Longitude'],ascending=[0,1])
            
            a = []
            for x_ in range(len(trip.GiftId)):
               
                a.append([trip.iloc[x_,0],(trip.iloc[x_,1],trip.iloc[x_,2]),trip.iloc[x_,3]])
            b = bb_sort(a)
            if path_opt_test(a) <= path_opt_test(b):
                print("TripId",s_, "No Change", path_opt_test(a) , path_opt_test(b))
                bm += path_opt_test(a)
                for y_ in range(len(a)):
                    ou_.write(str(s_)+","+str(a[y_][0])+"\n")
            else:
                print("TripId ", s_, "Optimized", path_opt_test(a) - path_opt_test(b))
                bm += path_opt_test(b)
                for y_ in range(len(b)):
                    ou_.write(str(s_)+","+str(b[y_][0])+"\n")
        ou_.close()
        
        benchmark = 12506609022.33720
        if bm < benchmark:
            print(n, limit_, "Improvement", bm, bm - benchmark, benchmark)
        else:
            print(n, limit_, "Try again", bm, bm - benchmark, benchmark)
                