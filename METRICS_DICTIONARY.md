# Metrics Dictionary

For every metric, record its name, business meaning, formula, unit, data source, owner, review cadence, segmentation, exclusions, and known limitations.

## Activation rate

| Field | Definition |
|---|---|
| Business meaning | Tỷ lệ account mới đủ điều kiện đạt activation definition trong cửa sổ quy định |
| Formula | activated new eligible accounts / new eligible accounts |
| Unit | % |
| Data source | Product event store + governed account model |
| Owner | Head of Product |
| Review cadence | Tuần; cohort tháng |
| Segmentation | Acquisition cohort, plan, ICP, channel, region khi hợp lệ |
| Exclusions | Test/internal/fraud; account không đủ điều kiện theo contract metric |
| Limitations | Activation là proxy phụ thuộc definition; không chứng minh outcome hoặc retention; thay definition phá so sánh nếu không version/backfill |
| Cross-reference | P01-C01 |

## Billing correction rate

| Field | Definition |
|---|---|
| Business meaning | Tỷ lệ hóa đơn đã phát hành cần correction theo policy |
| Formula | corrected issued invoices / issued invoices |
| Unit | % |
| Data source | Billing system + support/finance correction log |
| Owner | Finance Operations |
| Review cadence | Tuần và tháng |
| Segmentation | Product, plan, region, correction reason |
| Exclusions | Test invoice; correction không do lỗi theo policy được công bố |
| Limitations | Nhiều lỗi trên một invoice vẫn có thể chỉ đếm một; lag do correction phát hiện muộn |
| Cross-reference | P01-C01 |

## Gross revenue retention (GRR)

| Field | Definition |
|---|---|
| Business meaning | Phần recurring revenue đầu kỳ được giữ lại sau churn và contraction, không tính expansion |
| Formula | (opening recurring revenue − churn − contraction) / opening recurring revenue |
| Unit | % |
| Data source | Governed billing/finance ledger |
| Owner | Finance/Revenue Operations |
| Review cadence | Tháng và quý |
| Segmentation | Start cohort, plan, ICP, region, currency policy |
| Exclusions | Expansion; one-time revenue; account ngoài recurring-revenue scope |
| Limitations | Nhạy với FX, M&A, reactivation, contract timing và scope policy; cần reconciliation với Finance |
| Cross-reference | P01-C01; sẽ chuẩn hóa sâu hơn ở Part 05/06 |

## Recurring value rate

| Field | Definition |
|---|---|
| Business meaning | Tỷ lệ eligible active accounts thực hiện ít nhất một recurring value event trong cửa sổ đo |
| Formula | eligible active accounts with ≥1 recurring value event / eligible active accounts |
| Unit | % |
| Data source | Product event store + governed account/eligibility model |
| Owner | CPO/Product owner |
| Review cadence | Tuần; cohort tháng/quý |
| Segmentation | Plan, ICP, tenure, cohort, region khi hợp lệ |
| Exclusions | Test/internal/fraud; account không đủ điều kiện theo metric contract |
| Limitations | Là North Star proxy, không tự chứng minh business outcome hoặc nhân quả; phụ thuộc chất lượng event/eligibility definition |
| Cross-reference | P01-C01 |

## SLO attainment

| Field | Definition |
|---|---|
| Business meaning | Tỷ lệ service events hợp lệ đáp ứng tiêu chí “good” trong SLO window |
| Formula | good valid service events / valid service events |
| Unit | % |
| Data source | Observability/SLI pipeline |
| Owner | Service owner/SRE |
| Review cadence | Liên tục; ngày/tuần/tháng theo SLO |
| Segmentation | Service, region, user journey, plan nếu SLO định nghĩa |
| Exclusions | Chỉ exclusion được SLO document phê duyệt |
| Limitations | Chất lượng phụ thuộc SLI và user-journey coverage; aggregate có thể che cohort bị ảnh hưởng |
| Cross-reference | P01-C01; sẽ mở rộng ở Part 15 |

## Time to first value (TTFV)

| Field | Definition |
|---|---|
| Business meaning | Thời gian từ lúc account đủ điều kiện đến first value event đầu tiên |
| Formula | median(first value timestamp − eligibility timestamp), hiển thị kèm completion rate |
| Unit | Thời gian |
| Data source | Product event store + account eligibility model |
| Owner | Product + Customer Success |
| Review cadence | Tuần; cohort tháng |
| Segmentation | Plan, ICP, onboarding path, cohort |
| Exclusions | Test/internal/fraud; record timestamp invalid; exclusion khác phải công khai |
| Limitations | Median chỉ trên completers gây survivorship bias nếu không hiển thị completion; event có thể chỉ là proxy của value |
| Cross-reference | P01-C01 |
