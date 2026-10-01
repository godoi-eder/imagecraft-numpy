import argparse
import os 
from imagecraft.core import (
    to_grayscale,
    invert_colors,
    adjust_brightness,
    apply_blur
)
from imagecraft.utils import load_image_as_array, save_array_as_image

def main():
    parser = argparse.ArgumentParser(description = 'ImageCraft-NumPy: Processamento de Imagem via CLI com NumPy.')
    parser.add_argument('input_path', type = str, help = 'Caminho da imagem de entrada.')
    parser.add_argument('output_path', type = str, help = 'Caminho para salver a imagem processada.')
    
    # Argumentos para as operações
    parser.add_argument('--grayscale', action = 'store_true', help = 'Converte a imagem para escala de cinza.')
    parser.add_argument('--invert', action = 'store_true', help = 'Inverte as cores da imagem.')
    parser.add_argument('--brightness', type = int, help = 'Ajusta o brilho (valor entre -255 e 255).')
    parser.add_argument('--blur', type = int, help = 'Aplica um filtro de blur (ex.: 1, 3, 5).')
    
    args = parser.parse_args()
    
    # Garante que o diretório de saída exista
    output_dir = os.path.driname(args.output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok = True)
        
    try:
        # Carrega a imagem
        image_array = load_image_as_array(args.input_path)
        processed_array = image_array.copy()
        
        # Aplica as transformações na ordem
        if args.grayscale:
            processed_array = to_grayscale(processed_array)
        if args.invert:
            processed_array = invert_colors(processed_array)
        if args.brightness is not None:
            processed_array = apply_blur(processed_array, args.blur)
            
        # Salva a imagem processada
        save_array_as_image(processed_array, args.output_path)
        
    except (FileNotFoundError, IOError) as e:
        print(e)
    except Exception as e:
        print(f'Um erro inesperado ocorreu: {e}')

if __name__ == '__main__':
    main()
    