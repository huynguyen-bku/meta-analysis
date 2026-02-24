# Nghịch lý cộng tác người–AI: Phân tích meta liên ngành trên 278 kích thước hiệu ứng

**Tác giả**: Vu Minh Ngo, Le Van Duy, Huy Nguyen, Vuong TT Ngoc

**Tạp chí**: JABES (2026)

---

## Tóm tắt

Trí tuệ nhân tạo (AI) ngày càng được triển khai song hành với con người trong quá trình ra quyết định, dựa trên giả định rằng sự kết hợp giữa phán đoán con người và độ chính xác thuật toán sẽ cho kết quả vượt trội. Nghiên cứu này kiểm chứng hệ thống giả định đó trên bốn ngành—Y tế, Kinh doanh, Truyền thông, và Khu vực công—được lựa chọn vì có quy mô ứng dụng AI trong ra quyết định lớn và hệ sinh thái nhiệm vụ đủ khác biệt để đánh giá tính khái quát. Tổng hợp 278 kích thước hiệu ứng từ 67 nghiên cứu thực nghiệm bao gồm 90 thí nghiệm riêng biệt trong giai đoạn 2020–2024, chúng tôi áp dụng mô hình hiệu ứng ngẫu nhiên ba bậc qua ba phép so sánh: nhóm cộng tác so với thành viên có hiệu suất cao nhất, nhóm so với con người độc lập, và nhóm so với AI độc lập. Nhóm người–AI hoạt động kém hơn có ý nghĩa so với thành viên có hiệu suất cao nhất (*g* = −0,529, *p* < 0,001). Mô hình này bất đối xứng: AI cải thiện đáng kể hiệu suất con người (*g* = +0,494, *p* < 0,001), nhưng con người không cải thiện có ý nghĩa hiệu suất AI (*g* = +0,145, *p* = 0,128). Mức dị biệt cực cao (I² = 90–99%) cho thấy bối cảnh đóng vai trò quyết định. Ngành nghề nổi lên là biến điều tiết chủ đạo: Truyền thông là lĩnh vực duy nhất mà con người cải thiện AI đáng tin cậy (*g* = +1,01), trong khi Kinh doanh có thâm hụt sâu nhất (*g* = −0,93). Hồi quy meta đa biến xác nhận loại nhiệm vụ và kiến trúc AI điều tiết các hiệu ứng ngay cả sau khi kiểm soát đồng thời. Phân tích xu hướng cho thấy tổn thất cộng hưởng đang thu hẹp, với năm 2023 đánh dấu lần đầu chi phí cộng tác tiến đến zero. Các kết quả phản bác việc áp dụng đại trà cơ chế giám sát con người và ủng hộ thiết kế cộng tác phù hợp bối cảnh.

**Từ khóa**: cộng tác người–AI, phân tích meta, ra quyết định, tăng cường, cộng hưởng, con người tham gia vào vòng lặp xử lý

---

## 1. Giới thiệu

Trong thập kỷ qua, trí tuệ nhân tạo (AI) chuyển từ công cụ hỗ trợ sang tác nhân tham gia trực tiếp vào quá trình ra quyết định trong các lĩnh vực trọng yếu như y tế, kinh doanh, truyền thông và khu vực công. Ở nhiều bối cảnh, đây là những quyết định có tính đặt cược cao, nơi sai sót có thể gây hậu quả nghiêm trọng và khó đảo ngược. Bác sĩ X-quang xem xét các bản quét được AI đánh dấu. Thẩm phán tham vấn điểm rủi ro thuật toán. Nhà phân tích tài chính dựa vào dự báo học máy (machine learning) như thực hành chuẩn (Brynjolfsson & McAfee, 2017; Davenport & Ronanki, 2018; Kleinberg và cs., 2018). Nền tảng chung của các triển khai này là một giả định: cơ chế con người tham gia vào vòng lặp xử lý (human-in-the-loop) kết hợp thế mạnh bổ trợ, trong đó con người đóng góp khả năng hiểu bối cảnh và phán đoán đạo đức, còn AI đóng góp tốc độ xử lý, tính nhất quán, năng lực nhận diện mẫu ở quy mô lớn, và khả năng làm việc không mệt mỏi. Theo lý thuyết, sự kết hợp sẽ cho kết quả vượt trội.

Nhưng bằng chứng thực nghiệm ngày càng đi ngược lại giả định đó. Trong chẩn đoán hình ảnh, tư pháp hình sự, kiểm duyệt nội dung, dự báo tài chính, việc thêm con người vào hệ thống AI hoặc thêm AI vào quy trình con người đôi khi làm *giảm* hiệu suất thay vì cải thiện (Bansal và cs., 2021; Buçinca và cs., 2021; Green & Chen, 2019). Những sai lệch hành vi như phụ thuộc quá mức vào gợi ý tự động, hoặc can thiệp điều chỉnh dựa trên trực giác nhưng thiếu căn cứ thực nghiệm, có thể làm suy yếu lợi ích của thuật toán. Nhìn từ kinh tế học tổ chức, điều này không quá bất ngờ. Lý thuyết chi phí giám sát (Alchian & Demsetz, 1972) đã chỉ ra rằng giám sát chỉ tạo giá trị khi người giám sát có đủ thông tin phân biệt đầu ra đúng và sai, một điều kiện khó đáp ứng khi đối tượng giám sát là hệ thống AI vận hành theo cơ chế hầu như không quan sát được. Câu hỏi không còn là liệu cộng tác có đôi khi thất bại, mà là thất bại với tần suất nào, ở mức độ nào, trong những điều kiện gì, và liệu có bối cảnh nào sự phối hợp thực sự hiệu quả.

Trong các lĩnh vực ràng buộc pháp lý và dịch vụ công, thất bại cộng tác không chỉ là câu chuyện hiệu suất trung bình. Khi quyết định được tự động hóa và triển khai ở quy mô lớn, sai lệch nhỏ có thể bị nhân rộng, trong khi cơ chế truy vết và trách nhiệm giải trình trở nên mờ hơn. Vì vậy, cần một đánh giá định lượng có hệ thống về khi nào cộng tác tạo giá trị, khi nào phá hủy giá trị, và những yếu tố bối cảnh nào điều tiết các hiệu ứng này.

Nghiên cứu này tổng hợp **278 kích thước hiệu ứng** từ **67 nghiên cứu bình duyệt** bao gồm **90 thí nghiệm riêng biệt** trải rộng trên **bốn ngành**: Y tế, Kinh doanh, Truyền thông, và Khu vực công. Bốn ngành được lựa chọn vì đại diện cho những hệ sinh thái nhiệm vụ khác biệt căn bản—từ chẩn đoán hình ảnh y khoa, dự báo nhu cầu và định giá trong kinh doanh, kiểm duyệt nội dung và phát hiện thông tin sai lệch trong truyền thông, đến đánh giá rủi ro trong khu vực công—cho phép kiểm tra tính khái quát của các hiệu ứng cộng tác trên nhiều bối cảnh ra quyết định. Bao phủ giai đoạn 2020–2024, đây là phân tích meta toàn diện nhất về cộng tác ra quyết định người–AI cho đến nay.

Bốn câu hỏi nghiên cứu định hình phân tích. RQ1 hỏi liệu cộng tác người–AI tạo ra hay phá hủy giá trị so với cá nhân có hiệu suất cao nhất (cộng hưởng). RQ2 kiểm tra tính đối xứng: AI hỗ trợ người có tương đương người giám sát AI không? RQ3 đi vào bối cảnh, khảo sát vai trò điều tiết của ngành nghề, loại nhiệm vụ, kiến trúc AI, trình độ chuyên môn, và khả năng giải thích. RQ4 hỏi liệu thâm hụt cộng tác, nếu tồn tại, có đang thu hẹp theo thời gian.

Đóng góp chính của bài viết nằm ở ba điểm. Nó cung cấp bằng chứng liên ngành đầu tiên rằng nghịch lý cộng tác mang tính phổ quát, không phải đặc thù y tế hay khu vực công. Nó xác định ngành nghề là biến điều tiết chủ đạo, với Truyền thông là lĩnh vực duy nhất con người cải thiện AI đáng tin cậy. Và nó ghi nhận thâm hụt cộng tác đang thu hẹp theo thời gian. Trên nền tảng các kết quả đó, bài viết đề xuất một khung phân tích dựa trên lợi thế so sánh và thông tin bất đối xứng, có hàm ý cho cả thiết kế quản trị AI lẫn chính sách con người tham gia vào vòng lặp xử lý.

---

## 2. Cơ sở lý thuyết và giả thuyết

### 2.1 Cộng tác ra quyết định người–AI: bằng chứng thực nghiệm

Truyền thống so sánh phán đoán lâm sàng với phán đoán thống kê có lịch sử hơn nửa thế kỷ. Dawes, Faust, và Meehl (1989) tổng hợp bằng chứng cho thấy mô hình thống kê đơn giản thường vượt trội chuyên gia con người trong nhiều nhiệm vụ dự báo, từ chẩn đoán y tế đến dự đoán tái phạm. Grove và cộng sự (2000) mở rộng kết luận này qua phân tích meta 136 nghiên cứu: trong 63% trường hợp, phán đoán cơ học vượt trội hoặc ngang bằng phán đoán lâm sàng. AI hiện đại nối tiếp truyền thống này với năng lực vượt xa mô hình tuyến tính (Topol, 2019), nhưng cũng đặt ra câu hỏi mới: thay vì chọn giữa người *hoặc* máy, liệu *kết hợp* có cho kết quả tốt hơn?

Niềm tin phổ biến là có. Nhiều tổ chức triển khai cơ chế con người tham gia vào vòng lặp xử lý dựa trên giả định rằng con người bổ sung cho AI những năng lực thuật toán chưa có (Davenport & Ronanki, 2018; Brynjolfsson & McAfee, 2017). Nhưng bằng chứng thực nghiệm phức tạp hơn giả định đó. Bansal và cộng sự (2021) phát hiện rằng giải thích AI không nhất quán cải thiện hiệu suất nhóm, đôi khi còn phản tác dụng khi giải thích không phù hợp nhiệm vụ. Buçinca và cộng sự (2021) cho thấy phụ thuộc quá mức (overreliance) kéo hiệu suất nhóm xuống dưới mức AI độc lập. Green và Chen (2019) ghi nhận rằng thêm con người vào hệ thống AI dự đoán tái phạm không cải thiện độ chính xác mà làm tăng thiên lệch chủng tộc. Dietvorst và cộng sự (2015) mô tả hiện tượng e ngại thuật toán (algorithm aversion): sau khi thấy AI mắc lỗi, người dùng bác bỏ thuật toán ngay cả khi nó vẫn vượt trội năng lực con người. Castelo và cộng sự (2019) cho thấy hiệu ứng này phụ thuộc loại nhiệm vụ: sự e ngại mạnh hơn ở nhiệm vụ chủ quan so với khách quan. Burton và cộng sự (2020) tổng hợp 61 nghiên cứu về e ngại thuật toán, xác định năm nhóm nguyên nhân bao gồm kỳ vọng, quyền tự chủ, và khả năng tương thích nhận thức. Logg và cộng sự (2019) ghi nhận chiều ngược lại, ưa chuộng thuật toán (algorithm appreciation), trong đó người dùng tin tưởng AI quá mức.

Tuy nhiên, phần lớn các nghiên cứu trên xem xét từng hiện tượng riêng lẻ (phụ thuộc quá mức, e ngại thuật toán, giải thích AI) mà chưa có tổng hợp định lượng hệ thống qua nhiều ngành. Khoảng trống này đặt ra nhu cầu một phân tích meta liên ngành, cho phép ước lượng quy mô hiệu ứng cộng tác tổng thể, xác định biến điều tiết, và kiểm tra tính khái quát trên nhiều bối cảnh ra quyết định.

### 2.2 Khung lý thuyết

Chúng tôi tiếp cận cộng tác người–AI như một *hệ thống nhận thức chung*, trong đó con người và thuật toán phối hợp tạo thành một tác nhân ra quyết định duy nhất (Licklider, 1960; Jarrahi, 2018). Khi phân công phù hợp, AI đảm nhiệm xử lý và đề xuất dựa trên dữ liệu, còn con người giữ quyền kiểm soát, bối cảnh hóa, và chịu trách nhiệm giải trình. Tuy nhiên, cùng một cấu trúc cũng có thể tạo ra nghịch lý cộng hưởng khi hai bên cạnh tranh trên cùng một chiều năng lực hoặc khi bất đối xứng thông tin khiến con người không hiệu chuẩn được mức tin tưởng. Trên nền tảng đó, chúng tôi xây dựng khung giải thích dựa trên ba trụ cột lý thuyết.

**Thông tin bất đối xứng và chi phí giám sát.** Akerlof (1970) đã mô hình hóa tình huống một bên giao dịch thiếu thông tin để đánh giá chất lượng sản phẩm, dẫn đến lựa chọn ngược. Alchian và Demsetz (1972) mở rộng logic này sang bối cảnh tổ chức: giám sát chỉ tạo giá trị khi chi phí giám sát thấp hơn lợi ích phát hiện sai lệch, nghĩa là người giám sát cần đủ thông tin phân biệt đầu ra đúng và sai. Parasuraman và Riley (1997) đã ghi nhận hệ quả hành vi trong tự động hóa: khi con người không hiểu cơ chế nội bộ của hệ thống, họ rơi vào thiên lệch tự động hóa (automation bias), tức phụ thuộc quá mức vào hệ thống, hoặc từ chối sử dụng (disuse), tức bác bỏ thiếu căn cứ. Trong bối cảnh cộng tác người–AI, quy trình ra quyết định nội bộ của AI hầu như không quan sát được, tạo ra điều kiện cho cả hai dạng sai lệch. Trụ cột này dự đoán rằng con người ở vai trò giám sát AI sẽ gặp khó khăn hệ thống.

**Mô hình người phán đoán–người tư vấn (judge-advisor).** Sniezek và Buckley (1995) mô tả cấu trúc ra quyết định trong đó người phán đoán nhận tư vấn từ nguồn bên ngoài rồi đưa ra phán đoán cuối cùng. Người phán đoán hưởng lợi từ thông tin bổ sung mà không cần hiểu toàn bộ cơ chế tạo ra thông tin đó. Cấu trúc này tương tự cách con người sử dụng gợi ý AI ở vai trò người nhận hỗ trợ: họ giữ quyền kiểm soát, lọc gợi ý qua kinh nghiệm, và quyết định trong khung phán đoán vốn có. Trụ cột này dự đoán rằng AI ở vai trò người tư vấn sẽ nhất quán có ích, bất kể bối cảnh, vì cấu trúc thông tin của mối quan hệ người phán đoán–người tư vấn không thay đổi.

**Lợi thế so sánh.** Ricardo (1817) chứng minh rằng trao đổi mang lại lợi ích khi mỗi bên chuyên môn hóa vào lĩnh vực mình sở hữu lợi thế so sánh. Áp dụng vào cộng tác người–AI, giá trị gia tăng chỉ xuất hiện khi năng lực hai bên thực sự bổ trợ trên các khía cạnh khác nhau của nhiệm vụ. Khi AI đã vượt trội ở hầu hết các khía cạnh (nhiệm vụ phân loại, dự báo), phạm vi bổ trợ hẹp và cộng tác khó tạo thêm giá trị. Khi nhiệm vụ đòi hỏi năng lực đa dạng (sáng tạo, hiểu bối cảnh văn hóa), mỗi bên sở hữu một phần và tiềm năng cộng hưởng lớn. Trụ cột này dự đoán rằng loại nhiệm vụ và ngành nghề sẽ điều tiết mạnh hiệu ứng cộng tác.

Cuối cùng, hiệu suất cộng tác không nhất thiết tĩnh. Các can thiệp thiết kế nhằm buộc người dùng suy nghĩ, cung cấp giải thích, hoặc cho phép điều chỉnh khuyến nghị đã được chứng minh là có thể làm giảm phụ thuộc quá mức và thay đổi hiệu suất nhóm (Dietvorst và cs., 2018; Buçinca và cs., 2021; Bansal và cs., 2021). Điều này gợi ý rằng thâm hụt cộng hưởng có thể thu hẹp theo thời gian khi giao thức cộng tác và năng lực hiệu chuẩn của người dùng cùng trưởng thành, tạo cơ sở cho giả thuyết H4.

### 2.3 Giả thuyết

Từ khung lý thuyết trên và bằng chứng thực nghiệm hiện có, chúng tôi đặt bốn giả thuyết:

**H1 (Nghịch lý cộng hưởng).** Nhóm người–AI hoạt động kém hơn có ý nghĩa so với thành viên có hiệu suất cao nhất trên cả bốn ngành.

**H2 (Tăng cường bất đối xứng).** AI cải thiện đáng kể hiệu suất con người, nhưng con người không cải thiện có ý nghĩa hiệu suất AI. Mô hình người phán đoán–người tư vấn dự đoán hiệu ứng AI hỗ trợ người nhất quán dương; bất đối xứng thông tin dự đoán hiệu ứng người hỗ trợ AI yếu hoặc âm.

**H3 (Phụ thuộc bối cảnh).** Ngành nghề, loại nhiệm vụ, kiến trúc AI, trình độ chuyên môn, và khả năng giải thích điều tiết các hiệu ứng. Cụ thể, dựa trên nguyên lý lợi thế so sánh, cộng tác hiệu quả hơn ở nhiệm vụ sáng tạo (phạm vi bổ trợ rộng) so với nhiệm vụ quyết định, và ở bối cảnh giảm bất đối xứng thông tin (AI có giải thích, người tham gia là chuyên gia).

**H4 (Xu hướng cải thiện).** Thâm hụt cộng hưởng thu hẹp theo thời gian, phản ánh sự trưởng thành của cả công nghệ AI lẫn thiết kế giao diện cộng tác.

---

## 3. Phương pháp nghiên cứu

### 3.1 Chiến lược tìm kiếm và tiêu chí chọn mẫu

Chúng tôi tìm kiếm trên ACM Digital Library và Web of Science, kết hợp truy vết trích dẫn ngược và xuôi (backward/forward citations) để thu thập các nghiên cứu thực nghiệm về cộng tác ra quyết định người–AI công bố bằng tiếng Anh từ tháng 1/2020 đến tháng 12/2024, trên bốn ngành: Y tế, Kinh doanh, Truyền thông, và Khu vực công.

Tiêu chí đưa vào yêu cầu: (1) thiết kế thực nghiệm có kiểm soát; (2) có đầy đủ ba điều kiện: con người độc lập, AI độc lập, và cộng tác người–AI; (3) báo cáo đủ thống kê để tính kích thước hiệu ứng; (4) mô tả rõ ràng về người tham gia, nhiệm vụ, và hệ thống AI. Chúng tôi loại trừ các thiết kế quan sát, mô phỏng không có điều kiện cộng tác, và các nghiên cứu thiếu dữ liệu cần thiết.

Quá trình tìm kiếm thu được **67 nghiên cứu** thỏa mãn tiêu chí, đóng góp **278 kích thước hiệu ứng** từ **90 thí nghiệm riêng biệt**.

### 3.2 Trích xuất dữ liệu

Mỗi nghiên cứu được mã hóa trên **65 biến** bao gồm đặc điểm nghiên cứu, đặc điểm nhiệm vụ, thuộc tính hệ thống AI, thuộc tính người tham gia, và kết quả hiệu suất. Các biến mã hóa chính bao gồm:

- **Ngành**: Y tế, Kinh doanh, Truyền thông, hoặc Khu vực công
- **Loại nhiệm vụ**: Ra quyết định (*Decide*) hoặc sáng tạo/sinh tạo (*Create*)
- **Kiến trúc AI**: Học sâu (Deep Learning), ML truyền thống (Shallow Learning), hệ thống dựa trên luật, Phù thủy Oz (Wizard of Oz), hoặc AI mô phỏng (Simulated-AI)
- **Trình độ người tham gia**: Chuyên gia (chuyên viên trong lĩnh vực) hoặc Không chuyên (người lao động cộng đồng trực tuyến — crowdworker, sinh viên)
- **Khả năng giải thích của AI**: AI có cung cấp giải thích cho các khuyến nghị hay không
- **Điểm tin cậy AI**: AI có cung cấp điểm tin cậy (confidence score) hay không
- **Năm công bố**: 2020–2024

Với mỗi thí nghiệm, chúng tôi trích xuất thống kê hiệu suất cho ba điều kiện (nếu có): con người độc lập, AI độc lập, và nhóm người–AI. Khi nghiên cứu báo cáo nhiều thước đo kết quả hoặc nhiều điều kiện thí nghiệm, mỗi quan sát được xử lý như một kích thước hiệu ứng riêng biệt, phù hợp với thông lệ phân tích meta chuẩn.

### 3.3 Tính toán kích thước hiệu ứng (effect size)

Chúng tôi sử dụng Hedges' *g* làm thước đo kích thước hiệu ứng chính, vì chỉ số này hiệu chỉnh thiên lệch mẫu nhỏ vốn có trong Cohen's *d*. Ba phép so sánh cặp được tính cho mỗi thí nghiệm:

1. **Cộng hưởng mạnh** (*g_s*): Nhóm người–AI so với cá nhân có hiệu suất cao hơn (max giữa con người độc lập và AI độc lập). Giá trị dương cho thấy nhóm vượt trội hơn thành viên có hiệu suất cao nhất; giá trị âm cho thấy cộng tác phá hủy giá trị.

2. **AI hỗ trợ người** (*g_h*): Nhóm người–AI so với con người độc lập. Giá trị dương cho thấy AI cải thiện hiệu suất con người.

3. **Người hỗ trợ AI** (*g_a*): Nhóm người–AI so với AI độc lập. Giá trị dương cho thấy con người cải thiện hiệu suất AI.

Kích thước hiệu ứng được tính theo quy trình chuẩn (Borenstein và cs., 2009). Với mẫu độc lập:

$$d = \frac{\bar{X}_1 - \bar{X}_2}{S_p}, \quad S_p = \sqrt{\frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2}}$$

trong đó $\bar{X}_1$, $\bar{X}_2$ là trung bình nhóm và $S_p$ là độ lệch chuẩn gộp. Hiệu chỉnh thiên lệch mẫu nhỏ cho Hedges' *g*:

$$g = J \cdot d, \quad J = 1 - \frac{3}{4(n_1 + n_2 - 2) - 1}$$

Phương sai lấy mẫu của *g*:

$$v_i = \frac{n_1 + n_2}{n_1 n_2} + \frac{g_i^2}{2(n_1 + n_2)}$$

Với thiết kế trong cùng đối tượng (within-subjects), phương sai được điều chỉnh theo tương quan giữa các điều kiện $r$:

$$v_i^{(\text{dep})} = \frac{2(1 - r)}{n} + \frac{g_i^2}{2n}$$

Chiều hướng của tất cả thước đo hiệu suất được chuẩn hóa sao cho giá trị dương luôn biểu thị hiệu suất tốt hơn.

### 3.4 Khung phân tích

Trong bộ dữ liệu này, một bài báo thường đóng góp nhiều kích thước hiệu ứng từ nhiều thí nghiệm, điều kiện, hoặc thước đo. Các quan sát trong cùng một bài báo vì vậy có xu hướng tương quan; nếu coi chúng là độc lập như trong mô hình một bậc, sai số chuẩn thường bị đánh giá thấp và khoảng tin cậy trở nên quá hẹp. Để phản ánh đúng cấu trúc lồng nhau của dữ liệu và tận dụng toàn bộ bằng chứng mà không cần gộp thủ công các kết quả, chúng tôi sử dụng mô hình hiệu ứng ngẫu nhiên ba bậc (three-level random-effects model). Mô hình phân tách biến thiên của hiệu ứng thành: sai số lấy mẫu ở cấp kích thước hiệu ứng (level 1), khác biệt giữa các thí nghiệm/đo lường trong cùng bài báo (level 2), và khác biệt giữa các bài báo (level 3). Hai thành phần phương sai ngẫu nhiên (level 2 và level 3) được ước lượng bằng Restricted Maximum Likelihood (REML). Trong triển khai, chúng tôi ước lượng mô hình trong R bằng REML với hệ số chặn (intercept) ngẫu nhiên ở cấp bài báo (Paper_ID) và thí nghiệm lồng trong bài báo (Exp_ID) (Viechtbauer, 2010). Ước lượng tổng hợp:

$$\hat{g} = \frac{\sum_{i=1}^{k} w_i g_i}{\sum_{i=1}^{k} w_i}, \quad w_i = \frac{1}{v_i + \hat{\sigma}^2_{\text{within}} + \hat{\sigma}^2_{\text{between}}}$$

trong đó $w_i$ là trọng số nghịch đảo phương sai, $v_i$ là phương sai lấy mẫu của kích thước hiệu ứng *i*, và $\hat{\sigma}^2_{\text{within}}$, $\hat{\sigma}^2_{\text{between}}$ lần lượt là phương sai ngẫu nhiên giữa các thí nghiệm trong cùng bài báo và giữa các bài báo (ước lượng bằng REML). Tổng phương sai ngẫu nhiên $\hat{\tau}^2 = \hat{\sigma}^2_{\text{within}} + \hat{\sigma}^2_{\text{between}}$ phản ánh mức biến thiên thực sự ngoài sai số lấy mẫu. Việc đánh giá **dị biệt** là cần thiết vì một ước lượng trung bình có thể che giấu các bối cảnh mà cộng tác mang lại lợi ích hoặc gây tổn thất; khi dị biệt cao, mức độ khái quát của kết luận phụ thuộc nhiều vào khoảng dự đoán và phân tích biến điều tiết hơn là riêng giá trị trung bình. Chúng tôi kiểm định liệu biến thiên quan sát được có vượt quá mức kỳ vọng từ sai số lấy mẫu hay không bằng thống kê *Q* của Cochran. Nếu *Q* có ý nghĩa, dị biệt thực sự tồn tại và cần được mô hình hóa qua các biến điều tiết. Mức dị biệt được lượng hóa qua chỉ số $I^2$ (Higgins và cs., 2003):

$$I^2 = \max\!\left(0,\; \frac{Q - (k-1)}{Q}\right) \times 100\%$$

Với mỗi phép so sánh, chúng tôi ước lượng kích thước hiệu ứng tổng hợp ($\hat{g}$) với khoảng tin cậy 95%, các thống kê dị biệt ($\hat{\tau}^2$, $I^2$, và kiểm định *Q* của Cochran), cùng khoảng dự đoán phản ánh phạm vi mà 95% hiệu ứng thực sự dự kiến rơi vào.

Để xác định nguồn dị biệt, chúng tôi thực hiện phân tích nhóm con: ước lượng hiệu ứng ngẫu nhiên DerSimonian-Laird (DerSimonian & Laird, 1986) riêng cho từng mức của biến điều tiết, rồi so sánh bằng thống kê *Q*-between ($Q_{\text{between}} = Q_{\text{total}} - Q_{\text{within}}$, phân phối $\chi^2$) để kiểm định liệu biến điều tiết có giải thích dị biệt một cách có ý nghĩa hay không. Sáu biến điều tiết được khảo sát: Ngành, Loại nhiệm vụ, Loại AI, Trình độ chuyên môn, Khả năng giải thích AI, và Năm công bố. Bổ sung cho phân tích nhóm con, chúng tôi thực hiện **hồi quy meta** (meta-regression) đa biến bằng mô hình ba bậc REML (cùng cấu trúc ngẫu nhiên như phân tích chính), đưa đồng thời tất cả sáu biến điều tiết làm biến dự báo cố định, cho phép ước lượng hiệu ứng riêng của từng biến sau khi kiểm soát các biến còn lại. Thiên lệch xuất bản được đánh giá qua bốn kiểm định bổ trợ: kiểm định hồi quy Egger (Egger và cs., 1997) về bất đối xứng biểu đồ phễu (funnel plot), kiểm định tương quan hạng Begg (Begg & Mazumdar, 1994), phương pháp cắt và lấp (trim-and-fill) của Duval và Tweedie (2000), và chỉ số an toàn N (fail-safe N) của Rosenthal (1979).

**Bảng 1. Đặc điểm bộ dữ liệu**

| Đặc điểm | Phân loại | *k* | Số bài báo |
|---|---|---|---|
| **Ngành** | Y tế | 107 | 33 |
| | Truyền thông | 86 | 16 |
| | Kinh doanh | 46 | 12 |
| | Khu vực công | 39 | 10 |
| **Loại nhiệm vụ** | Quyết định | 252 | — |
| | Sáng tạo | 26 | — |
| **Kiến trúc AI** | Học sâu | 132 | — |
| | Dựa trên quy luật | 52 | — |
| | ML truyền thống | 46 | — |
| | Phù thủy Oz | 36 | — |
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

*Ghi chú.* *k* = số kích thước hiệu ứng. Kiến trúc AI: Học sâu = Deep Learning; Dựa trên quy luật = Rule-Based; ML truyền thống = Shallow Learning; Phù thủy Oz = Wizard of Oz (phương pháp thí nghiệm trong đó người vận hành điều khiển ngầm hệ thống, mô phỏng AI thực); AI mô phỏng = Simulated-AI. Cột "Số bài báo" chỉ báo cáo cho Ngành và Năm công bố — các phân loại mà mỗi bài báo chỉ thuộc một nhóm. Đối với các đặc điểm khác, một bài báo có thể đóng góp kích thước hiệu ứng vào nhiều nhóm con (ví dụ: một nghiên cứu có thể bao gồm cả điều kiện có và không có giải thích AI). Tổng số bài báo theo ngành (71) vượt 67 vì bốn bài báo thực hiện thí nghiệm trên nhiều hơn một ngành.

---

## 4. Kết quả nghiên cứu

### 4.1 Hiệu ứng tổng hợp

Ba phép so sánh phản ánh ba góc độ đánh giá cộng tác. *Cộng hưởng* so sánh hiệu suất nhóm người–AI với cá nhân có hiệu suất cao nhất (con người hoặc AI, tùy bên nào cao hơn): giá trị dương nghĩa là cộng tác tạo thêm giá trị vượt xa cả hai bên; giá trị âm nghĩa là nhóm tệ hơn cả bên mạnh nhất. *AI hỗ trợ người* so sánh nhóm người–AI với con người làm việc một mình, đo lường mức cải thiện khi con người có AI bên cạnh như công cụ hỗ trợ. *Người hỗ trợ AI* so sánh chiều ngược lại—nhóm người–AI với AI hoạt động một mình—đo lường liệu sự tham gia của con người có nâng hiệu suất AI hay không, tức giá trị thực sự của cơ chế giám sát có con người tham gia vào vòng lặp xử lý.

Kết quả tổng hợp từ mô hình ba bậc REML trên toàn bộ 278 kích thước hiệu ứng được trình bày trong Bảng 2.

**Bảng 2. Kết quả phân tích meta tổng hợp (Mô hình ba bậc REML)**

| So sánh | *k* | *g* | KTC 95% | *p* | τ² | I² (%) | Khoảng dự đoán |
|---|---|---|---|---|---|---|---|
| Cộng hưởng (Synergy) | 278 | −0.529 | [−0.659, −0.399] | < .001 | 1.145 | 98.41 | [−2.631, 1.572] |
| AI hỗ trợ người (Human Aug) | 278 | +0.494 | [+0.433, +0.554] | < .001 | 0.203 | 90.36 | [−0.392, 1.380] |
| Người hỗ trợ AI (AI Aug) | 278 | +0.145 | [−0.042, +0.332] | .128 | 2.431 | 99.28 | [−2.916, 3.207] |

*Ghi chú.* Synergy = Cộng hưởng; Human Aug = AI hỗ trợ người (Human Augmentation); AI Aug = Người hỗ trợ AI (AI Augmentation).

Hiệu ứng cộng hưởng tổng hợp đạt *g* = −0,529 (KTC 95% [−0,659, −0,399], *p* < 0,001): nhóm người–AI hoạt động kém hơn khoảng nửa độ lệch chuẩn so với cá nhân có hiệu suất cao nhất. Đây là hiệu ứng ở mức trung bình-lớn theo chuẩn Cohen, và không phải hiện tượng biên: 175 trong 278 kích thước hiệu ứng (63%) mang giá trị âm.

Nhưng con số tổng hợp che giấu một cấu trúc bất đối xứng. AI ở vai trò hỗ trợ con người tạo ra hiệu ứng tăng cường rõ ràng (*g* = +0,494, *p* < 0,001), trong khi con người ở vai trò giám sát AI chỉ đạt *g* = +0,145 (*p* = 0,128), không có ý nghĩa thống kê. Sự giám sát của con người, cơ chế mà nhiều khung quản trị AI coi là điều kiện bắt buộc, gần như không tạo ra khác biệt đo lường được. Cấu trúc bất đối xứng này sẽ lặp lại nhất quán qua cả phân tích nhóm con lẫn hồi quy meta.

Cả ba phép so sánh đều cho thấy mức dị biệt cực đoan (I² = 90–99%). Khoảng dự đoán cho cộng hưởng trải rộng, từ −2,631 đến +1,572. Bên cạnh xu hướng trung bình tiêu cực, vẫn tồn tại những bối cảnh cộng tác tạo ra giá trị thực sự. Câu hỏi tiếp theo là: bối cảnh nào?

![Hình 1. Tổng quan phân phối kích thước hiệu ứng và biểu đồ rừng (forest plot) tổng hợp](Experiment/outputs/figures/Figure1_Overview.png)

*Hình 1.* Phân phối Hedges' *g* cho 278 kích thước hiệu ứng theo từng loại so sánh (hàng trên) và biểu đồ rừng hiệu ứng ngẫu nhiên tổng hợp (hàng dưới). Biểu đồ tần suất (histogram) cho thấy sự tập trung của hiệu ứng cộng hưởng ở vùng âm, sự nhất quán dương của hiệu ứng AI hỗ trợ người, và mức phân tán lớn của hiệu ứng người hỗ trợ AI.

### 4.2 Phân tích biến điều tiết

Mức dị biệt cực cao (I² > 90%) đặt ra câu hỏi liệu hiệu ứng cộng tác có đồng nhất hay thay đổi tùy bối cảnh. Bảng 3 trình bày kết quả phân tích nhóm con theo sáu biến điều tiết.

**Bảng 3. Phân tích nhóm con theo biến điều tiết**

| Biến điều tiết | Mức | *k* | Cộng hưởng *g* | AI hỗ trợ người *g* | Người hỗ trợ AI *g* |
|---|---|---|---|---|---|
| **Loại nhiệm vụ** | Quyết định | 252 | −0.619*** | +0.496*** | +0.043 (ns) |
| | Sáng tạo | 26 | +0.372 (ns) | +0.467*** | +1.114*** |
| | *Q*-between *p* | | < .001 | .047 | < .001 |
| **Kiến trúc AI** | Học sâu | 132 | −0.204* | +0.396*** | +0.920*** |
| | Dựa trên quy luật | 52 | −1.247*** | +0.559*** | −0.876*** |
| | ML truyền thống | 46 | −0.506*** | +0.443*** | −0.362* |
| | AI mô phỏng | 12 | −1.290*** | +0.673*** | −1.272*** |
| | Phù thủy Oz | 36 | −0.435** | +0.734*** | −0.144 (ns) |
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

Kiến trúc AI cho mô hình tương tự nhưng cơ chế khác. Học sâu, thường linh hoạt hơn song dễ mắc lỗi trên trường hợp biên, có thâm hụt cộng hưởng nhỏ nhất (*g* = −0,204) và là loại AI duy nhất mà con người cải thiện có ý nghĩa (*g* = +0,920, *p* < 0,001). Hệ thống dựa trên quy luật và AI mô phỏng, vốn hoạt động theo logic cố định trên phạm vi hẹp, chịu thâm hụt sâu nhất (lần lượt *g* = −1,247 và −1,290). Khi AI đã được tối ưu hóa cho miền nhiệm vụ cụ thể, can thiệp con người có xu hướng đưa thêm nhiễu.

Trình độ chuyên môn kiểm soát mức độ tổn thất. Chuyên gia mất ít hơn khi cộng tác (*g* = −0,278 so với −0,648 cho người không chuyên) và hưởng lợi nhiều hơn từ AI (*g* = +0,595 so với +0,456). Chuyên gia có kiến thức nền để nhận diện khi nào gợi ý AI đáng tin; người không chuyên thiếu cơ sở phân biệt, dao động giữa phụ thuộc quá mức và bác bỏ thiếu căn cứ.

Khả năng giải thích AI có vai trò chọn lọc. Giải thích làm giảm thâm hụt cộng hưởng (từ *g* = −0,611 xuống −0,471, *Q*-between *p* < 0,001) nhưng không ảnh hưởng đến hiệu ứng AI hỗ trợ người (*p* = 0,615). Sự phân biệt này hợp lý nếu xét cấu trúc tương tác: ở vai trò giám sát, con người cần đánh giá đầu ra AI nên giải thích hữu ích; ở vai trò người nhận hỗ trợ, họ chỉ cần biết gợi ý chứ không cần hiểu tại sao.

Chiều thời gian cho thấy xu hướng khích lệ. Thâm hụt cộng hưởng giảm dần từ *g* = −0,835 (2020) qua −0,558 (2021) và −0,634 (2022), rồi tiến đến *g* = +0,013 (ns) vào năm 2023, lần đầu ước lượng tổng hợp vượt ngưỡng zero. Song song, AI hỗ trợ người tăng từ +0,404 (2020) lên +0,757 (2023). Tổn thất giảm, lợi ích tăng. Sự cải thiện kép này phù hợp với sự trưởng thành dần của công nghệ AI và thiết kế giao diện cộng tác, dù ước lượng năm 2024 (*g* = −0,665, *k* = 4) dựa trên mẫu quá nhỏ để diễn giải.

![Hình 2. Kích thước hiệu ứng theo nhóm con](Experiment/outputs/figures/FigureS5_Moderator_Bars.png)

*Hình 2.* Kích thước hiệu ứng theo nhóm con cho sáu biến điều tiết (hàng) qua ba phép so sánh (cột). Thanh đỏ: hiệu ứng âm; thanh xanh: hiệu ứng dương; đường lỗi: khoảng tin cậy 95%. Sự phân hóa rõ nhất xuất hiện theo loại nhiệm vụ, kiến trúc AI, và ngành. Truyền thông là ngành duy nhất có hiệu ứng dương ở phép so sánh người hỗ trợ AI.

![Hình 3. Xu hướng hiệu ứng cộng tác người–AI theo năm](Experiment/outputs/figures/FigureS1_Temporal_Trend.png)

*Hình 3.* Biến động ước lượng tổng hợp theo năm công bố (2020–2024) cho ba phép so sánh. Ba đường hiệu ứng hội tụ dần, với năm 2023 đánh dấu lần đầu tiên cộng hưởng vượt ngưỡng zero—gợi ý rằng nghịch lý cộng tác không cố định mà đang thu hẹp cùng sự trưởng thành của công nghệ và thiết kế giao diện.

![Hình 4. Heatmap tổng hợp hiệu ứng theo biến điều tiết](Experiment/outputs/figures/FigureS4_Summary_Heatmap.png)

*Hình 4.* Heatmap tổng hợp kích thước hiệu ứng theo tất cả các mức biến điều tiết và ba phép so sánh. Hai cụm bối cảnh phân biệt rõ: cộng tác hiệu quả (Sáng tạo, Truyền thông, Học sâu—vùng đỏ đậm ở cột Người hỗ trợ AI) và cộng tác phản tác dụng (Quyết định, Kinh doanh, Dựa trên quy luật—vùng xanh đậm ở cột Cộng hưởng). Bức tranh tổng thể phù hợp với khung lợi thế so sánh: giá trị cộng tác phụ thuộc vào phạm vi năng lực bổ trợ giữa người và AI.

Các phân tích nhóm con trên khảo sát từng biến điều tiết độc lập. Nhưng một biến có thể tương quan với biến khác (ví dụ: nhiệm vụ sáng tạo tập trung ở Truyền thông), khiến hiệu ứng riêng rẽ khó tách bạch. Hồi quy meta đa biến bằng mô hình 3 bậc REML cho phép kiểm tra liệu các mô hình trên có duy trì khi kiểm soát đồng thời tất cả sáu biến (Bảng 4).

**Bảng 4. Hồi quy meta đa biến (mô hình 3 bậc REML)**

| Biến dự báo | Cộng hưởng β | AI hỗ trợ người β | Người hỗ trợ AI β |
|---|---|---|---|
| Hệ số chặn | −0,533 | +0,693*** | −0,519 |
| *Ngành* (ref: Y tế) | | | |
|   Kinh doanh | −0,836* | −0,211 | −0,679 |
|   Truyền thông | −0,551 | −0,359 | +0,596 |
|   Khu vực công | +0,037 | −0,237 | +0,559 |
| *Loại nhiệm vụ* (ref: Quyết định) | | | |
|   Sáng tạo | +1,235* | −0,086 | +0,956 |
| *Kiến trúc AI* (ref: Học sâu) | | | |
|   Dựa trên quy luật | +1,442*** | +0,159 | +1,493*** |
|   ML truyền thống | −0,219 | +0,002 | −0,057 |
|   AI mô phỏng | +0,687 | +0,134 | +1,204 |
|   Phù thủy Oz | −0,229 | +0,146 | +0,455 |
| *Trình độ* (ref: Không chuyên) | | | |
|   Chuyên gia | +0,166 | −0,037 | +0,121 |
| *Giải thích AI* (ref: Không) | | | |
|   Có | +0,058 | +0,004 | +0,009 |
| Năm (tâm = 2022) | +0,145 | +0,005 | −0,012 |
| | | | |
| *QM* (df = 11) | 26,58*** | 0,88 (ns) | 32,86*** |
| *τ²* phần dư | 1,088 | 0,239 | 3,291 |

*Ghi chú.* \* *p* < .05, \*\*\* *p* < .001. Hệ số chặn (Intercept) = ước lượng hiệu ứng khi tất cả biến dự báo ở danh mục tham chiếu. QM = kiểm định Wald tổng thể (omnibus) cho toàn bộ biến điều tiết. τ² phần dư (residual) = phương sai giữa các nghiên cứu còn lại sau khi kiểm soát biến dự báo. ref = danh mục tham chiếu (reference category). Mô hình sử dụng cấu trúc ngẫu nhiên 3 bậc với ước lượng REML.

Kết quả phân hóa rõ rệt giữa ba phép so sánh. Với cộng hưởng, kiểm định tổng thể đạt ý nghĩa cao (QM = 26,58, *p* < 0,001). Hai biến dự báo nổi bật: ngành Kinh doanh chịu thâm hụt lớn hơn Y tế 0,84 SD (β = −0,836, *p* = 0,023), và nhiệm vụ sáng tạo có lợi thế 1,24 SD so với nhiệm vụ quyết định (β = +1,235, *p* = 0,011). Với người hỗ trợ AI, kiểm định tổng thể cũng đạt ý nghĩa (QM = 32,86, *p* < 0,001), chủ yếu nhờ kiến trúc AI.

Đáng chú ý nhất là phép so sánh AI hỗ trợ người: không có biến dự báo nào đạt ý nghĩa (QM = 0,88, *p* = 0,559). Hiệu ứng AI cải thiện con người bền vững qua mọi ngành, mọi loại nhiệm vụ, mọi kiến trúc AI, mọi trình độ người dùng. Sáu biến điều tiết không thu hẹp được mức phân tán giữa các nghiên cứu (τ² phần dư = 1,09–3,29), xác nhận rằng dị biệt xuất phát từ những yếu tố ngoài các biến đã mã hóa.

![Hình 5. Hệ số hồi quy meta đa biến](Experiment/outputs/figures/Figure5_MetaRegression_Coefficients.png)

*Hình 5.* Hệ số hồi quy meta đa biến (β ± KTC 95%) cho 11 biến dự báo qua ba phép so sánh. Điểm tròn đặc: hệ số có ý nghĩa thống kê (*p* < .05); điểm tròn rỗng: không có ý nghĩa. Đường dọc tại 0 đánh dấu ngưỡng không có hiệu ứng. Phần B (AI hỗ trợ người) không có biến nào đạt ý nghĩa (QM = 0,88, ns), xác nhận hiệu ứng AI cải thiện con người bền vững qua mọi bối cảnh.

### 4.3 Phân tích độ nhạy

Để kiểm tra tính ổn định của các ước lượng, chúng tôi thực hiện phân tích loại từng nghiên cứu (leave-one-out) cho cả ba phép so sánh, lần lượt loại bỏ từng nghiên cứu và tính lại ước lượng tổng hợp. Kết quả cho thấy không có nghiên cứu đơn lẻ nào chi phối ước lượng: cộng hưởng dao động trong khoảng [−0.549, −0.517], AI hỗ trợ người trong [+0.486, +0.498], và người hỗ trợ AI trong [+0.083, +0.160]. Hướng, độ lớn, và ý nghĩa thống kê của các hiệu ứng không thay đổi qua tất cả các lần lặp.

Phân tích meta tích lũy theo thứ tự thời gian cho thấy cả ba ước lượng hội tụ và ổn định sau khoảng 150 kích thước hiệu ứng, xác nhận rằng cơ sở bằng chứng hiện tại đủ lớn cho suy luận đáng tin cậy.

---

## 5. Thảo luận

### 5.1 Bất đối xứng thông tin và bài toán giám sát

Tại sao AI cải thiện con người nhưng con người không cải thiện AI? Câu trả lời nằm ở cấu trúc thông tin, không phải năng lực tuyệt đối.

Khi AI đóng vai trò công cụ hỗ trợ, con người giữ quyền kiểm soát, lọc gợi ý AI qua kinh nghiệm rồi quyết định trong khung phán đoán vốn có—tương tự mô hình người phán đoán–người tư vấn (Sniezek & Buckley, 1995). Hồi quy meta xác nhận: không biến điều tiết nào giải thích hiệu ứng AI hỗ trợ người (QM = 0,88, ns). Ngành, nhiệm vụ, kiến trúc AI thay đổi, nhưng cấu trúc người phán đoán–người tư vấn thì không.

Chiều ngược lại khác hẳn. Khi giám sát AI, con người phải đánh giá đầu ra của hệ thống mà quy trình nội bộ hầu như không quan sát được—bài toán thông tin bất đối xứng kinh điển (Akerlof, 1970). Giám sát chỉ tạo giá trị khi chi phí thấp hơn lợi ích phát hiện sai lệch (Alchian & Demsetz, 1972); điều kiện này khó đáp ứng với AI. Hệ quả hành vi đã được ghi nhận: thiên lệch tự động hóa và e ngại thuật toán (Parasuraman & Manzey, 2010; Dietvorst và cs., 2015; Logg và cs., 2019) đều xuất phát từ việc con người thiếu cơ sở hiệu chuẩn mức tin tưởng. Trong 69% trường hợp ở bộ dữ liệu này, AI vượt trội con người ở đường cơ sở, và sự can thiệp nhất quán làm giảm hiệu suất.

### 5.2 Lợi thế so sánh và ranh giới bổ trợ

Nguyên lý lợi thế so sánh (Ricardo, 1817) giải thích khi nào cộng tác thành công: khi năng lực hai bên bổ khuyết trên các khía cạnh khác nhau. Ở nhiệm vụ phân loại và dự báo, AI đã đạt hoặc vượt năng lực con người nên phạm vi bổ trợ hẹp (*g* = +0,043, ns cho người hỗ trợ AI). Ở nhiệm vụ sáng tạo, hai bộ năng lực giao nhau tối thiểu—AI mạnh về nhận diện mẫu, con người mạnh về phán đoán thẩm mỹ và bối cảnh hóa—tạo hiệu ứng bổ trợ lớn (*g* = +1,114, *p* < 0,001). Hồi quy meta xác nhận lợi thế này sau kiểm soát đồng thời (β = +1,235, *p* = 0,011).

Sự phân hóa ngành tuân theo logic tương tự. Truyền thông đòi hỏi hiểu bối cảnh văn hóa, sắc thái ngôn ngữ—năng lực AI chưa đủ—nên con người cải thiện AI rõ rệt (*g* = +1,011). Kinh doanh bao gồm chủ yếu nhiệm vụ dự báo đã được AI xử lý tốt, nên can thiệp con người tạo thêm nhiễu (β = −0,836, *p* = 0,023). Chuyên gia chịu tổn thất cộng hưởng nhỏ hơn (*g* = −0,278 so với −0,648), có lẽ nhờ tri thức ngầm cho phép nhận ra khi nào AI sai (Tschandl và cs., 2020), dù hiệu ứng này không duy trì sau kiểm soát (β = +0,166, ns).

### 5.3 Thiết kế thông tin và xu hướng thời gian

Khả năng giải thích AI giảm thâm hụt cộng hưởng (*Q*-between *p* < .001) nhưng không ảnh hưởng hiệu ứng AI hỗ trợ người (*p* = 0,615)—giải thích giúp ở vai trò giám sát nhưng không cần thiết ở vai trò nhận hỗ trợ, phù hợp với Bansal và cộng sự (2021). Thâm hụt cộng hưởng thu hẹp từ *g* = −0,835 (2020) xuống gần zero (2023), đồng thời AI hỗ trợ người tăng từ +0,404 lên +0,757, gợi ý rằng nghịch lý này không cố định mà đang cải thiện cùng sự trưởng thành của công nghệ và thiết kế giao diện. Dữ liệu năm 2024 (*k* = 4) quá ít để khẳng định xu hướng.

Về thiên lệch xuất bản, kiểm định Egger và Begg đều phát hiện bất đối xứng có ý nghĩa ở cả ba phép so sánh, và ước lượng cắt và lấp dịch chuyển theo hướng tiêu cực hơn. Tuy nhiên, chỉ số an toàn N rất cao (376.476 cho cộng hưởng), cho thấy các kết luận cốt lõi đủ vững trước thiên lệch.

### 5.4 Hàm ý cho thiết kế tổ chức và chính sách

Giá trị của cơ chế con người tham gia vào vòng lặp xử lý phụ thuộc vào ba yếu tố: lợi thế so sánh giữa người và AI trong nhiệm vụ cụ thể, mức bất đối xứng thông tin trong giao diện, và năng lực hiệu chuẩn của người giám sát. Đối với tổ chức, điều này đòi hỏi chuyển từ giả định "thêm con người luôn tốt hơn" sang đo lường thực nghiệm trước khi triển khai (Dietvorst và cs., 2018). Đối với chính sách, các quy định về con người tham gia vào vòng lặp xử lý áp dụng đồng nhất bất kể bối cảnh không được hỗ trợ bởi dữ liệu—khung pháp lý cần mang tính đặc thù theo ngành và nhiệm vụ. Trong các quyết định có ràng buộc pháp lý (đặc biệt ở khu vực công), yêu cầu "có con người trong vòng lặp" chỉ có ý nghĩa khi con người thực sự có thông tin và thẩm quyền để phát hiện, can thiệp, và sửa sai; nếu không, sai sót có thể bị tự động hóa và nhân rộng, trong khi trách nhiệm giải trình bị phân tán. Vì vậy, thay vì áp dụng một mẫu hình cộng tác đồng nhất, chính sách nên nhấn mạnh các điều kiện giám sát có hiệu lực (tính minh bạch phù hợp nhiệm vụ, quyền can thiệp, và quy trình kiểm định trước–sau triển khai).

---

## 6. Kết luận

Phân tích meta trên 278 kích thước hiệu ứng từ 67 nghiên cứu bao phủ bốn ngành cho thấy nghịch lý cộng tác người–AI mang tính phổ quát (*g* = −0,529, *p* < 0,001). Quan trọng hơn con số trung bình là cấu trúc bên dưới.

Kết quả xác nhận cả bốn giả thuyết: H1 (nghịch lý cộng hưởng khái quát hóa), H2 (tăng cường bất đối xứng, AI hỗ trợ người bền vững qua mọi bối cảnh), H3 (ngành và loại nhiệm vụ điều tiết mạnh), H4 (thâm hụt thu hẹp theo thời gian). Phát hiện ngoài dự kiến là phép so sánh AI hỗ trợ người hoàn toàn không phụ thuộc bối cảnh (QM = 0,88, ns), khẳng định mô hình người phán đoán–người tư vấn mạnh hơn dự đoán ban đầu.

Truyền thông là ngoại lệ cho thấy khung phân tích hoạt động: ở những nhiệm vụ đòi hỏi năng lực mà AI chưa có, sự tham gia của con người chuyển từ gánh nặng thành tài sản (*g* = +1,011). Xu hướng cải thiện theo thời gian cho thấy nghịch lý không phải định mệnh, thâm hụt thu hẹp từ *g* = −0,835 (2020) đến gần zero (2023).

Một số hạn chế cần cân nhắc. I² > 90% cho thấy các ước lượng tổng hợp mô tả xu hướng trung tâm của một phân phối rất rộng, khoảng dự đoán [−2,631, +1,572] cho cộng hưởng xác nhận điều này. Bộ dữ liệu mất cân bằng giữa nhiệm vụ quyết định (*k* = 252) và sáng tạo (*k* = 26), khiến ước lượng nhóm sáng tạo cần xác nhận thêm. Giai đoạn phân tích 2020–2024 trùng với thời kỳ AI tiến bộ nhanh, đặc biệt sự xuất hiện của mô hình ngôn ngữ lớn; các mô hình quan sát ở đây có thể dịch chuyển khi bức tranh công nghệ thay đổi. Thiên lệch xuất bản hiện diện ở cả ba phép so sánh, và ước lượng điều chỉnh gợi ý thâm hụt thực tế có thể còn lớn hơn.

Hai câu hỏi mở cho nghiên cứu tương lai. Thứ nhất, liệu xu hướng cải thiện có tiếp tục khi AI sinh tạo trở thành trung tâm cộng tác người-máy, hay sự phức tạp của các mô hình mới tạo ra những dạng bất đối xứng thông tin khác. Thứ hai, liệu các giao thức cộng tác động, chuyển đổi giữa quyết định của con người và AI dựa trên ước lượng hiệu suất thời gian thực, có thể vượt qua thiết kế tĩnh của cơ chế con người tham gia vào vòng lặp xử lý.

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

Jarrahi, M. H. (2018). Artificial intelligence and the future of work: Human–AI symbiosis in organizational decision making. *Business Horizons*, 61(4), 577–586.

Kleinberg, J., Lakkaraju, H., Leskovec, J., Ludwig, J., & Mullainathan, S. (2018). Human decisions and machine predictions. *The Quarterly Journal of Economics*, 133(1), 237–293.

Licklider, J. C. R. (1960). Man–computer symbiosis. *IRE Transactions on Human Factors in Electronics*, HFE-1(1), 4–11.

Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. *Organizational Behavior and Human Decision Processes*, 151, 90–103.

Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: An attentional integration. *Human Factors*, 52(3), 381–410.

Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors*, 39(2), 230–253.

Ricardo, D. (1817). *On the principles of political economy and taxation*. John Murray.

Rosenthal, R. (1979). The file drawer problem and tolerance for null results. *Psychological Bulletin*, 86(3), 638–641.

Sniezek, J. A., & Buckley, T. (1995). Cueing and cognitive conflict in judge-advisor decision making. *Organizational Behavior and Human Decision Processes*, 62(2), 159–174.

Topol, E. J. (2019). High-performance medicine: The convergence of human and artificial intelligence. *Nature Medicine*, 25(1), 44–56.

Tschandl, P., Rinner, C., Apalla, Z., Argenziano, G., et al. (2020). Human–computer collaboration for skin cancer recognition. *Nature Medicine*, 26(8), 1229–1234.

Viechtbauer, W. (2010). Conducting meta-analyses in R with the metafor package. *Journal of Statistical Software*, 36(3), 1–48.
