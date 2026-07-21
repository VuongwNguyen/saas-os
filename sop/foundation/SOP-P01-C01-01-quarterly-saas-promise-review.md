# SOP-P01-C01-01 — Quarterly SaaS Promise Review

- **Version:** 1.0.0
- **Effective date:** 2026-07-21
- **Owner:** CPO; Founder/CEO nếu chưa có CPO
- **Review cycle:** hàng năm hoặc sau thay đổi material

## Purpose và scope

Kiểm tra mỗi quý rằng lời hứa giá trị của từng product/plan/ICP còn đúng, đo được, đáng tin cậy và bền vững. SOP áp dụng cho SaaS/AI SaaS đang live hoặc chuẩn bị thay đổi material; incident response vẫn tuân theo runbook chuyên biệt.

## Participants

CPO (accountable), Product, Engineering/SRE, Security/Privacy, Customer Success/Support, GTM, Finance/RevOps và Data. Legal tham gia khi có claim, hợp đồng, privacy hoặc regulatory impact.

## Input và preconditions

- SaaS Promise Card phiên bản hiện hành.
- Dashboard snapshot theo cohort; metric definitions và freshness report.
- Incident/postmortem, support themes, customer research và decision log.
- Retention/revenue/cost-to-serve theo định nghĩa đã duyệt.
- Risk register, contractual commitments và thay đổi pháp lý liên quan.
- Người tham gia được quyền truy cập đúng mức; dữ liệu review đã tối thiểu hóa PII.

Không họp review nếu metric quan trọng chưa qua data-quality check. Thay vào đó mở data incident và ghi metric là `unavailable`, không điền số ước đoán như fact.

## Procedure

1. **T−10 ngày — khóa phạm vi.** Product Ops lập danh sách product/plan/ICP, owner và thay đổi material từ kỳ trước.
2. **T−7 — tạo evidence packet.** Data owner xuất snapshot có query/version/time window/segment. Agent có thể soạn nháp theo spec nhưng không kết luận thay owner.
3. **T−5 — kiểm tra dữ liệu.** Xác nhận denominator, deduplication, late events, timezone, eligibility và definition version.
4. **T−3 — pre-read.** Mỗi owner phân loại từng claim: fact, inference hoặc recommendation; ghi breach và unknown.
5. **T — review value loop.** So sánh activation, time to first value, recurring value theo cohort và qualitative evidence.
6. **T — review trust loop.** Xem SLO, severe incidents, security/privacy findings, billing corrections và support themes.
7. **T — review economic/learning loop.** Xem retention/cost-to-serve và tình trạng các hypothesis/action kỳ trước.
8. **T — quyết định.** Chọn một trong: giữ; instrument; experiment; remediate; thu hẹp promise; rollback; retire. Mỗi quyết định có evidence, owner, due date và verification signal.
9. **T+1 — approval.** Accountable owner ký minutes. Security/Legal/Finance ký phần thuộc quyền; executive ký risk acceptance hoặc material promise change.
10. **T+2 — publish nội bộ.** Version Promise Card, metric dictionary và decision log; chỉ gửi thông tin khách hàng qua quy trình communication đã duyệt.
11. **T+10 — verify.** Product Ops kiểm tra action đã được đưa vào system of record và escalation các mục quá hạn.

## Output và checklist đóng

- [ ] Review minutes có attendees, thời gian và evidence links.
- [ ] Mỗi breach/unknown có disposition.
- [ ] Action có accountable owner, due date và verification signal.
- [ ] Promise/metric thay đổi có version và approver.
- [ ] Risk acceptance có phạm vi, lý do và expiry date.
- [ ] Customer communication, nếu có, đã qua owner phù hợp.
- [ ] Evidence packet và audit log được lưu theo retention policy.

## SLA, escalation và audit

- Review thường kỳ hoàn tất trong 10 ngày làm việc đầu quý.
- Red breach được triage trong 1 ngày làm việc hoặc nhanh hơn theo incident/contract policy.
- Suspected security/privacy breach chuyển ngay cho Security Incident Commander; billing correctness cho Finance owner; contractual risk cho executive + Legal; data-quality breach cho Data owner.
- Audit record gồm input snapshot/hash, metric versions, prompt/model version nếu dùng AI, tool calls, output, reviewer overrides, approvals và decision log. Không lưu secret hoặc raw PII không cần thiết.

## Change log

| Version | Ngày | Thay đổi |
|---|---|---|
| 1.0.0 | 2026-07-21 | Phát hành cho review cùng P01-C01 |

