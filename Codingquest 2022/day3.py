import math
array = [[0,0,0],[911722,-200511,740826],[-591938,569644,-699242],[-769286,236018,-44245],[56598,770949,729975],[495946,-45417,-270352],[-860509,799685,446893],[90644,-28649,815445],[-22634,771730,-70208],[483845,-562791,16982],[-476438,-996959,117359],[-914633,118509,848396],[-330317,-644953,-765901],[-305960,341867,326983],[178721,354229,-957217],[-258771,-674162,373424],[603933,489651,32611],[929399,-109388,929381],[529724,-324013,-225620],[257410,-36065,-180844],[651864,-796118,-93157],[524017,-780163,32029],[818828,-475993,425035],[550676,-472332,-228198],[-98768,914796,947447],[-871993,-59731,787467],[-153413,-275121,487118],[-174301,126917,408901],[-585107,494887,495022],[392678,50901,665160],[158049,-398322,467159],[-416507,-816172,-196499],[-671738,-239965,229974],[212321,814900,204937],[640841,78849,-114701],[-117211,-63687,854460],[454780,258530,-685784],[745668,344413,659941],[457702,598720,-700006],[-430660,813928,-400180],[525455,-948205,-556751],[-621041,499826,510582],[-892437,637664,340479],[713308,-789180,-962193],[-536797,-737185,66982],[700355,479669,680509],[-370724,-334973,808018],[-259384,430396,787480],[848832,-636497,-989089],[927709,346002,537057],[781862,794715,-644512],[0,0,0]]

# The travel agent is selling a "visit every moon" tour for all the moons in the local system. It sounds exciting! 
# They even have a holographic 3 dimensional map of the moons hovering in the middle of the store. 
# You are fascinated by this and make a record of the 3d coordinates of each stop in the tour.

# You are curious to know the total distance you would have to travel if you
#  went on the tour, so you record all the coordinates in the order in which 
#  they will be visited. Using Pythagoras theorem in 3 dimensions,
#  you know you can calculate the distance by finding the total of all the various 
# hypotenuse distances between each pair of points.

result = 0
for i in range(len(array)-1):
    num = array[i+1][0] - array[i][0] #Finding the difference in coordinates, which is the distance we travelled.
    num2 = array[i+1][1] - array[i][1] # ...
    num3 = array[i+1][2] - array[i][2] # ...

    result += math.floor(math.sqrt(num*num + num2*num2 + num3*num3)) #Pythagoras theorem in 3d
    
print(result)