# imagecraft/utils.py

from PIL import Image
import numpy as np

def load_image_as_array(image_path: str) -> np.ndarray:
    '''
    Carrega uma imagem de um arquivo e a converte para um array NumPy.
    
    Args:
        image_path: Caminho para o arquivo de imagem.
        
    Returns:
        Um array NumPy representando a imagem.
    '''
    try:
        with Image.open(image_path) as img:
            return np.array(img)
    except FileNotFoundError:
        raise FileNotFoundError(f'Erro: Arquivo não encontrado em "{image_path}"')
    except Exception as e:
        raise IOError(f'Erro ao carregar a imagem: {e}')
    
def save_array_as_image(array: np.ndarray, output_path: str):
    '''
    Salve um array NumPy como um arquivo de imagem.
    
    Args:
        array: P array NumPy da imagem.
        output_path: Caminho onde a imagem será salva.
    '''
    try:
        # Garante que o array está no formato de 8-bits sem sinal
        if array.dtype != np.uint8:
            array = np.clip(array, 0, 255).astype(np.uint8)
        
        img = Image.fromarray(array)
        img.save(output_path)
        print(f'Imagem salva com sucesso em "{output_path}"')
    except Exception as e:
        raise IOError(f'Erro ao salvar a imagem: {e}')