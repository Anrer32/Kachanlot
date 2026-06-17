NDefines.NMilitary.MAX_DIVISION_SUPPORT_HEIGHT = 7
NDefines.NMilitary.MIN_DIVISION_BRIGADE_HEIGHT = 5



NDefines.NMilitary.UNIT_LEADER_ASSIGN_TRAIT_COST = 0
NDefines.NMilitary.CORPS_COMMANDER_DIVISIONS_CAP = 216
NDefines.NMilitary.FIELD_MARSHAL_DIVISIONS_CAP = 216
NDefines.NMilitary.GARRISON_ORDER_ARMY_CAP_FACTOR = 1.0

NDefines.NMilitary.DEPLOY_TRAINING_MAX_LEVEL = 2
NDefines.NMilitary.RELIABILTY_RECOVERY = 0.0 -- нерф абуза снаряги
NDefines.NMilitary.EQUIPMENT_COMBAT_LOSS_FACTOR = 0.7
NDefines.NCountry.EQUIPMENT_UPGRADE_CHUNK_MAX_SIZE = 100
NDefines.NCountry.REINFORCEMENT_EQUIPMENT_DELIVERY_SPEED = 100
NDefines.NCountry.REINFORCEMENT_MANPOWER_DELIVERY_SPEED = 200.0
NDefines.NCountry.SPECIAL_FORCES_CAP_MIN = 100000;	
	NDefines.NCountry.SCORCHED_EARTH_STATE_COST = 40			
NDefines.NMilitary.LAND_SPEED_MODIFIER = 0.032                  
NDefines.NMilitary.INFRASTRUCTURE_MOVEMENT_SPEED_IMPACT = -0.02;
NDefines.NMilitary.TRAINING_ATTRITION = 0.00
NDefines.NMilitary.EQUIPMENT_COMBAT_LOSS_FACTOR = 0.49
NDefines.NMilitary.PLANNING_MAX = 0.15
NDefines.NMilitary.EXPERIENCE_LOSS_FACTOR = 0.01
NDefines.NMilitary.ARMOR_VS_AVERAGE = 0 --vanilla 0.4  | eventually armor will be reworked when paradox finally releases their armor rework
NDefines.NMilitary.PEN_VS_AVERAGE = 0

---- Воздух
NDefines.NAir.PORT_STRIKE_DAMAGE_FACTOR = 1.7
NDefines.NAir.PORT_STRIKE_DAMAGE_FACTOR = 1.7
NDefines.NAir.NAVAL_STRIKE_DAMAGE_TO_STR = 1.7 -- бафф морбобров по дамагу
NDefines.NAir.NAVAL_STRIKE_DAMAGE_TO_ORG = 2.55 -- бафф морбобров по дамагу по организации
NDefines.NAir.AIR_WING_FLIGHT_SPEED_MULT = 0.1

NDefines.NAir.AIR_DEPLOYMENT_DAYS = 0 -- мгновенная развёрстка крыльев
NDefines.NAir.COMBAT_DAMAGE_SCALE = 0.3
NDefines.NAir.AIR_WING_MAX_STATS_ATTACK = 2000
NDefines.NAir.AIR_WING_ATTACK_LOGISTICS_RAILWAY_DAMAGE_SPILL_FACTOR = 0 
NDefines.NAir.AIR_WING_ATTACK_LOGISTICS_RAILWAY_DAMAGE_SPILL_FACTOR	= 0

NDefines.NAir.AIR_WING_ATTACK_LOGISTICS_INFRA_DAMAGE_SPILL_FACTOR	= 0
NDefines.NAir.AIR_WING_ATTACK_LOGISTICS_TRAIN_DAMAGE_FACTOR = 0 

NDefines.NAir.AIR_WING_ATTACK_LOGISTICS_DISRUPTION_MIN_DAMAGE_FACTOR = 0 
NDefines.NAir.AIR_WING_ATTACK_LOGISTICS_MAX_DISRUPTION_DAMAGE_TO_CONSIDER = 0

NDefines.NAir.AIR_WING_ATTACK_LOGISTICS_DIRECT_DISRUPTION_DAMAGE_FACTOR	 =  0
NDefines.NAir.AIR_WING_ATTACK_LOGISTICS_TRUCK_MAX_FACTOR = 0 
NDefines.NAir.NAVAL_STRIKE_CARRIER_MULTIPLIER = 14
NDefines.NMilitary.LAND_AIR_COMBAT_STR_DAMAGE_MODIFIER = 0.098   -- модификаторы на урон касами
NDefines.NMilitary.LAND_AIR_COMBAT_ORG_DAMAGE_MODIFIER = 0.062    -- 
NDefines.NMilitary.LAND_AIR_COMBAT_MAX_PLANES_PER_ENEMY_WIDTH = 0.4 -- зависимость количества влёта касов в бой от шф
NDefines.NAir.DISRUPTION_FACTOR = 6  
NDefines.NAir.ESCORT_FACTOR = 1
NDefines.NAir.DISRUPTION_DEFENCE_SPEED_FACTOR = 500
NDefines.NMilitary.ANTI_AIR_TARGETTING_TO_CHANCE = 0.05
NDefines.NMilitary.LAND_COMBAT_ORG_ARMOR_DEFLECTION_FACTOR = 0.5 -- damage reduction if armor outclassing enemy, will look at increasing if AT is too deadly to org. 
NDefines.NMilitary.LAND_COMBAT_STR_ARMOR_DEFLECTION_FACTOR = 0.8
NDefines.NMilitary.LAND_COMBAT_STR_DAMAGE_MODIFIER = 0.098 -- 0.06
NDefines.NMilitary.REINFORCEMENT_REQUEST_MAX_WAITING_DAYS = 1  -- Every X days the equipment will be sent, regardless if still didn't produced all that has been requested.
NDefines.NMilitary.REINFORCEMENT_REQUEST_DAYS_FREQUENCY = 1
NDefines.NMilitary.REINFORCE_CHANCE = 0.03
NDefines.NMilitary.SPEED_REINFORCEMENT_BONUS = 0.7
NDefines.NMilitary.ARMY_INITIATIVE_REINFORCE_FACTOR = 0.15
NDefines.NMilitary.PLANNING_DECAY = 0.1
NDefines.NMilitary.PLAN_STICKINESS_FACTOR = 20.0

NDefines.NAir.AA_INDUSTRY_AIR_DAMAGE_FACTOR = -0.036
NDefines.NAir.AIR_WING_MAX_STATS_BOMBING = 50000
NDefines.NNavy.SHORE_BOMBARDMENT_CAP = 0.35

----- Море


NDefines.NNavy.LEADER_EXPERIENCE_SCALE = 0.0
NDefines.NNavy.NAVAL_STRIKE_CARRIER_MULTIPLIER = 9.0
NDefines.NNavy.ANTI_AIR_MULT_ON_INCOMING_AIR_DAMAGE = 0.25

NDefines.NNavy.TRAINING_ACCIDENT_CHANCES = 0.00 --- кораблики не ломаются на тренировке

NDefines.NNavy.NAVAL_COMBAT_AIR_CAPITAL_TARGET_SCORE = 200 -- Попадание Авиков по линейке
NDefines.NNavy.NAVAL_COMBAT_AIR_CARRIER_TARGET_SCORE = 1 -- попадание авиков по авикам
NDefines.NProduction.CAPITAL_SHIP_MAX_NAV_FACTORIES_PER_LINE = 50
NDefines.NProduction.DEFAULT_MAX_NAV_FACTORIES_PER_LINE = 50
NDefines.NProduction.CONVOY_MAX_NAV_FACTORIES_PER_LINE = 50
NDefines.NNavy.SUPPLY_NEED_FACTOR = 1.5
NDefines.NNavy.NAVAL_MINES_IN_REGION_MAX = 1.0
NDefines.NNavy.NAVAL_MINES_PLANTING_SPEED_MULT = 0.00001
NDefines.NNavy.RELATIVE_SURFACE_DETECTION_TO_POSITIONING_FACTOR = 0.01 -- увеличивает обнаружение между 2 флотами, сторона с большим обнаружением получает бонус
NDefines.NNavy.MAX_POSITIONING_BONUS_FROM_SURFACE_DETECTION = 0.0 -- уменьшает бонус от обнаружения
NDefines.NNavy.AGGRESSION_TORPEDO_EFFICIENCY_ON_HEAVY_SHIPS = 1.1 -- приоритет атаки торпед по тяжам
NDefines.NNavy.AGGRESSION_TORPEDO_EFFICIENCY_ON_LIGHT_SHIPS = 0.01 -- приоритет атаки торпед по лт флоту

NDefines.NNavy.GUN_HIT_PROFILES = { -- hit profiles for guns, if target ih profile is lower the gun will have lower accuracy
		41.0,	-- big guns
		60.0,	-- torpedoes
		10.0,	-- small guns
	}
-- Асы удалены

NDefines.NAir.ACE_DEATH_CHANCE_BASE = 0
NDefines.NAir.ACE_DEATH_BY_OTHER_ACE_CHANCE = 0
NDefines.NAir.ACE_DEATH_CHANCE_PLANES_MULT = 0
NDefines.NAir.ACE_EARN_CHANCE_BASE = 0
NDefines.NAir.ACE_EARN_CHANCE_PLANES_MULT = 0



-- Стаки корабликов
NDefines.NNavy.MIN_SHIPS_FOR_HIGHER_SHIP_RATIO_PENALTY = 30 -- минимальное количество кораблей в соединение, чтобы начались штрафы от размещения
NDefines.NNavy.HIGHER_SHIP_RATIO_POSITIONING_PENALTY_FACTOR = 0.6 -- дебафф размещения
NDefines.NNavy.MAX_POSITIONING_PENALTY_FROM_HIGHER_SHIP_RATIO = 0.60 -- минус к урону
NDefines.NNavy.HIGHER_CARRIER_RATIO_POSITIONING_PENALTY_FACTOR = 0 -- штраф на своё соединение, за более большое авиа соединение у противка
NDefines.NNavy.MAX_CARRIER_RATIO_POSITIONING_PENALTY_FACTOR = 0.5 -- макс штраф за большее количество самолетов у противника на авиках
NDefines.NNavy.SCREEN_RATIO_FOR_FULL_SCREENING_FOR_CAPITALS = 1 -- кол-во требуемых кораблей охранения на 1 тяж корабль
NDefines.NNavy.SPEED_TO_ESCAPE_SPEED = 0.6 -- скорость побега с боя
NDefines.NNavy.BASE_JOIN_COMBAT_HOURS = 0.0 -- сколько кораблям надо прождать в часах, чтобы вступить в бой
NDefines.NNavy.SCREENING_EFFICIENCY_PENALTY_ON_MINIMUM_POSITIONING	= 0.1
NDefines.NNavy.AA_EFFICIENCY_PENALTY_ON_MINIMUM_POSITIONING	= 0.2

NDefines.NNavy.DAMAGE_PENALTY_ON_MINIMUM_POSITIONING = 0.5 -- штраф нанесения урона при плохом размещении
NDefines.NNavy.SCREENING_EFFICIENCY_PENALTY_ON_MINIMUM_POSITIONING = 0.5 -- понижение щитка при понижении размещения
NDefines.NNavy.AA_EFFICIENCY_PENALTY_ON_MINIMUM_POSITIONING = 0.35 -- дебафф на пво флота от размещения
NDefines.NNavy.POSITIONING_PENALTY_FOR_SHIPS_JOINED_COMBAT_AFTER_IT_STARTS = 0.01 -- каждый корабль в бою который получает штраф к размещению
NDefines.NNavy.MAX_POSITIONING_PENALTY_FOR_NEWLY_JOINED_SHIPS = 0.3 -- максимальный штраф за новые суда
NDefines.NNavy.POSITIONING_PENALTY_HOURLY_DECAY_FOR_NEWLY_JOINED_SHIPS = 0.3 -- накопленный штраф за новые суда который будет уменьшаться



---- продакшен

NDefines.NProduction.MAX_MIL_FACTORIES_PER_LINE = 300 -- максимальное количество заводов на линии
NDefines.NProduction.MINIMUM_NUMBER_OF_FACTORIES_TAKEN_BY_CONSUMER_GOODS_PERCENT = 0
NDefines.NIndustrialOrganisation.DESIGN_TEAM_CHANGE_XP_COST = 0


--Agency Upgrade
NDefines.NOperatives.AGENCY_CREATION_DAYS = 30						-- Number of days needed to create an intelligence agency
NDefines.NOperatives.AGENCY_UPGRADE_DAYS = 30						-- Number of days needed to upgrade an intelligence agency
NDefines.NOperatives.AGENCY_CREATION_FACTORIES = 0					-- Number of factories used to create an intelligence agency
NDefines.NCountry.MAX_PROPAGANDA_WAR_SUPPORT_IMPACT = 0.0
NDefines.NCountry.MAX_PROPAGANDA_STABILITY_IMPACT = 0.0
NDefines.NOperatives.OPERATIVE_BASE_PROPAGANDA_POWER = 0.0
NDefines.NOperatives.BOOST_IDEOLOGY_DRIFT_STACKING_FACTOR = 0.0
NDefines.NOperatives.BOOST_IDEOLOGY_MAX_DRIFT_BY_OPERATIVE = 0.0
NDefines.NOperatives.OPERATIVE_BASE_BOOST_IDEOLOGY = 0.0
NDefines.NOperatives.PROPAGANDA_OPERATIVE_STACKING_FACTOR = 0.0
NDefines.NOperatives.PROPAGANDA_COUNTRY_STACKING_FACTOR = 0.0


NDefines.NProduction.BASE_LICENSE_IC_COST = 0;
NDefines.NProduction.LICENSE_EQUIPMENT_BASE_SPEED = 0;
NDefines.NProduction.LICENSE_IC_COST_YEAR_INCREASE = 0;
NDefines.NProduction.MIN_LICENSE_ACTIVE_DAYS = 1


NDefines.NMilitary.COMBAT_STACKING_START = 3						-- ваниль - 8 -- при каком из делений начинается штраф за накопление
NDefines.NMilitary.COMBAT_STACKING_EXTRA = 1                      -- ваниль 4 -- дополнительное наложение из указаний
NDefines.NMilitary.COMBAT_STACKING_PENALTY = -0.18               -- ваниль -0,02 — сколько штрафов за деление

NDefines.NGame.GAME_SPEED_SECONDS = { 6000.0, 0.3, 0.15, 0.07, 0.0  }

------Technology------
NDefines.NAI.RESEARCH_DAYS_BETWEEN_WEIGHT_UPDATE = 1
NDefines.NAI.RESEARCH_AHEAD_BONUS_FACTOR = 100.0
NDefines.NAI.RESEARCH_AHEAD_OF_TIME_FACTOR = 0.0
NDefines.NAI.RESEARCH_BONUS_FACTOR = 0.1
NDefines.NAI.MAX_AHEAD_RESEARCH_PENALTY = 100
NDefines.NAI.RESEARCH_YEARS_BEHIND_FACTOR = 0.0

NDefines.NBuildings.BASE_FACTORY_REPAIR = 2.0			-- Default repair rate in percentage before factories are taken into account (1.0 equals 1%).
	NDefines.NBuildings.BASE_FACTORY_REPAIR_FACTOR = 4.0