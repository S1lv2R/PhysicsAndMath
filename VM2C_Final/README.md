# VM2C Final Round
# 1. Giới thiệu
## 1.1. Giới thiệu về kỳ thi
**Kỳ thi Mô hình hoá Toán học Việt Nam**  (Vietnam Mathematical Modelling Competition - viết tắt là VM2C) là kỳ thi mô hình hóa toán học lần đầu tiên được tổ chức ở Việt Nam, dựa theo mô hình tổ chức cuộc thi mô hình hóa uy tín trên thế giới.

Kỳ thi gồm 2 vòng. Ở mỗi vòng, thử thách của các đội là tìm ra giải pháp cho một vấn đề mở, thường thì không giống các bài tập về nhà hay dự án nhóm trên lớp học thông thường. Kỹ năng quản lý thời gian, làm việc nhóm, viết và trình bày báo cáo cũng quan trọng không kém khả năng tìm hiểu các kiến thức mới và tư duy ứng dụng vào thực tế.

Kỳ thi VM2C là một sân chơi bổ ích và thú vị, giúp các học sinh phát triển các kỹ năng cần thiết cho thế kỷ 21. Đội của mình rất vinh dự khi là một trong những đội đoạt huy chương đồng trong kỳ thi được tổ chức lần đầu tiên này.

## 1.2. Cảm nhận về kỳ thi
Mình là người thích nghiên cứu nhưng lại ghét làm bài tập, vì vậy mình rất thích kỳ thi VM2C. Kỳ thi này giúp mình có cảm giác như đang nhập vai thành một nhà khoa học thực thụ, phải tự tìm kiếm và nghiên cứu mọi thứ chứ không có sẵn công cụ nào cho mình.

Bên cạnh đó, do là toán mô hình nên không có một lời giải cụ thể nào, điều này cho phép chúng ta thỏa sức sáng tạo lời giải và tối ưu chúng.

Kỳ thi VM2C giúp mình cải thiện rất nhiều kỹ năng cần thiết trong thực tế, chẳng hạn như kỹ năng giải quyết vấn đề, quản lý thời gian, làm việc nhóm và thuyết trình. Minh tin rằng những kỹ năng này sẽ giúp ích rất nhiều trong tương lai.

# 2. Hướng giải quyết bài toán a vòng 2

> Do có giới hạn về thời gian, nên mình sẽ chỉ giải quyết bài toán a của vòng 2 (câu a trên dữ liệu 1 và dữ liệu 2).
 
> Đề vòng 2: [Đề thi](https://vm2c.viasm.edu.vn/images/VM2C%20-%20De%20thi%20Vong%20II.pdf "Đề thi")

## 2.1. Xử lý file lenh_san_xuat_Day_chuyen_?.txt
Đây là phần mà đã khiến mình không hoàn thành kịp phần thi của mình, mình đã quên mất file này cho đến khi vào ngày cuối cùng thì mình mới nhận ra là có sự tồn tại của file này. Về cơ bản là file cho bạn thời gian mở và đóng công xưởng (công xưởng không làm việc liên tục).

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

Với hướng làm của mình thì mình phải xử lý file đấy, và kiểm tra xem các ca nào sẽ hoạt động (hoạt động khi công xưởng mở). Như với file dữ liệu ở trên thì công xưởng mở cửa vào lúc ``2023-06-01 08:00:00`` và đóng cửa vào lúc ``2023-06-02 04:00:00``, từ dữ liệu đó thì ta biết được vào ngày ``2023-06-01`` sẽ có 3 ca là ca sáng, chiều và tối. Ta sẽ xử lý file ``lenh_san_xuat_Day_chuyen_1.txt`` như sau:

```
Ngày 1: có 3 ca sáng, chiều và tối 
Ngày 2: có 2 ca sáng và tối
Ngày 3: có 2 ca sáng và chiều
Ngày 4: có 3 ca sáng, chiều và tối
Ngày 5: có 1 ca chiều
```
Tuy nhiên để thuận tiện trong tính toán, ta sẽ biểu diễn lại dưới dạng ma trận $28 \times 3$ có biến nhị phân như sau:

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

File xử lý bằng tay để kiểm tra code hoạt động ổn: [processed_lenh_san_xuat_Day_chuyen_1.txt](https://github.com/SilverTD/PhysicsAndMath/blob/main/VM2C_Final/processed_lenh_san_xuat_Day_chuyen_1.txt "processed_lenh_san_xuat_Day_chuyen_1.txt")

## 2.2. Các biến số
Ta sẽ định nghĩa các biến số dùng trong tính toán như sau:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $X = \\{ x_{ilj} \\}$ là ma trận chứa các biến $x_{ij}$ với ý nghĩa công nhân $i$ được chọn làm ca thứ $j$ của công xưởng $l$ hay không.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $B = \\{b_{ilj} \\}$ là ma trận chứa các biến $b_{ilj}$ với ý nghĩa công nhân thứ $i$ có kĩ năng $j$ của công xưởng $l$ hay không.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $D = \\{d_{i} \\}$ là ma trận chứa các biến $d_{i}$ với ý nghĩa tổng số ngày làm việc của công nhân $i$ cho đến hiện tại.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $N = \\{n_{i} \\}$ là ma trận chứa các biến $n_{i}$ với ý nghĩa tổng số ca đêm làm việc của công nhân $i$ cho đến hiện tại.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $W = \\{ w_{i} \\}$ là ma trận chứa các biến $w_{i}$ với ý nghĩa công nhân thứ $i$ có được làm ca hiện tại hay không.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $R = \\{ r_{lj} \\}$ là ma trận chứa các biến $r_{lj}$ với ý nghĩa lượng nhân lực tối thiểu cần cho ca làm việc $j$ của công xưởng $l$.
##  2.3. Các ràng buộc
Ta sẽ xét ngày thứ $k$ $\rightarrow$ công xưởng thứ $l$ $\rightarrow$ ca làm việc thứ j:
1. Các công nhân chỉ làm các ca có đúng kĩ năng của mình:

$$
\begin{aligned}
x_{ilj} \leq b_{ilj} \ \ \ \forall i, l, j > 0
\end{aligned} 
$$

2. Các công nhân chỉ làm một kĩ năng duy nhất trong một ca trong ngày:

$$
\begin{aligned}
\sum\limits_{j}^{}x_{ilj} \leq 1 \ \ \ \forall i, l > 0
\end{aligned} 
$$

3. Tổng công nhân làm việc trong ca thứ $j$ (có kỹ năng $j$) tối thiểu là $r_{lj}$, ta có thêm biến $w_{i}$ nhằm đảm bảo các công nhân chỉ làm một ca duy nhất trong ngày và các công nhân làm ca đêm hôm trước sẽ không làm ca sáng hôm nay:

$$
\begin{aligned}
\sum\limits_{i}^{}(x_{ilj} * w_{i}) \geq r_{lj} \ \ \ \forall l, j > 0
\end{aligned} 
$$

4. Tổng số ngày làm việc của công nhân không vượt quá 24 ngày:

$$
\begin{aligned}
\sum\limits_{i}^{}(x_{ilj} + d_{i}) \leq 24 \ \ \ \forall l, j > 0
\end{aligned} 
$$

##  2.4. Hàm mục tiêu
Mục tiêu mà chúng ta cần tối ưu đầu tiên là số lượng công nhân tham gia làm việc luôn phải là nhỏ nhất:

$$
F_{1} = \sum\limits_{i}\sum\limits_{j}^{}x_{ij}
$$

Tiếp theo ta cần tối ưu độ công bằng giữa các công nhân, điều này có nghĩa độ chênh lệch số ca làm việc giữa các công nhân là nhỏ nhất có thể. Do ta đang xét từng ca trong từng ngày, nên mỗi lần xét ta sẽ luôn ưu tiên lựa chọn các công nhân có số ca làm việc ít nhất:

$$
F_{2} = \sum\limits_{i}\sum\limits_{j}^{}(x_{ij} * d_{i} * C(i))
$$

Tương tự với số ca đêm, ta cũng luôn lựa chọn các công nhân có số ca đêm làm việc ít nhất:

$$
F_{3} = \sum\limits_{i}\sum\limits_{j}^{}(x_{ij} * n_{i} * C(i))
$$

Với hàm số $C(i)$ (ta có thể xây dựng bằng cách dùng ma trận hoặc công thức toán học), ta định nghĩa như sau:

$$
\begin{equation*}
C(i) = 
\begin{cases}
      C & \text{nếu công nhân i có nhiều hơn 1 kĩ năng} \\
      1 & \text{ngược lại}
\end{cases}
\end{equation*}
$$

Điều đó có nghĩa, ta sẽ ưu tiên lựa chọn các công nhân có nhiều hơn một kĩ năng, như thế sẽ tránh trường hợp thiếu công nhân của các xưởng khác.

Hàm mục tiêu của chúng ta lúc này sẽ là tổng các hàm cần tối ưu ở trên $F_1, F_2, F_3$ và thêm các trọng số sao cho hợp lý nhất:

$$
OP = F_1 + A * F_2 + B * F_3
$$

Với $A$ và $B$ là các hằng số, do ta luôn ưu tiên độ công bằng các ca làm việc giữa các công nhân hơn nên hằng số $A$ lớn hơn hằng số $B$.

## 2.5. Áp dụng mô hình
### 2.5.1 Dữ liệu 1
**Dữ liệu** 1 ý (a) với 17 nhân sự, tổng công là 330.

Sau khi áp dụng mô hình trên với bộ dữ liệu 1 thì ta thu được kết quả như đồ thị dưới đây. Về cơ bản đây là một kết quả khá tốt đối với một mô hình khá đơn giản như của chúng ta đã làm.

![NQD_chart_1](https://github.com/SilverTD/Stuffs/assets/55396370/9f710531-5afa-43ed-98e8-627e39b171f3)
![NQD_chart_2](https://github.com/SilverTD/Stuffs/assets/55396370/8ed936d1-d230-45b4-8427-b0320bab11b4)

Ở đồ thị (1), ta thấy được $max = 22$ và $min = 16$:
- $max - min = 22 - 16 = 6$
- Trung bình: $\overline{x} \approx 19.41$
- Độ lệch chuẩn: $\sigma \approx 2.14$

Tương tự ở đồ thị (2), ta thấy được $max = 10$ và $min = 3$:
- $max - min = 10 - 3 = 7$
- Trung bình: $\overline{x} \approx 6.17$
- Độ lệch chuẩn: $\sigma \approx 2.3$

Từ các số liệu vừa tính toán ở trên, ta thấy được kết quả của chúng ta không hẳn là quá tệ. Các dữ liệu phân tán có thể xem là khá đồng đều.

Một số công nhân có số ngày ít thường là các công nhân chỉ có kỹ năng "Rot", vì trong mỗi ca, kỹ năng "Rot" chỉ cần 1 người làm duy nhất. Nên hiển nhiên các công nhân đó có số ca làm việc ít hơn.

### 2.5.2 Dữ liệu 2
**Dữ liệu** 2 ý (a) với 55 nhân sự, tổng công là 1116.

Dưới đây là đồ thị của kết quả:

![NQD_chart_2_1](https://github.com/SilverTD/SilverTD.github.io/assets/55396370/1eaf7025-4c33-4257-afc1-8f36954f1729)
![NQD_chart_2_2](https://github.com/SilverTD/SilverTD.github.io/assets/55396370/0df48706-a69d-4b68-ad77-4f260950e13f)


Ở đồ thị (1), ta thấy được $max = 24$ và $min = 16$:
- $max - min = 24 - 16 = 8$
- Trung bình: $\overline{x} \approx 20.29$
- Độ lệch chuẩn: $\sigma \approx 2.89$

Tương tự ở đồ thị (2), ta thấy được $max = 16$ và $min = 0$:
- $max - min = 16 - 0 = 16$
- Trung bình: $\overline{x} \approx 6.49$
- Độ lệch chuẩn: $\sigma \approx 4.36$

Từ các số liệu chúng ta vừa tính toán, ta thấy được mô hình của chúng ta đã xuất hiện các nhược điểm. Kết quả của đồ thị (1) với độ lệch chuẩn $2.89$ và $max - min = 8$, có thể thấy các dữ liệu dao động quanh giá trị trung bình khá mạnh. Tương tự với đồ thị (2), thậm chí là có người làm việc hăng say tới 16 ca đêm :joy:	. Do đó, mô hình chúng ta vừa xây dựng không hẳn là quá tốt, nhưng vẫn có thể chấp nhận được (hoặc không). Đây cũng chính là cái hay của toán mô hình, ta có thể xây dựng nhiều mô hình khác nhau và so sánh kết quả của chúng.

Toàn bộ source code của mình: [VM2C_Final](https://github.com/SilverTD/Stuffs/tree/main/VM2C_Final "VM2C Final")

Mọi ý tưởng và hướng đi mình vừa trình bày ở bên trên, đều là những ý tưởng, suy nghĩ của mình khi đang làm bài thi ở viện nghiên cứu <b>VIASM</b>: [VM2C_Vong2](https://github.com/SilverTD/Stuffs/tree/main/VM2C_Vong2 "VM2C Vong2")

## 2.6. Nhận xét
### 2.6.1. Ưu điểm
Đây vốn dĩ là một mô hình khá đơn sơ, đơn giản nên rất dễ hiểu, bên cạnh đó những thứ chúng ta làm không thực sự quá nặng toán. Cơ bản là chỉ làm theo những gì đề cho.

Kết quả mà chúng ta vừa tìm được trông khá ổn.

### 2.6.2. Nhược điểm
Chắc chắn là do mô hình còn quá đơn giản nên không thực sự quá tối ưu.

### 2.6.3. Cải thiện
Ở đây có rất nhiều cách cải thiện và phát triển thêm khác nhau, riêng mình sau khi tham khảo bài làm của đội trường chuyên <b>KHTN</b> thì mình thấy các bạn thêm vào "Độ bất mãn" trông cũng khá hay.

Mô hình chúng ta đang xét từng ca, do đó mỗi lần xét ta sẽ ưu tiên lựa chọn các công nhân có số ca làm ít. Chúng ta hoàn toàn có thể thử thay đổi hàm mục tiêu, như các đội khác thì chọn tối ưu độ lệch chuẩn ($max - min$).

**Lưu ý:** Trong quá trình làm việc, sau khi mô hình đã cho ra kết quả thì ta cần phải tạo một <b>Checker</b> để kiểm tra lại kết quả, xem kết quả đã thỏa mãn các ràng buộc hay chưa ? Vì cho dù kết quả có tối ưu, độ lệch chuẩn chỉ $0.1$ nhưng vi phạm điều kiện thì mọi thứ đều vô nghĩa.

# 3. Tổng kết
Do không có nhiều thời gian, nên tạm thời mình chỉ viết bài đăng giải quyết câu a. Nhưng nếu bạn đã đọc bài viết của mình, các bạn sẽ nắm được những gì bài toán yêu cầu và hướng đi, từ đó hình thành tư duy để giải quyết nốt các phần còn lại của bài toán. Do đây là toán mô hình, nên không có một lời giải cụ thể duy nhất, các bạn có thể tự sáng tạo nhiều lời giải khác nhau. Từ đó so sánh các kết quả và lựa chọn lời giải tốt nhất. Nghe cứ như một nhà khoa học thực thụ nhỉ ? 

Đây vốn dĩ là một cuộc thi khá hay phải không ? Nó hoàn toàn giúp chúng ta rèn luyện được khá nhiều kĩ năng có ích trong thực tế, và đây hoàn toàn là một cuộc thi xứng đáng để chúng ta trải nghiệm một lần.

# 4. Một số hình ảnh
![prize](https://github.com/SilverTD/Stuffs/assets/55396370/e74d2ecb-465e-4467-b1b2-1a8f859407aa)
![prize2](https://github.com/SilverTD/Stuffs/assets/55396370/506fddfb-20cb-4f91-a4f3-52e1275d1f7a)
![vm2c](https://github.com/SilverTD/Stuffs/assets/55396370/910ab01c-cc78-47c1-a7a2-da9a1b308b2a)


# 5. Tài liệu tham khảo
```
- Bài làm của đội trường chuyên KHTN: https://github.com/hsgs-wtg/Final-Round
- Tài liệu của VM2C: https://vm2c.viasm.edu.vn/
```
