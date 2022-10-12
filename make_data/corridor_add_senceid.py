import os
import shutil
from sys import prefix
from unicodedata import name

sence_dict = {
            '000299': '01',  #Normal
            '000210': '01',
            '000323': '01',
            '000225': '01',
            '000255': '01',
            '000286': '01',
            '000338': '01',
            '000238': '01',
            '000343': '01',
            '000239': '01',
            '000293': '02', #BagExchange
            '000290': '02', 
            '000295': '02', 
            '000248': '02', 
            '000308': '02', 
            '000254': '02', 
            '000232': '02', 
            '000236': '02', 
            '000277': '02', 
            '000292': '02', 
            '000357': '02', 
            '000320': '02', 
            '000242': '03', #CarryObject
            '000329': '03',
            '000209': '03',
            '000340': '03',
            '000335': '03',
            '000355': '03',
            '000249': '03',
            '000269': '03',
            '000333': '03',
            '000306': '03',
            '000300': '03',
            '000294': '03',
            '000247': '03',
            '000280': '03',
            '000279': '03',
            '000287': '03',
            '000218': '03',
            '000315': '03',
            '000349': '03',
            '000319': '03',
            '000344': '03',
            '000274': '03',
            '000276': '03',
            '000322': '03',
            '000229': '03',
            '000298': '03',
            '000237': '03',
            '000271': '03',
            '000309': '03',
            '000330': '03',
            '000268': '03',
            '000273': '03',
            '000233': '03',
            '000353': '03',
            '000302': '03',
            '000245': '03',
            '000235': '04',   #Chasing
            '000231': '04',
            '000351': '04',
            '000356': '04',
            '000307': '04',
            '000316': '04',
            '000312': '04',
            '000281': '04',
            '000311': '04',
            '000288': '04',
            '000264': '04',
            '000212': '04',
            '000214': '04',
            '000305': '04',
            '000259': '04',
            '000317': '04',
            '000297': '04',
            '000257': '04',
            '000296': '05',   #Cycling
            '000324': '05',
            '000350': '05',
            '000325': '05',
            '000253': '05',
            '000345': '05',
            '000318': '05',
            '000313': '05',
            '000270': '05',
            '000326': '05',
            '000289': '05',
            '000220': '06',  #Fighting
            '000278': '06',
            '000211': '06',
            '000266': '06',
            '000321': '06',
            '000251': '06',
            '000284': '06',
            '000213': '06',
            '000252': '07',    #Hiding
            '000243': '07',
            '000215': '07',
            '000352': '07',
            '000275': '07',
            '000272': '07',
            '000223': '07',
            '000217': '07',
            '000226': '07',
            '000230': '07',
            '000354': '08', #Loitering
            '000341': '08',
            '000216': '08',
            '000241': '08',
            '000331': '08',
            '000263': '08',
            '000303': '08',
            '000291': '08',
            '000342': '09',   #PlayingWithBall
            '000267': '09',
            '000265': '09',
            '000310': '09',
            '000327': '09',
            '000314': '09',
            '000244': '09',
            '000336': '09',
            '000346': '09',
            '000256': '09',
            '000222': '09',
            '000258': '09',
            '000334': '09',
            '000347': '09',
            '000221': '10',   #Protest
            '000283': '10',
            '000328': '10',
            '000246': '10',
            '000285': '10',
            '000219': '10',
            '000332': '10',
            '000240': '10',
            '000339': '10',
            '000348': '10',
            '000301': '10',
            '000234': '11', #SuddenRunning
            '000250': '11',
            '000358': '11',
            '000337': '11',
            '000260': '11',
            '000282': '11',
            '000261': '11',
            '000227': '11',
            '000262': '11',
            '000304': '11',
            '000224': '11',
            '000228': '11',
            }

def main_test():
    for one in os.listdir(source_dir):
        name = one.split(split_symbol)[0]
        sence_id = sence_dict[name]
        new_name = sence_id + '_' + one
        os.rename(os.path.join(source_dir, one), os.path.join(source_dir, new_name))
        
def main_train():
    for one in os.listdir(source_dir):
        name = one.split(split_symbol)[0]
        new_name = '01' + '_' + one
        os.rename(os.path.join(source_dir, one), os.path.join(source_dir, new_name))



if __name__ == '__main__':
    source_dir = '/home/yaboliu/data/cvae/corridor/training/frames'
    # split_symbol = '.'
    # main_test()
    # source_dir = '/home/yaboliu/data/cvae/corridor/training/pose/json_results'
    split_symbol = '_'
    main_train()