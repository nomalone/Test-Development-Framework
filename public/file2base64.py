import base64


def file_to_base64(file_path):

    try:
        with open(file_path, 'rb') as file:
            file_bytes = file.read()
            base64_str = base64.b64encode(file_bytes).decode('utf-8')
            file_type = file_path.split('.')[-1]
            file_name = file_path.split('/')[-1]

            if file_type in ["png", "jpg", "bmp", "tiff", "gif"]:
                data_header = f'data:image/{file_type.lower()};base64,'
                return data_header + base64_str, file_type, file_name
            else:
                return base64_str, file_type, file_name
    except Exception as e:
        print(f"文件转换base64时出错: {e}")

