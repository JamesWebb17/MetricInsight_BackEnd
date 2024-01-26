# config_handler.py

from flask import current_app

def get_config():
    try:
        # Récupérez la configuration depuis l'application Flask (variable globale)
        config = current_app.config['my_config']
        return config
    except Exception as e:
        print(f"Erreur lors de la récupération de la configuration : {str(e)}")
        return None

def save_config(new_config):

    config_dict = {
        'pidCheckbox': new_config.get('pidCheckbox'),
        'PIDInput': new_config.get('PIDInput'),
        'cpuCheckbox': new_config.get('cpuCheckbox'),
        'gpuCheckbox': new_config.get('gpuCheckbox'),
        'memoryCheckbox': new_config.get('memoryCheckbox'),
        'powerCheckbox': new_config.get('powerCheckbox'),
        'freqCheckbox': new_config.get('freqCheckbox'),
        'FreqInput': new_config.get('FreqInput'),
        'intervalCheckbox': new_config.get('intervalCheckbox'),
        'IntervalInput': new_config.get('IntervalInput'),
        'SmoothingCheckbox': new_config.get('SmoothingCheckbox'),
        'SmoothingInput': new_config.get('SmoothingInput'),
        'plotCheckbox': new_config.get('plotCheckbox'),
        'saveCheckbox': new_config.get('saveCheckbox'),
        'SaveInput': new_config.get('SaveInput'),
        'verboseCheckbox': new_config.get('verboseCheckbox'),
    }

    try:
        # Mettez à jour la configuration globale avec la nouvelle configuration
        current_app.config['my_config'] = config_dict
        return True
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de la configuration : {str(e)}")
        return False

def init_config():
    config_dict = {
        'pidCheckbox': False,
        'PIDInput': 0,
        'cpuCheckbox': False,
        'gpuCheckbox': False,
        'memoryCheckbox': False,
        'powerCheckbox': False,
        'freqCheckbox': False,
        'FreqInput': 0,
        'intervalCheckbox': False,
        'IntervalInput': 0,
        'SmoothingCheckbox': False,
        'SmoothingInput': 0,
        'plotCheckbox': False,
        'saveCheckbox': False,
        'SaveInput': 0,
        'verboseCheckbox': False,
    }

    try:
        # Mettez à jour la configuration globale avec la nouvelle configuration
        current_app.config['my_config'] = config_dict
        return True
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de la configuration : {str(e)}")
        return False