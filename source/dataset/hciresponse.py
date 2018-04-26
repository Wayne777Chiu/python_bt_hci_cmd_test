import dataset.showlogo as slogo
import dataset.bt_event

pdu_array=[]
find_sub_event = False
event_string=''

def display_response():
    global pdu_array,find_sub_event,event_string
    global pdu_array,find_sub_event,event_string
    if find_sub_event is True:
        sub_event = '0x' + str(pdu_array[3])
    else:
        sub_event = 'N/A'
    print(slogo.decode('+--------------------------------------------------------------------------%'))
    #print(slogo.decode('|'),' CMD: ','variable','(command code)','                       ')
    #print(slogo.decode('|'),' Group: ','group','(command group field)','                       ')
    print(slogo.decode('|'),' Event: ', event_string,'(0x'+''.join("{:02X} ".format(pdu_array[1]))+')')
    print(slogo.decode('|'),' SUB-Event: ', 'sub-event', '(',sub_event,')')
    print(slogo.decode('|'),' Parameter Length: ', pdu_array[2],'                       ')
    print(slogo.decode('|'),' Parameter: ', 'Parameter (0x'+ ' 0x'.join("{:02X}".format(b) for b in pdu_array[3:])+')')
    print(slogo.decode('p--------------------------------------------------------------------------q'))



def rx_data_analyzer(rx_data):
    global pdu_array,event_string
    pdu_array = list(rx_data)
    #parameter_length = pdu_array[2]

    find_sub_event, event_string =dataset.bt_event.get_event_code(pdu_array[1], pdu_array[3])
    display_response()

