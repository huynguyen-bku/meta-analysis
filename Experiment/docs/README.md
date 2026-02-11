# Tài Liệu Meta-Phân Tích: Cộng Tác Người-AI

Bộ tài liệu này cung cấp hướng dẫn toàn diện về dự án meta-phân tích cộng tác người-AI, bao gồm lý thuyết, phương pháp, kết quả và hướng dẫn lặp lại.

## 📚 Bộ Tài Liệu

| Tệp | Mục Đích | Đối Tượng | Thời Gian |
|-----|---------|----------|----------|
| **01_TONG_QUAN_NGHIEN_CUU.md** | Giới thiệu toàn cảnh dự án, câu hỏi, ý nghĩa | Tất cả mọi người | 15 phút |
| **02_PHUONG_PHAP_THONG_KE.md** | Chi tiết phương pháp thống kê, mô hình 3-level | Người quan tâm kỹ thuật | 30 phút |
| **03_QTRÌNH_PHAN_TICH.md** | Quy trình từng giai đoạn (01-06), đầu vào/đầu ra | Người muốn hiểu quy trình | 20 phút |
| **04_TOM_TAT_KET_QUA.md** | Kết quả chính, diễn giải, phát hiện quan trọng | Tất cả (chuyên gia hơn dùng 02) | 25 phút |
| **05_THONG_TIN_MODERATORS.md** | Chi tiết moderators (ngành, loại AI, expertise) | Người muốn hiểu tác động | 20 phút |
| **06_LAP_LAI.md** | Hướng dẫn cài đặt, chạy, gỡ lỗi phân tích | Người chạy lại phân tích | 30 phút |

## 🎯 Đường Dẫn Nhanh Theo Nhu Cầu

### Bạn là nhà quản lý / Quyết định chính sách?
```
1. Đọc: 01_TONG_QUAN_NGHIEN_CUU.md (Phần "Ý Nghĩa Nghiên Cứu")
2. Đọc: 04_TOM_TAT_KET_QUA.md (Toàn bộ)
3. Đặc biệt chú ý: Các khuyến nghị ứng dụng trong 05_THONG_TIN_MODERATORS.md
```

### Bạn là nhà nghiên cứu / Phân tích dữ liệu?
```
1. Đọc: 01_TONG_QUAN_NGHIEN_CUU.md (Toàn bộ)
2. Đọc: 02_PHUONG_PHAP_THONG_KE.md (Toàn bộ)
3. Đọc: 03_QTRÌNH_PHAN_TICH.md (Quy trình Chi Tiết)
4. Tham Khảo: 04_TOM_TAT_KET_QUA.md (Kết quả Chính)
5. Nếu lặp lại: 06_LAP_LAI.md
```

### Bạn muốn lặp lại phân tích?
```
1. Nhanh: 06_LAP_LAI.md → "Chạy Phân Tích"
2. Từ Scratch: 06_LAP_LAI.md → "Cài Đặt Từ Scratch"
3. Gỡ Lỗi: 06_LAP_LAI.md → "Gỡ Lỗi"
```

### Bạn quan tâm một moderator cụ thể?
```
→ Tìm trong 05_THONG_TIN_MODERATORS.md
  Ví dụ: "Bạn quan tâm ngành healthcare?"
  → Xem "1. Ngành Công Nghiệp > Healthcare"
```

## 🔑 Các Phát Hiện Chính (Tóm Tắt)

| So Sánh | Ước Tính | Ý Nghĩa | Ứng Dụng |
|---------|---------|---------|---------|
| **Strong Synergy** | g = -0.53 | HAI thường kém hơn tốt nhất | Cẩn trọng khi triển khai |
| **Human Aug** | g = +0.49 | AI tăng cường con người đáng kể | ✅ Khuyên áp dụng |
| **AI Aug** | g = +0.15 | Con người ít giúp AI | Con người không cần thiết cho AI |

### Khi Nào Cộng Tác Hoạt Động Tốt?
- ✅ **Create tasks** (viết, tóm tắt, thiết kế)
- ✅ **Healthcare** (công việc phức tạp)
- ✅ **Deep Learning AI** (linh hoạt hơn Rule-Based)
- ✅ **Người có chuyên môn** (biết cách sử dụng AI)

### Khi Nào Cộng Tác Kém?
- ❌ **Decide tasks** (ra quyết định)
- ❌ **Business** (AI thường tốt một mình)
- ❌ **Rule-Based AI** (dự đoán cứng nhắc)
- ❌ **Người không chuyên** (phân tâm bởi AI)

## 📊 Đầu Ra Chính

Tệp dữ liệu được tạo:
```
outputs/tables/
├── 01_effect_sizes_full.csv           # 278 kích thước hiệu ứng
├── 02_meta_results.csv                # 3 ước tính chính
├── 03_bias_summary.csv                # Đánh giá độ lệch xuất bản
├── 04_subgroup_results.csv            # Moderators analysis (~200 hàng)
├── 05_leave_one_out.csv               # Phân tích độ nhạy
├── 05_influence_diagnostics.csv       # Chẩn đoán ảnh hưởng
└── 06_industry_results.csv            # Phân tích ngành

outputs/figures/
├── Figure1_forestplot.png             # Biểu đồ rừng
├── Figure2_funnelplots.png            # Sơ đồ phễu (độ lệch)
├── Figure3_moderators.png             # Hiệu ứng moderator
└── Figure4_industry_deepdive.png       # Phân tích ngành
```

## 🛠️ Kỹ Thuật Chính

### Phương Pháp
- **3-level meta-analysis REML** (tính đến cấu trúc lồng nhau)
- **Hedges' g** (chỉ số kích thước hiệu ứng)
- **Đánh giá độ lệch xuất bản** (4 phương pháp: Egger, Begg, Trim-Fill, Fail-Safe N)
- **Phân tích moderators** (6 biến: ngành, loại AI, expertise, v.v.)

### Độ Không Đồng Nhất
- **I² > 90%**: Rất cao → Moderators quan trọng
- **Khoảng dự báo rộng**: [-2.6, 1.6] → Kết quả thay đổi nhiều

## 💡 Cách Sử Dụng Tài Liệu

### Trong Báo Cáo / Bài Báo
```markdown
Theo như tài liệu meta-analysis cộng tác người-AI
(xem 01_TONG_QUAN_NGHIEN_CUU.md, mục "Phương Pháp"),
chúng tôi sử dụng 3-level REML vì...
```

### Trình Bày
```
Slide 1: Tóm tắt từ 04_TOM_TAT_KET_QUA.md
Slide 2-3: Tác động moderators từ 05_THONG_TIN_MODERATORS.md
Slide 4: Phương pháp từ 02_PHUONG_PHAP_THONG_KE.md
```

### Lặp Lại / Mở Rộng
```
→ Theo 06_LAP_LAI.md từng bước
→ Tùy chỉnh ở mục "Tùy Chỉnh Phân Tích"
```

## ❓ Câu Hỏi Thường Gặp

**Q: Tại sao Strong Synergy âm?**
A: Xem 04_TOM_TAT_KET_QUA.md → "Strong Synergy (g = -0.53)"

**Q: AI nào hoạt động tốt nhất?**
A: Xem 05_THONG_TIN_MODERATORS.md → "3. Loại AI"

**Q: Làm cách nào để chạy phân tích?**
A: Xem 06_LAP_LAI.md → "Chạy Phân Tích"

**Q: Kết quả này có đáng tin không?**
A: Xem 04_TOM_TAT_KET_QUA.md → "Độ Không Đồng Nhất" & "Đánh Giá Độ Lệch Xuất Bản"

## 🔗 Liên Kết

| Liên Kết | Mô Tả |
|---------|-------|
| `../README.md` | Readme dự án chính |
| `../outputs/tables/` | Dữ liệu kết quả (CSV) |
| `../outputs/figures/` | Hình ảnh (PNG, PDF) |
| `../src/` | Mã nguồn Python |

## 📝 Lịch Sử Tài Liệu

| Phiên Bản | Ngày | Thay Đổi |
|---------|------|---------|
| 1.0 | Feb 2025 | Tạo bộ tài liệu hoàn chỉnh |

## ✍️ Cách Đóng Góp

Nếu bạn tìm thấy lỗi, không rõ hoặc cần cải tiến:
1. Ghi chú vị trí (tệp, mục)
2. Mô tả vấn đề
3. Gửi cho người bảo trì dự án

---

## 📖 Khóa Chú Thích Toàn Tài Liệu

```
✅ = Khuyên áp dụng / Ủng hộ bằng chứng mạnh
⚠️  = Cảnh báo / Xem xét kỹ
❌ = Không khuyên / Bằng chứng chống lại
🌟 = Phát hiện quan trọng
→  = Liên kết đến tài liệu khác
```

---

**Bắt Đầu**: Chọn tệp tài liệu thích hợp ở bên trên, hoặc đọc 01_TONG_QUAN_NGHIEN_CUU.md nếu không chắc chắn.

**Cuối Cùng**: Nếu bạn là người thực hiện phân tích, hãy bắt đầu với 06_LAP_LAI.md để cài đặt môi trường.
