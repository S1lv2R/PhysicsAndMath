# Ảnh điện trong điện môi

Điều kiện biên:

$$
\begin{equation}
D_{2n} - D_{1n} = \sigma_f
\end{equation}
$$

Trong đó: $D_{2n}, \ D_{1n}$ lần lượt là vector cảm ứng điện tại môi trường $2$ và môi trường $1$, $\sigma_f$ là mật độ điện tích tự do.

$$
\begin{equation}
E_{2t} - E_{1t} = 0
\end{equation}
$$

Trong trường tĩnh điện, điện trường không đổi do đó $\nabla \times \bold{E} = 0$, ngược lại $\nabla \times \bold{D} = \nabla \times \bold{P} \not= 0$.

Tuy nhiên nếu dùng định lý Gauss cho vector điện trường:

$$
\begin{equation}
E_{2n} - E_{1n} = \sigma
\end{equation}
$$

Thì lúc này, mật độ điện tích $\sigma = \sigma_f + \sigma_p$ bao gồm mật độ điện tích tự do và mật độ điện tích phân cực.

Do đó ta thường sử dụng vector cảm ứng điện $\bold{D}$ nhằm dễ dàng tìm được vector điện trường $\bold{E}$, vì $\bold{D}$ pháp tuyến liên tục tại mặt phân cách, trong khi $\bold{E}$ thì không.

## Một số câu hỏi thắc mắc và câu trả lời của mình
> 1. Tại sao một điện tích điểm đặt trong điện môi thì điện trường bị giảm đi một hằng số điện môi

Khi đặt điện tích trong môi trường điện môi rộng vô hạn, khi đó điện tích gây ra một điện trường $\bold{E}$ khiến môi trường điện môi bị phân cực. Ta sẽ đi chứng minh điều này:

Sử dụng định lý <i>Gauss</i> cho vector cảm ứng điện, ta tìm được vector cảm ứng điện:

$$
\begin{equation}
\bold{D} = \frac{q}{4\pi r^2} \hat{r}
\end{equation}
$$

Từ đây ta tìm được điện trường trong điện môi:

$$
\begin{equation}
\bold{E} = \frac{\bold{D}}{\epsilon} = \frac{q}{4\pi \epsilon r^2} \hat{r}
\end{equation}
$$

Ta có công thức độ phân cực:

$$
\begin{equation}
\bold{P} = \bold{D} - \epsilon_0 \bold{E} = \frac{q}{4\pi}(\frac{\epsilon - \epsilon_0}{\epsilon}) \frac{\hat{r}}{r^2}
\end{equation}
$$

Vậy mật độ điện tích khối lúc này là:

$$
\begin{equation}
\rho_p = -\nabla \cdot \bold{P} = \frac{q}{4\pi}(\frac{\epsilon - \epsilon_0}{\epsilon}) \nabla  (\frac{\hat{r}}{r^2})
 = -q(\frac{\epsilon - \epsilon_0}{\epsilon}) \delta^3(\bold{r})
 \end{equation}
$$

Trong đó $\delta^3(\bold{r})$ là hàm <i>Dirac Delta</i>. Mật độ điện tích $\rho_p$ chỉ có tại vị trí điện tích điểm $q$. Vậy điện môi bị phân cực tại bề mặt tiếp xúc với điện tích $q$ và trái dấu với điện tích.

Tổng điện tích lúc này bao gồm $Q = q + q_p = \dfrac{q}{\epsilon_r}$.

<b>Lưu ý:</b> Tổng các điện tích phân cực lúc này khác 0, vì chỉ có các điện tích trái dấu tại bề mặt tiếp xúc. Thế còn các điện tích phân cực dương đã đi đâu ? Chúng ở rìa của môi trường điện môi, tuy nhiên trong trường hợp này môi trường điện môi là vô hạn do đó các điện tích phân cực dương lúc này nằm ở vô cùng (do đó ta bỏ qua sự ảnh hưởng của chúng).

Ngược lại, nếu môi trường điện môi là hữu hạn thì ta không thể bỏ qua sự ảnh hưởng của các điện tích dương nằm ở rìa môi trường điện môi này. Nhìn vào chất điện môi của một tụ điện, ta thấy 2 rìa của chất điện môi bị phân cực với cùng điện tích và trái dấu nhau.

> 2. Giả sử một quả cầu điện tích $Q > 0$ bán kính $a$, được bao quanh bởi một quả cầu điện môi đồng tâm bán kính $b$. Điện trường bên trong và bên ngoài quả cầu điện môi sẽ như nào ?

Khi này điện tích $Q$ gây ra điện trường làm phân cực điện môi, tuy nhiên quả cầu điện môi sẽ bị phân cực thành phần âm và phần dương (vì chất điện môi lúc này là hữu hạn). Phần âm tại bề mặt tiếp xúc với $Q$ và phân dương cùng độ lớn tại bề mặt quả cầu điện môi.

Lúc này điện trường bên trong điện môi bị giảm đi $\epsilon_r$ lần, vì chất điện môi lúc này bị phân cực thành âm và dương tạo ra một điện trường đều ngược hướng $\bold{E'}$ với điện trường $\bold{E_0}$ do $Q$ tạo ra, tổng hợp hai điện trường này:

$$
\begin{equation}
\bold{E}_{in} = \bold{E_0} + \bold{E'} = \frac{\bold{E_0}}{\epsilon_r}
\end{equation}
$$

Điện trường bên ngoài chất điện môi lúc này giống như điện trường do điện tích gây ra bình thường:

$$
\begin{equation}
\bold{E}_{out} = \bold{E_0}
\end{equation}
$$

Ta có thể dùng định lý Gauss cho điện trường để chứng minh điều này:

$$
\begin{equation}
\int \bold{E} \cdot d\bold{A} = \frac{Q_{total}}{\epsilon_0} = \frac{Q + Q_p}{\epsilon_0}
\end{equation}
$$

Trong đó $Q_p$ là tổng các điện tích phân cực và nó bằng 0. Vậy điện trường lúc này giống như do điện tích $Q$ gây ra.

> 3. Cùng cấu hình 2, Tại sao vừa ra khỏi điện môi thì điện trường lại tăng về như điện trường do điện tích $Q$ gây ra ? Thứ gì đã giúp tăng cường độ điện trường về như cũ ?

Hãy nhớ về vật dẫn (giả sử thay điện môi thành vật dẫn), tại sao trong vật dẫn điện trường bằng 0 nhưng ra khỏi vật dẫn thì lại có điện trường do điện tích $Q$ gây ra ? Đấy là vì trên bề mặt vật dẫn lúc này có các điện tích mặt (và nó bằng với điện tích $Q$).

Tương tự khi điện trường bị giảm trong điện môi, ngay khi chúng ra ngoài và được tăng thêm nhờ cương độ điện trường của các điện tích phân cực tại bề mặt chất điện môi.

> 4. Chia mặt phẳng thành 2 nửa vô hạn, một bên là môi trường $\epsilon_1$, một bên là $\epsilon_2$. Đặt điện tích $Q > 0$ bên trong môi trường $\epsilon_1$, chuyện gì sẽ xảy ra?

Đầu tiên, điện tích $Q$ khiến môi trường $\epsilon_1$ phân cực, xuất hiện các điện tích mặt $Q_1'$ trái dấu tại bề mặt tiếp xúc với $Q$ khiến điện trường giảm đi $\epsilon_1$ lần. Tại bề mặt phân cách của môi trường $\epsilon_1$ sẽ xuất hiện các điện tích $Q_1'$ dương. Đồng thời khiến môi trường $\epsilon_2$ phân cực tại bề mặt phân cách, lúc này xuất hiện thêm các điện tích âm $Q_2'$ tại bề mặt phân cách của môi trường $\epsilon_2$.

<b>Lưu ý:</b> $Q_1' \not= Q_2'$ vì $\epsilon_1 \not= \epsilon_2$.

Ta có thể tìm được mật độ điện tích $\sigma_{p1}$ và $\sigma_{p2}$ tại bề mặt phân cách hai môi trường:

$$
\begin{equation*}
\sigma_{p1} = \bold{P_1} \cdot \hat{n}
\end{equation*}
$$

$$
\begin{equation*}
\sigma_{p2} = \bold{P_2} \cdot \hat{n}
\end{equation*}
$$

Mật độ điện tích tại bề mặt phân cách lúc này:

$$
\begin{equation}
\sigma_p = (\bold{P_1} - \bold{P_2}) \cdot \hat{n}
\end{equation}
$$

<b>Lưu ý:</b> $\bold{P_1}$ sẽ trái dấu với $\bold{P_2}$.