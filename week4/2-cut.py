import datetime

with open('./raw.txt') as f:
    top = []
    data = {}
    user = ['RMUn6owxz3Npjow@ku.ac.th',
            'RMUjtMPNJ6aT3TB@ku.ac.th',
            'RMUpKGYn9d5by4N@ku.ac.th',
            'RMUpKmcaiQtXA57@ku.ac.th',
            'RMUkdLcDsnd6MSH@ku.ac.th']
    lines = f.read().splitlines()
    print('time,user,ip_src,ip_dst,port_dst,hostname')
    for a in lines:
        data = a.split(' ')
        if (data[1] in user):
            time = int(data[0])/1000000
            time = str(datetime.datetime.fromtimestamp(time)).split(' ')
            data[0] = time[1]
            print(','.join(data))
        