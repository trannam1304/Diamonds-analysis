# Nhận xét phần 2 — Diamonds

Dữ liệu sạch thực tế: **53,772 dòng × 10 cột**. Kiểm định KS bootstrap tham số: B=1999, seed=42, mức ý nghĩa 5%; đánh giá sáu giả thuyết bằng hiệu chỉnh Holm.

## price (USD)

Mean = **3,931.1373**, median = **2,401.0000**, SD = 3,985.8530, CV = 101.39%. Skewness = **1.6183** (lệch phải); excess kurtosis = 2.1797. Khoảng ghi nhận từ 326.0000 đến 18,823.0000; Q1 = 951.0000, Q3 = 5,324.0000. Giữ lại 3,519 quan sát vượt ngưỡng IQR (6.54%).

- Normal: D=0.184567; p_MC=0.000500 (sàn Monte Carlo, không phải p thật đã biết); p_Holm=0.003000 ⇒ bác bỏ H0

- Lognormal: D=0.084169; p_MC=0.000500 (sàn Monte Carlo, không phải p thật đã biết); p_Holm=0.003000 ⇒ bác bỏ H0

- Exponential: D=0.093867; p_MC=0.000500 (sàn Monte Carlo, không phải p thật đã biết); p_Holm=0.003000 ⇒ bác bỏ H0

Cả ba ứng viên đều bị bác bỏ ở mức 5% sau Holm; không gán biến cho một phân phối đã thử. Lognormal có D nhỏ nhất trong ba ứng viên (D=0.084169, tương ứng độ chênh CDF tối đa khoảng 8.42 điểm phần trăm); đây là so sánh tương đối, không thay thế kết luận kiểm định.

**Đọc đuôi trên cùng Q–Q plot:** P99 thực nghiệm = 17,365.2900 USD; P99 dự đoán bởi các mô hình đã fit: Normal = 13,203.6180; Lognormal = 25,498.7181; Exponential = 18,103.5564 USD. Mô hình có P99 lớn hơn thực nghiệm dự đoán phân vị này cao hơn dữ liệu; mô hình có P99 nhỏ hơn dự đoán thấp hơn dữ liệu. Sai khác có thể quan sát trên Q–Q, và việc một phân vị gần nhau chưa bảo đảm cả phân phối phù hợp. Normal còn gán **16.20%** xác suất cho price âm, không phù hợp miền vật lý/kinh tế của biến.

## carat (carat)

Mean = **0.7975**, median = **0.7000**, SD = 0.4732, CV = 59.33%. Skewness = **1.1132** (lệch phải); excess kurtosis = 1.2460. Khoảng ghi nhận từ 0.2000 đến 5.0100; Q1 = 0.4000, Q3 = 1.0400. Giữ lại 1,867 quan sát vượt ngưỡng IQR (3.47%).

- Normal: D=0.122582; p_MC=0.000500 (sàn Monte Carlo, không phải p thật đã biết); p_Holm=0.003000 ⇒ bác bỏ H0

- Lognormal: D=0.103606; p_MC=0.000500 (sàn Monte Carlo, không phải p thật đã biết); p_Holm=0.003000 ⇒ bác bỏ H0

- Exponential: D=0.283774; p_MC=0.000500 (sàn Monte Carlo, không phải p thật đã biết); p_Holm=0.003000 ⇒ bác bỏ H0

Cả ba ứng viên đều bị bác bỏ ở mức 5% sau Holm; không gán biến cho một phân phối đã thử. Lognormal có D nhỏ nhất trong ba ứng viên (D=0.103606, tương ứng độ chênh CDF tối đa khoảng 10.36 điểm phần trăm); đây là so sánh tương đối, không thay thế kết luận kiểm định.

**Đọc đuôi trên cùng Q–Q plot:** P99 thực nghiệm = 2.1700 carat; P99 dự đoán bởi các mô hình đã fit: Normal = 1.8982; Lognormal = 2.6228; Exponential = 3.6727 carat. Mô hình có P99 lớn hơn thực nghiệm dự đoán phân vị này cao hơn dữ liệu; mô hình có P99 nhỏ hơn dự đoán thấp hơn dữ liệu. Sai khác có thể quan sát trên Q–Q, và việc một phân vị gần nhau chưa bảo đảm cả phân phối phù hợp. Normal còn gán **4.59%** xác suất cho carat âm, không phù hợp miền vật lý/kinh tế của biến.

## Các mốc tập trung của carat

0.30 carat: 2,596 quan sát (4.83%); 0.31 carat: 2,238 quan sát (4.16%); 1.01 carat: 2,238 quan sát (4.16%). Histogram/KDE và ECDF thể hiện các vùng tập trung, Q–Q có các đoạn bậc thang do giá trị lặp. Ba mô hình mật độ trơn đã thử không tái hiện đầy đủ cấu trúc này. Chưa đủ căn cứ quy các đỉnh cho một nguyên nhân thị trường cụ thể.

## Xác suất thực nghiệm đáng chú ý

- **price <= 1.000 USD**: 14,470/53,772 quan sát = **26.91%**.
- **price > 5.000 USD**: 14,666/53,772 quan sát = **27.27%**.
- **price > 10.000 USD**: 5,194/53,772 quan sát = **9.66%**.
- **carat <= 0,5 carat**: 18,863/53,772 quan sát = **35.08%**.
- **carat >= 1 carat**: 18,984/53,772 quan sát = **35.30%**.
- **carat >= 2 carat**: 2,129/53,772 quan sát = **3.96%**.

## Giới hạn phương pháp

Price được ghi theo USD nguyên; carat nằm trên lưới 0,01 carat, nên có nhiều giá trị trùng. Bootstrap hiện mô phỏng phân phối liên tục và fit lại tham số, chưa mô phỏng cơ chế làm tròn. P-value được diễn giải dưới các giả định đã nêu, bao gồm các quan sát độc lập, cùng phân phối và mô hình liên tục; cần đọc cùng D, histogram/KDE, Q–Q và ECDF.

Lognormal có D nhỏ nhất trong ba ứng viên không đồng nghĩa dữ liệu tuân theo lognormal. Khi không có mẫu mô phỏng vượt D quan sát, p_MC = 1/(B+1) = 0.0005 là sàn Monte Carlo, không phải p-value thật đã biết chính xác.

Kết luận áp dụng cho tập Diamonds đang phân tích; chưa đủ cơ sở suy rộng cho toàn bộ thị trường kim cương.
