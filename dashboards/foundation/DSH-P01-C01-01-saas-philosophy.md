# DSH-P01-C01-01 — SaaS Philosophy Dashboard

- **Version:** 1.0.0
- **Dashboard owner:** CPO
- **Data steward:** Head of Data/Analytics
- **Review:** operational hàng tuần; executive hàng tháng; promise hàng quý

## Mục đích và layout

Dashboard trả lời: khách hàng có nhận giá trị lặp lại; dịch vụ có giữ trust; và economics có bền vững hay không. Không dùng dashboard này để suy luận nhân quả nếu chưa có thiết kế phân tích phù hợp.

```text
[Data freshness] [Definition version] [Selected cohort]
[Recurring value rate] [Activation] [Time to first value]
[SLO attainment]       [Severe incidents] [Billing correction]
[GRR]                  [Cost-to-serve]     [Open red actions]
[Cohort trend]         [Segment breakdown] [Annotations/decisions]
```

## Metric contracts

| Metric | Formula | Segment/exclusion | Source | Owner | Alert |
|---|---|---|---|---|---|
| Recurring value rate | eligible active accounts có ≥1 recurring value event trong window / eligible active accounts trong window | plan, ICP, tenure; loại test/internal | product events + account model | CPO | dưới red threshold đã duyệt |
| Activation rate | new eligible accounts đạt activation definition trong activation window / new eligible accounts | acquisition cohort, plan; loại fraud/test | product events | Head of Product | cohort dưới threshold |
| Time to first value | median(timestamp first value − timestamp eligibility) | chỉ account có first value; luôn hiển thị completion rate cạnh median | events/warehouse | Product + CS | tăng vượt threshold hoặc completion giảm |
| SLO attainment | good valid service events / valid service events | service, region, plan; exclusion phải theo SLO doc | observability | SRE owner | theo error-budget policy |
| GRR | (opening recurring revenue − churn − contraction) / opening recurring revenue | currency policy, cohort; không cộng expansion | billing/finance ledger | Finance/RevOps | dưới threshold |
| Billing correction rate | invoices cần correction / invoices issued | product, region; loại test | billing + support | Finance Ops | bất kỳ critical pattern hoặc vượt threshold |
| Severe incidents | số incident theo severity policy trong window | service/region | incident system | VP Engineering | theo incident policy |
| Open red actions | action red quá hạn / tổng action red đang mở | owner/function | decision/action log | CPO Ops | >0 quá hạn |

## Baseline, target và threshold

Mỗi metric lấy baseline từ kỳ được ghi trong Promise Card. Target và threshold do accountable owner phê duyệt sau khi xem risk appetite, contract và phân phối lịch sử. Dashboard phải hiển thị `unknown`, không thay bằng 0, khi thiếu giá trị.

## Data quality và alerts

- Freshness badge đỏ khi chậm hơn SLA; tạm ngừng kết luận metric liên quan.
- Mỗi tile hiện formula/version, denominator, time zone, window và last updated.
- Definition change tạo annotation và không nối chuỗi thời gian nếu không backfill tương thích.
- Alert định tuyến tới owner và incident/action system; alert không tự động thay promise hoặc gửi khách hàng.

## Review script

1. Kiểm tra freshness/schema/definition trước trend.
2. Xem North Star proxy với guardrails.
3. Drill down cohort/segment; ghi Simpson’s paradox risk nếu aggregate khác cohort.
4. Đối chiếu incident, release, campaign và pricing annotations.
5. Ghi fact → inference → recommendation riêng biệt.
6. Tạo action có owner/due date/verification signal.

