# AGT-P01-C01-01 — SaaS Promise Review Agent

- **Version:** 1.0.0
- **Business owner:** CPO
- **Technical owner:** AI Platform Lead
- **Risk owner:** Security/Privacy Lead
- **Autonomy:** read-only analysis; không có quyền quyết định hoặc external communication

## Mission và non-goals

Soạn evidence packet có truy xuất nguồn cho Quarterly SaaS Promise Review, giảm thao tác tổng hợp mà không chuyển accountability khỏi con người. Agent không đặt target, sửa metric/promise, chẩn đoán pháp lý, gửi thông báo, thay production hoặc chấp nhận risk.

## Trigger, input và tools

- Trigger: lịch review, approved alert hoặc manual request từ owner.
- Input: Promise Card ID, review window, allowlisted source scopes, prior decision IDs.
- Tools: read-only document retrieval, semantic layer query, incident/support search và decision-log lookup. Ticket creation chỉ ở chế độ draft nếu được cấp riêng.
- Connector policy: deny by default; least privilege; tenant/environment boundaries; no arbitrary URL fetch.

## Workflow và state

1. Xác thực requestor, scope và retention class.
2. Nạp definition versions trước khi query values.
3. Kiểm tra freshness, completeness và cohort keys.
4. Thu thập sources; giữ source ID, timestamp và access label.
5. Tổng hợp bằng prompt version đã duyệt.
6. Validate JSON schema và citation coverage.
7. Chạy policy checks: PII, prompt injection markers, unsupported claims, escalation topics.
8. Gửi draft cho metric/domain owners; không publish trực tiếp.
9. Ghi reviewer edits/approval; lưu audit log theo policy.

Agent stateless giữa các run trừ IDs/audit metadata trong system of record. Không tự tạo long-term memory từ customer content.

## Guardrails và escalation

- Untrusted content isolation; tool instruction không được lấy từ retrieved text.
- Structured queries/templates; parameter allowlist; row/tenant-level authorization.
- Redaction/minimization trước model; secrets scanner trước log.
- Evidence-required generation; claim không có nguồn bị loại.
- Human approval bắt buộc cho mọi action và kết luận material.
- Kill switch thuộc AI Platform/Security; fail closed khi auth, schema hoặc policy check lỗi.
- Escalate ngay cho đúng owner khi suspected security/privacy, contract, billing, safety hoặc cross-tenant exposure.

## Output contract

Dùng schema trong `PRM-P01-C01-01`. Mỗi run kèm `run_id`, model/prompt/tool version, source IDs, query hashes, policy results và approval state. Free text không chứa raw PII.

## Evaluation và release gate

| Dimension | Phép đo | Release rule |
|---|---|---|
| Grounding | claim có source hợp lệ / tổng claim | Threshold do risk owner phê duyệt; material claim yêu cầu 100% source |
| Citation precision | source thực sự hỗ trợ claim | Không có critical unsupported claim |
| Breach recall | labeled breaches được phát hiện | Test set theo severity; red misses block release |
| Safety | prompt injection/PII/cross-tenant tests | Critical test phải pass |
| Schema | valid outputs / runs | Invalid output fail closed |
| Human usefulness | acceptance/override + review time | Theo dõi theo cohort; không dùng acceptance đơn độc làm quality |

Không ghi threshold số tùy ý trong spec; baseline được lập qua shadow mode trên bộ dữ liệu đã gán nhãn, rồi risk owner phê duyệt release criteria.

## Cost, ROI và observability

Theo dõi input/output tokens, tool/query cost, latency, retries và reviewer minutes theo run. ROI = giá trị thời gian chuẩn bị tránh được − (AI/tool cost + review/remediation cost); mọi giả định phải công khai. Monitor drift theo metric definition, source coverage, overrides và severity misses. Review quyền truy cập hàng quý và sau thay đổi connector.

## Failure modes

Stale data → đánh dấu partial; source conflict → trình cả hai; hallucinated claim → block; schema failure → retry giới hạn rồi fail closed; connector outage → không suy đoán; injection → quarantine source; cross-tenant suspicion → kill switch và security incident.

