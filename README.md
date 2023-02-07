<div align="center">
 <img src="https://readme-typing-svg.herokuapp.com/?lines=STM32+Remote+control+stepper+motor.;&font=Roboto" />
 <p align="center">
 <img title="MDOG_GGB" src='https://img.shields.io/badge/MTO-2.0-brightgreen.svg' />
 <img title="MDOG_GGB" src='https://img.shields.io/badge/Python-3.9-yellow.svg' />
 <img title="MDOG_GGB" src='https://img.shields.io/static/v1?label=Author&message=@Martin&color=red'/>
 
 </p>
  <img height="137px" src="https://github-readme-stats.vercel.app/api?username=MartinXMax&hide_title=true&hide_border=true&show_icons=trueline_height=21&text_color=000&icon_color=000&bg_color=0,ea6161,ffc64d,fffc4d,52fa5a&theme=graywhite" />
  
   
 <table>
  <tr>
      <th>Internet Control</th>
  </tr>
  <tr>
    <th>Server:Traffic forwarding</th>
  </tr>
  <tr>
    <th>Controlled end</th>
  </tr>
  <tr>
    <th>Control terminal</th>
  </tr>
 
 </table>
</div>

## Wiring schematic diagram

![图片名称](https://raw.githubusercontent.com/MartinxMax/STM32_Remote-control-/master/%C2%96%C2%96Demo_image/Wiring_diagram.png "Help")

# demonstration
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

