# Nghịch lý cộng tác người-AI: Phân tích meta liên ngành trên 278 kích thước hiệu ứng

**Tác giả**: Vu Minh Ngo, Le Van Duy, Huy Nguyen, Vuong TT Ngoc

**Hội thảo**: JABES 2026

---

## Tóm tắt

Trí tuệ nhân tạo (AI) ngày càng được triển khai song hành với con người trong quá trình ra quyết định, dựa trên giả định rằng sự kết hợp giữa phán đoán con người và độ chính xác thuật toán sẽ cho kết quả vượt trội. Nghiên cứu này thách thức giả định đó. Tổng hợp 278 kích thước hiệu ứng từ 67 nghiên cứu thực nghiệm trên bốn ngành (Y tế, Kinh doanh, Truyền thông, Khu vực công), chúng tôi áp dụng mô hình hiệu ứng ngẫu nhiên ba bậc (REML) qua ba phép so sánh: nhóm cộng tác so với thành viên giỏi nhất, nhóm so với con người đơn lẻ, và nhóm so với AI đơn lẻ. Nhóm người-AI hoạt động kém hơn có ý nghĩa so với thành viên giỏi nhất (*g* = −0,529, *p* < 0,001). Mô hình này bất đối xứng: AI cải thiện đáng kể hiệu suất con người (*g* = +0,494, *p* < 0,001), nhưng con người không cải thiện có ý nghĩa hiệu suất AI (*g* = +0,145, *p* = 0,128). Mức dị biệt cực cao (I² = 90–99%) cho thấy bối cảnh đóng vai trò quyết định. Ngành nghề nổi lên là biến điều tiết chủ đạo: Truyền thông là lĩnh vực duy nhất mà con người cải thiện AI đáng tin cậy (*g* = +1,01), trong khi Kinh doanh có thâm hụt sâu nhất (*g* = −0,93). Meta-regression đa biến xác nhận loại nhiệm vụ và kiến trúc AI điều tiết các hiệu ứng ngay cả sau khi kiểm soát đồng thời. Phân tích xu hướng cho thấy tổn thất cộng hưởng đang thu hẹp, với năm 2023 đánh dấu lần đầu chi phí cộng tác tiến đến zero. Các kết quả phản bác việc áp dụng đại trà cơ chế human-in-the-loop và ủng hộ thiết kế cộng tác phù hợp bối cảnh.

**Từ khóa**: cộng tác người-AI, phân tích meta, ra quyết định, tăng cường, cộng hưởng, human-in-the-loop

---

## 1. Giới thiệu

Trí tuệ nhân tạo đang len lỏi vào các quyết định có tính đặt cược cao trên khắp nền kinh tế. Bác sĩ X-quang xem xét các bản quét được AI đánh dấu. Thẩm phán tham vấn điểm rủi ro thuật toán. Nhà phân tích tài chính dựa vào dự báo machine learning như thực hành chuẩn (Brynjolfsson & McAfee, 2017; Davenport & Ronanki, 2018; Kleinberg và cs., 2018). Nền tảng chung của các triển khai này là một giả định: hệ thống human-in-the-loop kết hợp thế mạnh bổ trợ, trong đó con người đóng góp khả năng hiểu bối cảnh và phán đoán đạo đức, còn AI đóng góp tốc độ xử lý, tính nhất quán, năng lực nhận diện mẫu ở quy mô lớn, và khả năng làm việc không mệt mỏi. Theo lý thuyết, sự kết hợp sẽ cho kết quả vượt trội.

Nhưng bằng chứng thực nghiệm ngày càng đi ngược lại giả định đó. Trong chẩn đoán hình ảnh, tư pháp hình sự, kiểm duyệt nội dung, dự báo tài chính, việc thêm con người vào hệ thống AI hoặc thêm AI vào quy trình con người đôi khi làm *giảm* hiệu suất thay vì cải thiện (Bansal và cs., 2021; Buçinca và cs., 2021; Green & Chen, 2019). Nhìn từ kinh tế học tổ chức, điều này không quá bất ngờ. Lý thuyết chi phí giám sát (Alchian & Demsetz, 1972) đã chỉ ra rằng giám sát chỉ tạo giá trị khi người giám sát có đủ thông tin phân biệt đầu ra đúng và sai, một điều kiện khó đáp ứng khi đối tượng giám sát là hệ thống AI vận hành theo cơ chế hầu như không quan sát được. Câu hỏi không còn là liệu cộng tác có đôi khi thất bại, mà là thất bại với tần suất nào, ở mức độ nào, trong những điều kiện gì, và liệu có bối cảnh nào sự phối hợp thực sự hiệu quả.

Nghiên cứu trước đó của chúng tôi (Ngo và cs., 2025), công bố trên *Applied Economics Letters*, đã cung cấp bằng chứng hệ thống đầu tiên về nghịch lý cộng tác này với 146 kích thước hiệu ứng từ hai ngành Y tế và Khu vực công. Phân tích đó phát hiện hiệu ứng cộng hưởng âm có ý nghĩa (*g* = −0,380) song song với hiệu ứng AI hỗ trợ người đáng kể (*g* = +0,622), xác lập cấu trúc bất đối xứng cơ bản: AI giúp con người, nhưng con người không giúp AI. Tuy nhiên, việc giới hạn phạm vi ở hai ngành để lại câu hỏi then chốt: *liệu mô hình này có khái quát hóa được cho nền kinh tế rộng hơn hay không?*

Nghiên cứu hiện tại mở rộng cơ sở bằng chứng lên **278 kích thước hiệu ứng** từ **67 nghiên cứu bình duyệt** bao gồm **90 thí nghiệm riêng biệt** trải rộng trên **bốn ngành**: Y tế, Kinh doanh, Truyền thông, và Khu vực công. Hai ngành bổ sung mang đến những hệ sinh thái nhiệm vụ khác biệt căn bản: Kinh doanh (dự báo nhu cầu, định giá, tuyển dụng) và Truyền thông (kiểm duyệt nội dung, phát hiện thông tin sai lệch). Sự mở rộng này không chỉ tăng mẫu mà đưa vào các bối cảnh nơi năng lực con người và AI giao thoa theo cách khác hẳn hai ngành ban đầu. Bao phủ giai đoạn 2020–2024, đây là phân tích meta toàn diện nhất về cộng tác ra quyết định người-AI cho đến nay.

Bốn câu hỏi nghiên cứu định hình phân tích. RQ1 hỏi liệu cộng tác người-AI tạo ra hay phá hủy giá trị so với cá nhân giỏi nhất (cộng hưởng). RQ2 kiểm tra tính đối xứng: AI hỗ trợ người có tương đương người giám sát AI không? RQ3 đi vào bối cảnh, khảo sát vai trò điều tiết của ngành nghề, loại nhiệm vụ, kiến trúc AI, trình độ chuyên môn, và khả năng giải thích. RQ4 hỏi liệu thâm hụt cộng tác, nếu tồn tại, có đang thu hẹp theo thời gian.

Đóng góp chính của bài viết nằm ở ba điểm. Nó cung cấp bằng chứng liên ngành đầu tiên rằng nghịch lý cộng tác mang tính phổ quát, không phải đặc thù y tế hay khu vực công. Nó xác định ngành nghề là biến điều tiết chủ đạo, với Truyền thông là lĩnh vực duy nhất con người cải thiện AI đáng tin cậy. Và nó ghi nhận thâm hụt cộng tác đang thu hẹp theo thời gian. Trên nền tảng các kết quả đó, bài viết đề xuất một khung phân tích dựa trên lợi thế so sánh và thông tin bất đối xứng, có hàm ý cho cả thiết kế quản trị AI lẫn chính sách human-in-the-loop.

---

## 2. Cơ sở lý thuyết và giả thuyết

### 2.1 Cộng tác ra quyết định người-AI: bằng chứng thực nghiệm

Truyền thống so sánh phán đoán lâm sàng với phán đoán thống kê có lịch sử hơn nửa thế kỷ. Dawes, Faust, và Meehl (1989) tổng hợp bằng chứng cho thấy mô hình thống kê đơn giản thường vượt trội chuyên gia con người trong nhiều nhiệm vụ dự báo, từ chẩn đoán y tế đến dự đoán tái phạm. Grove và cộng sự (2000) mở rộng kết luận này qua phân tích meta 136 nghiên cứu: trong 63% trường hợp, phán đoán cơ học vượt trội hoặc ngang bằng phán đoán lâm sàng. AI hiện đại nối tiếp truyền thống này với năng lực vượt xa mô hình tuyến tính (Topol, 2019), nhưng cũng đặt ra câu hỏi mới: thay vì chọn giữa người *hoặc* máy, liệu *kết hợp* có cho kết quả tốt hơn?

Niềm tin phổ biến là có. Nhiều tổ chức triển khai human-in-the-loop dựa trên giả định rằng con người bổ sung cho AI những năng lực thuật toán chưa có (Davenport & Ronanki, 2018; Brynjolfsson & McAfee, 2017). Nhưng bằng chứng thực nghiệm phức tạp hơn giả định đó. Bansal và cộng sự (2021) phát hiện rằng giải thích AI không nhất quán cải thiện hiệu suất nhóm, đôi khi còn phản tác dụng khi giải thích không phù hợp nhiệm vụ. Buçinca và cộng sự (2021) cho thấy phụ thuộc quá mức (overreliance) kéo hiệu suất nhóm xuống dưới mức AI đơn lẻ. Green và Chen (2019) ghi nhận rằng thêm con người vào hệ thống AI dự đoán tái phạm không cải thiện độ chính xác mà làm tăng thiên lệch chủng tộc. Dietvorst và cộng sự (2015) mô tả hiện tượng algorithm aversion: sau khi thấy AI mắc lỗi, người dùng bác bỏ thuật toán ngay cả khi nó vẫn vượt trội năng lực con người. Castelo và cộng sự (2019) cho thấy hiệu ứng này phụ thuộc loại nhiệm vụ: aversion mạnh hơn ở nhiệm vụ chủ quan so với khách quan. Burton và cộng sự (2020) tổng hợp 61 nghiên cứu về algorithm aversion, xác định năm nhóm nguyên nhân bao gồm kỳ vọng, quyền tự chủ, và khả năng tương thích nhận thức. Logg và cộng sự (2019) ghi nhận chiều ngược lại, algorithm appreciation, trong đó người dùng tin tưởng AI quá mức.

Ngo và cộng sự (2025) cung cấp tổng hợp hệ thống đầu tiên về câu hỏi này. Phân tích meta trên 146 kích thước hiệu ứng từ 43 nghiên cứu trong Y tế và Khu vực công phát hiện ba kết quả cốt lõi: nhóm cộng tác hoạt động kém hơn thành viên giỏi nhất (*g* = −0,380, *p* < 0,001); AI cải thiện đáng kể hiệu suất con người (*g* = +0,622); và con người không cải thiện có ý nghĩa hiệu suất AI. Mức dị biệt cực cao (I² > 90%) gợi ý bối cảnh đóng vai trò quyết định, nhưng phạm vi hai ngành chưa đủ để giải mã. Nghiên cứu hiện tại mở rộng phạm vi đó sang bốn ngành, cho phép kiểm tra tính khái quát và xác định nguồn dị biệt.

### 2.2 Khung lý thuyết

Chúng tôi xây dựng khung giải thích dựa trên ba trụ cột lý thuyết.

**Thông tin bất đối xứng và chi phí giám sát.** Akerlof (1970) đã mô hình hóa tình huống một bên giao dịch thiếu thông tin để đánh giá chất lượng sản phẩm, dẫn đến lựa chọn ngược. Alchian và Demsetz (1972) mở rộng logic này sang bối cảnh tổ chức: giám sát chỉ tạo giá trị khi chi phí giám sát thấp hơn lợi ích phát hiện sai lệch, nghĩa là người giám sát cần đủ thông tin phân biệt đầu ra đúng và sai. Parasuraman và Riley (1997) đã ghi nhận hệ quả hành vi trong tự động hóa: khi con người không hiểu cơ chế nội bộ của hệ thống, họ rơi vào automation bias (phụ thuộc quá mức) hoặc disuse (bác bỏ thiếu căn cứ). Trong bối cảnh cộng tác người-AI, quy trình ra quyết định nội bộ của AI hầu như không quan sát được, tạo ra điều kiện cho cả hai dạng sai lệch. Trụ cột này dự đoán rằng con người ở vai trò giám sát AI sẽ gặp khó khăn hệ thống.

**Mô hình judge-advisor.** Sniezek và Buckley (1995) mô tả cấu trúc ra quyết định trong đó người quyết định (judge) nhận tư vấn từ nguồn bên ngoài (advisor) rồi đưa ra phán đoán cuối cùng. Judge hưởng lợi từ thông tin bổ sung mà không cần hiểu toàn bộ cơ chế tạo ra thông tin đó. Cấu trúc này tương tự cách con người sử dụng gợi ý AI ở vai trò người nhận hỗ trợ: họ giữ quyền kiểm soát, lọc gợi ý qua kinh nghiệm, và quyết định trong khung phán đoán vốn có. Trụ cột này dự đoán rằng AI ở vai trò advisor sẽ nhất quán có ích, bất kể bối cảnh, vì cấu trúc thông tin của mối quan hệ judge-advisor không thay đổi.

**Lợi thế so sánh.** Ricardo (1817) chứng minh rằng trao đổi mang lại lợi ích khi mỗi bên chuyên môn hóa vào lĩnh vực mình sở hữu lợi thế so sánh. Áp dụng vào cộng tác người-AI, giá trị gia tăng chỉ xuất hiện khi năng lực hai bên thực sự bổ trợ trên các khía cạnh khác nhau của nhiệm vụ. Khi AI đã vượt trội ở hầu hết các khía cạnh (nhiệm vụ phân loại, dự báo), phạm vi bổ trợ hẹp và cộng tác khó tạo thêm giá trị. Khi nhiệm vụ đòi hỏi năng lực đa dạng (sáng tạo, hiểu bối cảnh văn hóa), mỗi bên sở hữu một phần và tiềm năng cộng hưởng lớn. Trụ cột này dự đoán rằng loại nhiệm vụ và ngành nghề sẽ điều tiết mạnh hiệu ứng cộng tác.

### 2.3 Giả thuyết

Từ khung lý thuyết trên và bằng chứng của Ngo và cộng sự (2025), chúng tôi đặt bốn giả thuyết cho bộ dữ liệu mở rộng:

**H1 (Nghịch lý cộng hưởng).** Nhóm người-AI hoạt động kém hơn có ý nghĩa so với thành viên giỏi nhất, mở rộng phát hiện của Ngo và cộng sự (2025) từ hai lên bốn ngành.

**H2 (Tăng cường bất đối xứng).** AI cải thiện đáng kể hiệu suất con người, nhưng con người không cải thiện có ý nghĩa hiệu suất AI. Mô hình judge-advisor dự đoán hiệu ứng AI hỗ trợ người nhất quán dương; bất đối xứng thông tin dự đoán hiệu ứng người hỗ trợ AI yếu hoặc âm.

**H3 (Phụ thuộc bối cảnh).** Ngành nghề, loại nhiệm vụ, kiến trúc AI, trình độ chuyên môn, và khả năng giải thích điều tiết các hiệu ứng. Cụ thể, dựa trên nguyên lý lợi thế so sánh, cộng tác hiệu quả hơn ở nhiệm vụ sáng tạo (phạm vi bổ trợ rộng) so với nhiệm vụ quyết định, và ở bối cảnh giảm bất đối xứng thông tin (AI có giải thích, người tham gia là chuyên gia).

**H4 (Xu hướng cải thiện).** Thâm hụt cộng hưởng thu hẹp theo thời gian, phản ánh sự trưởng thành của cả công nghệ AI lẫn thiết kế giao diện cộng tác.

---

## 3. Phương pháp nghiên cứu

### 3.1 Chiến lược tìm kiếm và tiêu chí chọn mẫu

Nghiên cứu này mở rộng chiến lược tìm kiếm từ phân tích meta trước đó (Ngo, 2025), vốn giới hạn ở Y tế và Khu vực công, sang bốn ngành bao gồm thêm Kinh doanh và Truyền thông. Chúng tôi tìm kiếm trên ACM Digital Library, Web of Science, kết hợp truy vết trích dẫn xuôi và ngược (backward/forward citations) để thu thập các nghiên cứu thực nghiệm về cộng tác ra quyết định người-AI công bố bằng tiếng Anh từ tháng 1/2020 đến tháng 12/2024.

Tiêu chí đưa vào yêu cầu: (1) thiết kế thực nghiệm; (2) có đầy đủ ba điều kiện: con người đơn lẻ, AI đơn lẻ, và nhóm cộng tác; (3) báo cáo đủ thống kê để tính kích thước hiệu ứng; (4) mô tả rõ ràng về người tham gia, nhiệm vụ, và hệ thống AI. Chúng tôi loại trừ các thiết kế quan sát, mô phỏng không có điều kiện cộng tác, và các nghiên cứu thiếu dữ liệu cần thiết.

Quá trình tìm kiếm ban đầu (Ngo, 2025) thu được 45 nghiên cứu đủ tiêu chí, trong đó 43 nghiên cứu thuộc Y tế và Khu vực công đóng góp 146 kích thước hiệu ứng. Trong nghiên cứu hiện tại, việc mở rộng phạm vi sang Kinh doanh và Truyền thông (sử dụng cùng cơ sở dữ liệu, cùng tiêu chí, cập nhật đến tháng 12/2024) bổ sung thêm 24 nghiên cứu, nâng tổng số lên **67 nghiên cứu** đóng góp **278 kích thước hiệu ứng** từ **90 thí nghiệm riêng biệt**.

### 3.2 Trích xuất dữ liệu

Mỗi nghiên cứu được mã hóa trên **65 biến** bao gồm đặc điểm nghiên cứu, đặc điểm nhiệm vụ, thuộc tính hệ thống AI, thuộc tính người tham gia, và kết quả hiệu suất. Quy trình mã hóa được thực hiện nhất quán với nghiên cứu gốc (Ngo, 2025). Các biến mã hóa chính bao gồm:

- **Ngành**: Y tế, Kinh doanh, Truyền thông, hoặc Khu vực công
- **Loại nhiệm vụ**: Ra quyết định (*Decide*) hoặc sáng tạo/sinh tạo (*Create*)
- **Kiến trúc AI**: Deep learning, Shallow learning (ML truyền thống), hệ thống dựa trên luật, Wizard of Oz (AI mô phỏng), hoặc Simulated-AI
- **Trình độ người tham gia**: Chuyên gia (chuyên viên trong lĩnh vực) hoặc Không chuyên (crowdworker, sinh viên)
- **Khả năng giải thích của AI**: AI có cung cấp giải thích cho các khuyến nghị hay không
- **Điểm tin cậy AI**: AI có cung cấp điểm tin cậy (confidence score) hay không
- **Năm công bố**: 2020–2024

Với mỗi thí nghiệm, chúng tôi trích xuất thống kê hiệu suất cho ba điều kiện (nếu có): con người đơn lẻ, AI đơn lẻ, và nhóm người-AI. Khi nghiên cứu báo cáo nhiều thước đo kết quả hoặc nhiều điều kiện thí nghiệm, mỗi quan sát được xử lý như một kích thước hiệu ứng riêng biệt, phù hợp với thông lệ phân tích meta chuẩn.

### 3.3 Tính toán kích thước hiệu ứng

Chúng tôi sử dụng Hedges' *g* làm thước đo kích thước hiệu ứng chính, vì chỉ số này hiệu chỉnh thiên lệch mẫu nhỏ vốn có trong Cohen's *d*. Ba phép so sánh cặp được tính cho mỗi thí nghiệm:

1. **Cộng hưởng mạnh** (*g_s*): Nhóm người-AI so với cá nhân có hiệu suất cao hơn (max giữa con người đơn lẻ và AI đơn lẻ). Giá trị dương cho thấy nhóm vượt trội hơn thành viên giỏi nhất; giá trị âm cho thấy cộng tác phá hủy giá trị.

2. **AI hỗ trợ người** (*g_h*): Nhóm người-AI so với con người đơn lẻ. Giá trị dương cho thấy AI cải thiện hiệu suất con người.

3. **Người hỗ trợ AI** (*g_a*): Nhóm người-AI so với AI đơn lẻ. Giá trị dương cho thấy con người cải thiện hiệu suất AI.

Kích thước hiệu ứng được tính theo quy trình chuẩn (Borenstein và cs., 2009). Với mẫu độc lập:

$$d = \frac{\bar{X}_1 - \bar{X}_2}{S_p}, \quad S_p = \sqrt{\frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2}}$$

trong đó $\bar{X}_1$, $\bar{X}_2$ là trung bình nhóm và $S_p$ là độ lệch chuẩn gộp. Hiệu chỉnh thiên lệch mẫu nhỏ cho Hedges' *g*:

$$g = J \cdot d, \quad J = 1 - \frac{3}{4(n_1 + n_2 - 2) - 1}$$

Phương sai lấy mẫu của *g*:

$$v_i = \frac{n_1 + n_2}{n_1 n_2} + \frac{g_i^2}{2(n_1 + n_2)}$$

Với thiết kế lặp lại (within-subjects), phương sai được điều chỉnh theo tương quan giữa các điều kiện $r$:

$$v_i^{(\text{dep})} = \frac{2(1 - r)}{n} + \frac{g_i^2}{2n}$$

Chiều hướng của tất cả thước đo hiệu suất được chuẩn hóa sao cho giá trị dương luôn biểu thị hiệu suất tốt hơn.

### 3.4 Khung phân tích

Phương pháp phân tích chính là mô hình hiệu ứng ngẫu nhiên ba bậc (three-level random-effects model) ước lượng bằng REML (`rma.mv` trong `metafor`; Viechtbauer, 2010; cấu trúc ngẫu nhiên: `~ 1 | Paper_ID / Exp_ID`), cho phép tách phương sai giữa các bài báo (level 3) và giữa các thí nghiệm trong cùng bài báo (level 2). Cấu trúc này phù hợp với dữ liệu có nhiều kích thước hiệu ứng lồng nhau trong cùng nghiên cứu. Ước lượng tổng hợp:

$$\hat{g} = \frac{\sum_{i=1}^{k} w_i g_i}{\sum_{i=1}^{k} w_i}, \quad w_i = \frac{1}{v_i + \hat{\tau}^2}$$

trong đó $w_i$ là trọng số nghịch đảo phương sai, $v_i$ là phương sai lấy mẫu của nghiên cứu *i*, và $\hat{\tau}^2$ là phương sai giữa các nghiên cứu. Trong mô hình ba bậc, $\hat{\tau}^2$ được phân tách thành $\sigma^2_{\text{between}}$ (giữa bài báo) và $\sigma^2_{\text{within}}$ (giữa thí nghiệm trong bài báo), ước lượng bằng REML. Thống kê dị biệt *Q* của Cochran:

$$Q = \sum_{i=1}^{k} w_i^* \left(g_i - \hat{g}_{\text{FE}}\right)^2, \quad w_i^* = 1/v_i$$

với $\hat{g}_{\text{FE}}$ là ước lượng hiệu ứng cố định. Mức dị biệt được lượng hóa qua chỉ số $I^2$ (Higgins và cs., 2003):

$$I^2 = \max\!\left(0,\; \frac{Q - (k-1)}{Q}\right) \times 100\%$$

Với mỗi phép so sánh, chúng tôi ước lượng kích thước hiệu ứng tổng hợp ($\hat{g}$) với khoảng tin cậy 95%, các thống kê dị biệt ($\hat{\tau}^2$, $I^2$, và kiểm định *Q* của Cochran), cùng khoảng dự đoán phản ánh phạm vi mà 95% hiệu ứng thực sự dự kiến rơi vào.

Để xác định nguồn dị biệt, chúng tôi thực hiện phân tích nhóm con: ước lượng hiệu ứng ngẫu nhiên DerSimonian-Laird riêng cho từng mức của biến điều tiết, rồi so sánh bằng thống kê *Q*-between ($Q_{\text{between}} = Q_{\text{total}} - Q_{\text{within}}$, phân phối $\chi^2$) để kiểm định liệu biến điều tiết có giải thích dị biệt một cách có ý nghĩa hay không. Sáu biến điều tiết được khảo sát: Ngành, Loại nhiệm vụ, Loại AI, Trình độ chuyên môn, Khả năng giải thích AI, và Năm công bố. Bổ sung cho phân tích nhóm con, chúng tôi thực hiện **meta-regression** đa biến bằng mô hình ba bậc REML (cùng cấu trúc `~ 1 | Paper_ID / Exp_ID`), đưa đồng thời tất cả sáu biến điều tiết làm biến dự báo cố định, cho phép ước lượng hiệu ứng riêng của từng biến sau khi kiểm soát các biến còn lại. Thiên lệch xuất bản được đánh giá qua bốn kiểm định bổ trợ: kiểm định hồi quy Egger (Egger và cs., 1997) về bất đối xứng funnel plot, kiểm định tương quan hạng Begg (Begg & Mazumdar, 1994), phương pháp trim-and-fill của Duval và Tweedie (2000), và chỉ số fail-safe N của Rosenthal (1979).

**Bảng 1. Đặc điểm bộ dữ liệu**

| Đặc điểm | Phân loại | *k* | Số bài báo |
|---|---|---|---|
| **Ngành** | Y tế | 107 | 33 |
| | Truyền thông | 86 | 16 |
| | Kinh doanh | 46 | 12 |
| | Khu vực công | 39 | 10 |
| **Loại nhiệm vụ** | Quyết định | 252 | — |
| | Sáng tạo | 26 | — |
| **Kiến trúc AI** | Deep Learning | 132 | — |
| | Dựa trên quy luật (Rule-Based) | 52 | — |
| | ML truyền thống | 46 | — |
| | Wizard of Oz | 36 | — |
| | AI mô phỏng | 12 | — |
| **Trình độ người tham gia** | Không chuyên | 182 | — |
| | Chuyên gia | 96 | — |
| **Giải thích AI** | Có giải thích | 163 | — |
| | Không giải thích | 115 | — |
| **Năm công bố** | 2020 | 62 | 11 |
| | 2021 | 93 | 22 |
| | 2022 | 65 | 20 |
| | 2023 | 54 | 11 |
| | 2024 | 4 | 3 |
| **Tổng** | | **278** | **67** |

*Ghi chú.* *k* = số kích thước hiệu ứng. Cột "Số bài báo" chỉ báo cáo cho Ngành và Năm công bố — các phân loại mà mỗi bài báo chỉ thuộc một nhóm. Đối với các đặc điểm khác, một bài báo có thể đóng góp kích thước hiệu ứng vào nhiều nhóm con (ví dụ: một nghiên cứu có thể bao gồm cả điều kiện có và không có giải thích AI). Tổng số bài báo theo ngành (71) vượt 67 vì bốn bài báo thực hiện thí nghiệm trên nhiều hơn một ngành.

---

## 4. Kết quả nghiên cứu

### 4.1 Hiệu ứng tổng hợp

Kết quả tổng hợp từ mô hình hiệu ứng ngẫu nhiên ba bậc REML trên toàn bộ 278 kích thước hiệu ứng được trình bày trong Bảng 2.

**Bảng 2. Kết quả phân tích meta tổng hợp (Mô hình ba bậc REML)**

| So sánh | *k* | *g* | KTC 95% | *p* | τ² | I² (%) | Khoảng dự đoán |
|---|---|---|---|---|---|---|---|
| Cộng hưởng (Synergy) | 278 | −0.529 | [−0.659, −0.399] | < .001 | 1.145 | 98.41 | [−2.631, 1.572] |
| AI hỗ trợ người (Human Aug) | 278 | +0.494 | [+0.433, +0.554] | < .001 | 0.203 | 90.36 | [−0.392, 1.380] |
| Người hỗ trợ AI (AI Aug) | 278 | +0.145 | [−0.042, +0.332] | .128 | 2.431 | 99.28 | [−2.916, 3.207] |

Hiệu ứng cộng hưởng tổng hợp đạt *g* = −0,529 (KTC 95% [−0,659, −0,399], *p* < 0,001): nhóm người-AI hoạt động kém hơn khoảng nửa độ lệch chuẩn so với thành viên giỏi nhất. Đây là hiệu ứng ở mức trung bình-lớn theo chuẩn Cohen, và không phải hiện tượng biên: 175 trong 278 kích thước hiệu ứng (63%) mang giá trị âm.

Nhưng con số tổng hợp che giấu một cấu trúc bất đối xứng. AI ở vai trò hỗ trợ con người tạo ra hiệu ứng tăng cường rõ ràng (*g* = +0,494, *p* < 0,001), trong khi con người ở vai trò giám sát AI chỉ đạt *g* = +0,145 (*p* = 0,128), không có ý nghĩa thống kê. Sự giám sát của con người, cơ chế mà nhiều khung quản trị AI coi là điều kiện bắt buộc, gần như không tạo ra khác biệt đo lường được. Cấu trúc bất đối xứng này sẽ lặp lại nhất quán qua cả phân tích nhóm con lẫn meta-regression.

Cả ba phép so sánh đều cho thấy mức dị biệt cực đoan (I² = 90–99%). Khoảng dự đoán cho cộng hưởng trải rộng, từ −2,631 đến +1,572. Bên cạnh xu hướng trung bình tiêu cực, vẫn tồn tại những bối cảnh cộng tác tạo ra giá trị thực sự. Câu hỏi tiếp theo là: bối cảnh nào?

![Hình 1. Tổng quan phân phối kích thước hiệu ứng và forest plot tổng hợp](../Experiment/outputs/figures/Figure1_Overview.png)

*Hình 1.* Phân phối Hedges' *g* cho 278 kích thước hiệu ứng theo từng loại so sánh (hàng trên) và forest plot hiệu ứng ngẫu nhiên tổng hợp (hàng dưới). Histogram cho thấy sự tập trung của hiệu ứng cộng hưởng ở vùng âm, sự nhất quán dương của hiệu ứng AI hỗ trợ người, và mức phân tán lớn của hiệu ứng người hỗ trợ AI.

### 4.2 Kiểm định thiên lệch xuất bản

Bảng 3 trình bày kết quả từ bốn kiểm định bổ trợ.

**Bảng 3. Thiên lệch xuất bản**

| Kiểm định | Cộng hưởng | AI hỗ trợ người | Người hỗ trợ AI |
|---|---|---|---|
| **Egger's intercept** | 1.930 | 1.419 | 4.569 |
| **Egger's *p*** | .031 | < .001 | < .001 |
| **Thiên lệch (Egger)** | Có | Có | Có |
| **Begg's τ** | 0.185 | 0.185 | 0.173 |
| **Begg's *p*** | < .001 | < .001 | < .001 |
| **Thiên lệch (Begg)** | Có | Có | Có |
| **Trim-and-fill bổ sung** | 29 | 11 | 14 |
| **Trim-fill *g* điều chỉnh** | −0.812 | +0.356 | −0.508 |
| **Fail-safe N** | 376,476 | 132,306 | 44,576 |

Tin xấu trước: thiên lệch xuất bản hiện diện rõ ràng. Cả Egger lẫn Begg đều phát hiện bất đối xứng có ý nghĩa ở cả ba phép so sánh. Trim-and-fill ước tính 29, 11, và 14 nghiên cứu thiếu. Sau bổ sung, ước lượng dịch chuyển theo hướng tiêu cực hơn: cộng hưởng từ −0,529 xuống −0,812; AI hỗ trợ người từ +0,494 xuống +0,356; và đáng chú ý nhất, người hỗ trợ AI chuyển từ +0,145 (dương, ns) xuống −0,508 (âm, có ý nghĩa). Nếu thiên lệch ảnh hưởng, nó theo hướng làm giảm nhẹ mức nghiêm trọng, thâm hụt thực tế có thể lớn hơn con số báo cáo.

Tin tốt: fail-safe N ở mức rất cao, đặc biệt 376.476 cho cộng hưởng. Cần hàng trăm nghìn nghiên cứu null mới kéo được hiệu ứng về mức không có ý nghĩa. Các kết luận cốt lõi đủ vững.

![Hình 2. Chẩn đoán thiên lệch xuất bản](../Experiment/outputs/figures/Figure2_Publication_Bias.png)

*Hình 2.* Đánh giá thiên lệch xuất bản cho cả ba phép so sánh. Hàng trên: funnel plot với các nghiên cứu quan sát (vòng tròn rỗng) và nghiên cứu bổ sung bằng trim-and-fill (vòng tròn đặc). Hàng dưới: kiểm định hồi quy Egger. Tất cả các phép so sánh đều cho thấy bất đối xứng có ý nghĩa thống kê, với ước lượng điều chỉnh tiêu cực hơn quan sát.

### 4.3 Phân tích biến điều tiết

Mức dị biệt cực cao (I² > 90%) đặt ra câu hỏi liệu hiệu ứng cộng tác có đồng nhất hay thay đổi tùy bối cảnh. Bảng 4 trình bày kết quả phân tích nhóm con theo sáu biến điều tiết.

**Bảng 4. Phân tích nhóm con theo biến điều tiết**

| Biến điều tiết | Mức | *k* | Cộng hưởng *g* | AI hỗ trợ người *g* | Người hỗ trợ AI *g* |
|---|---|---|---|---|---|
| **Loại nhiệm vụ** | Quyết định | 252 | −0.619*** | +0.496*** | +0.043 (ns) |
| | Sáng tạo | 26 | +0.372 (ns) | +0.467*** | +1.114*** |
| | *Q*-between *p* | | < .001 | .047 | < .001 |
| **Kiến trúc AI** | Deep Learning | 132 | −0.204* | +0.396*** | +0.920*** |
| | Dựa trên quy luật | 52 | −1.247*** | +0.559*** | −0.876*** |
| | ML truyền thống | 46 | −0.506*** | +0.443*** | −0.362* |
| | Mô phỏng AI | 12 | −1.290*** | +0.673*** | −1.272*** |
| | Wizard of Oz | 36 | −0.435** | +0.734*** | −0.144 (ns) |
| | *Q*-between *p* | | < .001 | < .001 | < .001 |
| **Chuyên gia** | Không | 182 | −0.648*** | +0.456*** | +0.169 (ns) |
| | Có | 96 | −0.278** | +0.595*** | +0.052 (ns) |
| | *Q*-between *p* | | < .001 | < .001 | < .001 |
| **Giải thích AI** | Không | 115 | −0.611*** | +0.515*** | −0.009 (ns) |
| | Có | 163 | −0.471*** | +0.478*** | +0.249 (ns) |
| | *Q*-between *p* | | < .001 | .615 | .004 |
| **Năm** | 2020 | 62 | −0.835*** | +0.404*** | −0.103 (ns) |
| | 2021 | 93 | −0.558*** | +0.445*** | −0.118 (ns) |
| | 2022 | 65 | −0.634*** | +0.450*** | +0.616* |
| | 2023 | 54 | +0.013 (ns) | +0.757*** | +0.283 (ns) |
| | 2024 | 4 | −0.665* | +0.600*** | −0.665* |
| | *Q*-between *p* | | < .001 | < .001 | < .001 |

*Ghi chú.* \* *p* < .05, \*\* *p* < .01, \*\*\* *p* < .001. *Q*-between kiểm định mức giải thích dị biệt giữa các nhóm của biến điều tiết.

Sự phân hóa rõ rệt nhất xuất hiện theo loại nhiệm vụ (*Q*-between *p* < 0,001 ở cả ba phép so sánh). Với 252 kích thước hiệu ứng thuộc nhiệm vụ ra quyết định: cộng hưởng âm sâu (*g* = −0,619), con người gần như không đóng góp gì cho AI (*g* = +0,043, ns). 26 quan sát thuộc nhiệm vụ sáng tạo cho bức tranh ngược hẳn: cộng hưởng chuyển dương (*g* = +0,372, chưa đạt ý nghĩa do mẫu nhỏ), và con người cải thiện AI hơn một độ lệch chuẩn (*g* = +1,114, *p* < 0,001). Cộng tác dường như chỉ phát huy khi năng lực hai bên bổ khuyết thay vì cạnh tranh trên cùng một chiều.

Kiến trúc AI cho mô hình tương tự nhưng cơ chế khác. Deep learning, thường linh hoạt hơn song dễ mắc lỗi trên trường hợp biên, có thâm hụt cộng hưởng nhỏ nhất (*g* = −0,204) và là loại AI duy nhất mà con người cải thiện có ý nghĩa (*g* = +0,920, *p* < 0,001). Hệ thống dựa trên quy luật và AI mô phỏng, vốn hoạt động theo logic cố định trên phạm vi hẹp, chịu thâm hụt sâu nhất (lần lượt *g* = −1,247 và −1,290). Khi AI đã được tối ưu hóa cho miền nhiệm vụ cụ thể, can thiệp con người có xu hướng đưa thêm nhiễu.

Trình độ chuyên môn kiểm soát mức độ tổn thất. Chuyên gia mất ít hơn khi cộng tác (*g* = −0,278 so với −0,648 cho người không chuyên) và hưởng lợi nhiều hơn từ AI (*g* = +0,595 so với +0,456). Chuyên gia có kiến thức nền để nhận diện khi nào gợi ý AI đáng tin; người không chuyên thiếu cơ sở phân biệt, dao động giữa phụ thuộc quá mức và bác bỏ thiếu căn cứ.

Khả năng giải thích AI có vai trò chọn lọc. Giải thích làm giảm thâm hụt cộng hưởng (từ *g* = −0,611 xuống −0,471, *Q*-between *p* < 0,001) nhưng không ảnh hưởng đến hiệu ứng AI hỗ trợ người (*p* = 0,615). Sự phân biệt này hợp lý nếu xét cấu trúc tương tác: ở vai trò giám sát, con người cần đánh giá đầu ra AI nên giải thích hữu ích; ở vai trò người nhận hỗ trợ, họ chỉ cần biết gợi ý chứ không cần hiểu tại sao.

Chiều thời gian cho thấy xu hướng khích lệ. Thâm hụt cộng hưởng giảm dần từ *g* = −0,835 (2020) qua −0,558 (2021) và −0,634 (2022), rồi tiến đến *g* = +0,013 (ns) vào năm 2023, lần đầu ước lượng tổng hợp vượt ngưỡng zero. Song song, AI hỗ trợ người tăng từ +0,404 (2020) lên +0,757 (2023). Tổn thất giảm, lợi ích tăng. Sự cải thiện kép này phù hợp với sự trưởng thành dần của công nghệ AI và thiết kế giao diện cộng tác, dù ước lượng năm 2024 (*g* = −0,665, *k* = 4) dựa trên mẫu quá nhỏ để diễn giải.

![Hình 3. Kích thước hiệu ứng theo nhóm con](../Experiment/outputs/figures/FigureS5_Moderator_Bars.png)

*Hình 3.* Kích thước hiệu ứng theo nhóm con cho sáu biến điều tiết (hàng) qua ba phép so sánh (cột). Thanh đỏ: hiệu ứng âm; thanh xanh: hiệu ứng dương; đường lỗi: khoảng tin cậy 95%. Sự phân hóa rõ nhất xuất hiện theo loại nhiệm vụ, kiến trúc AI, và ngành. Truyền thông là ngành duy nhất có hiệu ứng dương ở phép so sánh người hỗ trợ AI.

Các phân tích nhóm con trên khảo sát từng biến điều tiết độc lập. Nhưng một biến có thể tương quan với biến khác (ví dụ: nhiệm vụ sáng tạo tập trung ở Truyền thông), khiến hiệu ứng riêng rẽ khó tách bạch. Meta-regression đa biến bằng mô hình 3 bậc REML cho phép kiểm tra liệu các mô hình trên có duy trì khi kiểm soát đồng thời tất cả sáu biến (Bảng 5).

**Bảng 5. Meta-regression đa biến (3-level REML)**

| Biến dự báo | Cộng hưởng β | AI hỗ trợ người β | Người hỗ trợ AI β |
|---|---|---|---|
| Intercept | −0,533 | +0,693*** | −0,519 |
| *Ngành* (ref: Y tế) | | | |
|   Kinh doanh | −0,836* | −0,211 | −0,679 |
|   Truyền thông | −0,551 | −0,359 | +0,596 |
|   Khu vực công | +0,037 | −0,237 | +0,559 |
| *Loại nhiệm vụ* (ref: Quyết định) | | | |
|   Sáng tạo | +1,235* | −0,086 | +0,956 |
| *Kiến trúc AI* (ref: Deep Learning) | | | |
|   Dựa trên quy luật | +1,442*** | +0,159 | +1,493*** |
|   ML truyền thống | −0,219 | +0,002 | −0,057 |
|   AI mô phỏng | +0,687 | +0,134 | +1,204 |
|   Wizard of Oz | −0,229 | +0,146 | +0,455 |
| *Trình độ* (ref: Không chuyên) | | | |
|   Chuyên gia | +0,166 | −0,037 | +0,121 |
| *Giải thích AI* (ref: Không) | | | |
|   Có | +0,058 | +0,004 | +0,009 |
| Năm (tâm = 2022) | +0,145 | +0,005 | −0,012 |
| | | | |
| *QM* (df = 11) | 26,58*** | 0,88 (ns) | 32,86*** |
| *τ²* residual | 1,088 | 0,239 | 3,291 |

*Ghi chú.* \* *p* < .05, \*\*\* *p* < .001. QM = kiểm định Wald omnibus cho toàn bộ biến điều tiết. Mô hình sử dụng cấu trúc ngẫu nhiên 3 bậc (Paper_ID / Exp_ID) với ước lượng REML.

Kết quả phân hóa rõ rệt giữa ba phép so sánh. Với cộng hưởng, kiểm định omnibus đạt ý nghĩa cao (QM = 26,58, *p* < 0,001). Hai biến dự báo nổi bật: ngành Kinh doanh chịu thâm hụt lớn hơn Y tế 0,84 SD (β = −0,836, *p* = 0,023), và nhiệm vụ sáng tạo có lợi thế 1,24 SD so với nhiệm vụ quyết định (β = +1,235, *p* = 0,011). Với người hỗ trợ AI, kiểm định omnibus cũng đạt ý nghĩa (QM = 32,86, *p* < 0,001), chủ yếu nhờ kiến trúc AI.

Đáng chú ý nhất là phép so sánh AI hỗ trợ người: không có biến dự báo nào đạt ý nghĩa (QM = 0,88, *p* = 0,559). Hiệu ứng AI cải thiện con người bền vững qua mọi ngành, mọi loại nhiệm vụ, mọi kiến trúc AI, mọi trình độ người dùng. Sáu biến điều tiết không thu hẹp được mức phân tán giữa các nghiên cứu (τ² residual = 1,09–3,29), xác nhận rằng dị biệt xuất phát từ những yếu tố ngoài các biến đã mã hóa.

![Hình 5. Hệ số meta-regression đa biến](../Experiment/outputs/figures/Figure5_MetaRegression_Coefficients.png)

*Hình 5.* Hệ số meta-regression đa biến (β ± KTC 95%) cho 11 biến dự báo qua ba phép so sánh. Điểm tròn đặc: hệ số có ý nghĩa thống kê (*p* < .05); điểm tròn rỗng: không có ý nghĩa. Đường dọc tại 0 đánh dấu ngưỡng không có hiệu ứng. Panel B (AI hỗ trợ người) không có biến nào đạt ý nghĩa (QM = 0,88, ns), xác nhận hiệu ứng AI cải thiện con người bền vững qua mọi bối cảnh.

### 4.4 Phân tích theo ngành

Ngành nghề giải thích mức dị biệt lớn nhất trong tất cả các biến điều tiết: *Q*-between đạt 885,66 cho cộng hưởng, 440,80 cho AI hỗ trợ người, 2.668,19 cho người hỗ trợ AI (tất cả *p* < .001). Con số này vượt xa mọi biến khác, và cả phân tích nhóm con lẫn meta-regression đều xác nhận.

**Bảng 6. Ma trận Ngành × So sánh**

| Ngành | *k* | Cộng hưởng *g* [KTC 95%] | AI hỗ trợ người *g* [KTC 95%] | Người hỗ trợ AI *g* [KTC 95%] |
|---|---|---|---|---|
| **Kinh doanh** | 46 | −0.926*** [−1.230, −0.623] | +0.706*** [+0.577, +0.835] | −0.732*** [−1.100, −0.364] |
| **Truyền thông** | 86 | −0.487*** [−0.774, −0.199] | +0.276*** [+0.191, +0.360] | +1.011*** [+0.553, +1.468] |
| **Y tế** | 107 | −0.306*** [−0.484, −0.128] | +0.632*** [+0.517, +0.747] | +0.087 (ns) [−0.133, +0.308] |
| **Khu vực công** | 39 | −0.703*** [−0.958, −0.447] | +0.428*** [+0.284, +0.573] | −0.581*** [−0.881, −0.282] |

*Ghi chú.* \*\*\* *p* < .001. Tất cả ước lượng từ mô hình hiệu ứng ngẫu nhiên DerSimonian-Laird.

Kết quả nổi bật nhất nằm ở ngành Truyền thông (*k* = 86). Đây là ngành duy nhất mà con người cải thiện AI ở mức lớn và có ý nghĩa: *g* = +1,011, hơn một độ lệch chuẩn. Kiểm duyệt nội dung, phát hiện thông tin sai lệch, đánh giá văn bản sáng tạo là những nhiệm vụ đòi hỏi hiểu biết bối cảnh văn hóa và nắm bắt sắc thái ngôn ngữ mà AI hiện tại chưa đủ năng lực xử lý. Ở đây, con người sở hữu điều mà AI thiếu, và sự phối hợp phản ánh đúng nghĩa bổ trợ. Dù hiệu ứng cộng hưởng vẫn âm (*g* = −0,487), mức thâm hụt nhỏ hơn nhiều so với ngành khác, và hiệu ứng AI hỗ trợ người ở mức khiêm tốn nhất (*g* = +0,276), gợi ý rằng trong lĩnh vực này, con người ít cần AI hỗ trợ hơn là AI cần con người.

Bức tranh đảo ngược ở Kinh doanh và Khu vực công. Hai ngành này chia sẻ cùng mô hình: thâm hụt cộng hưởng lớn (Kinh doanh *g* = −0,926; Khu vực công *g* = −0,703), AI hỗ trợ người hiệu quả, nhưng con người làm suy giảm có ý nghĩa hiệu suất AI (lần lượt *g* = −0,732 và −0,581). Trong các nhiệm vụ dự báo nhu cầu, định giá, đánh giá rủi ro tư pháp, hỗ trợ quyết định chính sách, AI đã hoạt động gần mức tối ưu, và bất kỳ can thiệp nào từ con người đều có xu hướng đưa thêm nhiễu. Ở Khu vực công, phát hiện này đặc biệt đáng lưu ý: nhiều khuôn khổ pháp lý hiện hành bắt buộc giám sát con người chính trong những lĩnh vực mà dữ liệu cho thấy sự giám sát đó phản tác dụng.

Y tế (*k* = 107) nằm giữa hai cực. Thâm hụt cộng hưởng nhỏ nhất (*g* = −0,306), AI hỗ trợ người hiệu quả (*g* = +0,632), và hiệu ứng người hỗ trợ AI gần bằng không (*g* = +0,087, ns). Giám sát con người không cải thiện nhưng cũng không làm giảm hiệu suất AI. Có lẽ sự trưởng thành của ứng dụng AI y tế, với giao thức thực nghiệm nghiêm ngặt và quy trình đào tạo người dùng hoàn thiện, giúp giảm thiểu cả hai loại sai lệch (phụ thuộc quá mức lẫn bác bỏ thiếu căn cứ).

Nhìn chung, giá trị của human-in-the-loop phụ thuộc vào khoảng cách năng lực giữa người và AI trong từng hệ sinh thái nhiệm vụ. Ở lĩnh vực AI đã đáp ứng tốt yêu cầu, can thiệp con người gây nhiễu; ở lĩnh vực nhiệm vụ đòi hỏi năng lực AI chưa đạt, vai trò con người vẫn thiết yếu.

![Hình 4. Phân tích toàn diện theo ngành](../Experiment/outputs/figures/Figure4_Industry_Comprehensive.png)

*Hình 4.* Phân tích toàn diện theo ngành. Panel trái: biểu đồ violin thể hiện phân phối kích thước hiệu ứng trong từng ngành. Panel giữa: forest plot ước lượng tổng hợp với khoảng tin cậy 95%. Panel phải: heatmap kích thước hiệu ứng qua các ngành và phép so sánh.

### 4.5 Phân tích độ nhạy

Để kiểm tra tính ổn định của các ước lượng, chúng tôi thực hiện phân tích leave-one-out cho cả ba phép so sánh, lần lượt loại bỏ từng nghiên cứu và tính lại ước lượng tổng hợp. Kết quả cho thấy không có nghiên cứu đơn lẻ nào chi phối ước lượng: cộng hưởng dao động trong khoảng [−0.549, −0.517], AI hỗ trợ người trong [+0.486, +0.498], và người hỗ trợ AI trong [+0.083, +0.160]. Hướng, độ lớn, và ý nghĩa thống kê của các hiệu ứng không thay đổi qua tất cả các lần lặp.

Phân tích meta tích lũy theo thứ tự thời gian cho thấy cả ba ước lượng hội tụ và ổn định sau khoảng 150 kích thước hiệu ứng, xác nhận rằng cơ sở bằng chứng hiện tại đủ lớn cho suy luận đáng tin cậy. Kết quả chi tiết được trình bày trong Hình phụ lục S3.

---

## 5. Thảo luận

### 5.1 Bất đối xứng thông tin và bài toán giám sát

Tại sao AI cải thiện con người nhưng con người không cải thiện AI? Câu trả lời nằm ở cấu trúc thông tin, không phải năng lực tuyệt đối.

Khi AI đóng vai trò công cụ hỗ trợ, con người vẫn giữ quyền kiểm soát quá trình ra quyết định. Họ tiếp nhận gợi ý của AI như một nguồn thông tin bổ sung, lọc qua kinh nghiệm và tri thức ngầm (tacit knowledge), rồi quyết định trong khung phán đoán vốn có. Cấu trúc này tương tự mô hình "judge-advisor" (Sniezek & Buckley, 1995): người quyết định hưởng lợi từ thông tin bổ sung mà không cần hiểu toàn bộ cơ chế tạo ra thông tin đó. Meta-regression đa biến cho kết quả đáng chú ý: khi kiểm soát đồng thời cả sáu biến điều tiết, không biến nào giải thích hiệu ứng AI hỗ trợ người (QM = 0,88, *p* = 0,559). Nhiệm vụ thay đổi, ngành thay đổi, kiến trúc AI thay đổi, nhưng cấu trúc thông tin trong mối quan hệ judge-advisor thì không.

Chiều ngược lại khác hẳn. Khi con người giám sát AI, họ phải đánh giá đầu ra của một hệ thống mà quy trình nội bộ hầu như không quan sát được. Đây là bài toán thông tin bất đối xứng kinh điển (Akerlof, 1970): người giám sát thiếu thông tin phân biệt đầu ra đúng và sai. Alchian và Demsetz (1972) đã chỉ ra rằng giám sát chỉ tạo giá trị khi chi phí giám sát thấp hơn lợi ích từ việc phát hiện sai lệch. Trong phần lớn bối cảnh cộng tác người-AI mà chúng tôi khảo sát, điều kiện này không được đáp ứng.

Cơ chế hành vi đã được ghi nhận. Parasuraman và Manzey (2010) cho thấy automation bias xuất hiện ở cả chuyên gia lẫn người mới, không thể khắc phục bằng huấn luyện đơn thuần. Dietvorst và cộng sự (2015) và Logg và cộng sự (2019) mô tả hai dạng phản ứng đối lập: automation bias (phụ thuộc quá mức vào thuật toán) và algorithm aversion (bác bỏ thuật toán khi thấy nó mắc lỗi). Cả hai đều phi tối ưu, và cùng xuất phát từ việc con người thiếu cơ sở để hiệu chuẩn mức tin tưởng. Kết quả là sự can thiệp mang tính bán-ngẫu nhiên (semi-random) so với độ chính xác hệ thống của AI. Trong 69% trường hợp trong bộ dữ liệu này, AI vượt trội con người ở đường cơ sở, và sự can thiệp nhất quán làm giảm hiệu suất.

Cần thận trọng khi mở rộng kết luận này sang các miền chưa được khảo sát. Bộ dữ liệu tập trung ở bốn ngành cụ thể, và cấu trúc thông tin trong các ngành khác (ví dụ sản xuất, giáo dục) có thể khác. Dù vậy, hàm ý chính sách khó bỏ qua. Đạo luật AI của EU, Sắc lệnh Hành pháp của Hoa Kỳ về An toàn AI, và nhiều khuôn khổ quản trị tổ chức đều xây dựng trên tiền đề rằng thêm một khâu xem xét của con người luôn tốt hơn không có. Dữ liệu cho thấy tiền đề đó cần xem xét lại, ít nhất trong các bối cảnh mà giám sát con người gây hại có ý nghĩa thống kê (Kinh doanh *g* = −0,73; Khu vực công *g* = −0,58).

### 5.2 Lợi thế so sánh và ranh giới của sự bổ trợ

Phần trên giải thích tại sao giám sát thất bại. Nguyên lý lợi thế so sánh (Ricardo, 1817) giải thích khi nào cộng tác thành công: khi mỗi bên sở hữu lợi thế rõ rệt trên những khía cạnh khác nhau của nhiệm vụ.

Sự phân tách giữa nhiệm vụ ra quyết định và nhiệm vụ sáng tạo minh họa rõ nhất. Ở nhiệm vụ phân loại và dự báo, AI hiện tại thường đã đạt hoặc vượt năng lực con người, khoảng cách lợi thế so sánh hẹp. Thêm con người vào chủ yếu tạo thêm nhiễu. Ở nhiệm vụ sáng tạo, AI mạnh về nhận diện mẫu và tổng hợp thông tin; con người mạnh về bối cảnh hóa và phán đoán thẩm mỹ. Hai bộ năng lực giao nhau tối thiểu. Hiệu ứng người hỗ trợ AI phản ánh điều đó: *g* = +1,114 cho sáng tạo, *g* = +0,043 (ns) cho quyết định. Meta-regression xác nhận: sau khi kiểm soát ngành, kiến trúc AI, trình độ chuyên gia, nhiệm vụ sáng tạo vẫn có lợi thế 1,24 SD (β = +1,235, *p* = 0,011).

Sự phân hóa theo ngành tuân theo logic tương tự, dù chúng tôi không cho rằng đây là giải thích duy nhất. Truyền thông (*g* = +1,011 cho người hỗ trợ AI) đòi hỏi hiểu biết bối cảnh văn hóa, sắc thái ngôn ngữ, chuẩn mực xã hội, nhận diện châm biếm, phân biệt ý kiến và sự kiện. AI hiện tại chưa xử lý tốt những yếu tố này. Kinh doanh (*g* = −0,926 cho cộng hưởng) bao gồm chủ yếu các nhiệm vụ dự báo mà AI đã đạt hiệu suất cao. Sau khi kiểm soát các yếu tố gây nhiễu, ngành Kinh doanh vẫn chịu thâm hụt lớn hơn Y tế 0,84 SD (β = −0,836, *p* = 0,023). Tuy nhiên, cần ghi nhận rằng sự phân bổ loại nhiệm vụ không đồng đều giữa các ngành, và một phần hiệu ứng ngành có thể phản ánh cấu trúc nhiệm vụ hơn là đặc trưng riêng của ngành.

Chuyên gia chịu tổn thất cộng hưởng nhỏ hơn (*g* = −0,278 so với −0,648). Tschandl và cộng sự (2020) ghi nhận kết quả tương tự trong da liễu: bác sĩ ít kinh nghiệm nhất hưởng lợi nhiều nhất từ AI, nhưng chỉ chuyên gia mới biết khi nào bác bỏ gợi ý sai. Có lẽ vì họ sở hữu tri thức mà AI không có: trực giác nghề nghiệp về dấu hiệu bất thường, kinh nghiệm tích lũy với trường hợp biên, khả năng nhận ra khi nào AI sai dựa trên hiểu biết sâu về miền vấn đề. Người không chuyên thiếu năng lực đặc thù này, nên sự tham gia của họ không bổ sung gì ngoài nhiễu. Dù vậy, meta-regression không tìm thấy hiệu ứng trình độ sau kiểm soát (β = +0,166, ns), gợi ý rằng vai trò của chuyên môn có thể bị giao thoa với ngành và loại nhiệm vụ trong dữ liệu hiện tại.

Một quan sát bổ sung: cộng hưởng có xu hướng dương trong các trường hợp mà con người vượt trội AI ở đường cơ sở, và âm khi AI vượt trội. AI vượt trội con người trong 193/278 trường hợp (69%). Nghịch lý cộng tác, do đó, không phải thuộc tính bất biến mà phản ánh cấu trúc lợi thế so sánh hiện tại. Khi AI chạm giới hạn năng lực hoặc khi nhiệm vụ dịch chuyển sang các miền mà con người có lợi thế, tiềm năng cộng tác sẽ thay đổi.

### 5.3 Vai trò của thiết kế thông tin trong hiệu chuẩn niềm tin

Nếu vấn đề cốt lõi là bất đối xứng thông tin, giải pháp hướng đến là giảm chính sự bất đối xứng đó, cung cấp cho người giám sát thêm tín hiệu về trạng thái nội bộ của AI. Dữ liệu cung cấp hai bằng chứng gián tiếp.

Trong các nghiên cứu mà AI cung cấp điểm tin cậy, thâm hụt cộng hưởng nhỏ hơn đáng kể (trung bình *g* = −0,116 so với −0,717). Biến này chưa đủ mẫu để phân tích nhóm con chính thức, nhưng mô hình nhất quán với lý thuyết hiệu chuẩn niềm tin: khi con người biết AI "tự tin" hay "không chắc", họ có cơ sở tốt hơn để quyết định khi nào chấp nhận và khi nào can thiệp. Điểm tin cậy cho phép người giám sát quan sát một phần trạng thái nội bộ của hệ thống, về bản chất là một cơ chế giảm bất đối xứng thông tin.

Khả năng giải thích cho kết quả tương tự nhưng có chọn lọc: giảm thâm hụt cộng hưởng (*Q*-between *p* < .001) mà không ảnh hưởng đến hiệu ứng AI hỗ trợ người (*p* = 0,615). Giải thích giúp con người ở vai trò giám sát, nơi họ cần đánh giá đầu ra AI; nhưng không cần thiết ở vai trò người nhận hỗ trợ, nơi gợi ý đã đủ. Phân biệt này phù hợp với Bansal và cộng sự (2021) về vai trò không đồng nhất của giải thích AI, và với Lai và Tan (2019) cho thấy dự đoán của mô hình cải thiện hiệu suất con người hơn 20%, nhưng giải thích thêm không mang lại lợi ích bổ sung đáng kể.

Xu hướng cải thiện theo thời gian gợi ý thêm. Thâm hụt cộng hưởng thu hẹp từ *g* = −0,835 (2020) xuống gần zero (2023), đồng thời hiệu ứng AI hỗ trợ người tăng từ +0,404 lên +0,757. Giai đoạn 2020–2023 chứng kiến sự trưởng thành nhanh của cả công nghệ AI lẫn thiết kế giao diện: các hệ thống mới hơn tích hợp tốt hơn cơ chế giải thích và trực quan hóa mức tin cậy. Nhưng chúng tôi không thể tách bạch hiệu ứng của thiết kế thông tin khỏi sự tiến bộ thuần túy của năng lực AI với dữ liệu hiện tại. Nếu vai trò thiết kế là thực, nó mở ra hướng can thiệp cụ thể: thay vì tranh luận có nên human-in-the-loop hay không, nên đầu tư vào *cách* thiết kế giao diện cộng tác.

Dữ liệu năm 2024 (*k* = 4) quá ít để rút ra kết luận, và xu hướng cải thiện có thể không đơn điệu.

### 5.4 Hàm ý cho thiết kế tổ chức và chính sách

Từ các phân tích trên, một nguyên tắc thiết kế dần hiện ra. Giá trị của human-in-the-loop không cố định mà phụ thuộc vào cấu trúc lợi thế so sánh giữa người và AI trong nhiệm vụ cụ thể, mức độ bất đối xứng thông tin trong giao diện cộng tác, và năng lực hiệu chuẩn niềm tin của người giám sát.

Cộng tác hiệu quả khi nhiệm vụ có vùng bổ trợ năng lực rộng (nhiệm vụ sáng tạo, lĩnh vực Truyền thông), giao diện cung cấp đủ thông tin để con người đánh giá đầu ra AI, và người giám sát có đủ chuyên môn để sử dụng thông tin đó. Khi một hoặc nhiều điều kiện không đáp ứng, can thiệp con người gây nhiễu nhiều hơn bổ trợ. Tất nhiên, khung này đơn giản hóa một thực tế phức tạp hơn: các tương tác bậc hai giữa ba yếu tố chưa được kiểm tra trong dữ liệu hiện tại, và có thể tồn tại những yếu tố bối cảnh khác mà chúng tôi chưa mã hóa.

Đối với nhà quản lý, nguyên tắc này đòi hỏi chuyển từ giả định "thêm con người luôn tốt hơn" sang "đo lường trước, triển khai có chọn lọc." Dietvorst và cộng sự (2018) cho thấy chỉ cần cho phép người dùng điều chỉnh nhỏ đầu ra thuật toán đã giảm đáng kể algorithm aversion và cải thiện hiệu suất. Tổ chức cần so sánh hiệu suất giữa con người đơn lẻ, AI đơn lẻ, và nhóm cộng tác cho từng nhiệm vụ trước khi quyết định cấu trúc triển khai. Đối với nhà hoạch định chính sách, các quy định human-in-the-loop áp dụng đồng nhất bất kể ngành và nhiệm vụ không được hỗ trợ bởi dữ liệu. Khung pháp lý cần mang tính đặc thù hơn, yêu cầu giám sát con người ở những bối cảnh dữ liệu cho thấy nó tạo giá trị, và cho phép linh hoạt ở những bối cảnh mà nó không cần thiết hoặc phản tác dụng.

---

## 6. Kết luận

Từ 146 lên 278 kích thước hiệu ứng, từ hai lên bốn ngành. Nghịch lý cộng tác người-AI được xác lập trong nghiên cứu trước (Ngo và cs., 2025) khái quát hóa với hiệu ứng tổng hợp thậm chí lớn hơn (*g* = −0,529 so với −0,380). Nhưng quan trọng hơn con số trung bình là cấu trúc bên dưới.

Kết quả xác nhận cả bốn giả thuyết: H1 (nghịch lý cộng hưởng khái quát hóa), H2 (tăng cường bất đối xứng, AI hỗ trợ người bền vững qua mọi bối cảnh), H3 (ngành và loại nhiệm vụ điều tiết mạnh), H4 (thâm hụt thu hẹp theo thời gian). Phát hiện ngoài dự kiến là phép so sánh AI hỗ trợ người hoàn toàn không phụ thuộc bối cảnh (QM = 0,88, ns), khẳng định mô hình judge-advisor mạnh hơn dự đoán ban đầu.

Truyền thông là ngoại lệ cho thấy khung phân tích hoạt động: ở những nhiệm vụ đòi hỏi năng lực mà AI chưa có, sự tham gia của con người chuyển từ gánh nặng thành tài sản (*g* = +1,011). Xu hướng cải thiện theo thời gian cho thấy nghịch lý không phải định mệnh, thâm hụt thu hẹp từ *g* = −0,835 (2020) đến gần zero (2023).

Một số hạn chế cần cân nhắc. I² > 90% cho thấy các ước lượng tổng hợp mô tả xu hướng trung tâm của một phân phối rất rộng, khoảng dự đoán [−2,631, +1,572] cho cộng hưởng xác nhận điều này. Bộ dữ liệu mất cân bằng giữa nhiệm vụ quyết định (*k* = 252) và sáng tạo (*k* = 26), khiến ước lượng nhóm sáng tạo cần xác nhận thêm. Giai đoạn phân tích 2020–2024 trùng với thời kỳ AI tiến bộ nhanh, đặc biệt sự xuất hiện của mô hình ngôn ngữ lớn; các mô hình quan sát ở đây có thể dịch chuyển khi bức tranh công nghệ thay đổi. Thiên lệch xuất bản hiện diện ở cả ba phép so sánh, và ước lượng điều chỉnh gợi ý thâm hụt thực tế có thể còn lớn hơn.

Hai câu hỏi mở cho nghiên cứu tương lai. Thứ nhất, liệu xu hướng cải thiện có tiếp tục khi AI sinh tạo trở thành trung tâm cộng tác người-máy, hay sự phức tạp của các mô hình mới tạo ra những dạng bất đối xứng thông tin khác. Thứ hai, liệu các giao thức cộng tác động, chuyển đổi giữa quyết định của con người và AI dựa trên ước lượng hiệu suất thời gian thực, có thể vượt qua thiết kế human-in-the-loop tĩnh.

Thông điệp trung tâm: sự giám sát của con người không mang giá trị tự thân. Giá trị đó phụ thuộc vào việc con người có sở hữu lợi thế so sánh, có đủ thông tin giám sát, và có đủ chuyên môn. Thiết kế chính sách và tổ chức cần phản ánh điều này.

---

## Tài liệu tham khảo

Akerlof, G. A. (1970). The market for "lemons": Quality uncertainty and the market mechanism. *Quarterly Journal of Economics*, 84(3), 488–500.

Alchian, A. A., & Demsetz, H. (1972). Production, information costs, and economic organization. *American Economic Review*, 62(5), 777–795.

Bansal, G., Wu, T., Zhou, J., Fok, R., Nushi, B., Kamar, E., Ribeiro, M. T., & Weld, D. S. (2021). Does the whole exceed its parts? The effect of AI explanations on complementary team performance. *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems*, 1–16.

Begg, C. B., & Mazumdar, M. (1994). Operating characteristics of a rank correlation test for publication bias. *Biometrics*, 50(4), 1088–1101.

Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2009). *Introduction to meta-analysis*. John Wiley & Sons.

Brynjolfsson, E., & McAfee, A. (2017). The business of artificial intelligence. *Harvard Business Review*, 95(7), 3–11.

Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To trust or to think: Cognitive forcing functions can reduce overreliance on AI in AI-assisted decision-making. *Proceedings of the ACM on Human-Computer Interaction*, 5(CSCW1), 1–21.

Burton, J. W., Stein, M.-K., & Jensen, T. B. (2020). A systematic review of algorithm aversion in augmented decision making. *Journal of Behavioral Decision Making*, 33(2), 220–239.

Castelo, N., Bos, M. W., & Lehmann, D. R. (2019). Task-dependent algorithm aversion. *Journal of Marketing Research*, 56(5), 809–825.

Davenport, T. H., & Ronanki, R. (2018). Artificial intelligence for the real world. *Harvard Business Review*, 96(1), 108–116.

Dawes, R. M., Faust, D., & Meehl, P. E. (1989). Clinical versus actuarial judgment. *Science*, 243(4899), 1668–1674.

DerSimonian, R., & Laird, N. (1986). Meta-analysis in clinical trials. *Controlled Clinical Trials*, 7(3), 177–188.

Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion: People erroneously avoid algorithms after seeing them err. *Journal of Experimental Psychology: General*, 144(1), 114–126.

Dietvorst, B. J., Simmons, J. P., & Massey, C. (2018). Overcoming algorithm aversion: People will use imperfect algorithms if they can (even slightly) modify them. *Management Science*, 64(3), 1155–1170.

Duval, S., & Tweedie, R. (2000). Trim and fill: A simple funnel-plot-based method of testing and adjusting for publication bias in meta-analysis. *Biometrics*, 56(2), 455–463.

Egger, M., Davey Smith, G., Schneider, M., & Minder, C. (1997). Bias in meta-analysis detected by a simple, graphical test. *BMJ*, 315(7109), 629–634.

Green, B., & Chen, Y. (2019). The principles and limits of algorithm-in-the-loop decision making. *Proceedings of the ACM on Human-Computer Interaction*, 3(CSCW), 1–24.

Grove, W. M., Zald, D. H., Lebow, B. S., Snitz, B. E., & Nelson, C. (2000). Clinical versus mechanical prediction: A meta-analysis. *Psychological Assessment*, 12(1), 19–30.

Higgins, J. P. T., Thompson, S. G., Deeks, J. J., & Altman, D. G. (2003). Measuring inconsistency in meta-analyses. *BMJ*, 327(7414), 557–560.

Kleinberg, J., Lakkaraju, H., Leskovec, J., Ludwig, J., & Mullainathan, S. (2018). Human decisions and machine predictions. *The Quarterly Journal of Economics*, 133(1), 237–293.

Lai, V., & Tan, C. (2019). On human predictions with explanations and predictions of machine learning models: A case study on deception detection. *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT\*)*, 29–38.

Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. *Organizational Behavior and Human Decision Processes*, 151, 90–103.

Ngo, V. M., et al. (2025). Human-AI collaboration in high-stakes decisions: A meta-analysis of healthcare and public sectors. *Applied Economics Letters*. Taylor & Francis.

Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors*, 52(3), 381–410.

Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors*, 39(2), 230–253.

Ricardo, D. (1817). *On the principles of political economy and taxation*. John Murray.

Rosenthal, R. (1979). The file drawer problem and tolerance for null results. *Psychological Bulletin*, 86(3), 638–641.

Sniezek, J. A., & Buckley, T. (1995). Cueing and cognitive conflict in judge-advisor decision making. *Organizational Behavior and Human Decision Processes*, 62(2), 159–174.

Topol, E. J. (2019). High-performance medicine: The convergence of human and artificial intelligence. *Nature Medicine*, 25(1), 44–56.

Tschandl, P., Rinner, C., Apalla, Z., Argenziano, G., et al. (2020). Human–computer collaboration for skin cancer recognition. *Nature Medicine*, 26(8), 1229–1234.

Viechtbauer, W. (2010). Conducting meta-analyses in R with the metafor package. *Journal of Statistical Software*, 36(3), 1–48.

---

## Phụ lục

### Phụ lục A: Danh sách Viết tắt

| Viết tắt | Thuật ngữ đầy đủ (Tiếng Anh) | Ý nghĩa (Tiếng Việt) |
|---|---|---|
| **AI** | Artificial Intelligence | Trí tuệ nhân tạo |
| ***β*** | Regression Coefficient | Hệ số hồi quy |
| **CI / KTC** | Confidence Interval | Khoảng tin cậy |
| ***d*** | Cohen's *d* | Chỉ số kích thước hiệu ứng Cohen |
| ***df*** | Degrees of Freedom | Bậc tự do |
| **DL** | DerSimonian-Laird Model | Mô hình hiệu ứng ngẫu nhiên (dùng cho phân tích nhóm con) |
| **REML** | Restricted Maximum Likelihood | Ước lượng hợp lý cực đại giới hạn (dùng cho phân tích chính và meta-regression) |
| ***g*** | Hedges' *g* | Chỉ số kích thước hiệu ứng chuẩn hóa |
| **I²** | Percentage of Variance Due to Heterogeneity | Tỷ lệ phần trăm dị biệt |
| ***k*** | Number of Effect Sizes | Số lượng kích thước hiệu ứng |
| ***n*** | Sample Size | Kích thước mẫu |
| **ns** | Not Significant | Không có ý nghĩa thống kê (*p* ≥ .05) |
| ***p*** | *p*-value | Giá trị *p* (mức ý nghĩa thống kê) |
| ***Q*** | Cochran's *Q* Statistic | Kiểm định dị biệt (heterogeneity test) |
| ***QB*** / ***Q*-between** | Between-Group *Q* Statistic | Kiểm định liệu biến điều tiết giải thích dị biệt |
| ***QM*** | Omnibus Wald Test Statistic | Kiểm định Wald tổng thể cho toàn bộ biến dự báo |
| **ref** | Reference Category | Danh mục tham chiếu |
| **REML** | Restricted Maximum Likelihood | Phương pháp ước lượng khả năng cực đại có hạn chế |
| ***τ*** | Tau | Độ lệch chuẩn của các hiệu ứng thực sự |
| ***τ²*** | Tau-Squared / Between-Study Variance | Phương sai ước lượng giữa các nghiên cứu |
| **RQ** | Research Question | Câu hỏi nghiên cứu |

**Ghi chú.** Trong các bảng và kết quả, mức ý nghĩa thống kê được ký hiệu như sau: \* *p* < .05; \*\* *p* < .01; \*\*\* *p* < .001. Các ký hiệu toán học và biến (*g*, *d*, *p*, *Q*, β, τ², *n*, *k*) được in nghiêng theo quy ước APA lần thứ 7. KTC là viết tắt tiếng Việt của "Khoảng tin cậy" tương ứng với CI (Confidence Interval) tiếng Anh. Tất cả các viết tắt sử dụng trong bản thảo này được liệt kê ở trên, ngoại trừ những viết tắt được biết đến rộng rãi (ví dụ: NHS, AI ở mục đích sử dụng chung) hoặc chỉ được sử dụng một lần.

---

### Phụ lục B: Hình S1 — Xu hướng theo thời gian

![Hình S1. Xu hướng hiệu ứng cộng tác người-AI theo năm](../Experiment/outputs/figures/FigureS1_Temporal_Trend.png)

*Hình S1.* Biến động ước lượng tổng hợp theo năm công bố (2020–2024) cho ba phép so sánh. Thâm hụt cộng hưởng giảm dần qua các năm, đạt mức gần zero vào năm 2023. Đồng thời, hiệu ứng AI hỗ trợ người tăng từ *g* = +0.404 (2020) lên *g* = +0.757 (2023), phản ánh sự cải thiện song song của cả công nghệ AI lẫn thiết kế giao diện cộng tác.

### Phụ lục C: Hình S2 — Forest plot mức nghiên cứu

![Hình S2. Forest plot toàn bộ 278 kích thước hiệu ứng](../Experiment/outputs/figures/FigureS6_Study_Forest.png)

*Hình S2.* Forest plot mức nghiên cứu cho toàn bộ 278 kích thước hiệu ứng, xếp theo độ lớn trong từng phép so sánh. Mỗi đường ngang thể hiện khoảng tin cậy 95% của một kích thước hiệu ứng riêng lẻ; màu đỏ biểu thị hiệu ứng âm, màu xanh biểu thị hiệu ứng dương. Đường cong tích lũy cho thấy tỷ lệ nghiên cứu có hiệu ứng âm so với dương. Ở phép so sánh cộng hưởng, 175 trong 278 quan sát (63%) nằm ở vùng âm; ở phép so sánh AI hỗ trợ người, 228 (82%) nằm ở vùng dương; ở phép so sánh người hỗ trợ AI, phân bổ gần cân bằng với 148 âm (53%) và 130 dương (47%), phù hợp với ước lượng tổng hợp không có ý nghĩa thống kê (*p* = .128).

### Phụ lục D: Hình S3 — Phân tích độ nhạy

![Hình S3. Phân tích leave-one-out và meta tích lũy](../Experiment/outputs/figures/FigureS3_Sensitivity.png)

*Hình S3.* Kết quả phân tích độ nhạy. Phần trên: phân tích leave-one-out cho thấy ước lượng tổng hợp ổn định khi lần lượt loại bỏ từng nghiên cứu — không có nghiên cứu nào có ảnh hưởng chi phối. Phần dưới: phân tích meta tích lũy theo thứ tự thời gian, cho thấy cả ba ước lượng hội tụ sau khoảng 150 kích thước hiệu ứng.

### Phụ lục E: Hình S4 — Heatmap tổng hợp

![Hình S4. Heatmap tổng hợp hiệu ứng theo biến điều tiết](../Experiment/outputs/figures/FigureS4_Summary_Heatmap.png)

*Hình S4.* Heatmap tổng hợp kích thước hiệu ứng theo tất cả các mức biến điều tiết và ba phép so sánh. Màu đỏ biểu thị hiệu ứng dương, màu xanh biểu thị hiệu ứng âm, cường độ màu phản ánh độ lớn. Heatmap cung cấp cái nhìn toàn cảnh về các vùng mà cộng tác người-AI mang lại lợi ích (Sáng tạo, Truyền thông, Deep Learning) so với các vùng phản tác dụng (Quyết định, Kinh doanh, Dựa trên quy luật).
