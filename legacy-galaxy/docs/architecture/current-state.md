# Текущее состояние архитектуры Galaxy

Дата: 2026-10-03. Назначение сверялось с реальными импортами и вызовами в CLI, MCP, Context Compiler и benchmark-коде; имя каталога само по себе не считалось доказательством назначения. После подготовки этой карты focus новой версии сужен до Context, Memory, Experience, Skills/Learning и Evidence. Большие platform/agent ideas заморожены.

## Текущий путь Codex и benchmark

```text
Codex MCP / SWE-bench A/B / paired suite
                  │
                  ▼
       galaxy_core.integrations.legacy_context
                  │
                  ▼
       galaxy_core.context.ContextCompiler
          ├── brain.store / brain.reconcile
          ├── context.experience / capsules
          ├── attention.AttentionEngine
          │      ├── brain.semantic.PortableEmbedder
          │      └── world.FutureGraph / WorldSnapshot
          └── world.ProjectWorldModel / scanner

SWE-bench evaluator, action traces, integrity ledger, reports
```

Главное наблюдение: основной путь `get_context` — это legacy composition из ContextCompiler и нескольких связанных механизмов. `ContextCompiler` непосредственно вызывает attention, World Model/Future Graph, reconciliation, память и capsules. `mcp_server.py`, CLI и benchmark runners используют эту цепочку. Она обёрнута compatibility adapter; её внутренний pipeline сохраняется для честного сравнения и пока не заменён новой retrieval схемой.

## Карта существенных компонентов

`used_by` указывает на проверяемые внутренние вызовы, а не полный список сторонних пользователей. «Benchmark dependency» означает прямую зависимость текущих benchmark adapters.

| Component | Purpose | Dependencies / used by | Benchmark dependency | Status / category |
|---|---|---|---|---|
| `galaxy_core.contracts` (обычный модуль) | Event, state reference, experience, evidence, context package/protocol | Только stdlib; используется integration adapter | Метаданные пакета совместимы с отчётами | Малые value objects и protocol, без отдельного runtime слоя |
| `galaxy_core.event_log.JsonlEventJournal` (обычный модуль) | Малый append-only журнал нормализованных событий | Только stdlib + Event contract; пока не заменяет старые журналы | Не является evaluator ledger | Utility module; ещё не подключён к task/agent/evaluator event sources |
| `galaxy_core.brain.memory.MemoryStore` | SQLite store для структурированных memories, источника, source hash, confidence, статуса и audit revisions | stdlib/SQLite; facade BrainStore, CLI, memory tests | Косвенно через ContextCompiler | Memory foundation candidate; новые записи получают explicit manual/run/legacy origin |
| `galaxy_core.brain.store.BrainStore` | Совмещает MemoryStore с semantic index, entity graph, goals и consolidation | MemoryStore + labs.semantic + graph/consolidation; ContextCompiler и CLI | Косвенно через ContextCompiler | LEGACY/experimental facade; не равен простой Memory модели |
| `galaxy_core.context.experience.ExperienceStore` | Evidence-linked task episodes, retrieval, retract, repeat-success pattern detection | stdlib + SQLite; ContextCompiler, suite и experience-bench adapters | Да: continuity/experience benchmarks | Experience foundation already used; persistent schema remains in `context/` |
| `galaxy_core.engine.verification.VerificationStore` | Логи проверок, хеши и проверяемость доказательств запусков | storage helpers; autonomy engine | Benchmark integrity использует отдельный путь и свои artifacts | Execution-tooling component; не входит автоматически в новый foundation path |
| `galaxy_core.skills` (новый) | Skill/SkillCandidate value objects, evidence-gated lifecycle, exact repeated-lesson detection from independent experiences | `contracts.EvidenceRef`; no model and no database | Not yet in task benchmark path | Narrow Skills/Learning foundation; output stays candidate until reviewed/evaluated |
| `galaxy_core.integrations.legacy_context` | Совместимый перевод legacy ContextPacket в explicit ContextPackage; сохраняет исходный markdown and inventories | Импортирует `contracts.py` и legacy ContextCompiler | Да: MCP, SWE-bench, paired suite | INTEGRATION / compatibility boundary |
| `galaxy_core.context.compiler.ContextCompiler` | Полный сбор контекста, кэш и orchestration retrieval/state | `attention`, `world`, `brain`, experience, capsules; MCP, CLI, suite, SWE-bench и другие benches | Да, центральная зависимость ON | LEGACY implementation за compatibility boundary; алгоритмы ниже помечены experimental |
| `galaxy_core.context.capsules` | Component maps из WorldSnapshot | `world.models`; ContextCompiler | Через ContextCompiler | EXPERIMENTAL supporting mechanism; пока остаётся по compatibility path |
| `galaxy_core.labs.attention` | Hybrid candidate ranking, embeddings, graph expansion, gates, budgeting | `world`, `labs.semantic`, `labs.future_graph`; ContextCompiler, kernel, retrieval benchmarks | Да, прямо или через ContextCompiler | EXPERIMENTAL retrieval mechanism; implementation физически изолирован, старый `galaxy_core.attention.*` — facade |
| `galaxy_core.world.scanner/models/model` | Структурный snapshot репозитория и обновления состояния | filesystem, SQLite, `world.events`; ContextCompiler, kernel, CLI | Косвенно через ContextCompiler | Legacy/experimental project-state implementation; заморожена вне узкого scope |
| `galaxy_core.labs.future_graph` | Bounded structural impact/Future Graph | WorldSnapshot; Attention, ContextCompiler, CLI | Косвенно | EXPERIMENTAL; implementation изолирован, `galaxy_core.world.future` — facade |
| `galaxy_core.world.drift` | Structural drift comparisons | WorldSnapshot; world model/CLI | Нет прямой зависимости | EXPERIMENTAL / diagnostic |
| `galaxy_core.world.events.WorldEventLog` | SQLite change feed для World Model | `world.model` | Нет прямой зависимости | LEGACY narrow event log; не общий task/event contract |
| `galaxy_core.labs.memory_reconcile` | Проверки устаревания и конфликтов memory | BrainStore; ContextCompiler, CLI | Косвенно | EXPERIMENTAL evidence-analysis mechanism; old import path — facade |
| `galaxy_core.labs.semantic` | Portable semantic embeddings | Attention Engine | Через retrieval | EXPERIMENTAL; old import path — facade |
| `galaxy_core.kernel` | Watch/projector поверх World Model и Attention | world + attention + capsules; CLI | Отдельные замеры есть, основной SWE harness не зависит | EXPERIMENTAL |
| `galaxy_core.engine.planning`, `engine.autonomy*`, `agents` | Планирование DAG, исполнение, роли, модели и изолированные workspaces | providers, policy, storage, verification; CLI | Не используется SWE-bench codex executor | EXPERIMENTAL runtime / возможные будущие Codex integration |
| `galaxy_core.engine.decisions` | Narrow probabilistic decision fabric | provider/model adapters, deterministic policy | Нет | EXPERIMENTAL |
| `galaxy_core.providers` | OpenAI-compatible, local и legacy CLI provider adapters | HTTP/local processes; planning/discovery | Нет | INTEGRATION |
| `galaxy_core.discovery` | Grill/interview, DAG discovery, provider research | providers, brain, storage; CLI | Нет | EXPERIMENTAL product surface |
| `galaxy_core.vault` | Markdown notes, links, local note graph | filesystem + SQLite; optional CLI commands | Нет | LEGACY/experimental adjacent surface; вне текущего узкого scope |
| `galaxy_core.benchmark` | OFF/ON runners, ContextBench, experience/repo/SWE adapters, trajectory/evidence reports | codex, datasets/SWE-bench optional deps, context interfaces | Сама benchmark infrastructure | INTEGRATION / evaluation tooling |
| `galaxy_core.mcp_server` | Read-only `get_context` MCP endpoint | `ContextCompiler` через integration adapter; MCP SDK | Воспроизводится MCP smoke tests | INTEGRATION, главный текущий Codex path |
| `galaxy.py` | CLI composition/root entrypoint | Импортирует compiler, brain, world, engine, attention, discovery, providers и vault по командам | CLI может запускать benchmark | INTEGRATION / legacy composition root |

## Граница новой версии

Мы не создаём отдельную Galaxy Core архитектуру. В обычных модулях `contracts.py` и `event_log.py` лежат только небольшие value objects и append utility. Они не импортируют retrieval, World Model, providers, модели, MCP или benchmark evaluator. Основной продуктовый фокус версии: Context, Memory, Experience, Skills/Learning и Evidence.

Текущая реализация сборки контекста остаётся за `galaxy_core.integrations.legacy_context`. Это совместимый переходный адаптер, сохраняющий backend, точный rendered text, выбранные файлы, context hash и evaluator artifacts. В context item явно указано, что source — starting point, а не гарантия места решения.

## Выявленные реальные зависимости

- `galaxy_core.contracts` и `event_log` остаются обычными stdlib-only модулями; runtime-specific adapters могут их импортировать.
- Контрактные модули не импортируют `labs`, `attention`, `world`, `brain`, `engine`, CLI, MCP или benchmark.
- Legacy ContextCompiler всё ещё вызывает Attention Engine, World Model/Future Graph, BrainStore/Reconciler, ExperienceStore и CapsuleStore. Этот путь намеренно сохранён за явным compatibility adapter; isolation не означает, что текущий MCP backend уже перестал использовать эти experiments.
- `ContextBench` и `RepoBench-R` вызывают Attention напрямую, потому что измеряют сам retriever; их следует считать экспериментальными evaluator adapters, а не product runtime.
- `WorldEventLog` обслуживает только World Model и не является общим журналом действий агента или benchmark.
- SWE-bench хранит собственные `manifest.json`, `context.md`, `context-items.json`, `trajectory.jsonl`, evaluator logs, report hashes и leakage audit. Эти данные остаются вне нового JSONL event journal.
- Primary paired suite и SWE-bench формируют compact `experience.json`; туда входят outcome, action-count summary, task/run IDs и hashes/ссылки на evidence. Raw trace остаётся отдельным архивом.
- `ExperienceStore.patterns()` уже находит одинаковые verified-success lessons с различными run IDs; новый `skills.py` формирует evidence-backed кандидаты, но не добавляет их к context и не активирует.

## Переиспользование и состояние функций

1. Существующие package paths (`context`, `attention`, `world`, `brain`) публично импортируются CLI, тестами и benchmark scripts; compatibility facades нужны для миграции.
2. `ContextCompiler` совмещает orchestration, retrieval, сбор памяти, cache и rendering. Менять алгоритм без benchmark причины нельзя.
3. `ExperienceStore` по смыслу относится к Experience, но находится в `context/`; пока сохраняем путь.
4. Evidence имеет несколько форматов: verification ledger, context source provenance, benchmark run artifacts и world events. Они не объединяются автоматически.
5. `ContextPackage.reason` и `confidence` описывают provenance конкретного item. Они не утверждают, что item полезен или что решение находится в его файле.
6. Нормализованная сущность не извлекается отдельно от символов/путей; symbols нельзя выдавать за отдельное entity knowledge.
7. `galaxy_core.labs` содержит Attention Engine, Future Graph, semantic embedder и memory reconciliation. Agent runtime, Discovery/Grill, kernel, Vault и capsules не участвуют в обязательном узком 5-part product scope и заморожены, если их изменение не нужно для этих пяти основ.
8. Новый `SkillCandidate` пока является in-memory proposal; persistent Skill registry и held-out validation workflow требуют отдельного benchmark-запроса.

## Ограничения точки А

- `ContextPackage` — audit wrapper над прежним ContextPacket. Новый retrieval/ranking алгоритм не внедрён; внешний MCP-вызов пока не передаёт отдельный `task_id`.
- В benchmark `context-items.json` связывает переданные пути с открытиями и изменениями, наблюдаемыми в Codex trace. Это path-level observation, не доказательство semantic usefulness.
- Не все способы чтения файлов раскрываются в trace parser, поэтому отсутствие совпадения не доказывает, что агент не видел содержимое.
- `Experience` JSON артефакт компактен и evidence-linked. Автоматический transfer из произвольных SWE-bench runs в будущие задачи не заявлен.
- `skills.py` группирует точные повторяющиеся lessons с разными run IDs и создаёт кандидаты в памяти процесса; persistence, semantic clustering и candidate-to-benchmark orchestration не реализованы.
- ExperienceBench v0.1 — отдельный трёхрукавный экспериментальный runner с контролируемым датасетом; он требует calibration/frozen run и не доказывает общий benefit.
- `.git` в текущем каталоге — пустая директория без Git metadata. `git status`, HEAD и diff для этого checkout получить не удалось; каталог не переинициализировался.
