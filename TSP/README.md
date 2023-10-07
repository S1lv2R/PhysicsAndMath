
# Giải bài toán TSP (Traveling Salesman Problem)
## Phát biểu bài toán
Bài toán được phát biểu như sau một người giao hàng cần đi giao hàng tại n thành phố. Xuất phát từ một thành phố nào đó, đi qua các thành phố khác để giao hàng và trở về thành phố ban đầu. Mỗi thành phố chỉ đến một lần, khoảng cách từ một thành phố đến các thành phố khác là xác định được. Giả thiết rằng mỗi thành phố đều có đường đi đến các thành phố còn lại. Khoảng cách giữa hai thành phố có thể là khoảng cách địa lý, có thể là cước phí di chuyển hoặc thời gian di chuyển. Ta gọi chung là độ dài. Hãy tìm một chu trình (một đường đi khép kín thỏa mãn điều kiện trên) sao cho tổng độ dài các cạnh là nhỏ nhất. Hay còn nói là tìm một phương án có giá nhỏ nhất.

Bài toán có thể biểu diễn bởi một đồ thị có hướng có trọng số $G = (V, E)$.
Với V là tập hợp các đỉnh, E là tập hợp các cạnh của đồ thị.
## Giải quyết
### Biến và ma trận
Đầu tiên ta biểu diễn lại đồ thị dưới dạng ma trận $M$ khoảng cách đối xứng (symmetrical).

Đầu tiên ta gọi $c_{ij}$ là khoảng cách đi từ đỉnh i sang đỉnh j. Ta sẽ biểu diễn ma trận $M$ như sau:

$$
M= \begin{pmatrix}
c_{11} & c_{12} & \dots & c_{1n}\\  
c_{21} & c_{22} & \dots & c_{2n} \\
\dots & \dots & \dots & \dots \\
c_{n1} & c_{n2} & \dots & c_{nn} 
\end{pmatrix}
$$

Ở đây ta sẽ giải quyết bài toán TSP bằng quy hoạch tuyến tính dùng biến nhị phân. Ta gọi:

$$
\begin{equation}
x_{ij} = 
\begin{cases}
      1 & \text{nếu ta chọn đi từ đỉnh i đến j} \\
      0 & \text{ngược lại}
\end{cases}
\end{equation}
$$

Ta tiếp tục có ma trận $X$ là các biến $x_{ij}$, ví dụ với một chu trình như sau: 1 - 2 - 3 - 4 - 1 thì ta có một ma trận như sau:

$$
X = \begin{pmatrix}
0 & 1 & 0 & 0\\  
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
1 & 0 & 0 & 0 
\end{pmatrix}
$$

### Các ràng buộc
1. (mapping constraints) Điều kiện ràng buộc đầu tiên là bậc của mỗi đỉnh là 2, điều này có ý nghĩa rằng mỗi đỉnh phải có 2 đường đi nối với nó, gồm đường đi vào và đường đi ra.

$$
\begin{aligned}
\sum\limits_{i = 0}^{n - 1}x_{ij} = 1 \ \ \ \ \ \forall j \in \mathbb{N} \cap [0; n)
\end{aligned} 
$$


$$
\begin{aligned}
\sum\limits_{j = 0}^{n - 1}x_{ij} = 1 \ \ \ \ \ \forall i \in \mathbb{N} \cap [0; n)
\end{aligned} 
$$

2. (un-looped constraints) Mỗi đỉnh không tự đi trực tiếp tới chính nó được, do đó ta có:
$$x_{ii} = 0 \ \ \ \ \ \forall i \in \mathbb{N} \cap [0; n)$$

4. (sub-tour elimination constraints) Đây cũng là điều kiện quan trọng nhất của bài toán, ta cần loại bỏ các chu trình con.
   Ta có $V := {1, \dots, n }$ là tập hợp các đỉnh của đồ thị, và ta lại có $S \subset V$ thì:

$$\sum\limits_{i \in S }\sum\limits_{j \in S}x_{ij} \leq |S| - 1 \ \ \ \ \forall S \subset V, |S| \in \mathbb{N} \cap [2; n)$$
Nghĩa rằng khi ta có một chu trình con thì tổng các cạnh nối của chúng phải nhỏ hơn hoặc bằng tổng các đỉnh của chúng trừ 1. Điều này cho thấy rằng các chu trình con sẽ không bao giờ tồn tại.

### Hàm mục tiêu
Hàm mục tiêu của chúng ta chắc chắn là tổng quãng đường của chu trình phải là nhỏ nhất.

$$
\begin{aligned}
\text{min} \ \ F = \sum c_{ij}x_{ij}\ \ \ \ \ \forall i, j \in \mathbb{N} \cap [0; n)
\end{aligned} 
$$

### Nhược điểm và khắc phục
Ở ràng buộc cuối cùng, ta thấy nó sẽ có cực kì nhiều điều kiện như vậy. Cụ thể với đồ thị n đỉnh thì ta có $2^n - n - 2$ điều kiện.
- $2^n$ cách chọn các chu trình con.
- $n$ cách chọn các chu trình con chỉ có 1 đỉnh.
- $2$ cách chọn các chu trình con có 0 đỉnh hoặc n đỉnh.

Để khắc phục, ta sẽ cứ việc tìm nghiệm mà không cần điều kiện này. Khi ta có đã tìm được nghiệm thì sẽ kiểm tra xem chu trình này có đủ n đỉnh hay chưa ? Nếu chưa thì ta thêm điều kiện này vào để khử sub-tour và tiếp tục giải với điều kiện vừa bổ sung.

## Tài liệu tham khảo
Tôi đã tham khảo tài liệu rất hay của anh Hoàng Anh Quân, đây là tài liệu mà tôi đã được tập huấn tại viện nghiên cứu cao cấp về toán VIASM cho cuộc thi VM2C 2023.
