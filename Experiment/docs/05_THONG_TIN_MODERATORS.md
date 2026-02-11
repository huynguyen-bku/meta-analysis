# Thông Tin Chi Tiết Về Các Biến Điều Hòa (Moderators)

## Tổng Quan

Các moderators giúp giải thích **tại sao** hiệu ứng cộng tác khác nhau giữa các bối cảnh. Với I² > 90%, moderators rất quan trọng để hiểu đầy đủ hình ảnh.

## 1. Ngành Công Nghiệp (Industry)

### Phân Loại

```
├─ Business (n=46 hiệu ứng)
│   Ví dụ: Công ty viết, phân tích dữ liệu, quản lý dự án
│
├─ Communication (n=86 hiệu ứng)
│   Ví dụ: Dịch thuật, tóm tắt, phê bình viết
│
├─ Healthcare (n=107 hiệu ứng)
│   Ví dụ: Chẩn đoán y tế, lập kế hoạch điều trị, phát hiện bệnh
│
└─ Public Sector (n=39 hiệu ứng)
    Ví dụ: Hỗ trợ quyết định chính sách, phân tích chương trình công
```

### Tìm Kiếm Chính

#### Strong Synergy (HAI vs. max{H,A})

```
Healthcare:     g = -0.31  [Tốt nhất - kém hơn ít nhất]
Communication:  g = -0.49  [Vừa phải]
Public Sector:  g = -0.70  [Tồi tệ]
Business:       g = -0.93  [Tồi tệ nhất - kém nhất rõ ràng]

Q_between p < 0.001 ⟹ Ngành có ý nghĩa giải thích độ không đồng nhất
```

**Diễn Giải**:
- **Healthcare**: Công việc phức tạp → Con người & AI bổ sung tốt
  - Bác sĩ cần xem xét chẩn đoán AI
  - Hiếm khi một mình tốt hơn
  - Strong Synergy âm nhưng nhỏ (-0.31)

- **Business**: Công việc rõ ràng hơn → Một người hoặc AI thường tốt
  - Công ty có thể dùng AI một mình
  - Cộng tác phức tạp hơn lợi ích
  - Strong Synergy âm lớn (-0.93)

#### Human Augmentation (HAI vs. Human)

```
Healthcare:     g = 0.74  [Lợi ích lớn nhất]
Communication:  g = 0.45  [Lợi ích vừa phải]
Public Sector:  g = 0.45  [Lợi ích vừa phải]
Business:       g = 0.34  [Lợi ích nhỏ nhất]
```

**Suy Luận**:
- Y Tế: Con người được tăng cường NHIỀU nhất bởi AI
- Kinh Doanh: Con người được tăng cường ít nhất
- Có thể vì AI đã tối ưu cho Business → Ít cần cải thiện

### Khuyến Nghị Ứng Dụng

| Ngành | Khuyến Nghị |
|-------|------------|
| **Healthcare** | ✅ Đầu tư vào cộng tác con người-AI |
| **Communication** | ✅ Hỗ trợ tốt, nhưng tùy nhiệm vụ |
| **Public Sector** | ⚠️ Xem xét kỹ, hiệu ứng không nhất quán |
| **Business** | ❌ AI một mình thường tốt hơn cộng tác |

---

## 2. Loại Nhiệm Vụ (Task_Type)

### Phân Loại

```
├─ Decide (n=252 hiệu ứng) - 90%
│   Ví dụ: Ra quyết định, đánh giá tùy chọn, xác định vấn đề
│
└─ Create (n=26 hiệu ứng) - 10%
    Ví dụ: Viết bài, tóm tắt, tạo nội dung, thiết kế
```

### Tìm Kiếm Chính

#### Strong Synergy

```
Create:  g = +0.37  [DƯƠNG - Synergy thực sự!]
Decide:  g = -0.62  [Âm - Không có synergy]

Q_between p < 0.001 ⟹ Loại nhiệm vụ giải thích đáng kể
```

**Phát Hiện Quan Trọng**:
- **CREATE là ngoại lệ**: Duy nhất có Strong Synergy dương
  - Người + AI tạo cái gì đó **tốt hơn** một mình cái gì đó
  - Có thể vì:
    - Sáng tạo cần đầu vào từ cả hai
    - AI cung cấp ý tưởng, người tinh chỉnh
    - Lặp lại - cải tiến

- **DECIDE là tiêu chuẩn âm**: Không có synergy
  - Ra quyết định thường một người hoặc AI tốt
  - Con người phân tâm bởi gợi ý AI
  - Kéo thẩm phán của con người

#### Human Augmentation

```
Create:  g = 1.01  [Cải thiện LỚAN rất]
Decide:  g = 0.47  [Cải thiện vừa phải]

Q_between p < 0.001 ⟹ Khác biệt rõ ràng
```

**Diễn Giải**:
- **CREATE**: Con người được tăng cường rất nhiều (1.01 = hiệu ứng rất lớn)
  - AI giúp người tạo nội dung tốt hơn nhiều
  - Cơ chế: Gợi ý, kiểm tra lỗi, hiểu sắc thái
  - Thực tế: Những người viết sử dụng AI hơn những người ra quyết định

- **DECIDE**: Con người được tăng cường hơn (0.47)
  - AI cung cấp dữ liệu, con người quyết định
  - Ít tăng cường hơn sáng tạo

#### AI Augmentation

```
Create:  g = 0.59  [Con người giúp đáng kể]
Decide:  g = 0.12  [Con người giúp ít]
```

**Phát Hiện**:
- **CREATE**: Con người được coi là giúp con người (0.59)
  - Phản hồi của người là quý giá cho AI
  - Cộng tác ngôn ngữ/sáng tạo: Con người giúp AI học

- **DECIDE**: Con người không giúp AI (0.12 ≈ 0)
  - AI quyết định tốt - ít cần input
  - Lỗi con người có thể làm cho AI tồi

### Khuyến Nghị Ứng Dụng

| Loại Nhiệm Vụ | Khuyến Nghị |
|---|---|
| **Create (Viết, Tóm Tắt, Thiết Kế)** | ✅✅✅ Cộng tác rất tốt - Đầu tư |
| **Decide (Ra Quyết Định)** | ⚠️ Cộng tác vừa phải - Cần thiết kế cẩn thận |

---

## 3. Loại AI (AI_Type_Cleaned)

### Phân Loại

```
├─ Deep (n=132) - 47%
│   Ví dụ: LLM (GPT, Claude), mạng nơ-ron sâu, mô hình thị giác
│
├─ Rule-Based (n=52) - 19%
│   Ví dụ: Hệ thống chuyên gia, quy tắc if-then, logic mờ
│
├─ Shallow (n=46) - 17%
│   Ví dụ: Cây quyết định, SVM, hồi quy
│
├─ Simulated-AI (n=12) - 4%
│   Ví dụ: Con người giả vờ là AI trong thí nghiệm (Wizard-of-Oz)
│
└─ Wizard of Oz (n=36) - 13%
    (Lưu ý: Overlap có thể - Simulated-AI có thể là loại Wizard-of-Oz)
```

### Tìm Kiếm Chính

#### Strong Synergy

```
Deep Learning:  g = -0.20  [Tốt nhất - kém hơn ít nhất]
Shallow:        g = -0.51  [Vừa phải]
Wizard of Oz:   g = -0.43  [Vừa phải]
Rule-Based:     g = -1.25  [Tồi tệ]
Simulated-AI:   g = -1.29  [Tồi tệ nhất]

Q_between p < 0.001 ⟹ Loại AI giải thích đáng kể
```

**Phát Hiện Quan Trọng**:

| Loại AI | Strong Synergy | Diễn Giải |
|---------|---------|-----------|
| **Deep Learning** | -0.20 | ✅ Tốt nhất cho cộng tác |
| Shallow | -0.51 | Vừa phải |
| Wizard of Oz | -0.43 | Vừa phải |
| Rule-Based | -1.25 | ❌ Tồi tệ - khó hợp tác |
| Simulated-AI | -1.29 | ❌ Tồi tệ nhất |

**Tại Sao Deep Learning Tốt Hơn?**
- **Linh hoạt**: DL thích ứng tốt với bối cảnh
- **Ít sai lệch**: Các quy tắc cứng nhắc dễ sai → Người phải ghi đè
- **Tương tác**: DL có thể học từ phản hồi con người
- **Độ tin cậy**: Con người tin DL hơn Rule-Based

**Tại Sao Rule-Based Tồi?**
- Quy tắc cứng nhắc → Dễ sai lệch
- Người phải ghi đè thường → Tải nhận thức cao
- Ít linh hoạt → Không thích ứng

#### Human Augmentation

```
Deep Learning:  g = 0.56
Shallow:        g = 0.48
Wizard of Oz:   g = 0.45
Rule-Based:     g = 0.33
Simulated-AI:   g = 0.44
```

**Mô Hình**: Tất cả đều tăng cường con người, nhưng Deep Learning tốt nhất

---

## 4. Chuyên Môn của Người Tham Gia (Participant_Expert)

### Phân Loại

```
├─ Yes (n=96) - 35%
│   Ví dụ: Bác sĩ trong thí nghiệm chẩn đoán, luật sư trong thí nghiệm pháp lý
│
└─ No (n=182) - 65%
    Ví dụ: Sinh viên, mọi người thường xuyên, cộng tác viên Amazon Mechanical Turk
```

### Tìm Kiếm Chính

#### Strong Synergy

```
Expert:     g = -0.28  [Tốt hơn]
Non-Expert: g = -0.65  [Tồi tệ hơn]

Q_between p < 0.001 ⟹ Chuyên môn giải thích đáng kể
```

**Diễn Giải**:
- **Chuyên Gia hoạt động tốt hơn 2x** trong cộng tác
  - Strong Synergy -0.28 vs -0.65 (kém ít hơn 0.37 điểm)
  - Tại sao?
    - Biết khi nào nên tin tưởng AI
    - Biết khi nào AI sai lệch
    - Tích hợp ý kiến AI hiệu quả hơn
    - Ít bị phân tâm bởi giao diện AI

- **Người không chuyên hoạt động kém**
  - Có thể bị phân tâm bởi gợi ý AI
  - Không biết khi nào nên nghi ngờ AI
  - Tham số của con người cao hơn

#### Human Augmentation

```
Expert:     g = 0.69  [Lợi ích lớn]
Non-Expert: g = 0.40  [Lợi ích vừa phải]

Q_between p < 0.001 ⟹ Khác biệt rõ ràng
```

**Suy Luận**:
- Chuyên Gia được tăng cường hơn (0.69 vs 0.40)
- Có thể vì chuyên gia biết cách sử dụng AI tốt

### Khuyến Nghị Ứng Dụng

| Người Tham Gia | Khuyến Nghị |
|---|---|
| **Chuyên Gia** | ✅ Cộng tác hoạt động tốt - Tận dụng |
| **Người Không Chuyên** | ⚠️ Cộng tác kém - Cần đào tạo |

**Hàm Ý**: Đào tạo con người cách hợp tác với AI là chìa khóa

---

## 5. Bao Gồm Giải Thích AI (AI_Expl_Incl)

### Phân Loại

```
├─ Yes (n=163) - 58%
│   Ví dụ: "AI dự đoán X vì [lý do]"
│
└─ No (n=115) - 42%
    Ví dụ: "AI dự đoán X" (không có lý do)
```

### Tìm Kiếm Chính

#### Strong Synergy

```
With Explanation:    g = -0.47  [Tốt hơn một chút]
Without Explanation: g = -0.61  [Xấu hơn]

Q_between p < 0.001 ⟹ Giải thích có ý nghĩa (nhưng hiệu ứng nhỏ)
```

**Phát Hiện**:
- Giải thích **giúp một chút** (-0.47 vs -0.61)
- Nhưng khác biệt không lớn (0.14 điểm)
- Tại sao không lớn hơn?
  - Có thể giải thích chất lượng thấp
  - Có thể không phải tất cả giải thích đều hữu ích
  - Định nghĩa "giải thích" có thể thay đổi

#### Human Augmentation

```
With:    g = 0.49
Without: g = 0.47
```

**Kết Quả**: Không khác biệt rõ ràng
- Giải thích không thay đổi lợi ích con người
- Con người được tăng cường ở cả hai trường hợp

### Khuyến Nghị Ứng Dụng

- Giải thích AI **có lợi nhưng không quá quan trọng**
- Chất lượng giải thích quan trọng hơn sự hiện diện
- Cần phát triển giải thích tốt hơn

---

## 6. Năm Xuất Bản (Year)

### Phân Loại & Kích Thước Mẫu

```
2020: n=62
2021: n=93
2022: n=65
2023: n=54
2024: n=4 (quá nhỏ - không đáng tin)
```

### Tìm Kiếm Chính

#### Strong Synergy

```
2024: g = -0.81  (n=4, không đáng tin)
2020: g = -0.84  [Tồi tệ]
2022: g = -0.63  [Vừa phải]
2021: g = -0.56  [Vừa phải]
2023: g = +0.01  [🌟 DƯƠNG! Cộng tác cải thiện?]

Q_between p < 0.001 ⟹ Xu hướng thời gian có ý nghĩa
```

**Phát Hiện Quan Trọng**:
- **2023 là điểm ngoặt**: Lần đầu tiên Strong Synergy gần bằng 0 (thay vì âm)
- **Xu hướng**: -0.84 (2020) → +0.01 (2023)
- **Giải Thích**:
  - Công nghệ AI cải thiện (LLM tốt hơn)
  - Giao diện con người-AI cải thiện
  - Điều phối tốt hơn
  - Người dùng học cách hợp tác tốt hơn

#### Human Augmentation

```
2023: g = 0.47  [Vừa phải]
2022: g = 0.49  [Vừa phải]
2021: g = 0.52  [Lợi ích lớn]
2020: g = 0.68  [Lợi ích RẤT lớn]
```

**Xu Hướng**: Giảm từ 2020 đến 2023 (0.68 → 0.47)
- **Diễn Giải**:
  - Các nghiên cứu sớm chọn chọn lọc (chỉ thường báo cáo những kết quả tốt)
  - Các nghiên cứu gần đây đa dạng hơn (bao gồm kết quả vừa phải)
  - Hoặc: AI cũ kỳ đấy tăng cường con người nhiều hơn AI mới

### Khuyến Nghị Ứng Dụng

- **Công nghệ AI đang cải thiện** để cộng tác (2023 là tín hiệu tốt)
- Nhưng **2024 có quá ít dữ liệu** để kết luận
- Cần theo dõi xu hướng này

---

## Tương Tác Giữa Moderators

### Ví Dụ: Create Tasks & Deep Learning

```
Kết hợp tốt nhất:
- Task: CREATE (g = +0.37 Strong Synergy)
- AI: Deep Learning (g = -0.20 Strong Synergy)
→ Có thể kết hợp tốt nhất?
```

*Lưu ý: Tương tác chưa được phân tích chi tiết trong báo cáo này*

---

## Tóm Tắt Moderators

| Moderator | Tác Động Mạnh | Kế Tiếp |
|---|---|---|
| **Task Type** | ✅ Rất Mạnh (Create > Decide) | Tập trung vào Create tasks |
| **AI Type** | ✅ Rất Mạnh (Deep > Rule-Based) | Dùng Deep Learning |
| **Industry** | ✅ Rất Mạnh (Healthcare > Business) | Contextual |
| **Expertise** | ✅ Mạnh (Expert > Non-Expert) | Đào tạo con người |
| **Explanation** | ⚠️ Yếu | Cơ sở nhưng không quyết định |
| **Year** | ✅ Mạnh (Xu hướng dương) | Theo dõi công nghệ |

---

**Bước Tiếp Theo**: Xem 05_LAP_LAI.md để tự chạy phân tích
