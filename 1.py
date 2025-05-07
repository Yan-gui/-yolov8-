import torch
print(torch.cuda.is_available())  # True 表示可用 GPU
print(torch.cuda.get_device_name(0))  # 打印 GPU 名称（如 RTX 3060）
