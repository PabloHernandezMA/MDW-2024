import yaml

def validar_requisitos():
    try:
        with open('requisitos.yml', 'r') as f:
            data = yaml.safe_load(f)
            if 'requisitos' in data and len(data['requisitos']) > 0:
                print('requerimientook')
                return True
            else:
                print('Error: Requisitos incompletos o vacíos')
                return False
    except Exception as e:
        print(f"Error leyendo el archivo de requisitos: {e}")
        return False

if __name__ == '__main__':
    if validar_requisitos():
        exit(0)
    else:
        exit(1)
