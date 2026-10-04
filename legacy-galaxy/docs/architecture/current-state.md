# Текущее состояние архитектуры Galaxy

Дата: 2026-10-03. Назначение сверялось с реальными импортами и вызовами в CLI, MCP, Context Compiler и benchmark-коде; имя каталога само по себе не считалось доказательством назначения. После подготовки этой карты фокус новой версии сужен до Context, Memory, Experience, Skills/Learning и Evidence. Идеи крупных платформ и агентов заморожены.

## Текущий путь Codex и benchmark

```text
Codex MCP / SWE-bench A/B / парный набор
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

оценщик SWE-bench, трассы действий, журнал целостности, отчёты
```

Главное наблюдение: основной путь `get_context` — это унаследованная композиция из ContextCompiler и нескольких связанных механизмов. `ContextCompiler` непосредственно вызывает attention, World Model/Future Graph, reconciliation, память и capsules. `mcp_server.py`, CLI и benchmark runners используют эту цепочку. Она обёрнута адаптер совместимости; её внутренний pipeline сохраняется для честного сравнения и пока не заменён новой схемой поиска.

## Карта существенных компонентов

`used_by` указывает на проверяемые внутренние вызовы, а не на полный список внешних пользователей. «Зависимость бенчмарка» означает прямую зависимость текущих адаптеров бенчмарков.

| Компонент | Назначение | Зависимости / кто использует | Зависимость бенчмарка | Статус / категория |
|---|---|---|---|---|
| `galaxy_core.contracts` (обычный модуль) | событие, ссылка на состояние, опыт, доказательство, пакет/протокол контекста | Только стандартная библиотека; используется адаптером интеграции | Метаданные пакета совместимы с отчётами | Небольшие объекты-значения и протокол, без отдельного слоя runtime |
| `galaxy_core.event_log.JsonlEventJournal` (обычный модуль) | Небольшой журнал нормализованных событий только для добавления | Только стандартная библиотека и контракт Event; пока не заменяет старые журналы | Не является журналом оценщика | Вспомогательный модуль; ещё не подключён к источникам событий задач/агента/оценщика |
| `galaxy_core.brain.memory.MemoryStore` | Хранилище SQLite для структурированных воспоминаний, источника, хеша источника, уверенности, статуса и аудиторских редакций | Стандартная библиотека/SQLite; фасад BrainStore, CLI, тесты памяти | Косвенно через ContextCompiler | Кандидат основы Memory; новые записи получают явное происхождение manual/run/legacy |
| `galaxy_core.brain.store.BrainStore` | Объединяет MemoryStore с семантическим индексом, графом сущностей, целями и консолидацией | MemoryStore + labs.semantic + graph/consolidation; ContextCompiler и CLI | Косвенно через ContextCompiler | УНАСЛЕДОВАННЫЙ/экспериментальный фасад; не эквивалентен простой модели Memory |
| `galaxy_core.context.experience.ExperienceStore` | Эпизоды задач со ссылками на доказательства, поиск, отзыв, обнаружение повторяющихся успешных паттернов | stdlib + SQLite; ContextCompiler, suite и experience-bench adapters | Да: continuity/experience benchmarks | Основа Experience уже используется; постоянная схема остаётся в `context/` |
| `galaxy_core.engine.verification.VerificationStore` | Логи проверок, хеши и проверяемость доказательств запусков | storage helpers; autonomy engine | Для целостности бенчмарков используется отдельный путь и собственные артефакты | Компонент инструментов выполнения; автоматически не входит в новый путь основы |
| `galaxy_core.skills` (новый) | Объекты-значения Skill/SkillCandidate, жизненный цикл с проверкой доказательств, точное обнаружение повторяющихся уроков в независимом опыте | `contracts.EvidenceRef`; без модели и базы данных | Пока не входит в путь бенчмарка задач | Узкая основа Skills/Learning; результат остаётся кандидатом до проверки/оценки |
| `galaxy_core.integrations.legacy_context` | Совместимый перевод legacy ContextPacket в explicit ContextPackage; сохраняет исходный Markdown и описи | Импортирует `contracts.py` и legacy ContextCompiler | Да: MCP, SWE-bench, paired suite | ИНТЕГРАЦИЯ / граница совместимости |
| `galaxy_core.context.compiler.ContextCompiler` | Полная сборка контекста, кэш и оркестрация поиска/состояния | `attention`, `world`, `brain`, experience, capsules; MCP, CLI, suite, SWE-bench и другие benches | Да, центральная зависимость режима ON | УНАСЛЕДОВАННАЯ реализация за границей совместимости; алгоритмы ниже помечены как экспериментальные |
| `galaxy_core.context.capsules` | Карты компонентов из WorldSnapshot | `world.models`; ContextCompiler | Через ContextCompiler | ЭКСПЕРИМЕНТАЛЬНЫЙ вспомогательный механизм; пока остаётся на пути совместимости |
| `galaxy_core.labs.attention` | Гибридное ранжирование кандидатов, векторные представления, расширение графа, фильтры, распределение бюджета | `world`, `labs.semantic`, `labs.future_graph`; ContextCompiler, kernel, retrieval benchmarks | Да, прямо или через ContextCompiler | ЭКСПЕРИМЕНТАЛЬНЫЙ механизм поиска; реализация физически изолирована, старый `galaxy_core.attention.*` — фасад |
| `galaxy_core.world.scanner/models/model` | Структурный snapshot репозитория и обновления состояния | filesystem, SQLite, `world.events`; ContextCompiler, kernel, CLI | Косвенно через ContextCompiler | Унаследованная/экспериментальная реализация состояния проекта; заморожена вне узкого объёма |
| `galaxy_core.labs.future_graph` | Ограниченное структурное влияние/Future Graph | WorldSnapshot; Attention, ContextCompiler, CLI | Косвенно | ЭКСПЕРИМЕНТАЛЬНЫЙ; реализация изолирована, `galaxy_core.world.future` — facade |
| `galaxy_core.world.drift` | Сравнения структурного дрейфа | WorldSnapshot; world model/CLI | Нет прямой зависимости | ЭКСПЕРИМЕНТАЛЬНЫЙ / диагностический |
| `galaxy_core.world.events.WorldEventLog` | Лента изменений World Model на SQLite | `world.model` | Нет прямой зависимости | УНАСЛЕДОВАННЫЙ узкий журнал событий; не общий контракт задач/событий |
| `galaxy_core.labs.memory_reconcile` | Проверки устаревания и конфликтов памяти | BrainStore; ContextCompiler, CLI | Косвенно | ЭКСПЕРИМЕНТАЛЬНЫЙ механизм анализа доказательств; старый путь импорта — фасад |
| `galaxy_core.labs.semantic` | Переносимые семантические векторные представления | Attention Engine | Через retrieval | ЭКСПЕРИМЕНТАЛЬНЫЙ; старый путь импорта — фасад |
| `galaxy_core.kernel` | Наблюдатель/проектор поверх World Model и Attention | world + attention + capsules; CLI | Отдельные замеры есть, основной SWE harness не зависит | EXPERIMENTAL |
| `galaxy_core.engine.planning`, `engine.autonomy*`, `agents` | Планирование DAG, исполнение, роли, модели и изолированные workspaces | providers, policy, storage, verification; CLI | Не используется SWE-bench codex executor | ЭКСПЕРИМЕНТАЛЬНЫЙ runtime / возможная будущая интеграция Codex |
| `galaxy_core.engine.decisions` | Узкая вероятностная система принятия решений | provider/model adapters, deterministic policy | Нет | EXPERIMENTAL |
| `galaxy_core.providers` | Совместимые с OpenAI адаптеры провайдера для локальных и унаследованных CLI | HTTP/local processes; planning/discovery | Нет | INTEGRATION |
| `galaxy_core.discovery` | Опрос/интервью Grill, обнаружение DAG, исследование провайдера | providers, brain, storage; CLI | Нет | ЭКСПЕРИМЕНТАЛЬНАЯ поверхность продукта |
| `galaxy_core.vault` | Заметки Markdown, ссылки, локальный граф заметок | filesystem + SQLite; optional CLI commands | Нет | УНАСЛЕДОВАННАЯ/экспериментальная смежная область; вне текущего узкого объёма |
| `galaxy_core.benchmark` | Средства запуска OFF/ON, ContextBench, адаптеры experience/repo/SWE, отчёты о траекториях/доказательствах | codex, datasets/SWE-bench optional deps, context interfaces | Сама инфраструктура бенчмарков | ИНТЕГРАЦИЯ / средства оценки |
| `galaxy_core.mcp_server` | MCP endpoint `get_context` только для чтения | `ContextCompiler` через integration adapter; MCP SDK | Воспроизводится дымовыми тестами MCP | ИНТЕГРАЦИЯ, основной текущий путь Codex |
| `galaxy.py` | Композиция CLI/корневая точка входа | Импортирует compiler, brain, world, engine, attention, discovery, providers и vault по командам | CLI может запускать бенчмарк | INTEGRATION / унаследованная композиция root |

## Граница новой версии

Мы не создаём отдельную Galaxy Core архитектуру. В обычных модулях `contracts.py` и `event_log.py` лежат только небольшие value objects и append utility. Они не импортируют retrieval, World Model, providers, модели, MCP или benchmark evaluator. Основной продуктовый фокус версии: Context, Memory, Experience, Skills/Learning и Evidence.

Текущая реализация сборки контекста остаётся за `galaxy_core.integrations.legacy_context`. Это совместимый переходный адаптер, сохраняющий backend, точный отрендеренный текст, выбранные файлы, хеш контекста и артефакты оценщика. В элементе контекста явно указано, что источник — отправная точка, а не гарантия того, что решение находится в этом месте.

## Выявленные реальные зависимости

- `galaxy_core.contracts` и `event_log` остаются обычными stdlib-only модулями; адаптеры, специфичные для runtime могут их импортировать.
- Контрактные модули не импортируют `labs`, `attention`, `world`, `brain`, `engine`, CLI, MCP или benchmark.
- Legacy ContextCompiler всё ещё вызывает Attention Engine, World Model/Future Graph, BrainStore/Reconciler, ExperienceStore и CapsuleStore. Этот путь намеренно сохранён за явным адаптер совместимости; изоляция не означает, что текущий MCP backend уже перестал использовать эти experiments.
- `ContextBench` и `RepoBench-R` вызывают Attention напрямую, потому что измеряют сам retriever; их следует считать экспериментальными evaluator adapters, а не product runtime.
- `WorldEventLog` обслуживает только World Model и не является общим журналом действий агента или benchmark.
- SWE-bench хранит собственные `manifest.json`, `context.md`, `context-items.json`, `trajectory.jsonl`, evaluator logs, report hashes и leakage audit. Эти данные остаются вне нового JSONL event journal.
- Primary paired suite и SWE-bench формируют компактный `experience.json`; туда входят outcome, сводка числа действий, task/run IDs и hashes/ссылки на evidence. Исходная трассировка остаётся отдельным архивом.
- `ExperienceStore.patterns()` уже находит одинаковые verified-success lessons с различными run IDs; новый `skills.py` формирует evidence-backed кандидаты, но не добавляет их к context и не активирует.

## Переиспользование и состояние функций

1. Существующие package paths (`context`, `attention`, `world`, `brain`) публично импортируются CLI, тестами и benchmark scripts; compatibility facades нужны для миграции.
2. `ContextCompiler` совмещает orchestration, retrieval, сбор памяти, cache и rendering. Менять алгоритм без benchmark причины нельзя.
3. `ExperienceStore` по смыслу относится к Experience, но находится в `context/`; пока сохраняем путь.
4. Evidence имеет несколько форматов: verification ledger, context source provenance, benchmark run artifacts и world events. Они не объединяются автоматически.
5. `ContextPackage.reason` и `confidence` описывают provenance конкретного item. Они не утверждают, что item полезен или что решение находится в его файле.
6. Нормализованная сущность не извлекается отдельно от символов/путей; symbols нельзя выдавать за отдельное entity knowledge.
7. `galaxy_core.labs` содержит Attention Engine, Future Graph, semantic embedder и memory reconciliation. Agent runtime, Discovery/Grill, kernel, Vault и capsules не участвуют в обязательном узком 5-part объём продукта и заморожены, если их изменение не нужно для этих пяти основ.
8. Новый `SkillCandidate` пока является предложение в памяти процесса; постоянный реестр Skill и процесс проверки на отложенных задачах требуют отдельного benchmark-запроса.

## Ограничения точки А

- `ContextPackage` — обёртка аудита над прежним ContextPacket. Новый retrieval/ranking алгоритм не внедрён; внешний MCP-вызов пока не передаёт отдельный `task_id`.
- В benchmark `context-items.json` связывает переданные пути с открытиями и изменениями, наблюдаемыми в Codex trace. Это наблюдение на уровне путей, не доказательство семантическая полезность.
- Не все способы чтения файлов раскрываются в trace parser, поэтому отсутствие совпадения не доказывает, что агент не видел содержимое.
- `Experience` JSON артефакт компактен и с привязкой к доказательствам. Автоматический transfer из произвольных SWE-bench runs в будущие задачи не заявлен.
- `skills.py` группирует точные повторяющиеся lessons с разными run IDs и создаёт кандидаты в памяти процесса; persistence, semantic clustering и оркестрация проверки кандидатов бенчмарками не реализованы.
- ExperienceBench v0.1 — отдельный трёхрукавный экспериментальный runner с контролируемым датасетом; он требует калибровочный/зафиксированный запуск и не доказывает общий benefit.
- `.git` в текущем каталоге — пустая директория без метаданные Git. `git status`, HEAD и diff для этого checkout получить не удалось; каталог не переинициализировался.
