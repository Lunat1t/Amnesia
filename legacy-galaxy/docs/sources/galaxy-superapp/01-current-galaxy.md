# Источники: текущее состояние Galaxy

Это внутренние документы репозитория. Они описывают существующую реализацию и её границы; roadmap ссылается на них при описании точки А и технической последовательности.

## Реализованное ядро и архитектура

- [`docs/core-architecture.md`](../../core-architecture.md) — архивное описание World Model, drift, Future Graph, Attention, Context Compiler, решений и execution; это не активная архитектурная цель.
- [`README.md`](../../../README.md) — версия `3.2.1-alpha.19-evidence-integrity`, CLI, MCP `get_context`, локальная установка, опытные функции и известные пределы.
- [`docs/v4-roadmap.md`](../../v4-roadmap.md) — исторический план Core 4.0; новая версия следует узкому scope Context, Memory, Experience, Skills/Learning и Evidence.
- [`docs/architecture/current-state.md`](../../architecture/current-state.md) и [узкий scope основы](../../architecture/foundation.md) — карта фактической реализации, legacy/experimental компонентов и новой версии с фокусом на Context, Memory, Experience, Skills/Learning и Evidence. Старый Context Compiler по-прежнему использует experiment modules.

## Проверки и доказательства

- [`docs/core-v0.1-contract.md`](../../core-v0.1-contract.md) — контракт для проверки, помогает ли опыт прошлых запусков последующим независимым задачам; задаёт paired baseline, изоляцию и метрики.
- [`docs/evidence-integrity-alpha.19.md`](../../evidence-integrity-alpha.19.md) — что именно проверяет verification ledger и какие ограничения целостности остаются.
- [`docs/experience-bench-v0.1.md`](../../experience-bench-v0.1.md) — протокол анализа опыта и контекста; явно оговаривает, что retrieval/packet analysis сам по себе не доказывает успешность изменений кода.

## Прямые следствия для roadmap

- Точка А — локальное, ориентированное на код ядро, а не готовый SaaS или Obsidian-подобное приложение.
- Уже существуют гибридный retrieval, Context Compiler, локальная память, DAG execution и один read-only MCP tool; это не означает завершённую проверку их продуктового эффекта.
- Нельзя называть текущие локальные строки owner/team/reviewer аутентификацией или гарантией multi-tenant безопасности.
- Следующий шаг — закрыть измеримые пробелы качества и пользы на реальных задачах до крупного UI/SaaS строительства.

## Калибровка передачи опыта 2026-10-03

[CSV transfer pilot](../../experience-transfer-v1.md) проверил цепочку verified
Task A → Experience → Task B и отдельный context-only контроль. В одном запуске
B получил один Experience A; прочие context items совпали с контролем, verifier
logs прошли SHA-256 audit. B прошёл во всех условиях, поэтому улучшение успешности
не установлено. Paired suite поддерживает opt-in `use_prior_experience: false`;
обычный legacy OFF/ON путь сохраняет прежнее значение по умолчанию.

[Transfer v2](../../experience-transfer-v2.md) завершил ещё 18 калибровочных
agent task runs на трёх независимых синтетических парах. Доставка опыта и
контроли прошли audit, но успешность B не улучшилась; разница agent tokens
смешанная. Paired metrics теперь сохраняют `agent_usage`/`agent_duration_ms`
отдельно от `experience_extraction_usage`/`experience_extraction_ms`, сохраняя
legacy combined totals. Это калибровка pipeline, не доказательство пользы 5.0.

## Real-repository Experience challenge

[Протокол](../../real-experience-transfer-v1.md) выбирает настоящие независимые
SymPy maintenance-задачи из локального SWE-bench import. Добавлены opt-in
control/relevant/irrelevant/obsolete exposure к существующему SWE adapter,
evidence-gated extraction и отдельный native retrieval replay. Проверены source
commits, clean snapshots и hidden evaluator hashes. Новые model outcomes ещё
не измерены; task evaluator images и настоящие source/supersession episodes
остаются prerequisites. Обsolete нельзя выводить только из возраста записи.
