# Hướng Dẫn Lặp Lại (Reproducibility Guide)

## Mục Đích

Tài liệu này hướng dẫn bạn chạy lại phân tích từ đầu để xác minh kết quả.

## Yêu Cầu Hệ Thống

### Phần Cứng
- RAM: ≥ 8GB
- Đĩa: ≥ 2GB không gian trống
- CPU: Bất kỳ (nhanh hơn tốt hơn)

### Phần Mềm

#### Python
```bash
# Phiên bản
Python >= 3.9

# Kiểm tra
python --version
```

#### R + Packages
```bash
# Phiên bản
R >= 4.0

# Packages cần (chạy trong R)
install.packages(c("metafor", "clubSandwich", "reshape2", "ggplot2"))
```

**Lưu ý về metafor**:
- `metafor` xử lý 3-level REML
- `clubSandwich` cung cấp small-sample corrections

#### Python Packages

Xem `requirements.txt` trong `Experiment/`:

```bash
pandas              # Xử lý dữ liệu
numpy               # Toán học số
scipy               # Thống kê
matplotlib          # Vẽ biểu đồ
seaborn             # Biểu đồ nâng cao
rpy2               # Gọi R từ Python
openpyxl           # Đọc Excel
```

### Cài Đặt Từ Scratch

#### 1. Tạo Environment (Conda)

```bash
# Tạo environment mới
conda create -n jabes_meta python=3.10

# Kích hoạt
conda activate jabes_meta
```

#### 2. Cài Đặt Python Packages

```bash
cd /home/duyle/Research/JABES/meta-analysis/Experiment

# Cài từ requirements.txt
pip install -r requirements.txt

# Hoặc cài thủ công
pip install pandas numpy scipy matplotlib seaborn rpy2 openpyxl
```

#### 3. Cài Đặt R (nếu chưa có)

```bash
# Ubuntu/Debian
sudo apt-get install r-base r-base-dev

# macOS
brew install r

# Cài packages R
R
# Trong R:
install.packages("metafor")
install.packages("clubSandwich")
q()
```

#### 4. Thiết Lập Liên Kết R-Python

```bash
# Kiểm tra rpy2 có thể tìm R không
python -c "import rpy2.robjects; print('OK')"

# Nếu lỗi, thiết lập R_HOME
export R_HOME=$(R RHOME)
```

---

## Dữ Liệu Input

### Tệp Chính
- **Đường dẫn**: `Experiment/data/Data_Extraction_communication_public.xlsx`
- **Định dạng**: Excel (.xlsx)
- **Số Hàng**: ~278 (kích thước hiệu ứng)
- **Số Cột**: ~40 (biến số và kết quả)

### Kiểm Tra Dữ Liệu

```python
import pandas as pd

df = pd.read_excel('data/Data_Extraction_communication_public.xlsx')

# Kiểm tra
print(f"Hàng: {len(df)}")
print(f"Cột: {list(df.columns)}")
print(df.head())

# Kiểm tra cột cần
required = ['Paper_ID', 'Exp_ID_Cleaned', 'Year', 'Industry', 'Task_Type',
            'AI_Type_Cleaned', 'Participant_Expert', 'AI_Expl_Incl']
print(f"Cột còn thiếu: {set(required) - set(df.columns)}")
```

### Cấu Trúc Dữ Liệu

Mỗi hàng đại diện cho một **kích thước hiệu ứng** (không phải một nghiên cứu).

```
Một nghiên cứu có thể có NHIỀU hàng nếu:
- Kiểm tra nhiều nhiệm vụ
- Kiểm tra nhiều nhóm người
- Báo cáo nhiều kết quả (độ chính xác, tốc độ, v.v.)
```

Các cột dữ liệu chính:
- `Paper_ID`: Mã định danh công bố
- `Exp_ID_Cleaned`: ID thí nghiệm trong bài báo
- `ES_ID`: ID kích thước hiệu ứng duy nhất
- Dữ liệu số: `n_hai`, `mean_hai`, `sd_hai`, `n_human`, `mean_human`, `sd_human`, v.v.
- Moderators: `Industry`, `Task_Type`, `AI_Type_Cleaned`, `Participant_Expert`, `AI_Expl_Incl`, `Year`

---

## Chạy Phân Tích

### Tùy Chọn 1: Chạy Toàn Bộ Pipeline

```bash
cd /home/duyle/Research/JABES/meta-analysis/Experiment/src

# Toàn bộ (01-06 + 10-14)
python run_pipeline.py

# Chỉ phân tích (01-06)
python run_pipeline.py --analysis

# Chỉ hình (10-14)
python run_pipeline.py --figures
```

### Tùy Chọn 2: Chạy Giai Đoạn Riêng Lẻ

```bash
# 01 - Chuẩn Bị Dữ Liệu
python 01_data_preparation.py
# Output: outputs/tables/01_effect_sizes_full.csv

# 02 - Meta-Phân Tích Chính
python 02_main_meta_analysis.py
# Output: outputs/tables/02_meta_results.csv

# 03 - Đánh Giá Độ Lệch Xuất Bản
python 03_publication_bias.py
# Output: outputs/tables/03_bias_summary.csv

# 04 - Phân Tích Moderators
python 04_moderator_analysis.py
# Output: outputs/tables/04_subgroup_results.csv

# 05 - Phân Tích Độ Nhạy
python 05_sensitivity.py
# Output: outputs/tables/05_*.csv

# 06 - Phân Tích Ngành
python 06_industry_deep_dive.py
# Output: outputs/tables/06_industry_results.csv
```

### Thời Gian Chạy Dự Kiến

| Giai Đoạn | Thời Gian |
|----------|----------|
| 01 - Chuẩn Bị | 1-2 phút |
| 02 - Meta-Phân Tích | 2-5 phút (gọi R) |
| 03 - Độ Lệch | 1-2 phút |
| 04 - Moderators | 10-15 phút (4 moderators × 3 comparisons) |
| 05 - Độ Nhạy | 2-5 phút |
| 06 - Ngành | 5-10 phút |
| **Tổng** | ~30-40 phút |

---

## Kiểm Tra Kết Quả

### Cách 1: So Sánh với Đầu Ra Tham Chiếu

```bash
# Kiểm tra tệp được tạo
ls outputs/tables/

# Kiểm tra hình được tạo
ls outputs/figures/
```

**Tệp Dự Kiến**:
```
outputs/tables/
├── 01_effect_sizes_full.csv
├── 01_flagged_effect_sizes.csv
├── 02_meta_results.csv
├── 03_bias_summary.csv
├── 04_subgroup_results.csv
├── 05_leave_one_out.csv
├── 05_influence_diagnostics.csv
└── 06_industry_results.csv
```

### Cách 2: So Sánh Số Liệu Chính

```python
import pandas as pd

# Tải kết quả
meta_results = pd.read_csv('outputs/tables/02_meta_results.csv')

# Kiểm tra các giá trị chính
print(meta_results[['comparison', 'estimate', 'p_value', 'I2']])

# So sánh với tài liệu này:
# Strong Synergy: g ≈ -0.53, p < 0.001, I² ≈ 98.4%
# Human Aug: g ≈ 0.49, p < 0.001, I² ≈ 90.4%
# AI Aug: g ≈ 0.15, p ≈ 0.128, I² ≈ 99.3%
```

**Sai Số Chấp Nhận**:
- Ước tính (g): ± 0.01 (có thể khác do REML hội tụ)
- p-values: ± 0.01
- I²: ± 0.5%

### Cách 3: Kiểm Tra Bằng Hình Ảnh

```python
# Xem sơ đồ rừng (Forest Plot)
from PIL import Image
import matplotlib.pyplot as plt

fig = Image.open('outputs/figures/Figure1_forestplot.png')
plt.imshow(fig)
plt.axis('off')
plt.show()
```

---

## Gỡ Lỗi

### Lỗi Phổ Biến & Giải Pháp

#### 1. "R not found" hoặc "rpy2 import error"

**Nguyên Nhân**: R chưa cài hoặc rpy2 không tìm thấy

**Giải Pháp**:
```bash
# Kiểm tra R đã cài chưa
which R

# Nếu chưa cài
conda install -c r r-base

# Thiết lập R_HOME
export R_HOME=$(R RHOME)

# Cài lại rpy2
pip install --force-reinstall rpy2
```

#### 2. "Excel file not found"

**Nguyên Nhân**: Đường dẫn dữ liệu sai

**Giải Pháp**:
```python
# Kiểm tra đường dẫn
from pathlib import Path
data_path = Path('data/Data_Extraction_communication_public.xlsx')
print(f"Tồn tại: {data_path.exists()}")
print(f"Đường dẫn tuyệt đối: {data_path.absolute()}")

# Nếu chưa có, kiểm tra vị trí
import os
os.system('find ~ -name "Data_Extraction*.xlsx"')
```

#### 3. "metafor package not found" (trong lỗi R)

**Giải Pháp**:
```bash
# Cài metafor trong R
R
install.packages("metafor")
install.packages("clubSandwich")
q()
```

#### 4. Lỗi "Memory" khi chạy 04_moderator_analysis.py

**Nguyên Nhân**: Dữ liệu quá lớn cho phép tính 3-level REML

**Giải Pháp**:
- Giảm số moderators
- Hoặc sử dụng máy có RAM nhiều hơn

#### 5. Các giá trị NaN hoặc inf trong đầu ra

**Nguyên Nhân**: Dữ liệu bị mất hoặc lỗi nhập

**Kiểm Tra**:
```python
df = pd.read_csv('outputs/tables/01_effect_sizes_full.csv')

# Kiểm tra NaN
print(f"NaN trong es_s: {df['es_s'].isna().sum()}")
print(f"NaN trong var_es_s: {df['var_es_s'].isna().sum()}")

# Kiểm tra Inf
print(f"Inf trong es_s: {(df['es_s'] == float('inf')).sum()}")
```

---

## Tùy Chỉnh Phân Tích

### Thay Đổi Thông Số

#### Số Lần Lặp REML

File: `src/experiment_meta/meta_engine.py` (nếu được mở rộng)

```python
# Tăng hội tụ chính xác (mặc định: 1e-4)
fit_threelevel_reml(..., maxiter=1000, tol=1e-6)
```

#### Thêm Moderator Mới

File: `src/experiment_meta/config.py`

```python
MODERATORS = [
    "Industry",
    "Task_Type",
    "AI_Type_Cleaned",
    "Participant_Expert",
    "AI_Expl_Incl",
    "Year",
    "YOUR_NEW_MODERATOR",  # Thêm ở đây
]
```

#### Lọc Dữ Liệu

File: `src/01_data_preparation.py`

```python
# Chỉ dữ liệu từ 2022-2023
df = df[df['Year'].isin([2022, 2023])]

# Chỉ Create tasks
df = df[df['Task_Type'] == 'Create']
```

---

## Xác Thực Độc Lập

### Kiểm Tra Lại Bằng Công Cụ Khác

#### Metafor (R trực tiếp)

```r
# Load dữ liệu
df <- read.csv("outputs/tables/01_effect_sizes_full.csv")

# Fit 3-level REML
library(metafor)
model <- rma.mv(yi ~ 1, V = var, random = ~ 1 | study_id,
                data = df, method = "REML")
print(model)

# So sánh với Python output
```

#### Meta (Python package)

```python
# Cài đặt
pip install pymeta

# Ước tính nhanh
from pymeta import MetaAnalysis
ma = MetaAnalysis(df['es_s'], df['var_es_s'])
print(ma.summary())
```

---

## Báo Cáo Lỗi

Nếu bạn gặp lỗi khác không được liệt kê:

1. **Kiểm tra phiên bản package**:
   ```bash
   pip list | grep -E "pandas|numpy|scipy|rpy2"
   ```

2. **Xem log chi tiết**:
   ```bash
   python 02_main_meta_analysis.py 2>&1 | tee debug.log
   ```

3. **Báo cáo**:
   - Ghi lỗi đầy đủ
   - Phiên bản Python/R/packages
   - Hệ điều hành
   - Gửi cho nhóm phát triển

---

## Tối Ưu Hóa Hiệu Suất

### Chạy Song Song (Nếu Có)

```python
# 04_moderator_analysis.py
# Sửa để chạy moderators song song (nâng cao)

from multiprocessing import Pool

def analyze_moderator(mod):
    return run_all_moderators(df, [mod], es_col, var_col, name)

with Pool(4) as p:  # 4 processes
    results = p.map(analyze_moderator, MODERATORS)
```

### Sử Dụng Cache

```python
# Lưu kết quả trung gian để tránh tính toán lại
import pickle

# Lần đầu tiên
meta_results = fit_threelevel_reml(...)
with open('cache/meta_results.pkl', 'wb') as f:
    pickle.dump(meta_results, f)

# Lần tiếp theo
with open('cache/meta_results.pkl', 'rb') as f:
    meta_results = pickle.load(f)
```

---

## Lịch Sử Phiên Bản & Thay Đổi

### v1.0 (Feb 2025)
- ✅ Phân tích 3-level REML hoàn thành
- ✅ Đánh giá độ lệch xuất bản 4 phương pháp
- ✅ Phân tích moderators 6 biến
- ✅ Phân tích độ nhạy (leave-one-out)
- ✅ Phân tích ngành sâu

### Cải Tiến Tương Lai
- [ ] Tương tác moderator
- [ ] Meta-hồi quy với moderators liên tục
- [ ] Mô phỏng Monte Carlo cho CI
- [ ] Bản đồ nhiệt của hiệu ứng theo ngành × AI type

---

## Tham Khảo Thêm

- **Tài liệu metafor**: https://wviechtb.github.io/metafor/
- **Hướng dẫn PRISMA 2020**: https://www.prisma-statement.org/
- **Sách Meta-Analysis**: Borenstein, M. et al. (2021)

---

**Hoàn Tất**: Bạn hiện đã có đủ thông tin để lặp lại toàn bộ phân tích. Chúc bạn thành công!
