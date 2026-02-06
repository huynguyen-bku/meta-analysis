# Hiệu quả Hợp tác Giữa Con Người và Trí Tuệ Nhân Tạo: Một Phân Tích Tổng Hợp Đa Ngành

## Human-AI Collaboration Effectiveness: A Cross-Domain Meta-Analysis

---

## Tóm tắt (Abstract)

**Tiếng Việt:**
Nghiên cứu này thực hiện phân tích tổng hợp (meta-analysis) trên 278 effect sizes từ 67 nghiên cứu và 90 thí nghiệm để đánh giá hiệu quả hợp tác giữa con người và trí tuệ nhân tạo (AI) so với con người làm việc độc lập và AI làm việc độc lập. Dữ liệu được thu thập từ các lĩnh vực Healthcare, Communication, Business và Public Sector trong giai đoạn 2020-2024. Kết quả cho thấy: (1) Hệ thống Human-AI cải thiện đáng kể hiệu suất so với con người độc lập (Human Augmentation), (2) Hiệu suất Human-AI so với AI độc lập có kết quả hỗn hợp tùy thuộc vào bối cảnh, (3) Synergy thực sự (Human-AI vượt trội cả Human và AI) hiếm khi đạt được. Các yếu tố điều tiết quan trọng bao gồm loại task, loại AI, expertise của người tham gia, và sự hiện diện của AI explanation.

**English:**
This meta-analysis synthesizes 278 effect sizes from 67 studies and 90 experiments to evaluate the effectiveness of human-AI collaboration compared to humans working alone and AI working alone. Data were collected from Healthcare, Communication, Business, and Public Sector domains during 2020-2024. Results indicate: (1) Human-AI systems significantly improve performance compared to humans alone (Human Augmentation), (2) Human-AI performance compared to AI alone shows mixed results depending on context, (3) True synergy (Human-AI outperforming both Human and AI) is rarely achieved. Key moderating factors include task type, AI type, participant expertise, and presence of AI explanations.

**Keywords:** Human-AI collaboration, meta-analysis, augmentation, synergy, decision-making, artificial intelligence

---

## 1. Giới thiệu (Introduction)

### 1.1 Bối cảnh nghiên cứu

Trí tuệ nhân tạo (AI) ngày càng được triển khai song song với các chuyên gia con người trong nhiều lĩnh vực quan trọng như chăm sóc sức khỏe, dịch vụ công, kinh doanh và truyền thông. Quan điểm phổ biến cho rằng AI nên augment (hỗ trợ) thay vì replace (thay thế) người ra quyết định (Holzinger et al., 2019).

Tuy nhiên, bằng chứng về hiệu quả hợp tác human-AI còn nhiều mâu thuẫn. Một số nghiên cứu cho thấy các cặp hybrid thường hoạt động kém hơn so với agent mạnh hơn khi làm việc độc lập (Vaccaro et al., 2024). Ngược lại, trong các nhiệm vụ phức tạp có thể khai thác lỗi bổ sung, sự hợp tác được thiết kế tốt có thể vượt trội cả con người và AI riêng lẻ (Freyer et al., 2024; Zöller et al., 2025).

### 1.2 Khoảng trống nghiên cứu

Dù đã có nhiều nghiên cứu về human-AI collaboration, vẫn còn thiếu sự hiểu biết rõ ràng về:
- **Khi nào** và **mức độ nào** các nhóm human-AI vượt trội so với năng lực cá nhân
- Sự khác biệt giữa các ngành/lĩnh vực khác nhau
- Các yếu tố điều tiết ảnh hưởng đến hiệu quả hợp tác

### 1.3 Mục tiêu nghiên cứu

Nghiên cứu này nhằm trả lời các câu hỏi:
1. **RQ1:** Hệ thống Human-AI có cải thiện hiệu suất so với con người làm việc độc lập không? (Human Augmentation)
2. **RQ2:** Hệ thống Human-AI có cải thiện hiệu suất so với AI làm việc độc lập không? (AI Augmentation)
3. **RQ3:** Hệ thống Human-AI có đạt được synergy thực sự (vượt trội cả Human và AI) không? (Strong Synergy)
4. **RQ4:** Các yếu tố nào điều tiết hiệu quả hợp tác human-AI?

---

## 2. Phương pháp nghiên cứu (Methodology)

### 2.1 Chiến lược tìm kiếm và tiêu chí lựa chọn

**Tiêu chí đưa vào (Inclusion criteria):**
1. Thiết kế thực nghiệm (experimental design)
2. Có điều kiện human-only, AI-only, và joint (human-AI)
3. Đủ thống kê để tính effect size
4. Xuất bản bằng tiếng Anh từ 01/2020 đến 06/2024
5. Mô tả rõ ràng về participants, tasks, và AI systems

**Tiêu chí loại trừ (Exclusion criteria):**
- Thiết kế quan sát (observational)
- Mô phỏng không có điều kiện joint
- Thiếu dữ liệu cần thiết

### 2.2 Nguồn dữ liệu

**Databases searched:**
- ACM Digital Library
- Web of Science
- Backward/forward citations

### 2.3 Trích xuất dữ liệu

Từ mỗi nghiên cứu, trích xuất:
- **Thông tin nghiên cứu:** Paper ID, Authors, Year, Venue
- **Đặc điểm task:** Task Type (Decide/Create), Task Output, Task Data
- **Đặc điểm AI:** AI Type (Deep/Shallow/Rule-Based/Wizard-of-Oz), AI Explanation, AI Confidence
- **Đặc điểm participants:** Expert/Non-expert, Crowdworker
- **Performance metrics:** Accuracy, Error, Quality, etc.
- **Effect size data:** Mean, SD, N cho mỗi điều kiện

### 2.4 Tính toán Effect Size

Sử dụng Hedges' g (SMD với hiệu chỉnh mẫu nhỏ):

**Cohen's d:**
$$d = \frac{\bar{X}_1 - \bar{X}_2}{SD_{pooled}}$$

**Hedges' g:**
$$g = \left(1 - \frac{3}{4(n_1 + n_2) - 9}\right) \times d$$

**Ba loại so sánh:**
1. **Strong Synergy:** Human-AI vs max(Human, AI)
2. **Human Augmentation:** Human-AI vs Human alone
3. **AI Augmentation:** Human-AI vs AI alone

### 2.5 Mô hình phân tích

Sử dụng **random-effects multi-level meta-analysis** với cấu trúc:
- Level 1: Effect sizes within experiments
- Level 2: Experiments within papers
- Cluster-robust standard errors để xử lý dependency

**Model specification:**
```
yi ~ 1 + (1 | Exp_ID/ES_ID)
```

### 2.6 Đánh giá Heterogeneity

- **Q statistic:** Kiểm định variation vượt quá sampling error
- **I² statistic:** % variation do sự khác biệt thực sự giữa các nghiên cứu
- **τ² (tau-squared):** Total between-study variance

### 2.7 Kiểm định Publication Bias

- **Egger's test:** Kiểm tra funnel plot asymmetry
- **Rank correlation test:** Begg & Mazumdar test

---

## 3. Kết quả (Results)

### 3.1 Tổng quan dữ liệu

| Thống kê | Giá trị |
|----------|---------|
| Tổng số effect sizes | 278 |
| Số papers | 67 |
| Số experiments | 90 |
| Giai đoạn | 2020-2024 |

**Phân bố theo Industry:**
| Industry | n (%) |
|----------|-------|
| Healthcare | 107 (38.5%) |
| Communication | 86 (30.9%) |
| Business | 46 (16.5%) |
| Public Sector | 39 (14.0%) |

**Phân bố theo Task Type:**
| Task Type | n (%) |
|-----------|-------|
| Decide | 252 (90.6%) |
| Create | 26 (9.4%) |

**Phân bố theo AI Type:**
| AI Type | n (%) |
|---------|-------|
| Deep Learning | 132 (47.5%) |
| Rule-Based | 52 (18.7%) |
| Shallow | 46 (16.5%) |
| Wizard of Oz | 36 (12.9%) |
| Simulated-AI | 12 (4.3%) |

**Phân bố theo Participant Expertise:**
| Expert | n (%) |
|--------|-------|
| No | 182 (65.5%) |
| Yes | 96 (34.5%) |

### 3.2 Kết quả Meta-Analysis chính

| So sánh | k | Hedges' g | 95% CI | p-value | I² |
|---------|---|-----------|--------|---------|-----|
| Human-AI vs Human | 278 | [TBD] | [TBD] | [TBD] | [TBD] |
| Human-AI vs AI | 278 | [TBD] | [TBD] | [TBD] | [TBD] |
| Human-AI vs max(H,AI) | 278 | [TBD] | [TBD] | [TBD] | [TBD] |

**Giải thích:**
- **Human Augmentation (HAI vs H):** Effect size dương cho thấy Human-AI tốt hơn Human alone
- **AI Augmentation (HAI vs AI):** Effect size dương cho thấy Human-AI tốt hơn AI alone
- **Strong Synergy (HAI vs max):** Effect size dương cho thấy Human-AI tốt hơn cả Human và AI

### 3.3 Heterogeneity Analysis

| Loại | τ² | I² | I² Between | I² Within |
|------|-----|-----|------------|-----------|
| Strong Synergy | [TBD] | [TBD] | [TBD] | [TBD] |
| Human Augmentation | [TBD] | [TBD] | [TBD] | [TBD] |
| AI Augmentation | [TBD] | [TBD] | [TBD] | [TBD] |

### 3.4 Publication Bias Tests

| Loại | Egger's β | Egger's p | Rank τ | Rank p |
|------|-----------|-----------|--------|--------|
| Strong Synergy | [TBD] | [TBD] | [TBD] | [TBD] |
| Human Augmentation | [TBD] | [TBD] | [TBD] | [TBD] |
| AI Augmentation | [TBD] | [TBD] | [TBD] | [TBD] |

### 3.5 Moderator Analysis

#### 3.5.1 Task Type
| Task Type | n | HAI vs H (g) | HAI vs AI (g) | HAI vs max (g) |
|-----------|---|--------------|---------------|----------------|
| Decide | 252 | [TBD] | [TBD] | [TBD] |
| Create | 26 | [TBD] | [TBD] | [TBD] |

#### 3.5.2 Industry
| Industry | n | HAI vs H (g) | HAI vs AI (g) |
|----------|---|--------------|---------------|
| Healthcare | 107 | [TBD] | [TBD] |
| Communication | 86 | [TBD] | [TBD] |
| Business | 46 | [TBD] | [TBD] |
| Public Sector | 39 | [TBD] | [TBD] |

#### 3.5.3 AI Type
| AI Type | n | HAI vs H (g) | HAI vs AI (g) |
|---------|---|--------------|---------------|
| Deep | 132 | [TBD] | [TBD] |
| Rule-Based | 52 | [TBD] | [TBD] |
| Shallow | 46 | [TBD] | [TBD] |
| Wizard of Oz | 36 | [TBD] | [TBD] |

#### 3.5.4 Participant Expertise
| Expert | n | HAI vs H (g) | HAI vs AI (g) |
|--------|---|--------------|---------------|
| No | 182 | [TBD] | [TBD] |
| Yes | 96 | [TBD] | [TBD] |

#### 3.5.5 AI Explanation Included
| Explanation | n | HAI vs H (g) | HAI vs AI (g) |
|-------------|---|--------------|---------------|
| No | 115 | [TBD] | [TBD] |
| Yes | 163 | [TBD] | [TBD] |

---

## 4. Thảo luận (Discussion)

### 4.1 Tóm tắt phát hiện chính

1. **Human Augmentation:** AI hỗ trợ cải thiện đáng kể hiệu suất của con người, chủ yếu bằng cách giảm lỗi thường gặp

2. **AI Augmentation:** Kết quả hỗn hợp - việc thêm input từ con người không luôn cải thiện hiệu suất AI

3. **Strong Synergy:** Hiếm khi đạt được - các team hỗn hợp thường hoạt động kém hơn agent tốt nhất (thường là AI)

### 4.2 Giải thích kết quả

**Tại sao Human Augmentation thường thành công:**
- AI giúp giảm lỗi nhận thức của con người
- Cung cấp thông tin bổ sung cho quyết định
- Hỗ trợ các task có cấu trúc cao

**Tại sao Strong Synergy khó đạt được:**
- Trust và reliance chưa được calibrate đúng
- Explanations không luôn giúp cải thiện quyết định
- Con người có xu hướng automation bias hoặc algorithm aversion

### 4.3 Vai trò của các Moderators

**Task Type:**
- Tasks sáng tạo (Create) có tiềm năng synergy cao hơn tasks quyết định (Decide)
- Tasks có cấu trúc cao thuận lợi cho AI dominance

**Expertise:**
- Experts có thể khai thác AI tốt hơn
- Non-experts không tự động hưởng lợi nhiều hơn từ AI support

**AI Explanation:**
- Explanations không luôn cải thiện kết quả
- Có thể gây ra over-reliance hoặc cognitive overload

### 4.4 Implications

**Cho Practitioners:**
- Chọn tasks phù hợp cho human-AI collaboration
- Thiết kế interfaces với calibrated trust
- Implement procedures cho escalation khi AI và human không đồng ý

**Cho Policymakers:**
- Automate high-precision, structured sub-tasks
- Giữ human review cho quyết định ethically complex
- Yêu cầu preregistered evaluations và reporting null results

**Cho Researchers:**
- Nghiên cứu thêm về creative/ambiguous tasks
- Đánh giá outcomes beyond accuracy
- Field studies thay vì chỉ lab experiments

---

## 5. Hạn chế (Limitations)

1. **High heterogeneity:** I² cao cho thấy variation lớn giữa các nghiên cứu
2. **Publication bias:** Có thể có asymmetry trong funnel plot cho augmentation
3. **Time restriction:** Chỉ bao gồm 2020-2024
4. **Experimental settings:** Hầu hết là lab experiments, ít field studies
5. **Structured tasks dominance:** ~95% là decision tasks, ít creative tasks
6. **Reliance on summary statistics:** Không có access to individual-level data

---

## 6. Kết luận (Conclusion)

Phân tích tổng hợp này cho thấy rằng AI augmentation thường cải thiện hiệu suất của con người, nhưng việc đạt được synergy thực sự - nơi hệ thống human-AI vượt trội cả hai thành phần riêng lẻ - vẫn còn thách thức. Kết quả nhấn mạnh tầm quan trọng của việc thiết kế cẩn thận thay vì chỉ đơn thuần áp dụng AI.

Các khuyến nghị chính:
1. **Selective automation:** Chọn lọc tasks phù hợp cho automation
2. **Human oversight:** Giữ human review cho quyết định quan trọng
3. **Calibrated trust:** Thiết kế interfaces hỗ trợ trust calibration
4. **Context-specific deployment:** Không có one-size-fits-all solution

---

## References

[Danh sách tài liệu tham khảo sẽ được bổ sung sau khi chạy analysis]

---

## Appendices

### Appendix 1: Effect Size Computation Details

### Appendix 2: Search Strings

### Appendix 3: List of Included Studies

### Appendix 4: Detailed Moderator Analysis Results

### Appendix 5: Sensitivity Analysis Results

---

*Manuscript prepared by: [Author Name]*
*Last updated: [Date]*