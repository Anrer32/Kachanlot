# Реестр ID: независимая часть старта IRE 1936

Область утверждения, баланс и блокеры: [START_1936.md](ireland/START_1936.md).
Все IDs ниже собственные, country scope IRE. Коллизии с недоступными vanilla/DLC
пока не проверены. Старые четыре ключа IRE остаются legacy и не назначаются.

| ID | Тип / файл-владелец | Использование |
| --- | --- | --- |
| `IRE_KLN_idea_economic_war` | country spirit, `common/ideas/IRE_KLN_ideas.txt` | init; RU/EN имя и `_desc` |
| `IRE_KLN_idea_underfunded_defence` | country spirit, `common/ideas/IRE_KLN_ideas.txt` | init; RU/EN имя и `_desc` |
| `IRE_KLN_idea_agrarian_economy` | country spirit, `common/ideas/IRE_KLN_ideas.txt` | init; RU/EN имя и `_desc` |
| `IRE_KLN_idea_civil_war_legacy` | country spirit, `common/ideas/IRE_KLN_ideas.txt` | init; RU/EN имя и `_desc` |
| `IRE_KLN_idea_incomplete_sovereignty` | country spirit, `common/ideas/IRE_KLN_ideas.txt` | init; RU/EN имя и `_desc` |
| `IRE_KLN_idea_state_industrial_policy` | country spirit, `common/ideas/IRE_KLN_ideas.txt` | init; RU/EN имя и `_desc` |
| `IRE_KLN_effect_initialize_spirits_1936` | scripted effect, `common/scripted_effects/IRE_KLN_effects.txt` | on_startup IRE; вход защищён тегом, датой и флагом |
| `IRE_KLN_flag_spirits_1936_initialized` | country flag; записывает только init | отсутствует на новом старте; устанавливается после назначения; не очищается |

Внешние зависимости: тег IRE; системный on_startup; picture tokens
`generic_production_bonus`, `generic_army_problems`, `generic_pp_unity_bonus`.
Токены картинок и modifiers имеют образцы в существующем common/ideas; спрайты
и фактическая поддержка движком требуют vanilla/игры. Не добавлены персонажи,
события, ID регионов, OOB или ссылки на предполагаемые отсутствующие объекты.

## Политический каркас по утверждённому дизайну

Полный реестр фокусов и отложенных действий:
[FOCUS_140_MANIFEST.csv](ireland/FOCUS_140_MANIFEST.csv).
Определены только `IRE_KLN_focus_P01`–`IRE_KLN_focus_P28`; остальные 112 ID
остаются резервом. Названия и родители получены из утверждённого источника.

| ID / семейство | Владелец | Состояние |
| --- | --- | --- |
| `IRE_KLN_tree_main` | `common/national_focus/IRE_KLN_focus.txt` | opt-in политический предпросмотр |
| `IRE_KLN_focus_P01`–`IRE_KLN_focus_P28` | тот же файл | определены связи, gameplay-эффекты deferred |
| `IRE_KLN_rule_focus_preview` | `common/game_rules/IRE_KLN_rules.txt` | правило, по умолчанию DISABLED |
| `IRE_KLN_rule_group` | RU/EN focus localisation | локализованная группа правила |
| `IRE_KLN_preview_disabled`, `IRE_KLN_preview_enabled` и `_desc` | RU/EN focus localisation | варианты правила |
| `IRE_KLN_tt_focus_preview` | RU/EN focus localisation | честное предупреждение вместо награды |

Параметры `DISABLED`/`ENABLED` — значения локального правила, не глобальные ID
маршрутов. У фокусов есть RU/EN ключи имени и `_desc`. Внешняя GFX-зависимость:
`GFX_goal_generic_political_pressure`, ранее используется в `usa.txt`.
Ни один выполненный preview-фокус не означает реальное принятие закона или
смену правительства. [Отчёт и ограничения](ireland/FOCUS_GRAPH_REPORT.md).
