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
