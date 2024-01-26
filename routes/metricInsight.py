from flask import Blueprint, jsonify, request

import threading
import queue
from copy import deepcopy

from GPU.utilisation import web_utilisation_gpu

global shared_queues

MetricInsight_blueprint = Blueprint('MetricInsight', __name__, url_prefix='/MetricInsight')


@MetricInsight_blueprint.route('/test', methods=['GET'])
def test():
    print("Debut du traitement...")
    #T = conso(shared_queue)
    #if not T:
        #print("Fin du traitement.")
    return jsonify("STOP")
    #print("Données envoyées : ", T)
    #return jsonify(T)


@MetricInsight_blueprint.route('/start', methods=['POST'])
def start():
    data_received = request.get_json()

    pid_checkbox_value = data_received.get('pidCheckbox', False)
    pid_value = data_received.get('pidInput', 0)

    gpu_checkbox_value = data_received.get('gpuCheckbox', False)
    cpu_checkbox_value = data_received.get('cpuCheckbox', False)
    mem_checkbox_value = data_received.get('memoryCheckbox', False)
    power_checkbox_value = data_received.get('powerCheckbox', False)

    freq_checkbox_value = data_received.get('freqCheckbox', False)
    freq_value = data_received.get('FreqInput', 10)

    interval_checkbox_value = data_received.get('intervalCheckbox', False)
    interval_value = data_received.get('IntervalInput', float('inf'))

    plot_checkbox_value = data_received.get('plotCheckbox', False)

    smoothing_checkbox_value = data_received.get('smoothingCheckbox', False)
    smoothing_value = data_received.get('SmoothingInput', 1)

    save_checkbox_value = data_received.get('saveCheckbox', False)
    save_value = data_received.get('SaveInput', "")

    configuration = {
        'pidCheckbox': pid_checkbox_value,
        'pidInput': pid_value,
        'gpuCheckbox': gpu_checkbox_value,
        'cpuCheckbox': cpu_checkbox_value,
        'memoryCheckbox': mem_checkbox_value,
        'powerCheckbox': power_checkbox_value,
        'freqCheckbox': freq_checkbox_value,
        'FreqInput': freq_value,
        'intervalCheckbox': interval_checkbox_value,
        'IntervalInput': interval_value,
        'plotCheckbox': plot_checkbox_value,
        'smoothingCheckbox': smoothing_checkbox_value,
        'SmoothingInput': smoothing_value,
        'saveCheckbox': save_checkbox_value,
        'SaveInput': save_value
    }

    # Check if the configuration is valid
    if (configuration['cpuCheckbox'] or configuration['gpuCheckbox'] or configuration['memoryCheckbox'] or
            configuration['powerCheckbox']):
        response_data = {'acknowledgement': True}
        print('Lancement de MetricInsight...')
        MetricInsight(configuration)
    else:
        response_data = {'acknowledgement': False}

    print('Data send :', response_data)

    return jsonify(response_data)


def MetricInsight(configuration):
    MAX_QUEUE_SIZE = int(configuration['FreqInput']) * 10

    global shared_queues
    shared_queues = {}

    treads = {}

    if configuration['cpuCheckbox']:
        shared_queues['CPU'] = queue.Queue(MAX_QUEUE_SIZE)
        treads['thread_CPU'] = threading.Thread(target=conso, args=(shared_queues['CPU'], configuration))

    if configuration['gpuCheckbox']:
        shared_queues['GPU'] = queue.Queue(MAX_QUEUE_SIZE)
        treads['thread_GPU'] = threading.Thread(target=web_utilisation_gpu, args=(shared_queues['GPU'], configuration))

    if configuration['memoryCheckbox']:
        shared_queues['MEM'] = queue.Queue(MAX_QUEUE_SIZE)
        treads['thread_MEM'] = threading.Thread(target=conso, args=(shared_queues['MEM'], configuration))

    if configuration['powerCheckbox']:
        shared_queues['POWER'] = queue.Queue(MAX_QUEUE_SIZE)
        treads['thread_POWER'] = threading.Thread(target=conso, args=(shared_queues['POWER'], configuration))

    # Start threads
    for t in treads:
        treads[t].start()


def conso(shared_queues):
    L = []
    queues_copy = {}

    # Copy des queues
    for item, key in shared_queues:
        with item.mutex:
            queues_copy[key] = deepcopy(item.queue)

    # Vidange de la copie
    for item in queue_copy:
        print(f"Consommé: {item}")
        shared_queue.get()

        # Vérifier si c'est le signal de fin
        if item == "STOP":
            print("Le producteur a terminé. Fin du traitement.")
            return False
        L.append(item)

    print("Fin du traitement.")
    return L
