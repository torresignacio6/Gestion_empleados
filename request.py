import requests

def consultar_api():
    URL = 'https://jsonplaceholder.typicode.com/todos '
    try:
        respuesta = requests.get(URL)
        respuesta.raise_for_status()
        
        if respuesta.status_code==200:
          print ('solicitud_exitosa')
          print ('data: ',respuesta.json())

    except requests.exceptions.Timeout:
        print("La solicitud ha excedido el tiempo de espera.")
    except requests.exceptions.ConnectionError:
        print(" error de conexion")
    except requests.exceptions.RequestException:
        print("errror en la solicitud")