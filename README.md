# STM32 controls stepping motor via internet
* Wiring schematic diagram
![图片名称](https://raw.githubusercontent.com/MartinxMax/STM32_Remote-control-/master/%C2%96%C2%96Demo_image/Wiring_diagram.png "Help")
* Modify your host IP in the main. c file
```Serial_SendString("AT+CIPSTART=\"TCP\",\"xx.xx.xx.xx\",\"10030\"\r\n");```
* Public IP server startup service

```#python3 Server.py```

    
![图片名称](https://raw.githubusercontent.com/MartinxMax/STM32_Remote-control-/master/%C2%96%C2%96Demo_image/Server.png "Help")


* Device connection server

    ![图片名称](https://github.com/MartinxMax/STM32_Remote-control-/blob/master/%C2%96%C2%96Demo_image/head2.png "Help")

* Set a point A

    ![图片名称](https://github.com/MartinxMax/STM32_Remote-control-/blob/master/%C2%96%C2%96Demo_image/A.png?raw=true "Help")

* Client sends command

```#python3 Client.py```

    ![图片名称](https://raw.githubusercontent.com/MartinxMax/STM32_Remote-control-/master/%C2%96%C2%96Demo_image/return.png "Help")

* The server forwards traffic

    ![图片名称](https://raw.githubusercontent.com/MartinxMax/STM32_Remote-control-/master/%C2%96%C2%96Demo_image/run.png "Help")

* STM32 receives the data and drives the stepping motor

    ![图片名称](https://raw.githubusercontent.com/MartinxMax/STM32_Remote-control-/master/%C2%96%C2%96Demo_image/B.png "Help")

