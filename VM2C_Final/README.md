

 # VM2C FINAL ROUND
## Giới thiệu về kỳ thi
**Kỳ thi Mô hình hoá Toán học Việt Nam**  (Vietnam Mathematical Modelling Competition - viết tắt là VM2C) là kỳ thi mô hình hóa toán học lần đầu tiên được tổ chức ở Việt Nam, dựa theo mô hình tổ chức cuộc thi mô hình hóa uy tín trên thế giới.

Kỳ thi gồm 2 vòng. Ở mỗi vòng, thử thách của các đội là tìm ra giải pháp cho một vấn đề mở, thường thì không giống các bài tập về nhà hay dự án nhóm trên lớp học thông thường. Kỹ năng quản lý thời gian, làm việc nhóm, viết và trình bày báo cáo cũng quan trọng không kém khả năng tìm hiểu các kiến thức mới và tư duy ứng dụng vào thực tế.

Đây là một kỳ thi khá hay và mới lạ, nó hoàn toàn khác so với các kỳ thi học sinh giỏi khác. Và đội của mình cũng là đội đoạt huy chương đồng trong kỳ thi được tổ chức lần đầu tiên này !

## Cảm nhận về kỳ thi
Mình vốn là người thích nghiên cứu nhưng ghét làm bài tập, nên kỳ thi này khá hợp với mình. Kỳ thi này giúp bạn như nhập vai vào một nhà khoa học đang nghiên cứu vậy, mọi thứ đều phải tự tìm kiếm, nghiên cứu chứ không hề có sẵn các công cụ cho bạn dùng. Và do là toán mô hình nên không có cụ thể một lời giải nào cả, do đó bạn có thể thỏa sức sáng tạo lời giải và tối ưu chúng. Kỳ thi này giúp bạn cải thiện rất nhiều kĩ năng trong thực tế như kĩ năng giải quyết vấn đề, quản lí thời gian, làm việc nhóm, thuyết trình,... Và một khi đã học thì phải biết cách áp dụng những kiến thức đó trong thực tế.

## Hướng giải quyết bài toán vòng 2
### Xử lý file lenh_san_xuat_Day_chuyen_1.txt
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

Từ đó ta có thể thay thế dữ liệu đã xử lý thành ma trận đơn giản và dễ hiểu hơn:

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

Đến đây ta đã hoàn thành trong việc xử lý file ``lenh_san_xuat_Day_chuyen_1.txt`` thành một ma trận nhị phân giúp ta thuận lợi trong việc tính toán sau này. Việc xử lý file này khá phức tạp vì nó chứa nhiều trường hợp khác nhau và nếu bất cẩn trong xử lý file này thì những thuật toán của chúng ta cho dù hoạt động tốt nhưng vẫn sẽ cho ra kết quả không chính xác.

Ví dụ như trong ngày ``2023-06-01`` sẽ có 3 ca: sáng, chiều và tối nhưng bạn xử lý file chỉ còn mỗi 2 ca: sáng, chiều thì dẫn đến kết quả sẽ sai (vì thiếu mất ca tối).

Source code xử lý file này: [data_processing.py](https://github.com/SilverTD/PhysicsAndMath/blob/main/VM2C_Final/data_processing.py "data_processing.py")

File xử lý bằng tay để kiểm tra code mình hoạt động ổn: [processed_lenh_san_xuat_Day_chuyen_1.txt](https://github.com/SilverTD/PhysicsAndMath/blob/main/VM2C_Final/processed_lenh_san_xuat_Day_chuyen_1.txt "processed_lenh_san_xuat_Day_chuyen_1.txt")
