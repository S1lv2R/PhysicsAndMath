# VM2C Final Round
# 1. Giới thiệu
## 1.1. Giới thiệu về kỳ thi
**Kỳ thi Mô hình hoá Toán học Việt Nam**  (Vietnam Mathematical Modelling Competition - viết tắt là VM2C) là kỳ thi mô hình hóa toán học lần đầu tiên được tổ chức ở Việt Nam, dựa theo mô hình tổ chức cuộc thi mô hình hóa uy tín trên thế giới.

Kỳ thi gồm 2 vòng. Ở mỗi vòng, thử thách của các đội là tìm ra giải pháp cho một vấn đề mở, thường thì không giống các bài tập về nhà hay dự án nhóm trên lớp học thông thường. Kỹ năng quản lý thời gian, làm việc nhóm, viết và trình bày báo cáo cũng quan trọng không kém khả năng tìm hiểu các kiến thức mới và tư duy ứng dụng vào thực tế.

Đây là một kỳ thi khá hay và mới lạ, nó hoàn toàn khác so với các kỳ thi học sinh giỏi khác. Và đội của mình cũng là đội đoạt huy chương đồng trong kỳ thi được tổ chức lần đầu tiên này !

## 1.2. Cảm nhận về kỳ thi
Mình vốn là người thích nghiên cứu nhưng ghét làm bài tập, nên kỳ thi này khá hợp với mình. Kỳ thi này giúp bạn trông như đang nhập vai vào một nhà khoa học đang nghiên cứu vậy, mọi thứ đều phải tự tìm kiếm, nghiên cứu chứ không hề có sẵn các công cụ cho bạn dùng. Và do là toán mô hình nên không có cụ thể một lời giải nào cả, do đó bạn có thể thỏa sức sáng tạo lời giải và tối ưu chúng. Kỳ thi này giúp bạn cải thiện rất nhiều kĩ năng trong thực tế như kĩ năng giải quyết vấn đề, quản lí thời gian, làm việc nhóm, thuyết trình,... Và một khi đã học thì phải biết cách áp dụng những kiến thức đó trong thực tế.

# 2. Hướng giải quyết bài toán 1a vòng 2
> Do có giới hạn về thời gian, nên mình sẽ chỉ giải quyết bài toán 1a của vòng 2 (câu a trên dữ liệu 1).
## 2.1. Xử lý file lenh_san_xuat_Day_chuyen_1.txt
Đây là phần mà đã khiến mình không hoàn thành kịp phần thi của mình, nó khá phức tạp trong việc xử lý file này và nó khiến mình mất khá nhiều thời gian. Về cơ bản là file cho bạn thời gian mở và đóng công xưởng (công xưởng không làm việc liên tục).

Đề bài cho biết trong một ngày có 3 ca:
+ Ca sáng: 6h - 14h.
+ Ca chiều: 14h - 22h.
+ Ca tối: 22h - 6h hôm sau.

```
Thoi_gian_bat_dau; Thoi_gian_ket_thuc
2023-06-01 08:00:00; 2023-06-02 04:00:00
2023-06-02 06:00:00; 2023-06-02 14:00:00
2023-06-02 22:00:00; 2023-06-03 06:00:00
2023-06-03 06:00:00; 2023-06-03 22:00:00
```

Với hướng làm của mình thì mình phải xử lý file đấy, và kiểm tra xem các ca nào sẽ hoạt động (hoạt động khi công xưởng mở). Như với file dữ liệu ở trên thì công xưởng mở cửa vào lúc ``2023-06-01 08:00:00`` và đóng cửa vào lúc ``2023-06-02 04:00:00``, từ dữ liệu đó thì ta biết được vào ngày ``2023-06-01`` sẽ có 3 ca là ca sáng, chiều và tối. Mình sẽ xử lý file ``lenh_san_xuat_Day_chuyen_1.txt`` như sau:

```
Ngày 1: có 3 ca sáng, chiều và tối 
Ngày 2: có 2 ca sáng và tối
Ngày 3: có 2 ca sáng và chiều
Ngày 4: có 3 ca sáng, chiều và tối
Ngày 5: có 1 ca chiều
```
Tuy nhiên để thuận tiện trong tính toán, mình sẽ biểu diễn lại dưới dạng ma trận $28 \times 3$ có biến nhị phân như sau:

$$
T_{28 \times 3} = \begin{pmatrix}
t_{1,1} & t_{1,2} & t_{1,3} \\
t_{2,1} & t_{2,2} & t_{2,3} \\
\vdots & \vdots & \vdots \\
t_{28,1} & t_{28,2} & t_{28,3}\\
\end{pmatrix}
$$

Tương ứng với 28 ngày và 3 ca mỗi ngày, ma trận có ý nghĩa:

$$
\begin{equation*}
t_{ij} = 
\begin{cases}
      1 & \text{nếu ca làm việc thứ j vào ngày i hoạt động} \\
      0 & \text{ngược lại}
\end{cases}
\ \ \ \ \ \ 1 \leq i \leq 28, \ 1 \leq j \leq 3
\end{equation*}
$$

Từ đó ta có thể thay thế dữ liệu đã xử lý thành một ma trận đơn giản và dễ hiểu hơn:

$$
T = \begin{pmatrix}
1 & 1 & 1\\  
1 & 0 & 1\\
1 & 1 & 0\\
1 & 1 & 1 \\
0 & 1 & 0 \\
 & \cdots & 
\end{pmatrix}
$$

Đến đây ta đã hoàn thành trong việc xử lý file ``lenh_san_xuat_Day_chuyen_1.txt`` thành một ma trận nhị phân giúp ta thuận lợi trong việc tính toán sau này. Việc xử lý file này khá quan trọng, vì nếu bất cẩn trong xử lý file thì những thuật toán của chúng ta cho dù hoạt động tốt nhưng vẫn sẽ cho ra kết quả không chính xác.

Ví dụ như trong ngày ``2023-06-01`` sẽ có 3 ca: sáng, chiều và tối nhưng bạn xử lý file chỉ còn mỗi 2 ca: sáng, chiều thì dẫn đến kết quả sẽ sai (vì thiếu mất ca tối).

Source code xử lý file này: [data_processing.py](https://github.com/SilverTD/PhysicsAndMath/blob/main/VM2C_Final/data_processing.py "data_processing.py")

File xử lý bằng tay để kiểm tra code mình hoạt động ổn: [processed_lenh_san_xuat_Day_chuyen_1.txt](https://github.com/SilverTD/PhysicsAndMath/blob/main/VM2C_Final/processed_lenh_san_xuat_Day_chuyen_1.txt "processed_lenh_san_xuat_Day_chuyen_1.txt")

## 2.2. Các biến số
Ta sẽ định nghĩa các biến số dùng trong tính toán như sau:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $X = \\{ x_{ij} \\}$ là ma trận chứa các biến $x_{ij}$ với ý nghĩa công nhân i được chọn làm ca làm việc $j$.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $B = \\{b_{ij} \\}$ là ma trận chứa các biến $b_{ij}$ với ý nghĩa công nhân thứ $i$ có kĩ năng $j$ hay không.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $D = \\{d_{i} \\}$ là ma trận chứa các biến $d_{i}$ với ý nghĩa tổng số ngày làm việc của công nhân $i$ cho đến hiện tại.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $N = \\{n_{i} \\}$ là ma trận chứa các biến $n_{i}$ với ý nghĩa tổng số ca đêm làm việc của công nhân $i$ cho đến hiện tại.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $W = \\{ w_{i} \\}$ là ma trận chứa các biến $w_{i}$ với ý nghĩa công nhân thứ $i$ có được làm ca hiện tại hay không.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $R = \\{ r_{j} \\}$ là ma trận chứa các biến $r_{j}$ với ý nghĩa lượng nhân lực tối thiểu cần cho ca làm việc $j$.
##  2.3. Các ràng buộc
Ta sẽ xét từng ca trong mỗi ngày, ta xét ngày thứ $l$:
1. Các công nhân chỉ làm các ca có đúng kĩ năng của mình:

$$
\begin{aligned}
x_{ij} \leq b_{ij} \ \ \ \ \ \forall i, j > 0
\end{aligned} 
$$

2. Các công nhân chỉ làm một kĩ năng duy nhất trong một ca trong ngày:

$$
\begin{aligned}
\sum\limits_{j}^{}x_{ij} \leq 1 \ \ \ \ \ \forall i, j > 0
\end{aligned} 
$$

3. Tổng công nhân làm việc trong ca thứ $j$ (có kỹ năng $j$) tối thiểu là $r_{j}$, ta có thêm biến $w_{i}$ nhằm đảm bảo các công nhân chỉ làm một ca duy nhất trong ngày và các công nhân làm ca đêm hôm trước sẽ không làm ca sáng hôm nay.:

$$
\begin{aligned}
\sum\limits_{i}^{}x_{ij} * w_{i} \geq r_{j} \ \ \ \ \ \forall i, j > 0
\end{aligned} 
$$

4. Tổng số ngày làm việc của công nhân không vượt quá 24 ngày:

$$
\begin{aligned}
\sum\limits_{i}^{}x_{ij} + d_{i} \leq 24 \ \ \ \ \ \forall i, j > 0
\end{aligned} 
$$

##  2.4. Hàm mục tiêu
Mục tiêu của chúng ta sẽ là tối ưu số ca làm việc là nhỏ nhất và đạt sự công bằng nhất giữa các công nhân. Điều này có nghĩa độ chênh lệch số ngày làm việc và số ca đêm làm việc của các công nhân là nhỏ nhất có thể.

Do ta đang xét từng ca trong từng ngày, nên mỗi lần xét ta sẽ luôn ưu tiên lựa chọn các công nhân có số ngày, số ca đêm nhỏ nhất. Điều đó có nghĩa:

$$
F_{1} = \sum\limits_{i}\sum\limits_{j}^{}x_{ij} * d_{i}
$$

$$
F_{2} = \sum\limits_{i}\sum\limits_{j}^{}x_{ij} * n_{i}
$$

$$
OP = min(A * F_1 + B * F_2)
$$

Với A và B là các hằng số, do ta ưu tiên độ công bằng ngày làm việc giữa các công nhân hơn nên hằng số A lớn hơn hằng số B.
## 2.5. Áp dụng mô hình
Sau khi áp dụng mô hình trên với bộ dữ liệu 1 thì ta thu được kết quả như đồ thị dưới đây. Về cơ bản đây là một kết quả khá tốt đối với một mô hình khá đơn giản như của chúng ta đã làm.
![chart_1](https://github.com/SilverTD/Stuffs/assets/55396370/1f3b4131-00e7-4534-9a0e-49083e3aaf0c)
![chart_2](https://github.com/SilverTD/Stuffs/assets/55396370/023e426e-09bb-4c15-b47d-1592a5d4ac5d)

Toàn bộ source code của mình: https://github.com/SilverTD/Stuffs/tree/main/VM2C_Final

Các ý tưởng và hướng đi, mình đều dùng lại những ý tưởng mà mình chưa hoàn thành được khi đang làm bài thi này ở viện <b>VISAM</b>: https://github.com/SilverTD/Stuffs/tree/main/VM2C_Vong2

Do đó có thể các đoạn code, ý tưởng của mình sẽ hơi đần, nên thông cảm cho mình nhé.

## 2.6. Nhận xét
### 2.6.1. Ưu điểm
Đây vốn dĩ là một mô hình khá đơn sơ, đơn giản nên rất dễ hiểu, bên cạnh đó những thứ chúng ta làm không thực sự quá nặng toán. Cơ bản là chỉ làm theo những gì đề cho.
Kết quả mà chúng ta vừa tìm được trông khá ổn.

### 2.6.2. Nhược điểm
Chắc chắn là do mô hình còn quá đơn giản nên không thực sự quá tối ưu. Do chúng ta đang xét qua từng ca và xử lý, cách này không hẳn là ổn. Cách tốt hơn là chúng ta xét tất cả các ngày.

# 3. Tổng kết
Do mình không hẳn là có nhiều thời gian, nên mình chỉ có thể viết bài đăng giải câu 1a thôi. Nhưng từ đó bạn đã thấy được cách hoạt động và hướng đi của mình, và bạn có thể tự nghiên cứu mà giải nốt các câu còn lại. Do đây là toán mô hình, nên không có một lời giải duy nhất, các bạn có thể tự sáng tạo nhiều lời giải khác nhau. Từ đó so sánh các kết quả và lựa chọn lời giải tốt nhất. Nghe cứ như một nhà khoa học thực thụ nhỉ ? 

Và đây là một cuộc thi khá là hay phải không ? Nó giúp mình rèn luyện tư duy giải quyết vấn đề, tư duy sáng tạo trong lời giải,... Mình mong cuộc thi này sẽ càng phát triển và nhiều bạn trẻ sẽ tham gia hơn !

# 4. Một số hình ảnh
![prize](https://github.com/SilverTD/Stuffs/assets/55396370/e74d2ecb-465e-4467-b1b2-1a8f859407aa)
![prize2](https://github.com/SilverTD/Stuffs/assets/55396370/506fddfb-20cb-4f91-a4f3-52e1275d1f7a)
![vm2c](https://github.com/SilverTD/Stuffs/assets/55396370/910ab01c-cc78-47c1-a7a2-da9a1b308b2a)


# 5. Tài liệu tham khảo
```
- Bài làm của các bạn chuyên KHTN: https://github.com/hsgs-wtg/Final-Round
- Tài liệu của VM2C: https://vm2c.viasm.edu.vn/
```
