from ultralytics import YOLO

if __name__ == '__main__':
    # 直接使用预训练权重或yaml文件创建模型
    # model = YOLO(r'yolov8n.pt')
    # model.train(cfg = 'ultralytics/cfg/default.yaml', data=r"D:\Dataset\AutoMine\Middle4-2127\Dataset_NoPedestrain\data_NoPedestrian.yaml", name='train-200epoch-v5InV8-ExistAnchor')

    #使用预训练权重+配置文件创建模型
    # 预训练模型
    model = YOLO(r"D:\Xueniansheji\Ultralytics-main\ultralytics\cfg\models\v8\yolov8n.pt")

    result = model.train(data=r"D:\Xueniansheji\Ultralytics-main\ultralytics\cfg\datasets\Dataset\data.yaml",
                         epochs=400,
                         batch=20,
                         patience=30,
                         learn = 0.01
                         )


    # #恢复中断的训练
    # Load a model
    # model = YOLO(r"E:\knowledge\YOLO-v8\ultralytics-main\runs\detect\VOC\train-200epoch-yolov8n.yaml\weights\last.pt")  # load a partially trained model
    # # Resume training
    # result = model.train(resume=True)

    # # 模型验证
    # model = YOLO(r"E:\knowledge\YOLO-v8\ultralytics-main\runs\detect\AutoMine-2107\300epoch\train-300epoch-yolov8n.yaml-1\weights\best.pt")
    # model.val( data= r"D:\Dataset\AutoMine\Middle4-2107\Dataset_NoPedestrain-2107\data_NoPedestrain-2107.yaml",
    #            cfg = 'ultralytics/cfg/default.yaml',
    #            split = 'test',
    #            project=r'E:\knowledge\YOLO-v8\ultralytics-main\runs\detect\AutoMine-2107',
    #            name='val-300epoch-yolov8n.yaml')

    # # 模型推理
    # model = YOLO(r"D:\YOLO-v8-app\YOLOv8-app-master\weights\best.pt")
    # model.predict(source=r"D:\Dataset\AutoMine\Middle4-2107\Dataset_NoPedestrain-2107\images\test",
    #               save=True,
    #               project=r'D:\YOLO-v8-app\runs\detect',
    #               name='predict-200epoch'
    #               )