# Project2DAG

ทำการเขียนDAGโดยpythonและbashเพื่อแปลงไฟล์txtเป็นcsv
 
 เรามีfile passwd.txt มีเนื้อหาข้างในดังนี้
 
 ![pass](https://github.com/manew-c/Project2DAG/assets/113186479/c189f802-b011-473f-95da-14208c7d1ae5)

เราจะทำการแปลงให้อยู่ในรูปแบบไฟล์csv และดึงมาแค่ตัดcolumn 1,3 และ 6
1.สร้างไฟล์ DAG ชื่อ my_first_dag.py

2.ส่วนแรกที่เขียนคือ import libaries ต่างๆ

   ![importlibary](https://github.com/manew-c/Project2DAG/assets/113186479/9de23cb1-80f1-4b2e-aaa6-139e3614b594)

3.เขียน DAG arguments

![dagArg](https://github.com/manew-c/Project2DAG/assets/113186479/9b8abffa-98b6-4250-b4bd-8c401d39587c)

4.เขียน DAG defined 

![defineDAG](https://github.com/manew-c/Project2DAG/assets/113186479/a8c36abf-8580-48ab-9908-be5abf452c8a)

5.เขียนtaskแรก คือการextract ในไฟล์ต้นฉบับมีdelimiterเป็น":" เราตัดเอาแค่column 1,3,6

![extrcact](https://github.com/manew-c/Project2DAG/assets/113186479/783cf66d-b900-4072-b4df-feab932378c6)

6. taskที่2 transform แปลงจาก":" เป็น ","
   
![transform](https://github.com/manew-c/Project2DAG/assets/113186479/39fed8c8-8ab5-4089-96df-afb78d4921a2)

7.เขียน pipeline ง่ายๆแค่ชื่อtaskตามด้วยสัญลักษณ์ >> เป็นการชี้ว่าไปtaskไหนต่อ

![datapipline](https://github.com/manew-c/Project2DAG/assets/113186479/7748f9f5-c8a2-4e0d-9694-c7b425b54984)

8.ทำการcopyไฟล์เราเข้าโฟลเดอร์ dags โดยคำสั่ง
 
 cp my_first_dag.py $AIRFLOW_HOME/dags

9.เช็คว่าdagเราเข้าairflowรึยัง

airflow dags list|grep "my-first-dag"

![checkdagUP](https://github.com/manew-c/Project2DAG/assets/113186479/b7cc1599-fef5-4150-aba4-787a33f2f8a2)


10.ไปดูใน apache airflow

จะเห็นdagที่เราอัพ
![checkinairflow](https://github.com/manew-c/Project2DAG/assets/113186479/18467231-58dc-4054-8dee-6ed12747e7cd)

ลองrun ถ้าขึ้นเขียวเข้มแสดงว่าsuccess
![rundag](https://github.com/manew-c/Project2DAG/assets/113186479/02a60354-a074-4713-8c30-46cc59710851)

task pipeline
![graphpipeline](https://github.com/manew-c/Project2DAG/assets/113186479/305facf9-b9ee-430c-8048-14b09863f2bc)

output ที่ได้หลัง run
![output](https://github.com/manew-c/Project2DAG/assets/113186479/9ef2c818-2d81-4ff3-b810-89bd9567f66c)






