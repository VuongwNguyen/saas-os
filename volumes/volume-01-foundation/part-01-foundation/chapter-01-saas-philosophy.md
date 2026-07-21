# P01-C01 — SaaS Philosophy

- **Trạng thái:** REVIEW
- **Phiên bản:** 0.9.0
- **Owner:** Chief Product Officer (CPO); giai đoạn sớm: Founder/CEO
- **Ngày kiểm tra nguồn gần nhất:** 2026-07-21
- **Phạm vi:** triết lý thiết kế và vận hành doanh nghiệp SaaS; không thay thế hướng dẫn kế toán, pháp lý hay bảo mật chuyên sâu

## 1. Overview

### Khái niệm

**Fact.** NIST định nghĩa Software as a Service (SaaS) là khả năng cho khách hàng sử dụng ứng dụng của nhà cung cấp chạy trên hạ tầng đám mây; khách hàng không quản lý hạ tầng nền, ngoại trừ một số cấu hình ứng dụng giới hạn. Định nghĩa này thuộc một mô hình cloud có năm đặc tính thiết yếu: tự phục vụ theo nhu cầu, truy cập mạng rộng, dùng chung tài nguyên, co giãn nhanh và dịch vụ được đo lường [NIST SP 800-145](https://csrc.nist.gov/pubs/sp/800/145/final).

**Inference.** Vì nhà cung cấp giữ trách nhiệm vận hành ứng dụng, SaaS không chỉ là “phần mềm bán theo tháng”. Đó là cam kết cung cấp **năng lực sử dụng được, an toàn và cải tiến liên tục** trong toàn bộ vòng đời khách hàng. Subscription là một cơ chế thu tiền thường gặp, không phải điều kiện đủ để một sản phẩm có tư duy SaaS.

**Recommendation.** Mọi quyết định sản phẩm nên trả lời bốn câu hỏi: khách hàng đạt outcome nào; họ nhận giá trị sớm và lặp lại ra sao; hệ thống giữ lời hứa dịch vụ thế nào; doanh nghiệp học và cải tiến bằng bằng chứng nào.

### Lịch sử, nguồn gốc và ý nghĩa

Phần mềm chuyển dần từ bản phát hành được giao rồi cài đặt tại chỗ sang ứng dụng do nhà cung cấp vận hành qua mạng. NIST chuẩn hóa taxonomy cloud năm 2011, nhưng chính NIST cũng ghi nhận thuật ngữ SaaS có từ thập niên 1990 [NIST SP 800-146](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-146.pdf). Song song, Service-Dominant Logic xem service là một quá trình áp dụng năng lực vì lợi ích của bên khác và giá trị được đồng kiến tạo, thay vì một đơn vị đầu ra được “giao” một lần [Vargo & Akaka, 2009](https://doi.org/10.1287/serv.1.1.32).

Điều này quan trọng vì nhà cung cấp SaaS đồng thời vận hành ba hệ:

1. **Hệ giá trị:** biến nhu cầu thành outcome có thể quan sát.
2. **Hệ dịch vụ:** duy trì reliability, security, support và trust.
3. **Hệ học hỏi:** biến telemetry và phản hồi thành quyết định, thay đổi và kiểm chứng mới.

### Phạm vi và sai lầm phổ biến

Chương này áp dụng cho B2B, B2C và AI SaaS, từ founder-led đến enterprise. Nó không quy định một kiến trúc, pricing model hay cadence duy nhất.

Sai lầm phổ biến là đồng nhất SaaS với recurring billing; tối ưu đăng ký mà bỏ quên adoption; coi release là kết thúc; dùng tăng trưởng để che reliability kém; hoặc tự động hóa AI trước khi xác lập owner và quyền phê duyệt.

## 2. Philosophy

### First principles

1. **Value in use over features shipped.** Tính năng chỉ có giá trị khi khách hàng dùng nó để đạt outcome.
2. **Service continuity over one-time delivery.** Bán hàng khởi tạo nghĩa vụ; không kết thúc nghĩa vụ.
3. **Trust is cumulative and fragile.** Reliability, security, privacy, billing và support đều là bề mặt sản phẩm.
4. **Learning loops over certainty.** Mọi roadmap là tập giả thuyết có mức bằng chứng khác nhau.
5. **Whole-lifecycle economics.** Acquisition, onboarding, operation, support, retention và expansion phải cùng nằm trong một mô hình.
6. **Automation with accountability.** Máy có thể quan sát và đề xuất; con người vẫn sở hữu quyết định rủi ro cao.

### Mental models

- **Promise–delivery–proof:** lời hứa thị trường → trải nghiệm thực tế → bằng chứng outcome.
- **Stock and flow:** customer base là stock; acquisition, churn và expansion là flow. Tăng đầu vào không sửa được rò rỉ giữ chân.
- **Compounding trust:** các tương tác đúng kỳ vọng tích lũy niềm tin; một sự cố nghiêm trọng có thể phá hủy nhanh hơn tốc độ xây dựng.
- **Constraint:** throughput của hành trình giá trị bị giới hạn ở bước yếu nhất, không phải đội bận nhất.

### Nguyên tắc vận hành

Mỗi lời hứa dịch vụ phải có owner, metric, ngưỡng cảnh báo và cadence review. Mỗi thay đổi quan trọng phải chỉ rõ giả thuyết, blast radius, khả năng rollback và tín hiệu thành công. Khi mục tiêu tăng trưởng xung đột với trust, quyết định cần được nâng cấp cho accountable executive thay vì âm thầm hạ chuẩn.

## 3. Core Concepts

| Thuật ngữ | Định nghĩa làm việc | Quan hệ |
|---|---|---|
| SaaS | Năng lực phần mềm do nhà cung cấp vận hành và khách hàng sử dụng qua mạng | Bao chứa product, service và learning system |
| Outcome | Thay đổi có giá trị mà khách hàng muốn đạt | Đích của value realization |
| Value realization | Khách hàng thực sự nhận và nhận biết outcome | Cần activation và recurring value |
| Service promise | Cam kết có thể kiểm chứng về giá trị và chất lượng dịch vụ | Được theo dõi bằng SLI/KPI |
| Trust | Mức khách hàng sẵn sàng phụ thuộc vào dịch vụ | Bị chi phối bởi reliability, security, privacy, billing, support |
| Learning loop | Chu trình evidence → decision → change → measurement | Kết nối discovery với operation |
| Customer lifecycle | Chuỗi evaluate → buy → onboard → adopt → renew/expand/leave | Đơn vị tối ưu xuyên chức năng |

### Concept map

```text
Nhu cầu khách hàng
  → Lời hứa giá trị
    → Onboarding → Hành vi tạo giá trị → Outcome
                       ↓                    ↓
                  Telemetry ← Trust ← Chất lượng dịch vụ
                       ↓
                 Learning loop → Thay đổi có kiểm soát
                       ↓
               Retention / Expansion / Advocacy
```

Ranh giới trách nhiệm: Product sở hữu value hypothesis; Engineering/SRE sở hữu khả năng dịch vụ; GTM sở hữu kỳ vọng đúng; Customer Success sở hữu value realization; Finance sở hữu tính đúng của mô hình kinh tế; executive owner giải quyết trade-off xuyên hệ.

## 4. Frameworks

### Framework A — Service-Dominant Logic (S-D Logic)

**Nguồn gốc.** Vargo và Lusch phát triển S-D Logic; nghiên cứu tiếp theo mô tả service như quá trình, tập trung vào tri thức/kỹ năng động và xem giá trị là quá trình cộng tác giữa nhà cung cấp với khách hàng [Lusch, Vargo & Wessels, 2008](https://doi.org/10.1147/sj.471.0005).

- **Thành phần:** năng lực của nhà cung cấp; tài nguyên của khách hàng; value proposition; tương tác; value-in-use.
- **Ưu điểm:** buộc đội ngũ nhìn qua feature và transaction; phù hợp onboarding, adoption, success.
- **Nhược điểm:** trừu tượng; không tự cung cấp metric, cadence hay accountability.
- **Dùng khi:** thiết kế value proposition, customer journey, service ecosystem.
- **Không dùng riêng khi:** cần điều khiển incident, unit economics hoặc portfolio.
- **Ví dụ SaaS:** phần mềm kế toán chỉ tạo giá trị khi dữ liệu/quy trình khách hàng kết hợp với năng lực sản phẩm để đóng sổ đúng.
- **Ví dụ AI SaaS:** copilot chỉ tạo giá trị khi output được đặt trong workflow, dữ liệu, policy và bước kiểm duyệt của khách hàng.

### Framework B — SaaS Operating Loops

Đây là **recommendation** của SaaS OS, tổng hợp từ đặc tính dịch vụ cloud của NIST, S-D Logic và nguyên tắc vận hành liên tục.

| Loop | Câu hỏi | Input → output | Metric tối thiểu |
|---|---|---|---|
| Value loop | Khách hàng đạt outcome chưa? | Problem evidence → value event | Activation rate, recurring value rate |
| Trust loop | Dịch vụ có đáng phụ thuộc? | Service signals → corrective action | SLO attainment, severe incidents |
| Learning loop | Ta học nhanh và đúng chưa? | Evidence → decision → experiment | Hypothesis cycle time, decision quality review |
| Economic loop | Giá trị có bền vững cho hai bên? | Cohort economics → allocation | Retention, gross margin, cost-to-serve |

- **Ưu điểm:** gắn owner, telemetry và review; nhìn toàn vòng đời.
- **Nhược điểm:** cần thống nhất event và data quality; dễ tạo vanity dashboard nếu outcome mơ hồ.
- **Dùng khi:** thiết kế operating model và quarterly review.
- **Không dùng riêng khi:** phân tích chiến lược cạnh tranh hoặc compliance chuyên ngành.
- **Ví dụ SaaS:** theo dõi cohort từ activation đến recurring use, incident và renewal.
- **Ví dụ AI SaaS:** thêm quality evaluation, override rate, latency, cost và policy violation vào value/trust loop.

### So sánh và cách kết hợp

| Tiêu chí | S-D Logic | SaaS Operating Loops |
|---|---|---|
| Trọng tâm | Bản chất tạo giá trị | Cơ chế điều hành |
| Đơn vị phân tích | Tương tác và đồng kiến tạo | Loop có owner/metric/cadence |
| Điểm mạnh | Chống feature-centricity | Chuyển triết lý thành hệ vận hành |
| Khoảng trống | Thiếu controls cụ thể | Có thể cơ giới hóa sai outcome |

Dùng S-D Logic để xác định **giá trị là gì**, rồi dùng Operating Loops để bảo đảm **giá trị được tạo, giữ và cải tiến thế nào**.

## 5. Workflow

### SaaS promise-to-learning workflow

| Trường | Thiết kế |
|---|---|
| Trigger | Sản phẩm/dịch vụ mới; thay đổi pricing/packaging; tín hiệu outcome/trust vượt ngưỡng; quarterly review |
| Input | ICP/problem evidence, journey, service telemetry, cohort data, economics, risk register |
| Owner | CPO; founder ở giai đoạn sớm |
| Participants | Product, Engineering/SRE, Security, GTM, CS, Finance, Data |
| SLA | Triage cảnh báo đỏ trong 1 ngày làm việc; review hệ thống hàng tháng; tái phê duyệt promise hàng quý |
| Output | SaaS Promise Card, metric contract, action/decision log, experiment hoặc remediation plan |

Luồng thực thi:

1. Mô tả ICP, job/outcome và bằng chứng; gắn mức tin cậy.
2. Viết value event đầu tiên và recurring value event có thể quan sát.
3. Đặt service promise cho reliability, security/privacy, support và billing.
4. Xác định metric contract: công thức, event, denominator, segment, owner, freshness.
5. Ghi baseline. Nếu chưa có baseline, ghi rõ `unknown` và kế hoạch đo; không bịa target.
6. Chọn target/threshold theo risk appetite và bằng chứng lịch sử.
7. Instrument, kiểm thử dữ liệu và phát hành với rollout/rollback phù hợp.
8. Review value, trust, learning và economic loop theo cohort.
9. Quyết định: giữ, cải tiến, thu hẹp, rollback hay dừng; ghi rationale.
10. Cập nhật promise, backlog, runbook và customer communication.

**Decision points.** Không phát hành nếu chưa có owner, signal an toàn hay rollback cho thay đổi rủi ro cao. Không scale acquisition nếu recurring value suy giảm chưa có giải thích. Escalate khi privacy/security, contractual SLO hoặc billing correctness có nguy cơ bị vi phạm.

**Feedback loop.** Action chỉ được đóng khi metric hồi phục hoặc một accountable owner chấp nhận residual risk bằng văn bản.

## 6. SOP

SOP chuẩn nằm tại [SOP-P01-C01-01 — Quarterly SaaS Promise Review](../../../../sop/foundation/SOP-P01-C01-01-quarterly-saas-promise-review.md).

Tóm tắt:

- **Purpose:** kiểm tra promise còn đúng, đo được và bền vững.
- **Scope:** từng product/plan/ICP trọng yếu.
- **Owner:** CPO; co-owner reliability là CTO/VP Engineering.
- **Input:** Promise Card, dashboard, incident/support themes, cohort economics, risk register.
- **Output:** decision log, owner/due date, promise/metric changes.
- **SLA:** hoàn tất trong 10 ngày làm việc đầu quý; red breach triage trong 1 ngày làm việc.
- **Escalation:** executive team và Security/Legal khi liên quan trust, hợp đồng, pháp lý hoặc dữ liệu.
- **Audit:** lưu snapshot input, minutes, approvals và thay đổi metric.
- **Version:** 1.0.0.

## 7. Templates

Template có thể sao chép tại [SaaS Promise Card](../../../../templates/foundation/TPL-P01-C01-01-saas-promise-card.md), gồm hướng dẫn, checklist, AI prompt và ví dụ điền sẵn.

Các trường bắt buộc:

| Nhóm | Trường |
|---|---|
| Customer | ICP, problem evidence, desired outcome, non-goals |
| Value | first value event, recurring value event, time window |
| Trust | reliability, security/privacy, support, billing promises |
| Measurement | metric contract, baseline, target, threshold, segments |
| Operation | owner, reviewers, cadence, escalation, rollback |
| Evidence | source, date, confidence, unresolved assumptions |

Template không cho phép AI tự điền baseline/target khi thiếu dữ liệu; giá trị thiếu phải là `unknown`.

## 8. Dashboard

Đặc tả triển khai nằm tại [SaaS Philosophy Dashboard](../../../../dashboards/foundation/DSH-P01-C01-01-saas-philosophy.md).

| Metric | Công thức | Loại | Owner | Chu kỳ |
|---|---|---|---|---|
| Recurring value rate | accounts có recurring value event trong cửa sổ / eligible active accounts | North Star proxy | CPO | Tuần, cohort tháng |
| Activation rate | activated new accounts / eligible new accounts | Leading | Head of Product | Tuần |
| Time to first value | median(first value time − eligibility time) | Leading | Product + CS | Tuần |
| SLO attainment | good service events / valid service events | Leading trust | VP Engineering/SRE | Ngày/tuần |
| Gross revenue retention | (opening recurring revenue − churn − contraction) / opening recurring revenue | Lagging | Finance/RevOps | Tháng |
| Billing correction rate | corrected invoices / issued invoices | Guardrail | Finance Ops | Tuần/tháng |

**Baseline/target.** Không có target phổ quát. Mỗi đội phải ghi baseline theo cohort rồi phê duyệt target và red threshold trong Promise Card. `Unknown` là trạng thái hợp lệ; số không có nguồn thì không hợp lệ.

**Alert.** Cảnh báo đỏ khi vi phạm contractual/security threshold, data freshness breach, hoặc metric guardrail vượt ngưỡng đã phê duyệt. Dashboard phải hiển thị denominator, segment, freshness và definition version để tránh so sánh sai.

## 9. AI Automation

Agent specification tại [SaaS Promise Review Agent](../../../../agents/foundation/AGT-P01-C01-01-saas-promise-review-agent.md); prompt tại [SaaS Promise Review Prompt](../../../../prompts/foundation/PRM-P01-C01-01-saas-promise-review.md).

### Use case và workflow

- **Role:** tổng hợp evidence, phát hiện breach/contradiction và soạn review packet.
- **Trigger:** lịch review; alert; thay đổi Promise Card/metric definition.
- **Data sources:** tài liệu đã duyệt, metric store, incident/support system, decision log; chỉ connector được allowlist.
- **Tools/MCP:** read-only knowledge/search/analytics connectors; ticket draft tool không có quyền gửi hoặc đóng.
- **Output:** JSON có evidence links, confidence, breaches, missing data và proposed actions.
- **HITL:** owner xác nhận metric meaning; Security/Legal duyệt kết luận thuộc phạm vi của họ; executive phê duyệt thay promise hoặc risk acceptance.

### Guardrails, evaluation và observability

Agent không được suy diễn nhân quả từ tương quan, tạo target, đổi metric definition, truy cập raw PII nếu không cần, gửi customer communication hay thực thi rollback. Nội dung từ ticket/tài liệu ngoài là dữ liệu không tin cậy và không được làm thay đổi system instruction. Mỗi claim phải có source ID và thời điểm.

Đánh giá bằng bộ review packet đã được con người gán nhãn: citation precision, breach recall, unsupported-claim rate, schema validity và reviewer override rate. Chi phí được theo dõi theo mỗi packet; ROI được đánh giá bằng thời gian chuẩn bị tiết kiệm **sau khi** trừ thời gian review và remediation. Log gồm model/prompt version, source IDs, tool calls, output hash, approval và retention class; không log secret hoặc nội dung nhạy cảm không cần thiết.

## 10. Anti-Patterns

| Anti-pattern | Red flag / root cause | Cách khắc phục |
|---|---|---|
| Subscription theater | MRR tăng nhưng adoption/outcome không được đo; nhầm billing với value | Định nghĩa value event và review theo cohort |
| Feature factory | Roadmap đo bằng output; discovery tách khỏi telemetry | Gắn feature với hypothesis, guardrail và sunset rule |
| Growth over trust | Che incident/billing complaint bằng aggregate growth | Tách trust scorecard và quyền stop-the-line |
| Average customer | Chỉ xem trung bình; bỏ qua plan, segment, tenure | Luôn hiển thị denominator và cohort |
| Target without baseline | Copy benchmark không cùng bối cảnh | Đo baseline, ghi assumption, phê duyệt target nội bộ |
| AI autopilot | Agent đổi promise/metric hoặc gửi quyết định | Read-only mặc định, schema, citations và approval gate |
| Perpetual beta | Dùng “beta” để né owner/SLO/data duty | Giới hạn cohort, exit criteria, rollback và expiry date |

## 11. Checklists & Decision Trees

### Readiness checklist

- [ ] ICP, problem evidence và desired outcome đã rõ.
- [ ] First/recurring value event đo được.
- [ ] Reliability, privacy/security, support và billing promise có owner.
- [ ] Metric contract có denominator, segment, freshness và version.
- [ ] Baseline có nguồn hoặc ghi `unknown` cùng kế hoạch đo.
- [ ] Rollout, rollback, incident và communication path sẵn sàng.
- [ ] AI/data processing đã qua review phù hợp.

### Execution và review checklist

- [ ] Kiểm tra data quality trước khi diễn giải.
- [ ] So sánh cohort, không chỉ aggregate.
- [ ] Tách fact, inference và recommendation.
- [ ] Mỗi action có owner, due date và verification signal.
- [ ] Risk acceptance có accountable approver và expiry.
- [ ] Metric/promise change có version history.

### Decision tree

```text
Promise/metric có breach?
├─ Không → Data có đủ và đúng?
│  ├─ Có → Tiếp tục; chọn experiment ưu tiên theo evidence
│  └─ Không → Sửa instrumentation; không kết luận hiệu quả
└─ Có → Liên quan security/privacy/contract/billing nghiêm trọng?
   ├─ Có → Stop/contain khi cần → escalate → human decision → communicate
   └─ Không → Chỉ một cohort?
      ├─ Có → Khoanh cohort → diagnose → remediate/experiment
      └─ Không → Giảm blast radius → incident/problem review → executive trade-off
```

### Escalation matrix

| Tình huống | Accountable | Consulted | Thời hạn triage |
|---|---|---|---|
| Security/privacy suspected breach | Security executive | Legal, Product, Engineering | Theo incident policy; ngay lập tức nếu critical |
| Contractual SLO risk | CTO/VP Engineering | CPO, Support, Account owner | Trong 1 ngày làm việc hoặc sớm hơn theo hợp đồng |
| Billing correctness | CFO/Finance owner | Product, Support, Legal | Trong 1 ngày làm việc |
| Value/adoption decline | CPO | Data, CS, GTM, Engineering | Kỳ review gần nhất; ngay nếu vượt red threshold |
| AI unsupported claim | AI system owner | Domain owner, Security | Dừng phát hành packet; sửa trước review |

## 12. Case Studies

Các case dưới đây là bằng chứng minh họa, không phải benchmark hay khẳng định nhân quả.

### Startup/bootstrapped — Basecamp

- **Context/problem:** theo tường thuật chính thức, 37signals xây Basecamp để giải quyết chính vấn đề quản lý dự án của công ty thiết kế.
- **Approach/system:** đưa công cụ nội bộ ra thị trường; sau khoảng một năm, doanh thu Basecamp vượt mảng thiết kế và công ty tập trung vào sản phẩm. Shape Up sau đó mô tả nguyên tắc “fixed time, variable scope”: appetite là ràng buộc thiết kế thay vì estimate [Basecamp history](https://basecamp.com/about), [Shape Up](https://basecamp.com/shapeup/1.2-chapter-03).
- **Metrics/outcome đã công bố:** nguồn chính thức nói sản phẩm phục vụ nhu cầu tương tự của hàng chục nghìn công ty và tạo doanh thu lớn hơn mảng thiết kế; không dùng con số này làm benchmark.
- **Failure/risk:** nhu cầu nội bộ không tự động đại diện thị trường; scope linh hoạt có thể cắt nhầm outcome nếu thiếu customer evidence.
- **Bài học chuyển giao:** founder-use là nguồn hypothesis tốt; bằng chứng trả tiền và sử dụng mới là validation. Dùng appetite để bảo vệ cadence nhưng giữ quality/trust như constraint.

### Scale-up — Atlassian

- **Context/problem:** Atlassian vận hành chuyển dịch khách hàng sang cloud và xây platform kết hợp collaboration, enterprise capability và AI.
- **Approach/system:** thư cổ đông FY2025 mô tả platform như cơ chế đưa tính năng ra thị trường, cross-sell, nâng edition và tích hợp trải nghiệm.
- **Metrics/outcome đã công bố:** FY2025 đạt hơn 5,2 tỷ USD doanh thu; cloud NRR khoảng 120%; 2,3 triệu AI MAU. Đây là số do công ty báo cáo, có bối cảnh thời điểm và không chứng minh riêng một chiến thuật gây ra outcome [Atlassian Q4 FY25 shareholder letter](https://www.atlassian.com/blog/announcements/shareholder-letter-q4fy25).
- **Failure/risk:** migration nhiều năm, execution risk, margin mix và enterprise GTM complexity được chính công ty nêu trong shareholder communications.
- **Bài học chuyển giao:** platform value phải nối với adoption, retention và economics; migration cần hybrid path, risk-adjusted guidance và telemetry riêng.

### Enterprise — Adobe

- **Context/problem:** Adobe vận hành danh mục phần mềm sáng tạo và trải nghiệm số chủ yếu qua subscription/hosted offerings.
- **Approach/system:** annual report mô tả subscription revenue là phí từ subscription và hosted service; ARR được dùng để theo dõi recurring business.
- **Metrics/outcome đã công bố:** tại 28/11/2025, Total Adobe ARR xấp xỉ 25,20 tỷ USD, tăng 11,5% từ 22,61 tỷ USD; cash flow from operations FY2025 là 10,03 tỷ USD. Đây là disclosure kế toán, không phải bằng chứng rằng subscription tự nó tạo ra outcome [Adobe FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm).
- **Failure/risk:** annual report nêu cạnh tranh, đổi mới công nghệ, security/privacy và khả năng dự báo retention/renewal là các rủi ro; recurring revenue không loại bỏ chúng.
- **Bài học chuyển giao:** recurring model cần nối product adoption với revenue recognition, service obligation, trust và cash; không quản trị chỉ bằng ARR.

### AI SaaS — OpenAI ChatGPT Enterprise

- **Context/problem:** tổ chức cần khai thác AI trong công việc nhưng vẫn cần quản trị workspace, quyền truy cập, dữ liệu và compliance.
- **Approach/system:** ChatGPT Enterprise là plan được quản lý ở cấp tổ chức, có centralized administration và enterprise privacy/security controls [OpenAI Help Center](https://help.openai.com/en/articles/8265053-what-is-chatgpt-enterprise). OpenAI công bố mặc định không dùng dữ liệu business để huấn luyện model và cung cấp encryption/access/retention controls [Business data privacy](https://openai.com/business-data/).
- **Metrics/outcome đã công bố:** báo cáo enterprise AI 2025 dùng telemetry khách hàng và survey; nó mô tả hơn một triệu business customers. Vì báo cáo do nhà cung cấp tự công bố, các claim về productivity phải được xem trong phạm vi phương pháp và không dùng làm causal benchmark [OpenAI enterprise AI report](https://openai.com/index/the-state-of-enterprise-ai-2025-report/).
- **Failure/risk:** model error, prompt injection, data leakage, policy misuse, cost và thay đổi capability; control của vendor không thay thế governance của khách hàng.
- **Bài học chuyển giao:** AI value loop phải đi cùng evaluation và human override; trust loop cần identity, permissions, retention, audit và connector governance.

## 13. References

Tất cả nguồn web được kiểm tra lần cuối ngày **2026-07-21**.

### Tài liệu chính thức và paper

1. Mell, P. & Grance, T. (2011), [NIST SP 800-145 — The NIST Definition of Cloud Computing](https://doi.org/10.6028/NIST.SP.800-145).
2. Badger, L. et al. (2012), [NIST SP 800-146 — Cloud Computing Synopsis and Recommendations](https://doi.org/10.6028/NIST.SP.800-146).
3. Lusch, R. F., Vargo, S. L. & Wessels, G. (2008), [Toward a conceptual foundation for service science](https://doi.org/10.1147/sj.471.0005).
4. Vargo, S. L. & Akaka, M. A. (2009), [Service-Dominant Logic as a Foundation for Service Science](https://doi.org/10.1287/serv.1.1.32).
5. Google Cloud, [Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).
6. Basecamp, [Where we came from](https://basecamp.com/about) và [Shape Up: Set Boundaries](https://basecamp.com/shapeup/1.2-chapter-03).
7. Atlassian (2025), [Q4 FY25 shareholder letter](https://www.atlassian.com/blog/announcements/shareholder-letter-q4fy25).
8. Adobe (2026), [FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm).
9. OpenAI, [Business data privacy](https://openai.com/business-data/), [ChatGPT Enterprise overview](https://help.openai.com/en/articles/8265053-what-is-chatgpt-enterprise), [State of Enterprise AI 2025](https://openai.com/index/the-state-of-enterprise-ai-2025-report/).

### Further reading

- [Agile Manifesto](https://agilemanifesto.org/) — nền tảng cho phản hồi và phần mềm hoạt động.
- [Google SRE Book](https://sre.google/sre-book/table-of-contents/) — reliability và vận hành dịch vụ.
- Các chương tương lai: P01-C02 mở rộng company system; P01-C04 mở rộng product thinking; P01-C06 mở rộng continuous improvement; P05 và P06 sẽ chuẩn hóa metrics và economics.

### Version history

| Phiên bản | Ngày | Thay đổi |
|---|---|---|
| 0.9.0 | 2026-07-21 | Bản đầy đủ đầu tiên cho human review; thêm framework, workflow, SOP, template, dashboard, AI automation và bốn case có nguồn |
