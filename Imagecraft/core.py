import numpy as np

def to_grayscale(image_array: np.ndarray) -> np.ndarray:
    '''
    Converte uma imagem colorida para escala de cinza usando a fórmula de luminosidade.
    '''
    if image_array.ndim != 3 or image_array.shape[2] < 3:
        print('A imagem já está em escala de cinza ou não tem canais de cor.')
        return image_array
    
    # Pesos padrão para R, G, B
    weights = np.array([0.2989, 0.5870, 0.1140])
    grayscale_array = np.dot(image_array[..., :3], weights)
    
    return grayscale_array.astype(np.uint8)

def invert_colors(image_array: np.ndarray) -> np.ndarray:
    '''
    Inverte as cores de imagem.
    '''
    return 255 - image_array

def adjust_brightness(image_array: np.ndarray, value: int) -> np.ndarray:
    '''
    Ajuste o brilho da imagem.
    
    Args:
        value: Um inteiro entre -255 e 255.
    '''
    # Usamos np.clip para garantir que os valores permaneçam no intervalo [0, 255]
    return np.clip(image_array.astype(np.int16) + value, 0, 255).astype(np.uint8)

def apply_blur(image_array: np.ndarray, strength: int = 1) -> np.ndarray:
    '''
    Aplica um filtro de blur (box blur) usando convolução simulada.
    
    Args:
        strength: A força do blur, relacionada ao tamanho do kernel (deve ser ímpar).
    '''
    if strength < 1:
        return image_array

    kernel_size = strength * 2 + 1
    padding = ((strength, strength), (strength, strength)) + ((0, 0),) * (image_array.ndim - 2)
    padded_array = np.pad(image_array, padding, mode='edge')
    blurred_array = np.zeros(image_array.shape, dtype=np.float32)

    # Soma cada janela do kernel para imagens em escala de cinza ou coloridas.
    height, width = image_array.shape[:2]
    for row in range(kernel_size):
        for column in range(kernel_size):
            blurred_array += padded_array[
                row:row + height,
                column:column + width,
            ]

    return (blurred_array / (kernel_size ** 2)).astype(np.uint8)
    