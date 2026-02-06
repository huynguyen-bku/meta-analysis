# DATA SCHEMA - Meta-Analysis Human-AI Collaboration

## Tổng quan cấu trúc dữ liệu

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        DATA_EXTRACTION_COMMUNICATION_PUBLIC.XLSX            │
│                              (278 rows × 65 columns)                        │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
   ┌─────────────┐           ┌─────────────┐            ┌─────────────┐
   │   PAPER     │           │ EXPERIMENT  │            │ EFFECT SIZE │
   │   LEVEL     │           │   LEVEL     │            │   LEVEL     │
   │  (67 papers)│           │(90 experiments)          │(278 ES)     │
   └─────────────┘           └─────────────┘            └─────────────┘
```

---

## 1. IDENTIFICATION VARIABLES (Biến định danh)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          HIERARCHICAL STRUCTURE                             │
│                                                                             │
│   Paper_ID ──────┬──────> Exp_ID ──────┬──────> ES_ID                      │
│   (Level 3)      │        (Level 2)    │        (Level 1)                  │
│                  │                     │                                    │
│   Ví dụ:         │                     │                                    │
│   Paper_ID = 5   │                     │                                    │
│        │         │                     │                                    │
│        ├─────────┼─> Exp_ID = 5.1 ────┼─> ES_ID = 5.1.1.1                  │
│        │         │                     │         5.1.2.1                    │
│        │         │                     │         5.1.3.1                    │
│        │         │                     │                                    │
│        └─────────┼─> Exp_ID = 5.2 ────┼─> ES_ID = 5.2.1.1                  │
│                  │                     │         5.2.2.1                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Trường | Kiểu | Mô tả | Ví dụ |
|--------|------|-------|-------|
| `Paper_Name` | String | Tên viết tắt của paper | "Poursabzi-Sangdeh_2021" |
| `Paper_ID` | Integer | Mã định danh paper (unique) | 5 |
| `Exp_ID` | Integer | Số thứ tự experiment trong paper | 1, 2, 3... |
| `Treatment_ID` | Integer | Số thứ tự treatment/condition | 1, 2, 3... |
| `Measure_ID` | Integer | Số thứ tự measure | 1 |
| `Exp_ID_Cleaned` | Float | Mã experiment duy nhất (Paper.Exp) | 5.1, 5.2 |
| `ES_ID` | String | Mã effect size duy nhất | "5.1.1.1" |

---

## 2. PAPER METADATA (Thông tin bài báo)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            PAPER INFORMATION                                │
│                                                                             │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐                │
│   │ Title   │    │ Authors │    │  Year   │    │ Venue   │                │
│   └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘                │
│        │              │              │              │                       │
│        ▼              ▼              ▼              ▼                       │
│   "Manipulating   "Poursabzi-     2021        "CHI 2021"                   │
│    and Measuring   Sangdeh,..."                                             │
│    Model..."                                                                │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────┐              │
│   │                      Industry                            │              │
│   │   ┌────────────┬────────────┬──────────┬──────────────┐ │              │
│   │   │ Healthcare │ Communication│ Business │Public Sector│ │              │
│   │   │   (38.5%)  │   (30.9%)   │ (16.5%) │   (14.0%)   │ │              │
│   │   └────────────┴────────────┴──────────┴──────────────┘ │              │
│   └─────────────────────────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Trường | Kiểu | Mô tả | Giá trị |
|--------|------|-------|---------|
| `Title` | String | Tiêu đề đầy đủ | "Manipulating and Measuring..." |
| `Authors` | String | Danh sách tác giả | "Poursabzi-Sangdeh, F.; ..." |
| `Year` | Integer | Năm xuất bản | 2020, 2021, 2022, 2023, 2024 |
| `Venue` | String | Nơi xuất bản | "CHI 2021", "Nature Medicine" |
| `Industry` | String | Ngành/lĩnh vực | Healthcare, Communication, Business, Public Sector |

---

## 3. EXPERIMENTAL DESIGN (Thiết kế thí nghiệm)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         EXPERIMENTAL DESIGN                                 │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                        Comp_Type (So sánh)                          │  │
│   │                                                                     │  │
│   │   ┌─────────────────────┐    ┌─────────────────────┐               │  │
│   │   │ Independent Samples │    │  Dependent Samples  │               │  │
│   │   │     (51.8%)         │    │      (48.2%)        │               │  │
│   │   │                     │    │                     │               │  │
│   │   │  Between-subjects   │    │  Within-subjects    │               │  │
│   │   │  (Different people) │    │  (Same people)      │               │  │
│   │   └─────────────────────┘    └─────────────────────┘               │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                        Exp_Design                                   │  │
│   │   "Mixed, Between-Subjects", "Within-Subjects", etc.                │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Trường | Kiểu | Mô tả | Giá trị |
|--------|------|-------|---------|
| `Exp_Design` | String | Thiết kế thí nghiệm chi tiết | "Mixed, Between-Subjects" |
| `Comp_Type` | String | Loại so sánh | "Independent Samples", "Dependent Samples" |

---

## 4. TASK CHARACTERISTICS (Đặc điểm nhiệm vụ)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           TASK CHARACTERISTICS                              │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                        Task_Type                                   │    │
│   │                                                                    │    │
│   │        ┌──────────────┐              ┌──────────────┐             │    │
│   │        │    DECIDE    │              │    CREATE    │             │    │
│   │        │   (90.6%)    │              │    (9.4%)    │             │    │
│   │        │              │              │              │             │    │
│   │        │ Phân loại,   │              │ Tạo nội dung,│             │    │
│   │        │ Chẩn đoán,   │              │ Viết văn bản │             │    │
│   │        │ Dự đoán      │              │              │             │    │
│   │        └──────────────┘              └──────────────┘             │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                      Task_Output_Cleaned                           │    │
│   │                                                                    │    │
│   │   ┌────────┐  ┌───────────┐  ┌─────────┐  ┌──────────────┐       │    │
│   │   │ Binary │  │ Categoric │  │ Numeric │  │ Open Response│       │    │
│   │   │ (45%)  │  │  (37.1%)  │  │ (8.6%)  │  │    (9.4%)    │       │    │
│   │   │        │  │           │  │         │  │              │       │    │
│   │   │ Yes/No │  │ A/B/C/D   │  │ Số liệu │  │  Văn bản tự  │       │    │
│   │   │ 0/1    │  │ Classes   │  │ cụ thể  │  │     do       │       │    │
│   │   └────────┘  └───────────┘  └─────────┘  └──────────────┘       │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                      Task_Data_Cleaned                             │    │
│   │                       (Loại dữ liệu đầu vào)                       │    │
│   │                                                                    │    │
│   │   ┌───────┐ ┌──────┐ ┌───────┐ ┌──────────┐ ┌──────┐ ┌───────┐   │    │
│   │   │ Text  │ │Image │ │Numeric│ │Categoric │ │ Code │ │ Video │   │    │
│   │   └───────┘ └──────┘ └───────┘ └──────────┘ └──────┘ └───────┘   │    │
│   └───────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Trường | Kiểu | Mô tả | Giá trị |
|--------|------|-------|---------|
| `Task_Desc` | String | Mô tả chi tiết task | "Predict housing prices" |
| `Marketing_Task` | String | Task marketing cụ thể | "Demand Forecasting", "No" |
| `Task_Type` | String | Loại task | "Decide", "Create" |
| `Task_Output` | String | Output gốc | "Numeric", "Binary" |
| `Task_Output_Cleaned` | String | Output đã chuẩn hóa | "Binary", "Categoric", "Numeric", "Open Response" |
| `Task_Data_Cleaned` | String | Loại dữ liệu đầu vào | "Text", "Image", "Numeric", "Categoric" |
| `Task_Data_Is*` | Boolean | Flags cho từng loại data | "Yes", "No" |

---

## 5. AI CHARACTERISTICS (Đặc điểm AI)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            AI CHARACTERISTICS                               │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                      AI_Type_Cleaned                               │    │
│   │                                                                    │    │
│   │   ┌──────────┐ ┌──────────┐ ┌───────────┐ ┌────────────┐          │    │
│   │   │   Deep   │ │ Shallow  │ │Rule-Based │ │Wizard of Oz│          │    │
│   │   │ (47.5%) │ │ (16.5%) │ │  (18.7%)  │ │  (12.9%)   │          │    │
│   │   │          │ │          │ │           │ │            │          │    │
│   │   │ CNN, RNN │ │ SVM, RF  │ │ If-then   │ │ Human giả  │          │    │
│   │   │ BERT,GPT │ │ LR, kNN  │ │ Expert    │ │  làm AI    │          │    │
│   │   └──────────┘ └──────────┘ └───────────┘ └────────────┘          │    │
│   │                                                                    │    │
│   │   ┌──────────────┐                                                │    │
│   │   │ Simulated-AI │  (4.3%) - AI mô phỏng cho thí nghiệm          │    │
│   │   └──────────────┘                                                │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                     AI Transparency Features                       │    │
│   │                                                                    │    │
│   │   ┌─────────────────────┐    ┌─────────────────────┐              │    │
│   │   │   AI_Expl_Incl      │    │   AI_Conf_Incl      │              │    │
│   │   │  (AI Explanation)   │    │  (AI Confidence)    │              │    │
│   │   │                     │    │                     │              │    │
│   │   │  Yes: 58.6%         │    │  Yes: 23.0%         │              │    │
│   │   │  No:  41.4%         │    │  No:  77.0%         │              │    │
│   │   │                     │    │                     │              │    │
│   │   │  "Tại sao AI đưa    │    │  "AI chắc chắn      │              │    │
│   │   │   ra quyết định?"   │    │   85% về kết quả"   │              │    │
│   │   └─────────────────────┘    └─────────────────────┘              │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                      Decision Authority                            │    │
│   │                                                                    │    │
│   │   Final_Decision: Ai ra quyết định cuối cùng?                     │    │
│   │   ┌──────────────────┐    ┌──────────────────┐                    │    │
│   │   │      Human       │    │        AI        │                    │    │
│   │   │  (Người quyết)   │    │   (AI quyết)     │                    │    │
│   │   └──────────────────┘    └──────────────────┘                    │    │
│   │                                                                    │    │
│   │   Division_Labor: Có phân chia công việc trước không?            │    │
│   │   ┌──────────────────┐    ┌──────────────────┐                    │    │
│   │   │       Yes        │    │        No        │                    │    │
│   │   └──────────────────┘    └──────────────────┘                    │    │
│   └───────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Trường | Kiểu | Mô tả | Giá trị |
|--------|------|-------|---------|
| `AI_Type` | String | Loại AI chi tiết | "CNN", "Random Forest" |
| `AI_Type_Cleaned` | String | Loại AI đã chuẩn hóa | "Deep", "Shallow", "Rule-Based", "Wizard of Oz" |
| `AI_Data_In` | String | Dữ liệu đầu vào của AI | "Image", "Text" |
| `AI_Data_Out` | String | Dữ liệu đầu ra của AI | "Numeric", "Binary" |
| `AI_Expl_Incl` | String | Có giải thích AI | "Yes", "No" |
| `AI_Conf_Incl` | String | Có độ tin cậy AI | "Yes", "No" |
| `AI_Expl_Type` | String | Loại giải thích | "Image", "Numeric", "Text" |
| `Final_Decision` | String | Ai quyết định cuối | "Human", "AI" |
| `Division_Labor` | String | Phân chia lao động | "Yes", "No" |
| `Condition_Name` | String | Tên điều kiện | "HAI = BB-2", "HAI = CLEAR-8" |

---

## 6. PARTICIPANT CHARACTERISTICS (Đặc điểm người tham gia)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PARTICIPANT CHARACTERISTICS                          │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                      Participant Types                             │    │
│   │                                                                    │    │
│   │   ┌──────────────────────────────────────────────────────────┐    │    │
│   │   │                   Participant_Expert                      │    │    │
│   │   │                                                          │    │    │
│   │   │   ┌─────────────────┐      ┌─────────────────┐          │    │    │
│   │   │   │   EXPERT (Yes)  │      │ NON-EXPERT (No) │          │    │    │
│   │   │   │     (34.5%)     │      │     (65.5%)     │          │    │    │
│   │   │   │                 │      │                 │          │    │    │
│   │   │   │ - Bác sĩ        │      │ - Sinh viên     │          │    │    │
│   │   │   │ - Chuyên gia    │      │ - Crowdworkers  │          │    │    │
│   │   │   │ - Professionals │      │ - General public│          │    │    │
│   │   │   └─────────────────┘      └─────────────────┘          │    │    │
│   │   └──────────────────────────────────────────────────────────┘    │    │
│   │                                                                    │    │
│   │   ┌──────────────────────────────────────────────────────────┐    │    │
│   │   │                Participant_Crowdworker                    │    │    │
│   │   │                                                          │    │    │
│   │   │   ┌─────────────────┐      ┌─────────────────┐          │    │    │
│   │   │   │ CROWDWORKER(Yes)│      │    OTHER (No)   │          │    │    │
│   │   │   │                 │      │                 │          │    │    │
│   │   │   │ - MTurk         │      │ - Lab study     │          │    │    │
│   │   │   │ - Prolific      │      │ - Field study   │          │    │    │
│   │   │   └─────────────────┘      └─────────────────┘          │    │    │
│   │   └──────────────────────────────────────────────────────────┘    │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                       Sample Sizes                                 │    │
│   │                                                                    │    │
│   │   N_Exp ─────────> Tổng số participants trong experiment          │    │
│   │       │                                                            │    │
│   │       ├──> N_Human ────> Số participants điều kiện Human only     │    │
│   │       │                                                            │    │
│   │       └──> N_HumanAI ──> Số participants điều kiện Human-AI       │    │
│   │                                                                    │    │
│   └───────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Trường | Kiểu | Mô tả | Giá trị |
|--------|------|-------|---------|
| `N_Exp` | Integer | Tổng số participants | 750, 1250 |
| `N_Human` | Integer | N trong điều kiện Human | 152, 252 |
| `N_HumanAI` | Integer | N trong điều kiện Human-AI | 147, 247 |
| `Participant_Type` | String | Loại participant | "Crowdworkers", "Experts" |
| `Participant_Type_2` | String | Loại bổ sung | "Students", "Professionals" |
| `Participant_Source` | String | Nguồn recruit | "MTurk", "Prolific" |
| `Participant_Expert` | String | Có phải expert | "Yes", "No" |
| `Participant_Crowdworker` | String | Có phải crowdworker | "Yes", "No" |

---

## 7. PERFORMANCE DATA (Dữ liệu hiệu suất)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PERFORMANCE DATA                                  │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                    THREE CONDITIONS                                │    │
│   │                                                                    │    │
│   │   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │    │
│   │   │  HUMAN ONLY  │  │   AI ONLY    │  │  HUMAN + AI  │            │    │
│   │   │              │  │              │  │              │            │    │
│   │   │ Avg_Perf_    │  │ Avg_Perf_    │  │ Avg_Perf_    │            │    │
│   │   │   Human      │  │   AI         │  │   HumanAI    │            │    │
│   │   │              │  │              │  │              │            │    │
│   │   │ Sd_Perf_     │  │ Sd_Perf_     │  │ Sd_Perf_     │            │    │
│   │   │   Human      │  │   AI         │  │   HumanAI    │            │    │
│   │   └──────────────┘  └──────────────┘  └──────────────┘            │    │
│   │          │                  │                  │                   │    │
│   │          └──────────────────┼──────────────────┘                   │    │
│   │                             │                                      │    │
│   │                             ▼                                      │    │
│   │                    ┌─────────────────┐                            │    │
│   │                    │    COMPARE      │                            │    │
│   │                    │                 │                            │    │
│   │                    │  Baseline =     │                            │    │
│   │                    │  max(H, AI)     │                            │    │
│   │                    │                 │                            │    │
│   │                    │  Worse =        │                            │    │
│   │                    │  min(H, AI)     │                            │    │
│   │                    └─────────────────┘                            │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                    ADJUSTED VALUES                                 │    │
│   │                                                                    │    │
│   │   *_Adj suffix = Đã điều chỉnh hướng (cao = tốt)                  │    │
│   │                                                                    │    │
│   │   Với metrics như "Error" (thấp = tốt):                           │    │
│   │   → Giá trị được đảo dấu để cao = tốt                             │    │
│   │                                                                    │    │
│   │   Ví dụ:                                                          │    │
│   │   Avg_Perf_Human = 330555 (Error)                                 │    │
│   │   Avg_Perf_Human_Adj = -330555 (Đảo dấu)                         │    │
│   └───────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.1 Performance Metrics

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| `Perf_Metric` | String | Metric gốc | "Prediction Error", "Accuracy" |
| `Perf_Metric_Cleaned` | String | Metric chuẩn hóa | "Accuracy" (81%), "Error" (6.1%), "Error Rate" (5.8%) |
| `Perf_Dir` | String | Hướng metric | "Up" (cao = tốt), "Down" (thấp = tốt) |

### 7.2 Raw Performance Values

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| `Avg_Perf_Human` | Float | Mean performance Human alone (raw) |
| `Avg_Perf_AI` | Float | Mean performance AI alone (raw) |
| `Avg_Perf_HumanAI` | Float | Mean performance Human-AI (raw) |
| `Sd_Perf_Human` | Float | SD performance Human |
| `Sd_Perf_AI` | Float | SD performance AI |
| `Sd_Perf_HumanAI` | Float | SD performance Human-AI |

### 7.3 Adjusted Performance Values

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| `Avg_Perf_Human_Adj` | Float | Mean Human (adjusted: cao = tốt) |
| `Avg_Perf_AI_Adj` | Float | Mean AI (adjusted: cao = tốt) |
| `Avg_Perf_HumanAI_Adj` | Float | Mean Human-AI (adjusted: cao = tốt) |
| `Baseline` | String | Agent tốt hơn | "AI" (69.4%), "Human" (30.6%) |
| `Avg_Perf_Baseline_Adj` | Float | Mean của agent tốt hơn (max) |
| `Avg_Perf_Worse_Adj` | Float | Mean của agent kém hơn (min) |
| `Sd_Perf_Baseline` | Float | SD của baseline |
| `Sd_Perf_Worse` | Float | SD của worse performer |
| `Synergy` | Integer | Có synergy thực sự? | 0 (No), 1 (Yes) |

---

## 8. EFFECT SIZE COMPUTATION (Tính Effect Size)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         EFFECT SIZE COMPUTATION                             │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                     HEDGES' g FORMULA                              │    │
│   │                                                                    │    │
│   │                      M₁ - M₂                                       │    │
│   │   Cohen's d = ──────────────────                                   │    │
│   │                   SD_pooled                                        │    │
│   │                                                                    │    │
│   │                              3                                     │    │
│   │   Hedges' g = (1 - ─────────────────) × d                         │    │
│   │                    4(n₁ + n₂) - 9                                  │    │
│   │                                                                    │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│   ┌───────────────────────────────────────────────────────────────────┐    │
│   │                   THREE TYPES OF COMPARISON                        │    │
│   │                                                                    │    │
│   │   1. HUMAN AUGMENTATION (HAI vs Human)                            │    │
│   │      ┌─────────────────────────────────────────────────────────┐  │    │
│   │      │ M₁ = Avg_Perf_HumanAI_Adj                               │  │    │
│   │      │ M₂ = Avg_Perf_Human_Adj                                 │  │    │
│   │      │ SD₁ = Sd_Perf_HumanAI                                   │  │    │
│   │      │ SD₂ = Sd_Perf_Human                                     │  │    │
│   │      │                                                          │  │    │
│   │      │ g > 0: Human-AI TỐT HƠN Human alone                     │  │    │
│   │      │ g < 0: Human alone TỐT HƠN Human-AI                     │  │    │
│   │      └─────────────────────────────────────────────────────────┘  │    │
│   │                                                                    │    │
│   │   2. AI AUGMENTATION (HAI vs AI)                                  │    │
│   │      ┌─────────────────────────────────────────────────────────┐  │    │
│   │      │ M₁ = Avg_Perf_HumanAI_Adj                               │  │    │
│   │      │ M₂ = Avg_Perf_AI_Adj                                    │  │    │
│   │      │ SD₁ = Sd_Perf_HumanAI                                   │  │    │
│   │      │ SD₂ = Sd_Perf_AI                                        │  │    │
│   │      │                                                          │  │    │
│   │      │ g > 0: Human-AI TỐT HƠN AI alone                        │  │    │
│   │      │ g < 0: AI alone TỐT HƠN Human-AI                        │  │    │
│   │      └─────────────────────────────────────────────────────────┘  │    │
│   │                                                                    │    │
│   │   3. STRONG SYNERGY (HAI vs max(Human, AI))                       │    │
│   │      ┌─────────────────────────────────────────────────────────┐  │    │
│   │      │ M₁ = Avg_Perf_HumanAI_Adj                               │  │    │
│   │      │ M₂ = Avg_Perf_Baseline_Adj (= max of H, AI)            │  │    │
│   │      │ SD₁ = Sd_Perf_HumanAI                                   │  │    │
│   │      │ SD₂ = Sd_Perf_Baseline                                  │  │    │
│   │      │                                                          │  │    │
│   │      │ g > 0: TRUE SYNERGY (HAI > cả H và AI)                  │  │    │
│   │      │ g < 0: NO SYNERGY (HAI không vượt trội)                 │  │    │
│   │      └─────────────────────────────────────────────────────────┘  │    │
│   └───────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 9. OTHER FIELDS (Các trường khác)

| Trường | Kiểu | Mô tả |
|--------|------|-------|
| `Est_ES` | String | Effect size có được ước lượng? | "Yes", "No" |
| `Notes` | String | Ghi chú 1 | Thông tin bổ sung |
| `Notes_2` | String | Ghi chú 2 | Thông tin bổ sung |

---

## 10. DATA FLOW DIAGRAM

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            DATA FLOW FOR META-ANALYSIS                      │
│                                                                             │
│   ┌────────────────┐                                                        │
│   │ RAW DATA       │                                                        │
│   │ (Excel file)   │                                                        │
│   └───────┬────────┘                                                        │
│           │                                                                 │
│           ▼                                                                 │
│   ┌────────────────────────────────────────────────────────────────────┐   │
│   │                    DATA PREPROCESSING                               │   │
│   │                                                                     │   │
│   │   1. Load data (pandas.read_excel)                                 │   │
│   │   2. Check missing values                                          │   │
│   │   3. Verify adjusted performance values                            │   │
│   └───────────────────────────────────────────────────────────────────┬┘   │
│                                                                        │    │
│           ┌────────────────────────────────────────────────────────────┘    │
│           │                                                                 │
│           ▼                                                                 │
│   ┌────────────────────────────────────────────────────────────────────┐   │
│   │                    COMPUTE EFFECT SIZES                             │   │
│   │                                                                     │   │
│   │   For each row:                                                    │   │
│   │   ├── es_h, var_h = compute_hedges_g(HAI vs Human)                │   │
│   │   ├── es_a, var_a = compute_hedges_g(HAI vs AI)                   │   │
│   │   ├── es_s, var_s = compute_hedges_g(HAI vs max)                  │   │
│   │   └── es_n, var_n = compute_hedges_g(HAI vs min)                  │   │
│   └───────────────────────────────────────────────────────────────────┬┘   │
│                                                                        │    │
│           ┌────────────────────────────────────────────────────────────┘    │
│           │                                                                 │
│           ▼                                                                 │
│   ┌────────────────────────────────────────────────────────────────────┐   │
│   │                    META-ANALYSIS                                    │   │
│   │                                                                     │   │
│   │   1. Random-effects model (DerSimonian-Laird)                      │   │
│   │   2. Heterogeneity (I², τ², Q)                                     │   │
│   │   3. Publication bias (Egger's, Rank test)                         │   │
│   │   4. Moderator analysis (subgroups)                                │   │
│   │   5. Sensitivity analysis (leave-one-out)                          │   │
│   └───────────────────────────────────────────────────────────────────┬┘   │
│                                                                        │    │
│           ┌────────────────────────────────────────────────────────────┘    │
│           │                                                                 │
│           ▼                                                                 │
│   ┌────────────────────────────────────────────────────────────────────┐   │
│   │                    OUTPUT                                           │   │
│   │                                                                     │   │
│   │   ├── Main_Results.csv (pooled effects)                           │   │
│   │   ├── ModeratorAnalysis_*.csv (subgroup results)                  │   │
│   │   ├── ForestPlot_*.png (visualizations)                           │   │
│   │   └── FunnelPlot_*.png (bias assessment)                          │   │
│   └────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 11. INTERPRETATION GUIDE

### Effect Size (Hedges' g) Interpretation

| Giá trị | Interpretation |
|---------|----------------|
| g ≈ 0.2 | Small effect |
| g ≈ 0.5 | Medium effect |
| g ≈ 0.8 | Large effect |
| g > 0 | Group 1 (Human-AI) tốt hơn Group 2 |
| g < 0 | Group 2 tốt hơn Group 1 (Human-AI) |

### Heterogeneity (I²) Interpretation

| Giá trị | Interpretation |
|---------|----------------|
| I² = 0-25% | Low heterogeneity |
| I² = 25-50% | Moderate heterogeneity |
| I² = 50-75% | Substantial heterogeneity |
| I² > 75% | Considerable heterogeneity |

### Baseline Interpretation

| Baseline | Meaning |
|----------|---------|
| "AI" | AI performed better than Human alone → AI là benchmark |
| "Human" | Human performed better than AI alone → Human là benchmark |

---

*Schema version: 1.0*
*Last updated: 2026*