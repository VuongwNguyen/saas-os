# TPL-P01-C01-01 — SaaS Promise Card

- **Template version:** 1.0.0
- **Liên kết:** P01-C01 — SaaS Philosophy

## Hướng dẫn

Tạo một card cho mỗi tổ hợp product/plan/ICP có lời hứa khác biệt material. Dùng nguồn nội bộ có link và ngày. Không có dữ liệu thì ghi `unknown`; không dùng benchmark ngoài làm target nếu chưa chứng minh tính tương đương.

## Template trống

```yaml
promise_id:
version:
status: draft | approved | retired
product:
plan:
icp:
owner:
reviewers: []
approved_at:
next_review:

customer:
  problem_statement:
  desired_outcome:
  evidence:
    - source_url:
      observed_at:
      evidence_type: interview | behavior | transaction | experiment | other
      confidence: low | medium | high
  non_goals: []

value:
  proposition:
  first_value_event:
  first_value_eligibility:
  recurring_value_event:
  recurring_window:

trust_promises:
  reliability:
  security_privacy:
  support:
  billing:

metrics:
  - metric_id:
    business_meaning:
    formula:
    numerator:
    denominator:
    unit:
    window:
    segments: []
    exclusions: []
    source:
    owner:
    definition_version:
    baseline: unknown
    baseline_period:
    target: unknown
    red_threshold: unknown
    freshness_sla:

operation:
  review_cadence:
  alert_route:
  rollback_or_containment:
  risk_acceptance_approver:

assumptions: []
open_questions: []
decision_log_url:
```

## Ví dụ điền sẵn (giả định minh họa, không phải case study)

```yaml
promise_id: DEMO-INVOICE-001
version: 0.1.0
status: draft
product: Demo Invoice SaaS
plan: Team
icp: Đội vận hành dịch vụ 5–20 người
owner: Demo Product Lead
reviewers: [Demo Engineering Lead, Demo Finance Ops]

customer:
  problem_statement: "Giảm lỗi thao tác khi lập hóa đơn lặp lại"
  desired_outcome: "Hóa đơn được chuẩn bị đúng quy trình và sẵn sàng cho người có thẩm quyền duyệt"
  evidence:
    - source_url: "internal://research/placeholder"
      observed_at: "YYYY-MM-DD"
      evidence_type: interview
      confidence: low
  non_goals: ["Tự động phê duyệt hoặc gửi hóa đơn"]

value:
  proposition: "Chuẩn bị hóa đơn lặp lại có kiểm soát"
  first_value_event: "authorized_user_approves_first_draft"
  first_value_eligibility: "account_has_valid_billing_profile"
  recurring_value_event: "authorized_user_approves_draft"
  recurring_window: "calendar_month"

metrics:
  - metric_id: recurring_value_rate
    formula: "eligible active accounts with >=1 approved draft / eligible active accounts"
    baseline: unknown
    target: unknown
    red_threshold: unknown
    owner: Demo Product Lead
```

Các tên và dữ liệu trên là giả định để minh họa cách điền, không mô tả doanh nghiệp có thật.

## Checklist

- [ ] Outcome mô tả thay đổi cho khách hàng, không phải feature.
- [ ] Event có eligibility, window và denominator.
- [ ] Trust promise bao phủ reliability, security/privacy, support, billing.
- [ ] Baseline/target có nguồn hoặc là `unknown`.
- [ ] Owner và approver là vai trò cụ thể.
- [ ] Assumption tách khỏi fact.
- [ ] Rollback/containment phù hợp blast radius.

## AI prompt hỗ trợ

> Kiểm tra Promise Card dưới đây. Không bổ sung số, nguồn hoặc claim chưa có. Trả về JSON gồm `missing_fields`, `contradictions`, `unmeasurable_promises`, `risk_flags`, `questions_for_owner`. Trích dẫn đường dẫn trường cho mỗi phát hiện. Không đề xuất target nếu baseline là `unknown`.

