# Phương Pháp Thống Kê

## Tổng Quan

Meta-phân tích này sử dụng **mô hình phân cấp ngẫu nhiên** để tổng hợp kích thước hiệu ứng trong khi tính đến cấu trúc dữ liệu lồng nhau và độ không đồng nhất. Phương pháp cân bằng sự chặt chẽ thống kê với khả năng diễn giải thực tế.

## Tại Sao Mô Hình 3 Cấp?

### Vấn Đề với Meta-Phân Tích Ngây Thơ

Meta-phân tích 2 cấp tiêu chuẩn giả định:
- Một kích thước hiệu ứng trên một nghiên cứu
- Sự độc lập giữa các kích thước hiệu ứng

**Thực Tế trong bộ dữ liệu này**:
- Nhiều kích thước hiệu ứng trên một nghiên cứu (ví dụ: cùng một cộng tác được kiểm tra trên các nhiệm vụ khác nhau)
- Các kích thước hiệu ứng từ cùng một nghiên cứu có tương quan
- Bỏ qua điều này vi phạm các giả định độc lập

**Hậu Quả khi bỏ qua lồng nhau**:
- Các lỗi chuẩn bị sai lệch (thường bị đánh giá thấp)
- Các thống kê kiểm tra được phóng đại (Lỗi Loại I)
- Tự tin sai lệch vào độ chính xác của ước tính tổng hợp

### Giải Pháp 3 Cấp

```
Cấp 1: Lỗi đo lường trong kích thước hiệu ứng
    ├─ Phương sai lấy mẫu (σ²_e)
    ├─ Phụ thuộc vào quy mô mẫu và biến đổi kết quả

Cấp 2: Biến đổi giữa kích thước hiệu ứng TRONG nghiên cứu
    ├─ Phương sai giữa kết quả (τ²_within)
    ├─ Các nghiên cứu kiểm tra nhiều nhiệm vụ/điều kiện
    ├─ Ví dụ: cùng một nghiên cứu kiểm tra "độ chính xác" và "tốc độ"

Cấp 3: Biến đổi giữa CÁC NGHIÊN CỨU
    ├─ Phương sai giữa các nghiên cứu (τ²_between)
    ├─ Các phương pháp, quần thể, hệ thống AI khác nhau
```

## Chỉ Số Kích Thước Hiệu Ứng: Hedges' g

### Tại Sao Hedges' g?

- **Sự khác biệt trung bình chuẩn hóa**: Cho phép so sánh trên các thang kết quả khác nhau
  - Ví dụ: Kết hợp "% độ chính xác" với "thời gian phản hồi (giây)"
- **Không bị sai lệch cho các mẫu nhỏ**: Hedges' g sửa chữa độ sai lệch trong Cohen's d
- **Dễ diễn giải**: 0.2 = nhỏ, 0.5 = trung bình, 0.8 = lớn (Tiêu chuẩn Cohen)

### Công Thức Tính Toán

Để so sánh giữa Nhóm 1 (ví dụ: HAI) vs Nhóm 2 (ví dụ: Người độc lập):

```
SD Gộp = √[((n₁-1)SD₁² + (n₂-1)SD₂²) / (n₁+n₂-2)]

Cohen's d = (Trung Bình₁ - Trung Bình₂) / SD Gộp

Hedges' g = d × (1 - 3/(4(n₁+n₂-2)-1))  [Sửa chữa sai lệch]

SE(g) = √[(n₁+n₂)/(n₁×n₂) + g²/(2(n₁+n₂-2))]

Phương Sai(g) = SE(g)²
```

### Diễn Giải Theo Hướng

| Kích Thước Hiệu Ứng | Diễn Giải | Ý Nghĩa |
|---|---|---|
| g > 0 | HAI vượt trội so với so sánh | Hiệu ứng cộng tác dương tính |
| g ≈ 0 | Không có sự khác biệt có ý nghĩa | Cộng tác trung lập hoặc hỗn hợp |
| g < 0 | HAI kém hơn so sánh | Cộng tác có hại hoặc can nhiễu |

### Ba Loại So Sánh

**1. Strong Synergy (es_s)**
```
Strong Synergy = Hiệu Suất(HAI) vs Hiệu Suất(max{Người, AI})
```
- Kiểm tra xem cộng tác có tạo ra lợi ích nổi hiện không
- Cả giá trị dương & âm đều có ý nghĩa
- Dương: Synergy thực sự; Âm: Không ai đơn độc tốt hơn

**2. Human Augmentation (es_h)**
```
Human Augmentation = Hiệu Suất(HAI) vs Hiệu Suất(Người độc lập)
```
- Kiểm tra xem AI có giúp hiệu suất con người không
- Dương: AI tăng cường; Âm: AI gây hại
- Kiểm tra cơ bản của "AI tập trung vào con người"

**3. AI Augmentation (es_a)**
```
AI Augmentation = Hiệu Suất(HAI) vs Hiệu Suất(AI độc lập)
```
- Kiểm tra xem con người có giúp hiệu suất AI không
- Dương: Con người cải thiện AI; Âm: Con người gây hại AI
- Kiểm tra cơ bản của "con người trong vòng lặp"

## Mô Hình Meta-Phân Tích Hiệu Ứng Ngẫu Nhiên

### Thông Số Mô Hình

```
Kích Thước Hiệu Ứng (i,j) = μ + u₃ⱼ + u₂ᵢⱼ + e₁ᵢⱼ

Trong Đó:
  μ = Hiệu ứng trung bình tổng thể (ước tính tổng hợp)
  u₃ⱼ ~ N(0, τ²_between)      Cấp 3: Giữa các nghiên cứu
  u₂ᵢⱼ ~ N(0, τ²_within)      Cấp 2: Giữa hiệu ứng trong nghiên cứu
  e₁ᵢⱼ ~ N(0, σ²_i)           Cấp 1: Lỗi lấy mẫu
```

### Thành Phần Phương Sai

| Thành Phần | Ý Nghĩa | Diễn Giải |
|---|---|---|
| σ²_e | Phương sai lấy mẫu | Độ chính xác của các nghiên cứu riêng lẻ (nghịch đảo của N) |
| τ²_within | Độ không đồng nhất hiệu ứng | Biến đổi trong các kết quả trong một nghiên cứu |
| τ²_between | Độ không đồng nhất giữa các nghiên cứu | Biến đổi trên các nghiên cứu khác nhau |

### Tổng Độ Không Đồng Nhất: I²

```
I² = (τ²_between + τ²_within) / (τ²_between + τ²_within + σ²_e)

Diễn Giải:
  I² < 25%     : Độ không đồng nhất thấp (các hiệu ứng đồng nhất)
  I² 25-75%    : Độ không đồng nhất trung bình
  I² > 75%     : Độ không đồng nhất cao (các hiệu ứng đa dạng)
```

**Trong phân tích này**: I² ≈ 90-99% cho thấy độ không đồng nhất cao
- Các kích thước hiệu ứng thay đổi đáng kể trên các nghiên cứu
- Nhu cầu mạnh mẽ để phân tích điều hòa
- Ước tính tổng hợp đại diện cho "trung bình" nhưng các hiệu ứng riêng lẻ có thể khác nhau

## Ước Tính Tham Số: REML

### Tại Sao REML (Restricted Maximum Likelihood)?

1. **Ít sai lệch hơn** so với Method of Moments (DerSimonian-Laird) cho τ²
2. **Xử lý dữ liệu không cân bằng** (số lượng hiệu ứng khác nhau trên một nghiên cứu)
3. **Tính chất mẫu nhỏ tốt hơn**
4. **Tiêu chuẩn ngành** cho meta-phân tích phân cấp

### Quy Trình Tính Toán

1. Tối đa hóa khả năng của dữ liệu có điều kiện trên các hiệu ứng cố định
2. Cập nhật lặp lại ước tính của:
   - μ (hiệu ứng tổng hợp)
   - τ²_within, τ²_between (thành phần phương sai)
3. Hội tụ khi thay đổi < ngưỡng dung sai

## Xác Thực Mô Hình: Kiểm Tra Chéo DL

### Dersimonian-Laird (DL) như Kiểm Tra Tính Vững

Sau ước tính REML, chúng ta so sánh kết quả với **mô hình DL (2 cấp)**:

```
DL sử dụng cấu trúc 2 cấp đơn giản hơn (bỏ qua lồng nhau trong nghiên cứu)
Kiểm tra xem các kết quả REML có nhạy cảm với thông số hóa phân cấp không
```

**Khi tương tự**: Kết quả vững chắc đối với lựa chọn mô hình
**Khi khác nhau**: Kết quả phụ thuộc vào tính toán 3 cấp
- Gợi ý rằng độ không đồng nhất trong nghiên cứu là đáng kể

## Kiểm Tra Ý Nghĩa Thống Kê

### Kiểm Tra Giả Thuyết

```
H₀: μ = 0  (Không có hiệu ứng trung bình)
H₁: μ ≠ 0  (Hiệu ứng tồn tại)

Thống kê kiểm tra: z = g / SE(g)
p-value: P(|Z| > |z|) từ phân phối bình thường tiêu chuẩn
```

**Diễn Giải**:
- p < 0.05: Có ý nghĩa thống kê (bác bỏ H₀)
- p ≥ 0.05: Không có ý nghĩa (hiệu ứng không rõ ràng)

### Khoảng Tin Cậy (95%)

```
95% CI = g ± 1.96 × SE(g)

Diễn Giải Thực Tế:
  - Nếu CI loại trừ 0: Có ý nghĩa ở α = 0.05
  - CI rộng: Ước tính không chính xác (cần thêm nghiên cứu)
  - CI hẹp: Ước tính chính xác (tự tin vào hướng/độ lớn)
```

### Khoảng Dự Đoán (95%)

```
95% PI = g ± 1.96 × √(τ² + SE²)

Ý Nghĩa: Trong một nghiên cứu mới được chọn ngẫu nhiên,
có 95% cơ hội hiệu ứng rơi vào khoảng này
(tính đến độ không đồng nhất giữa các nghiên cứu)
```

**Trường Hợp Sử Dụng**:
- Khoảng dự đoán rộng hơn khoảng tin cậy
- Phản ánh tốt hơn độ không đồng nhất dự kiến
- Quan trọng cho người thực hành: "Hiệu ứng có khả năng xảy ra trong bối cảnh của tôi là gì?"

## Phân Tích Điều Hòa: Kiểm Tra Q-Giữa

### Tại Sao Kiểm Tra Điều Hòa?

I² cao cho thấy các hiệu ứng không đồng đều. **Điều hòa** giúp giải thích biến đổi:

```
Q_tổng = Q_between + Q_within

Q_between kiểm tra xem các trung bình ở mức điều hòa khác nhau có ý nghĩa không
Q_within kiểm tra độ không đồng nhất còn lại sau khi điều hòa
```

### Quy Trình Phân Tích Nhóm Con

Cho mỗi điều hòa (ví dụ: "Ngành Công Nghiệp"):

1. **Phân tầng dữ liệu** theo mức điều hòa (Kinh Doanh, Truyền Thông, Y Tế, v.v.)
2. **Fit các mô hình riêng** cho từng mức
3. **Trích xuất ước tính** (kích thước hiệu ứng, SE, CI, I² cho mỗi mức)
4. **Tính toán Q_between** để kiểm tra hiệu ứng điều hòa tổng thể
5. **Báo cáo p-value**: p < 0.05 gợi ý điều hòa giải thích độ không đồng nhất

### Ví Dụ: Điều Hòa Ngành Công Nghiệp

```
Q_between = Σ [kᵢ(gᵢ - g_tổng)² / σ²ᵢ]

Trong Đó:
  kᵢ = số lượng hiệu ứng trong nhóm i
  gᵢ = ước tính tổng hợp cho nhóm i
  g_tổng = ước tính tổng hợp tổng thể
  σ²ᵢ = phương sai lấy mẫu trong nhóm i

p-value: P(χ²_df > Q_between) trong đó df = (# nhóm - 1)
```

## Đánh Giá Độ Lệch Xuất Bản

### Cách Tiếp Cận Bốn Phương Pháp

#### 1. Kiểm Tra Hồi Quy Egger

**Nguyên Lý**: Các nghiên cứu nhỏ hơn có độ chính xác kém; nếu chỉ có các nghiên cứu nhỏ dương tính được công bố, phễu không đối xứng.

```
Hiệu Ứng Chuẩn Hóa / SE = a + b × (1/SE)  [Hồi Quy]

H₀: b = 0 (đối xứng, không lệch)
H₁: b ≠ 0 (không đối xứng, có thể lệch)

p < 0.05 gợi ý độ lệch xuất bản
```

**Hạn Chế**: Nhạy cảm với độ không đồng nhất; nhiều dương tính giả

#### 2. Kiểm Tra Tương Quan Xếp Hạng Begg

**Nguyên Lý**: Thay thế cho Egger; sử dụng tương quan xếp hạng (phi tham số).

```
Kendall's τ = tương quan(Kích Thước Hiệu Ứng, Phương Sai)

H₀: τ = 0 (không tương quan, đối xứng)
H₁: τ ≠ 0 (tương quan có, không đối xứng)

p < 0.05 gợi ý độ lệch xuất bản
```

**Ưu Điểm**: Ít nhạy cảm với ngoại lệ hơn Egger

#### 3. Phương Pháp Trim-and-Fill

**Nguyên Lý**: Lặp lại xóa các nghiên cứu nhỏ nhất cho đến khi đạt đối xứng, sau đó ước tính những gì còn thiếu.

```
Đầu Ra:
  - Trimmed_k: Số lượng các nghiên cứu bị xóa
  - Adjusted_estimate: Ước tính tổng hợp g sau khi thêm các nghiên cứu còn thiếu

Diễn Giải:
  Nếu adjusted_g nhỏ hơn đáng kể: Độ lệch xuất bản phóng đại bản gốc
  Nếu adjusted_g ≈ bản gốc: Độ lệch có thể tối thiểu
```

**Hạn Chế**: Giả định các nghiên cứu còn thiếu ở một bên; phương pháp xấp xỉ

#### 4. Fail-Safe N (Rosenthal)

**Nguyên Lý**: Bao nhiêu các nghiên cứu kết quả rỗng chưa được công bố cần để lật lại ý nghĩa?

```
Fail-Safe N ≈ (Σ z²) / z_critical

N Lớn: Kết quả vững chắc (cần nhiều nulls chưa công bố để thay đổi kết luận)
N Nhỏ: Kết quả yếu (vài nghiên cứu có thể lật lại ý nghĩa)
```

**Ngưỡng**: FS-N > 5k + 10 (k = số lượng nghiên cứu) gợi ý sự vững chắc đầy đủ

## Phân Tích Độ Nhạy Cảm

### Phân Tích Bỏ Một Bên Ngoài

**Phương Pháp**: Tuần tự xóa mỗi nghiên cứu, fit lại mô hình

**Mục Đích**: Xác định các nghiên cứu ảnh hưởng dẫn ước tính tổng hợp

**Đầu Ra**:
- Estimate_LOO: Kích thước hiệu ứng mà không có nghiên cứu i
- Thay Đổi: Xóa thay đổi kết quả bao nhiêu?
- Ảnh Hưởng nếu: |Thay Đổi| > SE điển hình

### Chẩn Đoán Ảnh Hưởng

**Độ Đo**: Cook's distance, leverage, độ dư chuẩn hóa

**Diễn Giải**:
- Cook's D Cao: Nghiên cứu nặng nề ảnh hưởng đến ước tính tổng hợp
- Có thể bảo hành kiểm tra độ nhạy hoặc kiểm tra ngoại lệ

---

**Bước Tiếp Theo**: Xem 03_QTRÌNH_PHAN_TICH.md để hiểu cách các phương pháp này được áp dụng trong thực tế.
