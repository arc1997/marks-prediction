import mysql.connector
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

mydb = mysql.connector.connect(
  host=//host name,
  user=//user id,
  passwd=//password
)

y=int(input('enter student id'))

query=("SELECT DISTINCT CAST(CLASS_NAME AS UNSIGNED INTEGER) FROM db_8_may_2018.sm_classes a,db_8_may_2018.sm_marks b WHERE a.CLASS_ID = b.CLASS_ID and STUDENT_ID='%s';")%y
mycursor = mydb.cursor()
mycursor.execute(query)
myresult = mycursor.fetchall()

a=[i[0] for i in myresult]

total_mark=[]
obtained_mark=[]
obt_total_mark=[]
percentages=[]

for i in a:
    query = ("SELECT CAST(b.OBTAINED_MARKS AS UNSIGNED INTEGER), CAST(b.TOTAL_MARKS AS UNSIGNED INTEGER) FROM db_8_may_2018.sm_classes a,db_8_may_2018.sm_marks b WHERE a.CLASS_ID = b.CLASS_ID and b.STUDENT_ID='%s' and a.CLASS_NAME='%s'")%(y,i)
    mycursor1 = mydb.cursor()
    mycursor1.execute(query)
    myresult1 = mycursor1.fetchall()


    obtained_mark=[i[0] for i in myresult1]
    print(obtained_mark)
    total_mark = [i[1] for i in myresult1]
    for i in range(len(obtained_mark)):
        dummy = []
        f=obtained_mark[i]
        g=total_mark[i]
        dummy.append(f)
        dummy.append(g)
        s=dummy
        del dummy
        obt_total_mark.append(s)

    for i in obt_total_mark:
        for j in i:
            if j==0 or j==None:
                i.remove(i[1])
            if 0 in i:
                i.remove(0)
            if None in i:
                i.remove(None)


    print(obt_total_mark)
    filter_obt_total_mark = [x for x in obt_total_mark if x]
    print(filter_obt_total_mark)
    filter_obt_mark_list=[]
    filter_total_mark_list=[]
    for i in filter_obt_total_mark:
        filter_obt_mark=i[0]
        filter_total_mark=i[1]
        filter_obt_mark_list.append(filter_obt_mark)
        filter_total_mark_list.append(filter_total_mark)

    print(len(filter_obt_mark_list))
    print(len(filter_total_mark_list))



    b=filter_obt_mark_list
    c=filter_total_mark_list






    b=[i[0] for i in myresult1]

    for i in range(len(b)):
        if 0 in b:
            b.remove(0)


    c = [i[1] for i in myresult1]

    for i in range(len(c)):
        if 0 in c:
            c.remove(0)


    for i in range(len(b)):
        b[i] = (b[i] * 100) / c[i]


    marks_100=[]
    for i in c:
        mark=100-i
        i=i+mark
        marks_100.append(i)

    obtained_marks_total=np.sum(b)
    total_marks_total=np.sum(marks_100)
    percentage=(obtained_marks_total*100)/total_marks_total

    percentages.append(percentage)

    d=[]
    d.append(b)

e=[]
for i in d:
    for j in i:
        e.append(j)



x=np.reshape(e,(-1,1))
X_train, X_test = train_test_split(x, test_size=0.2)

kmeans = KMeans(n_clusters=2, max_iter=600, algorithm = 'auto')
kmeans.fit(x)


KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=600,n_clusters=2, n_init=100, n_jobs=100, precompute_distances='auto',random_state=0, tol=0.0001)

for i in range(len(x)):
    predict_me = np.array(x[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)


m=kmeans.cluster_centers_[0]
n=kmeans.cluster_centers_[1]
l=int(m[0])
k=int(n[0])

if l<k:
    min=l
    max=k
else:
    min=k
    max=l


z=(min+max+np.mean(e)+np.median(e))/4
print('The predicted percentage are',z)
percentages.append(z)



next_class_name=a[-1]+1
a.append(next_class_name)

class_names=[]
for i in a:
    class_name=str(i)+'th'
    class_names.append(class_name)


import matplotlib.pyplot as plt


plt.bar(class_names,percentages,width=0.6)

plt.xlabel('class')
plt.ylabel('percentage(%)')


plt.tight_layout()
plt.show()
