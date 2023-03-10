# LINE-bot-with-database
一個能幫使用者挑選出想喝的飲料的LINE機器人

111-1 Introduction to Database Systems - Final team project「今天要喝甚麼ㄋ」

實作將LINE Bot連線至資料庫

組員：110550033李欣螢、110550034孫承瑞、110550111莊宥瑋、110550158葉家蓁

# Introduction

我們設計了一個LINE Bot，他可以根據你的偏好推薦一杯符合需求的飲料給你，也可以向你推薦Editor’s choice。我們想要設計這樣的機器人是因為在日常生活中常常遇到想喝飲料卻選擇障礙，不知道該喝什麼的狀況，因此想要做一個可以幫自己選今天要喝什麼的聊天機器人。

# Database design

![image](https://user-images.githubusercontent.com/86657062/224308781-911abd7d-71c0-4dc4-b546-8c410cdfd2f3.png)

在column的命名上，考量到我們資料中的飲料店都位於台灣，未來若要更新資料時，用中文會更方便也更直覺，所以column的名稱和資料的內容皆以中文來儲存。另外，因為我們的程式在執行query時，每次都需要同時對很多個columns做篩選，所以我們沒有使用index。

在我們的資料庫中只包含了一個table: ”drink”，每筆資料都是一種品項的飲料，其中儲存了該飲料的價錢、甜度等詳細資料，因為各個columns之間並不存在partial dependency或transitive dependency，所以drink屬於BCNF。

# From the data sources to the database

我們的資料來源是台灣各家飲料店的菜單，但因為菜單大都由紙本或圖片的方式呈現，所以原始資料的csv檔是由我們自己手動輸入的。目前我們主要輸入了5家飲料店的菜單，未來有機會會持續更新。

![image](https://user-images.githubusercontent.com/86657062/224308873-5898864f-d28a-48cd-8f7d-f6d45c5860c5.png)

我們在pgAdmin 4中使用psql的\COPY指令將csv檔import至資料庫中，如下圖：

![image](https://user-images.githubusercontent.com/86657062/224309034-0cf1dca8-2608-4575-bbd8-dae9d1b244e9.png)

若想要增加新的飲料店的菜單，可以將資料輸入至csv檔後，再執行一次DELETE和\COPY，或是直接使用INSERT、UPDATE指令來新增、修改資料。
  
未來，也許可以在我們的LINE Bot中新增讓使用者自行輸入新品項的功能，只要將使用者輸入的資料轉換為INSERT指令，並執行該query，就可以直接更新資料庫，但此功能隱含了接收到錯誤資訊的風險，因此我們此次並未於LINE Bot中實作。

# Application with database

我們的LINE Bot會根據使用者輸入的資訊在資料庫中尋找匹配的資料並回傳給使用者，也可以持續將新的資料(手動)更新上去，因此需要與資料庫配合。我們使用AWS RDS架設資料庫，並用pgAdmin 4來管理。

![image](https://user-images.githubusercontent.com/86657062/224309130-6524f250-7321-4cb6-91a5-d7820766e716.png)

![image](https://user-images.githubusercontent.com/86657062/224309144-cdd21831-1e24-40ab-a472-08a4bb8f4d19.png)

我們會根據使用者選擇的需求，執行不同的query，舉例來說，如果使用者選擇了「預算$40以下、加料、甜度中等」，就會執行以下的query：

![image](https://user-images.githubusercontent.com/86657062/224309216-bb6ba390-460b-48df-afd1-d1d8d5e77de6.png)
 
而LINE Bot會從query的執行結果中隨機挑一個品項回覆在聊天室中：

![image](https://user-images.githubusercontent.com/86657062/224309250-73eb7684-e219-43aa-a91c-e45b10c9686f.png)

# Other details

我們的LINE Bot主體是用python寫的，建在AWS Lambda上，使用psycopg2函式連線到AWS RDS的資料庫，並透過AWS API Gateway和LINE Bot連接。
 
![image](https://user-images.githubusercontent.com/86657062/224309403-8e0a67c3-bbe5-4d74-8a6e-1e90c6c12ff3.png)

![image](https://user-images.githubusercontent.com/86657062/224309406-8b43c965-2f2e-4e5a-965f-bad081e543ec.png)

![image](https://user-images.githubusercontent.com/86657062/224309422-525aaa6c-9fe7-4973-97a5-99237aa5f7a3.png)

![image](https://user-images.githubusercontent.com/86657062/224309448-c47bf2e7-30c1-4921-9ee2-f99c3d4622ac.png)
 
最後附上我們的LINE Bot QR Code：

 ![messageImage_1672582365021](https://user-images.githubusercontent.com/86657062/224308357-8834fb32-d2bb-4b95-be5b-834d8d67f825.jpg)

