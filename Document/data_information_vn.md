# THÔNG TIN DỮ LIỆU - Meta-Analysis Human-AI Collaboration

## 1. Tổng quan dữ liệu

| Thông số | Giá trị |
|----------|---------|
| **Tên file** | Data_Extraction_communication_public.xlsx |
| **Tổng số effect sizes** | 278 |
| **Số papers duy nhất** | 67 |
| **Số experiments duy nhất** | 90 |
| **Số cột (biến)** | 65 |
| **Giai đoạn** | 2020-2024 |

---

## 2. Cấu trúc các biến (65 cột)

### 2.1 Thông tin Paper/Nghiên cứu

| Tên biến | Mô tả | Kiểu dữ liệu |
|----------|-------|--------------|
| `Paper_Name` | Tên viết tắt của paper | String |
| `Paper_ID` | Mã định danh paper | Integer |
| `Exp_ID` | Mã experiment trong paper | Integer |
| `Treatment_ID` | Mã treatment/condition | Integer |
| `Measure_ID` | Mã đo lường | Integer |
| `Exp_ID_Cleaned` | Mã experiment đã xử lý (Paper.Exp) | Float |
| `ES_ID` | Mã effect size duy nhất | String |
| `Title` | Tiêu đề đầy đủ của paper | String |
| `Authors` | Danh sách tác giả | String |
| `Year` | Năm xuất bản | Integer (2020-2024) |
| `Industry` | Ngành/lĩnh vực | String |
| `Venue` | Nơi xuất bản (journal/conference) | String |

### 2.2 Thiết kế thực nghiệm

| Tên biến | Mô tả | Giá trị |
|----------|-------|---------|
| `Exp_Design` | Thiết kế thí nghiệm | Mixed, Between-Subjects |
| `Comp_Type` | Loại so sánh | Independent Samples / Dependent Samples |

### 2.3 Đặc điểm Task

| Tên biến | Mô tả | Giá trị |
|----------|-------|---------|
| `Task_Desc` | Mô tả task | String |
| `Marketing_Task` | Task liên quan marketing | Yes/No hoặc tên cụ thể |
| `Task_Data_Cleaned` | Loại dữ liệu task | Numeric, Text, Image, Categoric, Code, Video |
| `Task_Data_IsCategoric` | Dữ liệu có phải categorical | Yes/No |
| `Task_Data_IsCode` | Dữ liệu có phải code | Yes/No |
| `Task_Data_IsImage` | Dữ liệu có phải hình ảnh | Yes/No |
| `Task_Data_IsNumeric` | Dữ liệu có phải số | Yes/No |
| `Task_Data_IsText` | Dữ liệu có phải text | Yes/No |
| `Task_Data_IsVideo` | Dữ liệu có phải video | Yes/No |
| `Task_Output` | Output của task | Numeric, Binary, Categoric, Open Response |
| `Task_Output_Cleaned` | Output đã chuẩn hóa | Binary, Categoric, Numeric, Open Response |
| `Task_Type` | Loại task | Decide / Create |

### 2.4 Đặc điểm AI

| Tên biến | Mô tả | Giá trị |
|----------|-------|---------|
| `AI_Type` | Loại AI chi tiết | String |
| `AI_Data_In` | Input của AI | String |
| `AI_Data_Out` | Output của AI | String |
| `AI_Type_Cleaned` | Loại AI đã chuẩn hóa | Deep, Shallow, Rule-Based, Wizard of Oz, Simulated-AI |
| `Final_Decision` | Ai ra quyết định cuối | Human / AI |
| `Division_Labor` | Phân chia lao động | Yes/No |
| `Condition_Name` | Tên điều kiện thí nghiệm | String |
| `AI_Expl_Incl` | Có giải thích AI | Yes/No |
| `AI_Conf_Incl` | Có độ tin cậy AI | Yes/No |
| `AI_Expl_Type` | Loại giải thích AI | Image, Numeric, Text, etc. |

### 2.5 Metrics và Performance

| Tên biến | Mô tả | Giá trị |
|----------|-------|---------|
| `Perf_Metric` | Metric đo lường chi tiết | String |
| `Perf_Metric_Cleaned` | Metric đã chuẩn hóa | Accuracy, Error, Error Rate, Quality, Score, Other |
| `Perf_Dir` | Hướng của metric | Up (cao tốt) / Down (thấp tốt) |

### 2.6 Thông tin Participants

| Tên biến | Mô tả | Giá trị |
|----------|-------|---------|
| `N_Exp` | Tổng số participants | Integer |
| `N_Human` | Số participants điều kiện Human | Integer |
| `N_HumanAI` | Số participants điều kiện Human-AI | Integer |
| `Participant_Type` | Loại participant | Crowdworkers, Experts, Students, etc. |
| `Participant_Type_2` | Loại participant bổ sung | String |
| `Participant_Source` | Nguồn recruit | MTurk, Prolific, etc. |
| `Participant_Expert` | Có phải expert | Yes/No |
| `Participant_Crowdworker` | Có phải crowdworker | Yes/No |

### 2.7 Dữ liệu Performance (Mean, SD)

#### 2.7.1 Cấu trúc thí nghiệm - Ba điều kiện (3 Groups/Conditions)

Mỗi thí nghiệm trong meta-analysis này có **3 điều kiện (groups)** được so sánh:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CẤU TRÚC THÍ NGHIỆM ĐIỂN HÌNH                           │
│                                                                             │
│   Participants được chia thành 3 nhóm (conditions):                        │
│                                                                             │
│   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│   │   GROUP 1       │  │   GROUP 2       │  │   GROUP 3       │            │
│   │   HUMAN ONLY    │  │   AI ONLY       │  │   HUMAN + AI    │            │
│   │                 │  │                 │  │                 │            │
│   │ Con người làm   │  │ AI làm task     │  │ Con người được  │            │
│   │ task một mình   │  │ một mình        │  │ hỗ trợ bởi AI   │            │
│   │ (không có AI)   │  │ (không có human)│  │ (collaboration) │            │
│   │                 │  │                 │  │                 │            │
│   │ N = N_Human     │  │ N = (computed)  │  │ N = N_HumanAI   │            │
│   └─────────────────┘  └─────────────────┘  └─────────────────┘            │
│          │                    │                    │                        │
│          ▼                    ▼                    ▼                        │
│   Avg_Perf_Human       Avg_Perf_AI         Avg_Perf_HumanAI                │
│   Sd_Perf_Human        Sd_Perf_AI          Sd_Perf_HumanAI                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 2.7.2 Ý nghĩa "Nhóm" (Group) trong dữ liệu

**QUAN TRỌNG:** Dữ liệu này KHÔNG cần groupby vì mỗi row đã là một effect size hoàn chỉnh với thông tin từ cả 3 điều kiện.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MỖI ROW TRONG DATASET                               │
│                                                                             │
│   Mỗi row (ES_ID) = 1 effect size = 1 so sánh trong 1 experiment           │
│                                                                             │
│   Row đã chứa SẴN thông tin tổng hợp từ 3 nhóm:                            │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ ES_ID: "5.1.1.1"                                                    │  │
│   │                                                                     │  │
│   │ Thông tin từ HUMAN GROUP:                                          │  │
│   │   - Avg_Perf_Human = 330555    (Mean của n người trong group)      │  │
│   │   - Sd_Perf_Human = 122515     (SD của n người trong group)        │  │
│   │   - N_Human = 252              (Số người trong group)              │  │
│   │                                                                     │  │
│   │ Thông tin từ AI GROUP:                                             │  │
│   │   - Avg_Perf_AI = 180000       (Performance của AI - thường 1 giá trị)│
│   │   - Sd_Perf_AI = 0             (SD = 0 nếu AI cho kết quả cố định) │  │
│   │                                                                     │  │
│   │ Thông tin từ HUMAN-AI GROUP:                                       │  │
│   │   - Avg_Perf_HumanAI = 232267  (Mean của n người được AI hỗ trợ)   │  │
│   │   - Sd_Perf_HumanAI = 56580    (SD của n người được AI hỗ trợ)     │  │
│   │   - N_HumanAI = 247            (Số người trong group)              │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 2.7.3 Công thức tính Mean và SD trong mỗi Group

**A. Mean (Trung bình) của mỗi nhóm:**

```
                    Σ(performance của từng người trong nhóm)
Avg_Perf_Group = ─────────────────────────────────────────────
                           N (số người trong nhóm)
```

**Ví dụ cụ thể:**
- 252 người làm task dự đoán giá nhà (Human only)
- Mỗi người dự đoán → có prediction error
- `Avg_Perf_Human = 330555` là trung bình prediction error của 252 người

**B. Standard Deviation (Độ lệch chuẩn) của mỗi nhóm:**

```
                    ┌─────────────────────────────────────┐
                    │  Σ(xᵢ - x̄)²                        │
Sd_Perf_Group = √  │ ─────────────                       │
                    │    N - 1                            │
                    └─────────────────────────────────────┘

Trong đó:
- xᵢ = performance của người thứ i
- x̄ = Avg_Perf_Group (mean)
- N = số người trong group
```

#### 2.7.4 Giải thích các biến Performance

| Tên biến | Mô tả chi tiết | Nguồn gốc |
|----------|----------------|-----------|
| `Avg_Perf_Human` | **Mean performance của nhóm Human only (raw)**. Trung bình hiệu suất của N_Human người làm task một mình, KHÔNG có AI hỗ trợ. | Tính từ dữ liệu thô của paper gốc |
| `Avg_Perf_AI` | **Mean performance của AI only (raw)**. Hiệu suất của AI làm task một mình. Thường là 1 giá trị cố định (AI cho cùng output với cùng input). | Báo cáo trong paper gốc |
| `Avg_Perf_HumanAI` | **Mean performance của nhóm Human-AI (raw)**. Trung bình hiệu suất của N_HumanAI người được AI hỗ trợ khi làm task. | Tính từ dữ liệu thô của paper gốc |
| `Sd_Perf_Human` | **SD của nhóm Human only**. Độ biến thiên hiệu suất giữa các cá nhân trong nhóm Human. | Tính từ dữ liệu thô hoặc báo cáo trong paper |
| `Sd_Perf_AI` | **SD của AI only**. Thường = 0 vì AI cho kết quả nhất quán. Nếu > 0, AI có variance (ví dụ: stochastic model). | Báo cáo trong paper gốc |
| `Sd_Perf_HumanAI` | **SD của nhóm Human-AI**. Độ biến thiên hiệu suất giữa các cá nhân khi được AI hỗ trợ. | Tính từ dữ liệu thô hoặc báo cáo trong paper |

#### 2.7.5 Giá trị Adjusted (*_Adj) - Chuẩn hóa hướng

**Vấn đề:** Các metrics có hướng khác nhau:
- **Accuracy**: Cao = Tốt (↑)
- **Error**: Thấp = Tốt (↓)

**Giải pháp:** Điều chỉnh để TẤT CẢ đều có hướng "Cao = Tốt"

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        QUY TẮC ADJUSTED VALUES                              │
│                                                                             │
│   Nếu Perf_Dir = "Up" (cao = tốt):                                         │
│       Avg_Perf_*_Adj = Avg_Perf_* (giữ nguyên)                             │
│                                                                             │
│   Nếu Perf_Dir = "Down" (thấp = tốt):                                      │
│       Avg_Perf_*_Adj = -1 × Avg_Perf_* (đảo dấu)                           │
│                                                                             │
│   VÍ DỤ:                                                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ Metric = "Prediction Error" (Perf_Dir = "Down")                     │  │
│   │                                                                     │  │
│   │ Avg_Perf_Human = 330555 (error cao = tệ)                           │  │
│   │ Avg_Perf_Human_Adj = -330555 (đảo dấu → giá trị âm hơn = tệ hơn)   │  │
│   │                                                                     │  │
│   │ Avg_Perf_AI = 180000 (error thấp hơn = tốt hơn)                    │  │
│   │ Avg_Perf_AI_Adj = -180000 (đảo dấu → giá trị ít âm = tốt hơn)      │  │
│   │                                                                     │  │
│   │ So sánh: -180000 > -330555 → AI tốt hơn Human ✓                    │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Tên biến | Mô tả chi tiết |
|----------|----------------|
| `Avg_Perf_Human_Adj` | Mean Human sau khi chuẩn hóa hướng. Luôn có ý nghĩa: **Cao = Tốt** |
| `Avg_Perf_AI_Adj` | Mean AI sau khi chuẩn hóa hướng. Luôn có ý nghĩa: **Cao = Tốt** |
| `Avg_Perf_HumanAI_Adj` | Mean Human-AI sau khi chuẩn hóa hướng. Luôn có ý nghĩa: **Cao = Tốt** |

#### 2.7.6 Baseline và Worse - Xác định agent tốt hơn/kém hơn

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    XÁC ĐỊNH BASELINE VÀ WORSE                               │
│                                                                             │
│   So sánh: Avg_Perf_Human_Adj vs Avg_Perf_AI_Adj                           │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ Nếu Avg_Perf_AI_Adj > Avg_Perf_Human_Adj:                          │  │
│   │     → AI tốt hơn Human                                              │  │
│   │     → Baseline = "AI"                                               │  │
│   │     → Avg_Perf_Baseline_Adj = Avg_Perf_AI_Adj (max)                │  │
│   │     → Avg_Perf_Worse_Adj = Avg_Perf_Human_Adj (min)                │  │
│   │     → Sd_Perf_Baseline = Sd_Perf_AI                                │  │
│   │     → Sd_Perf_Worse = Sd_Perf_Human                                │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ Nếu Avg_Perf_Human_Adj > Avg_Perf_AI_Adj:                          │  │
│   │     → Human tốt hơn AI                                              │  │
│   │     → Baseline = "Human"                                            │  │
│   │     → Avg_Perf_Baseline_Adj = Avg_Perf_Human_Adj (max)             │  │
│   │     → Avg_Perf_Worse_Adj = Avg_Perf_AI_Adj (min)                   │  │
│   │     → Sd_Perf_Baseline = Sd_Perf_Human                             │  │
│   │     → Sd_Perf_Worse = Sd_Perf_AI                                   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   CÔNG THỨC:                                                                │
│   Avg_Perf_Baseline_Adj = max(Avg_Perf_Human_Adj, Avg_Perf_AI_Adj)        │
│   Avg_Perf_Worse_Adj = min(Avg_Perf_Human_Adj, Avg_Perf_AI_Adj)           │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Tên biến | Mô tả chi tiết | Công thức |
|----------|----------------|-----------|
| `Baseline` | Agent nào tốt hơn khi làm việc một mình | "AI" nếu AI > Human, "Human" nếu Human > AI |
| `Avg_Perf_Baseline_Adj` | Performance của agent tốt hơn | max(Human_Adj, AI_Adj) |
| `Avg_Perf_Worse_Adj` | Performance của agent kém hơn | min(Human_Adj, AI_Adj) |
| `Sd_Perf_Baseline` | SD của agent tốt hơn | SD tương ứng với Baseline |
| `Sd_Perf_Worse` | SD của agent kém hơn | SD tương ứng với Worse |
| `Synergy` | Human-AI có vượt trội cả hai không? | 1 nếu HumanAI > Baseline, 0 nếu không |

#### 2.7.7 Công thức tính Effect Size (Hedges' g)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CÔNG THỨC HEDGES' g                                      │
│                                                                             │
│   Bước 1: Tính Pooled Standard Deviation                                   │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │              ┌──────────────────────────────────────────────┐       │  │
│   │              │ (n₁-1)×SD₁² + (n₂-1)×SD₂²                   │       │  │
│   │   SD_pooled = │ ────────────────────────────                │       │  │
│   │              │        n₁ + n₂ - 2                           │       │  │
│   │              └──────────────────────────────────────────────┘       │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   Bước 2: Tính Cohen's d                                                   │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                M₁ - M₂                                              │  │
│   │   Cohen's d = ──────────                                            │  │
│   │               SD_pooled                                             │  │
│   │                                                                     │  │
│   │   Trong đó:                                                         │  │
│   │   - M₁ = Mean của nhóm Human-AI (Avg_Perf_HumanAI_Adj)             │  │
│   │   - M₂ = Mean của nhóm so sánh (Human/AI/Baseline tùy loại)        │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   Bước 3: Hiệu chỉnh mẫu nhỏ → Hedges' g                                  │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                         3                                           │  │
│   │   J = 1 - ─────────────────────                                     │  │
│   │           4×(n₁ + n₂) - 9                                           │  │
│   │                                                                     │  │
│   │   Hedges' g = J × Cohen's d                                         │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   Bước 4: Tính Variance của Effect Size                                   │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │            n₁ + n₂        g²                                        │  │
│   │   Var(g) = ──────── + ────────── × J²                              │  │
│   │            n₁ × n₂    2×(n₁+n₂)                                     │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 2.7.8 Ba loại Effect Size được tính

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    BA LOẠI EFFECT SIZE                                      │
│                                                                             │
│   1. HUMAN AUGMENTATION (es_h): Human-AI vs Human                          │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │   M₁ = Avg_Perf_HumanAI_Adj                                         │  │
│   │   M₂ = Avg_Perf_Human_Adj                                           │  │
│   │   SD₁ = Sd_Perf_HumanAI                                             │  │
│   │   SD₂ = Sd_Perf_Human                                               │  │
│   │                                                                     │  │
│   │   Ý nghĩa:                                                          │  │
│   │   - g > 0: Human-AI TỐT HƠN Human alone → AI giúp cải thiện        │  │
│   │   - g < 0: Human alone TỐT HƠN Human-AI → AI làm giảm hiệu suất    │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   2. AI AUGMENTATION (es_a): Human-AI vs AI                                │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │   M₁ = Avg_Perf_HumanAI_Adj                                         │  │
│   │   M₂ = Avg_Perf_AI_Adj                                              │  │
│   │   SD₁ = Sd_Perf_HumanAI                                             │  │
│   │   SD₂ = Sd_Perf_AI                                                  │  │
│   │                                                                     │  │
│   │   Ý nghĩa:                                                          │  │
│   │   - g > 0: Human-AI TỐT HƠN AI alone → Human thêm giá trị          │  │
│   │   - g < 0: AI alone TỐT HƠN Human-AI → Human làm giảm hiệu suất    │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   3. STRONG SYNERGY (es_s): Human-AI vs max(Human, AI)                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │   M₁ = Avg_Perf_HumanAI_Adj                                         │  │
│   │   M₂ = Avg_Perf_Baseline_Adj (= max của Human và AI)               │  │
│   │   SD₁ = Sd_Perf_HumanAI                                             │  │
│   │   SD₂ = Sd_Perf_Baseline                                            │  │
│   │                                                                     │  │
│   │   Ý nghĩa:                                                          │  │
│   │   - g > 0: TRUE SYNERGY - Human-AI vượt trội CẢ Human VÀ AI        │  │
│   │   - g < 0: NO SYNERGY - Human-AI kém hơn agent tốt nhất            │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 2.7.9 Ví dụ cụ thể từ dữ liệu

```
┌─────────────────────────────────────────────────────────────────────────────┐
│   VÍ DỤ: ES_ID = "5.1.1.1" (Poursabzi-Sangdeh 2021)                        │
│                                                                             │
│   Task: Predict housing prices                                              │
│   Metric: Prediction Error (Perf_Dir = "Down" → thấp = tốt)                │
│                                                                             │
│   RAW VALUES:                                                               │
│   ├── Avg_Perf_Human = 330555 (error của Human alone)                      │
│   ├── Avg_Perf_AI = 180000 (error của AI alone)                            │
│   └── Avg_Perf_HumanAI = 232267 (error của Human-AI)                       │
│                                                                             │
│   ADJUSTED VALUES (đảo dấu vì Error):                                      │
│   ├── Avg_Perf_Human_Adj = -330555                                         │
│   ├── Avg_Perf_AI_Adj = -180000                                            │
│   └── Avg_Perf_HumanAI_Adj = -232267                                       │
│                                                                             │
│   SO SÁNH:                                                                  │
│   -180000 > -330555 → AI tốt hơn Human → Baseline = "AI"                   │
│   Avg_Perf_Baseline_Adj = -180000 (AI)                                     │
│   Avg_Perf_Worse_Adj = -330555 (Human)                                     │
│                                                                             │
│   SYNERGY CHECK:                                                            │
│   -232267 < -180000 → Human-AI KHÔNG vượt trội Baseline (AI)              │
│   → Synergy = 0 (Không có synergy thực sự)                                 │
│                                                                             │
│   TÍNH EFFECT SIZES:                                                        │
│   es_h (HAI vs Human): So sánh -232267 vs -330555 → g > 0 (HAI tốt hơn H) │
│   es_a (HAI vs AI): So sánh -232267 vs -180000 → g < 0 (AI tốt hơn HAI)   │
│   es_s (Strong Synergy): So sánh -232267 vs -180000 → g < 0 (No synergy)  │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 2.7.10 Tóm tắt bảng biến Performance

| Tên biến | Mô tả | Nguồn/Công thức |
|----------|-------|-----------------|
| `Avg_Perf_Human` | Mean performance Human alone (raw) | Từ paper gốc: mean của N_Human người |
| `Avg_Perf_AI` | Mean performance AI alone (raw) | Từ paper gốc: performance của AI |
| `Avg_Perf_HumanAI` | Mean performance Human-AI (raw) | Từ paper gốc: mean của N_HumanAI người |
| `Avg_Perf_Human_Adj` | Mean Human (adjusted) | = Avg_Perf_Human × (-1 nếu Perf_Dir="Down") |
| `Avg_Perf_AI_Adj` | Mean AI (adjusted) | = Avg_Perf_AI × (-1 nếu Perf_Dir="Down") |
| `Avg_Perf_HumanAI_Adj` | Mean Human-AI (adjusted) | = Avg_Perf_HumanAI × (-1 nếu Perf_Dir="Down") |
| `Baseline` | Agent tốt hơn | "AI" hoặc "Human" |
| `Avg_Perf_Baseline_Adj` | Mean của agent tốt hơn | = max(Human_Adj, AI_Adj) |
| `Avg_Perf_Worse_Adj` | Mean của agent kém hơn | = min(Human_Adj, AI_Adj) |
| `Synergy` | Có synergy không | 1 nếu HumanAI_Adj > Baseline_Adj, else 0 |
| `Sd_Perf_Human` | SD của nhóm Human | Từ paper gốc |
| `Sd_Perf_AI` | SD của AI | Từ paper gốc (thường = 0) |
| `Sd_Perf_HumanAI` | SD của nhóm Human-AI | Từ paper gốc |
| `Sd_Perf_Baseline` | SD của Baseline | SD tương ứng với Baseline |
| `Sd_Perf_Worse` | SD của Worse | SD tương ứng với Worse |

### 2.8 Khác

| Tên biến | Mô tả |
|----------|-------|
| `Est_ES` | Effect size đã ước lượng (Yes/No) |
| `Notes` | Ghi chú 1 |
| `Notes_2` | Ghi chú 2 |

---

## 3. Phân bố dữ liệu chi tiết

### 3.1 Theo Industry (Ngành)

| Industry | Số lượng | Tỷ lệ |
|----------|----------|-------|
| Healthcare | 107 | 38.5% |
| Communication | 86 | 30.9% |
| Business | 46 | 16.5% |
| Public Sector | 39 | 14.0% |

### 3.2 Theo Năm

| Năm | Số lượng | Tỷ lệ |
|-----|----------|-------|
| 2020 | 62 | 22.3% |
| 2021 | 93 | 33.5% |
| 2022 | 65 | 23.4% |
| 2023 | 54 | 19.4% |
| 2024 | 4 | 1.4% |

### 3.3 Theo Task Type

| Task Type | Số lượng | Tỷ lệ |
|-----------|----------|-------|
| Decide | 252 | 90.6% |
| Create | 26 | 9.4% |

### 3.4 Theo Task Output

| Task Output | Số lượng | Tỷ lệ |
|-------------|----------|-------|
| Binary | 125 | 45.0% |
| Categoric | 103 | 37.1% |
| Open Response | 26 | 9.4% |
| Numeric | 24 | 8.6% |

### 3.5 Theo AI Type

| AI Type | Số lượng | Tỷ lệ |
|---------|----------|-------|
| Deep Learning | 132 | 47.5% |
| Rule-Based | 52 | 18.7% |
| Shallow | 46 | 16.5% |
| Wizard of Oz | 36 | 12.9% |
| Simulated-AI | 12 | 4.3% |

### 3.6 Theo Baseline

| Baseline | Số lượng | Tỷ lệ |
|----------|----------|-------|
| AI | 193 | 69.4% |
| Human | 85 | 30.6% |

**Giải thích:** Baseline = AI nghĩa là AI có performance tốt hơn Human (trong 69.4% cases)

### 3.7 Theo Participant Expertise

| Expert | Số lượng | Tỷ lệ |
|--------|----------|-------|
| No | 182 | 65.5% |
| Yes | 96 | 34.5% |

### 3.8 Theo AI Explanation

| AI Explanation | Số lượng | Tỷ lệ |
|----------------|----------|-------|
| Yes | 163 | 58.6% |
| No | 115 | 41.4% |

### 3.9 Theo Performance Metric

| Metric | Số lượng | Tỷ lệ |
|--------|----------|-------|
| Accuracy | 225 | 81.0% |
| Error | 17 | 6.1% |
| Error Rate | 16 | 5.8% |
| Quality | 12 | 4.3% |
| Score | 4 | 1.4% |
| Other | 2 | 0.7% |
| Time | 1 | 0.4% |
| Specificity | 1 | 0.4% |

### 3.10 Theo Experimental Design

| Design | Số lượng | Tỷ lệ |
|--------|----------|-------|
| Independent Samples | 144 | 51.8% |
| Dependent Samples | 134 | 48.2% |

---

## 4. Các biến quan trọng cho Meta-Analysis

### 4.1 Biến để tính Effect Size

**Cho mỗi loại so sánh cần:**

1. **Human-AI vs Human (Human Augmentation):**
   - m1 = `Avg_Perf_HumanAI_Adj`
   - m2 = `Avg_Perf_Human_Adj`
   - sd1 = `Sd_Perf_HumanAI`
   - sd2 = `Sd_Perf_Human`
   - n1 = `N_HumanAI`
   - n2 = `N_Human`

2. **Human-AI vs AI (AI Augmentation):**
   - m1 = `Avg_Perf_HumanAI_Adj`
   - m2 = `Avg_Perf_AI_Adj`
   - sd1 = `Sd_Perf_HumanAI`
   - sd2 = `Sd_Perf_AI`
   - n1 = `N_HumanAI`
   - n2 = `N_Human`

3. **Human-AI vs max(Human, AI) (Strong Synergy):**
   - m1 = `Avg_Perf_HumanAI_Adj`
   - m2 = `Avg_Perf_Baseline_Adj`
   - sd1 = `Sd_Perf_HumanAI`
   - sd2 = `Sd_Perf_Baseline`
   - n1 = `N_HumanAI`
   - n2 = `N_Human`

### 4.2 Biến Clustering (cho multi-level model)

- **Level 3:** `Paper_ID` (papers)
- **Level 2:** `Exp_ID_Cleaned` (experiments within papers)
- **Level 1:** `ES_ID` (effect sizes within experiments)

### 4.3 Moderators (Biến điều tiết)

| Biến | Mô tả | Loại |
|------|-------|------|
| `Task_Type` | Decide vs Create | Categorical |
| `Industry` | Ngành | Categorical |
| `Task_Output_Cleaned` | Loại output | Categorical |
| `Task_Data_Cleaned` | Loại dữ liệu | Categorical |
| `AI_Type_Cleaned` | Loại AI | Categorical |
| `AI_Expl_Incl` | Có explanation | Binary |
| `AI_Conf_Incl` | Có confidence | Binary |
| `Participant_Expert` | Expert hay không | Binary |
| `Participant_Crowdworker` | Crowdworker hay không | Binary |
| `Comp_Type` | Loại design | Categorical |
| `Year` | Năm | Continuous |

---

## 5. Lưu ý khi phân tích

### 5.1 Xử lý Adjusted Performance

- Các biến `*_Adj` đã được điều chỉnh để hướng đều là "cao = tốt"
- Với metrics như Error (thấp = tốt), giá trị đã được đảo dấu

### 5.2 Xử lý Missing Data

- Kiểm tra NA trong các biến performance trước khi tính effect size
- Một số effect sizes có thể không tính được nếu thiếu SD

### 5.3 Dependency Structure

- Nhiều effect sizes từ cùng một experiment
- Nhiều experiments từ cùng một paper
- Cần dùng multi-level model hoặc robust standard errors

### 5.4 Baseline Interpretation

- `Baseline = AI` nghĩa là AI > Human trong study đó
- `Baseline = Human` nghĩa là Human > AI trong study đó
- Điều này ảnh hưởng đến việc tính Strong Synergy

---

## 6. So sánh với dữ liệu mẫu (Healthcare study)

| Thông số | Healthcare Study | Study mới |
|----------|------------------|-----------|
| Effect sizes | 146 | 278 |
| Papers | 43 | 67 |
| Experiments | ~100 | 90 |
| Industries | 2 (Healthcare, Public) | 4 (+ Communication, Business) |
| Time period | 2020-2024 | 2020-2024 |
| Task types | Decide (~95%) | Decide (90.6%) |

---

*Document created: January 2026*
*Data file: Data_Extraction_communication_public.xlsx*