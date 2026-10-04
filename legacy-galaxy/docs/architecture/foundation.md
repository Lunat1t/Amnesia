# Новая версия Galaxy: узкая фундаментальная основа

Galaxy пока не строит отдельную большую Core-платформу. В работе остаются пять взаимосвязанных механизмов:

1. **Context** — выбирает вероятно полезные источники для задачи и сохраняет точный пакет.
2. **Memory** — хранит структурированные факты с источником, временем и evidence.
3. **Experience** — компактно описывает исход прошлой задачи и то, чем он подтверждён.
4. **Skills / Learning** — обнаруживает повторяемые паттерны и предлагает кандидаты; promotion требует отдельной оценки.
5. **Evidence** — связывает утверждения и результаты с исходными файлами, запусками, проверками и hashes.

Codex, Claude и другие runtimes остаются исполнителями за адаптерами. Они не являются частью Galaxy memory/context storage.

## Практические ограничения

- Старый Context Compiler и retrieval pipeline сохраняются за compatibility adapter, чтобы benchmark сравнивал прежний exact context и новый наблюдаемый package.
- Experiment modules `labs/attention`, `labs/future_graph`, `labs/semantic` и `labs/memory_reconcile` не развиваются без конкретного вопроса из пяти основ.
- Отдельный Core layer, новый retrieval engine, World Model/Future Graph улучшения и большой orchestrator не входят в эту версию.
- Experience — это компактная запись outcome/provenance, а сырые action traces остаются в benchmark archive.
- Skill candidate — проверяемая гипотеза, не включённое правило.

Фактическая схема импортов, статусы и открытый долг перечислены в [current-state.md](current-state.md). Подтверждать полезность можно только фиксированными OFF/ON или experience-control экспериментами с сохранёнными evidence.
