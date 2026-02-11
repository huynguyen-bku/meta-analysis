# Quy Trình Phân Tích Meta

## Tổng Quan Pipeline

Quy trình phân tích gồm **6 giai đoạn phân tích chính** + **4 giai đoạn tạo hình** để từ dữ liệu thô đến các con số có ý nghĩa.

```
RAW DATA
   ↓
[01] Chuẩn Bị Dữ Liệu
   ├─ Tính toán kích thước hiệu ứng (Hedges' g)
   └─ Gắn cờ các trường hợp cạnh
   ↓ (01_effect_sizes_full.csv)
   ↓
[02] Meta-Phân Tích Chính
   ├─ 3-level REML (chính)
   ├─ DL 2-level (kiểm tra chéo)
   └─ Ước tính tổng hợp cho 3 so sánh
   ↓ (02_meta_results.csv)
   ↓
[03] Đánh Giá Độ Lệch Xuất Bản
   ├─ Egger test
   ├─ Begg test
   ├─ Trim-and-fill
   └─ Fail-safe N
   ↓ (03_bias_summary.csv)
   ↓
[04] Phân Tích Điều Hòa (Moderators)
   ├─ Phân tích nhóm con cho 6 moderators
   ├─ Kiểm tra Q-between cho mỗi moderator
   └─ Ước tính ở mỗi mức
   ↓ (04_subgroup_results.csv)
   ↓
[05] Phân Tích Độ Nhạy
   ├─ Leave-one-out (xóa từng nghiên cứu)
   └─ Chẩn đoán ảnh hưởng
   ↓ (05_leave_one_out.csv, 05_influence_diagnostics.csv)
   ↓
[06] Phân Tích Sâu Theo Ngành
   └─ Phân tích meta riêng cho mỗi ngành
   ↓ (06_industry_results.csv)
   ↓
VISUALIZATIONS & REPORTS
```

## Giai Đoạn 1: Chuẩn Bị Dữ Liệu (01_data_preparation.py)

### Mục Đích
- Tải dữ liệu từ Excel
- Tính toán kích thước hiệu ứng (Hedges' g) cho mỗi so sánh
- Gắn cờ các trường hợp cạnh (outliers, lỗi dữ liệu)

### Đầu Vào
- `Data_Extraction_communication_public.xlsx` - Dữ liệu được trích xuất thủ công từ các bài báo

### Quy Trình Chi Tiết

#### Bước 1: Tải Dữ Liệu
```python
# Tải Excel
df = pd.read_excel(DATA_PATH)
# ~278 hàng (kích thước hiệu ứng)
# Kiểm tra:
# - Số lượng hàng
# - Số lượng bài báo riêng biệt (Paper_ID)
# - Số lượng thí nghiệm (Exp_ID)
# - Khoảng năm xuất bản
```

**Kiểm Tra Chất Lượng Dữ Liệu**:
- Không có giá trị thiếu trong các cột chính
- Năm xuất bản hợp lệ (2020-2024)
- Số mẫu dương (n > 0)

#### Bước 2: Tính Toán Kích Thước Hiệu Ứng

Cho mỗi hiệu ứng, tính toán **3 Hedges' g**:

```
Es_s (Strong Synergy):     g = (Trung Bình_HAI - Trung Bình_max{H,A}) / SD_Gộp
Es_h (Human Augmentation): g = (Trung Bình_HAI - Trung Bình_Human) / SD_Gộp
Es_a (AI Augmentation):    g = (Trung Bình_HAI - Trung Bình_AI) / SD_Gộp
```

**Cách Tính Phương Sai**:
```python
# SE(g) = √[(n_1 + n_2)/(n_1 × n_2) + g²/(2(n_1 + n_2 - 2))]
var_es = SE(g)²
```

**Xử Lý Trường Hợp Đặc Biệt**:
- **SD = 0**: Không thể tính g (gắn cờ `flag_sd_zero`)
- **Dữ liệu bị mất**: Sử dụng giá trị SD từ các nghiên cứu tương tự nếu có thể
- **Hiệu ứng cực kỳ lớn**: |g| > 5 (gắn cờ `flag_extreme_es`)

#### Bước 3: Gắn Cờ Trường Hợp Cạnh

Xác định các trường hợp có thể cần kiểm tra kỹ lưỡng:

```
flag_sd_zero:      SD = 0 (không thể tính kích thước hiệu ứng)
flag_extreme_es:   |g| > 5 (lớn bất thường)
flag_wide_ci:      Độ rộng CI > 10 (rất không chính xác)
```

**Mục Đích**: Cho phép phân tích độ nhạy (bao gồm/loại trừ các trường hợp gắn cờ)

### Đầu Ra
- `01_effect_sizes_full.csv` - Tất cả 278 hiệu ứng với kích thước hiệu ứng, phương sai, cờ
- `01_flagged_effect_sizes.csv` - Tóm tắt các trường hợp gắn cờ để kiểm tra

## Giai Đoạn 2: Meta-Phân Tích Chính (02_main_meta_analysis.py)

### Mục Đích
- Tính ước tính tổng hợp bằng 3-level REML
- So sánh với DL 2-level làm kiểm tra chéo
- Báo cáo ước tính, SE, CI, dự báo khoảng, I²

### Mô Hình

```r
# Pseudo-code R (thực tế được gọi từ Python)
rma.mv(
  yi ~ 1,                        # Không có predictors (intercept-only)
  V = var_matrix,                # Phương sai lấy mẫu từ bước 1
  random = ~ 1 | study_id,       # Hiệu ứng ngẫu nhiên ở mức học
  method = "REML"                # Ước tính hạn chế ML
)
```

### Ba Kích Thước Ước Tính

| So Sánh | Diễn Giải | Kết Quả Mong Đợi |
|---------|-----------|-----------------|
| **Strong Synergy** | HAI vs max(H, AI) | Âm (HAI thường kém) |
| **Human Augmentation** | HAI vs Human | Dương (AI giúp con người) |
| **AI Augmentation** | HAI vs AI | Gần bằng 0 (con người không thay đổi AI) |

### Đầu Ra Chính
```
comparison,k,estimate,se,ci_lower,ci_upper,p_value,
tau2,I2,Q,Q_pval,pred_lower,pred_upper,method
```

**Ý Nghĩa từng cột**:
- `k`: Số lượng hiệu ứng được phân tích
- `estimate`: Ước tính Hedges' g tổng hợp
- `se`: Sai số chuẩn của ước tính
- `ci_lower/upper`: Khoảng tin cậy 95%
- `p_value`: Xác suất hiệu ứng ≠ 0
- `tau2`: Thành phần phương sai REML
- `I2`: Tỷ lệ phần trăm độ không đồng nhất
- `Q`: Chi-bình phương tổng thể
- `pred_lower/upper`: Khoảng dự báo 95%

## Giai Đoạn 3: Đánh Giá Độ Lệch Xuất Bản (03_publication_bias.py)

### Mục Đích
- Kiểm tra độ lệch xuất bản bằng 4 phương pháp độc lập
- Đánh giá sự tin cậy của ước tính tổng hợp

### Bốn Kiểm Tra Chi Tiết

#### 3A: Kiểm Tra Egger
```
Lôgic: Nếu chỉ các kết quả dương được công bố,
hàm số nhỏ (hiệu ứng nhỏ) sẽ bị thiếu trên sơ đồ phễu
→ Phễu không đối xứng → Egger p < 0.05
```

**Diễn Giải**:
- Egger_p < 0.05: Gợi ý độ lệch (nhưng xem cảnh báo dưới)
- Egger_p ≥ 0.05: Không có bằng chứng độ lệch rõ ràng
- **Cảnh báo**: Kiểm tra Egger sẽ cho dương tính giả khi I² rất cao

#### 3B: Kiểm Tra Begg
```
Lôgic: Phi tham số thay thế cho Egger
Tương quan Kendall giữa kích thước hiệu ứng và SE
```

**Ưu Điểm**:
- Ít nhạy cảm với ngoại lệ
- Bổ sung tốt cho Egger

#### 3C: Trim-and-Fill
```
Lôgic: Giả định một bên của phễu bị mất
Xóa từng bước các nghiên cứu nhỏ nhất cho đến khi đối xứng
Ước tính và thêm những cái bị mất lại
```

**Đầu Ra**:
```
TrimFill_Missing:   Số lượng nghiên cứu được "thêm" để đối xứng
TrimFill_Original:  Ước tính gốc
TrimFill_Adjusted:  Ước tính sau khi đảo ngược "loại bỏ"
```

**Diễn Giải**:
- Nếu Adjusted ≈ Original: Độ lệch tối thiểu
- Nếu Adjusted << Original: Độ lệch xuất bản phóng đại kết quả
- Ví dụ: Original = 0.5, Adjusted = 0.1 → Độ lệch nghiêm trọng

#### 3D: Fail-Safe N
```
Lôgic: Bao nhiêu kết quả rỗng chưa xuất bản cần để lật ý nghĩa?
```

**Quy Tắc Ngón Tay**:
- Fail-Safe N > 5k + 10: Kết quả vững chắc
- Fail-Safe N < 5k + 10: Kết quả có thể yếu

**Ví Dụ**:
- k = 278 nghiên cứu → Ngưỡng = 5(278) + 10 = 1,400
- Nếu Fail-Safe N = 2,000 → Vững chắc
- Nếu Fail-Safe N = 500 → Yếu, cần cảnh báo

### Đầu Ra
```
Comparison,Egger_intercept,Egger_p,Egger_Bias,Begg_tau,Begg_p,...
TrimFill_Missing,TrimFill_Adjusted,FailSafe_N
```

## Giai Đoạn 4: Phân Tích Điều Hòa (04_moderator_analysis.py)

### Mục Đích
- Kiểm tra xem 6 moderators có giải thích độ không đồng nhất không
- Tính ước tính riêng cho mỗi mức moderator

### Sáu Moderators

```
1. Industry
   ├─ Business (Kinh Doanh)
   ├─ Communication (Truyền Thông)
   ├─ Healthcare (Y Tế)
   └─ Public Sector (Khu Vực Công Cộng)

2. Task_Type
   ├─ Decide (Ra Quyết Định)
   └─ Create (Tạo Nội Dung)

3. AI_Type_Cleaned
   ├─ Deep (Deep Learning)
   ├─ Rule-Based (Dựa Trên Quy Tắc)
   ├─ Shallow (Shallow Learning)
   ├─ Simulated-AI (AI Mô Phỏng)
   └─ Wizard of Oz (Người Giấu Mặt)

4. Participant_Expert
   ├─ Yes (Chuyên Gia)
   └─ No (Không Chuyên Gia)

5. AI_Expl_Incl
   ├─ Yes (Bao Gồm Giải Thích)
   └─ No (Không Giải Thích)

6. Year
   ├─ 2020, 2021, 2022, 2023, 2024
```

### Quy Trình Phân Tích

Cho mỗi moderator:

```
1. Stratify dữ liệu theo mức moderator
2. Fit 3-level REML riêng cho mỗi mức
3. Trích xuất (g, SE, CI, I², k)
4. Tính Q_between để kiểm tra hiệu ứng tổng thể
5. Báo cáo p-value: p < 0.05 → Moderator có ý nghĩa
```

### Diễn Giải Q-Between

```
Q_between = Σ [k_i × (g_i - g_overall)² / SE_i²]

p < 0.05: Các mức moderator khác nhau có ý nghĩa
         (Moderator giải thích phần của độ không đồng nhất)

p ≥ 0.05: Không có khác biệt rõ ràng giữa các mức
         (Moderator không giải thích nhiều)
```

### Ví Dụ Kết Quả

Từ kết quả thực tế - **Strong Synergy bởi Industry**:

| Industry | k | g | SE | 95% CI | I² | Q_between | p |
|----------|---|---|----|--------|----|-----------|----|
| Business | 46 | -0.93 | 0.15 | [-1.23, -0.62] | 98.9% | 885.7 | 0.0*** |
| Communication | 86 | -0.49 | 0.15 | [-0.77, -0.20] | 99.0% | (same) | (same) |
| Healthcare | 107 | -0.31 | 0.09 | [-0.48, -0.13] | 93.9% | (same) | (same) |
| Public Sector | 39 | -0.70 | 0.13 | [-0.96, -0.45] | 98.6% | (same) | (same) |

**Diễn Giải**:
- Q_between p < 0.001: Industry khác biệt rõ ràng
- Business có hiệu ứng âm lớn nhất (-0.93)
- Healthcare có hiệu ứng âm nhỏ nhất (-0.31) nhưng vẫn âm

### Đầu Ra
```
moderator,level,k,estimate,se,ci_lower,ci_upper,p_value,I2,
tau2,Q,Q_pval,Q_between,Q_between_df,Q_between_pval,comparison
```

## Giai Đoạn 5: Phân Tích Độ Nhạy (05_sensitivity.py)

### Mục Đích
- Xác định các nghiên cứu ảnh hưởng cao đến ước tính tổng hợp
- Kiểm tra sự ổn định của kết quả

### Leave-One-Out Analysis

```
Thủ tục:
1. Xóa nghiên cứu thứ 1, fit 3-level REML trên phần còn lại
2. Ghi lại g, SE, thay đổi so với bản gốc
3. Lặp lại cho mỗi nghiên cứu
4. Xác định những cái có |Thay Đổi| > SE (ảnh hưởng cao)
```

**Đầu Ra**:
```
study_id, estimate, se, change_absolute, change_pct, cook_distance
```

**Sử Dụng**:
- Phát hiện outliers có ảnh hưởng cao
- Quyết định có nên loại trừ hoặc kiểm tra lại
- Xác nhận kết quả chính không phụ thuộc vào các trường hợp cá biệt

### Chẩn Đoán Ảnh Hưởng

**Cook's Distance**: Đo mức độ một điểm ảnh hưởng đến đường hồi quy

```
Diễn Giải:
- Cook's D > 0.1: Ảnh hưởng cao (xem xét kiểm tra)
- Cook's D < 0.01: Ảnh hưởng tối thiểu
```

## Giai Đoạn 6: Phân Tích Sâu Ngành (06_industry_deep_dive.py)

### Mục Đích
- Meta-phân tích riêng cho mỗi ngành công nghiệp
- Xem moderators khác hoạt động như thế nào trong mỗi ngành

### Quy Trình
```
Cho mỗi ngành:
1. Lọc dữ liệu (chỉ hiệu ứng từ ngành đó)
2. Fit 3-level REML
3. Phân tích moderators khác (Task, AI_Type, Expertise, năm)
4. Báo cáo tóm tắt cho từng ngành
```

---

## Chạy Pipeline

### Tất Cả
```bash
cd /home/duyle/Research/JABES/meta-analysis/Experiment/src
python run_pipeline.py
```

### Chỉ Phân Tích (01-06)
```bash
python run_pipeline.py --analysis
```

### Chỉ Hình (10-14)
```bash
python run_pipeline.py --figures
```

### Giai Đoạn Riêng Lẻ
```bash
python 01_data_preparation.py
python 02_main_meta_analysis.py
python 03_publication_bias.py
python 04_moderator_analysis.py
python 05_sensitivity.py
python 06_industry_deep_dive.py
```

## Bảng Kiểm Tra Chất Lượng Dữ Liệu

Sau mỗi giai đoạn, kiểm tra:

- [ ] Số lượng kích thước hiệu ứng giữ nguyên hoặc giảm có kiểm soát
- [ ] Không có NaN không mong muốn trong cột chính
- [ ] Các ước tính hợp lý (g trong khoảng -5 đến +5)
- [ ] p-values trong khoảng [0, 1]
- [ ] SE luôn dương
- [ ] I² trong khoảng [0, 100]

---

**Bước Tiếp Theo**: Xem 04_TOM_TAT_KET_QUA.md để hiểu ý nghĩa của các số liệu
