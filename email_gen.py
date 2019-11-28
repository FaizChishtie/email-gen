from __init__ import VERSION
from content import CONTENT, TIMES
import csv

def main():
    print(f'email-gen v{VERSION}\n~Faizaan')
    file = input('Enter csv file to be parsed~ ')
    split = to_split(input('Enter rows you\'d like to split (separate by comma)~ '))
    n_emails = int(input('Enter the number of emails to generate~ '))
    subject = input('Enter the subject for your email~ ')
    print(info([file,split,n_emails,subject]))
    formattable = _format(file, split)
    pack(formattable, bulk('MRT 411', 'Sunday, December 1st, 2019', n_emails), subject)

def pack(formattable, bulk, sub):
    print('~ packing')
    c = 0
    for packable in formattable:
        o = CONTENT
        o = o.format(subject=sub, email=packable['email'], name=bold(packable['fname']), reason=italic("On {} - you applied to: {}\n\t".format(packable['time'], packable['role']) + bold(bulk[c])), opt='\nPlease be there at least 5 minutes before your interview.', sign=sign())
        deploy(o, c)
        c += 1

def deploy(content, c):
    print('~ deploying email{}.txt'.format(c))
    f = open('email{}'.format(c), "w+")
    f.write(content)
    f.close()

def bulk(place, date, rep):
    print('~ bulking')
    content = "You have been scheduled for a 15 minute interview at {} on {} at {}."
    response = []
    for i in range(rep):
        o = content.format(place, date, TIMES[i])
        response.append(o)
    return response

def _format(file, split):
    print('~ formatting')
    response = []
    with open(file) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            sub_r = {}
            for i in range(len(split)):
                sub_r[split[i]] = row[split[i]]
            line_count += 1
            response.append(sub_r)
        print(f'~ processed {line_count} lines.')
    return response

def info(informable):
    o = '~inputs'
    for word in informable:
        o += '\n\t\t~' + str(word)
    return o

def to_split(splittable):
    return splittable.split(',')

def sign():
    return "This message is automated, please excuse any mistakes/errors.\nBest,\nFaizaan"

def bold(s):
    #return "<b>{}</b>".format(s)
    return s

def italic(s):
    #return "<i>{}</i>".format(s)
    return s


main()