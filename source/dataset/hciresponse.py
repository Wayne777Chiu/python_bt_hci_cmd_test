import dataset.showlogo as slogo
import dataset.bt_event

pdu_array=[]
find_sub_event = False
event_string=''


def rx_data_analyzer(rx_data):
    global pdu_array,event_string
    pdu_array = list(rx_data)
    #parameter_length = pdu_array[2]

    dataset.bt_event.description_event(pdu_array)

