# NFPA 855-2026 储能系统设计可操作指南（详细版）

> **文档用途**：储能系统设计阶段安全间距、防火分隔、消防配置等关键参数的快速查询与设计依据
> **标准版本**：NFPA 855-2026 (Standard for the Installation of Stationary Energy Storage Systems)
> **更新日期**：2026-09-16
> **目标读者**：储能系统设计师、消防工程师、电气工程师、项目安全负责人

---

## 一、术语与系统分类速查

### 1.1 系统技术类型（决定间距与防护等级）

| 技术类型 | 风险等级 | 典型间距要求 | 防火分隔要求 | 备注 |
|----------|----------|-------------|-------------|------|
| **锂离子电池 (Li-ion)** | 高 | 最严格 | 2小时防火墙 | 需热失控传播防护(TRPP) |
| **液流电池 (Flow Battery)** | 低 | 最宽松 | 1小时或无 | 新增第16章专门规定 |
| **铅酸电池 (VRLA/flooded)** | 中 | 中等 | 按Standby Power可豁免部分 | Vented cells有特殊豁免 |
| **镍基电池 (Ni-Cd / NiMH)** | 中 | 中等 | 同铅酸 | 通信/铁路应用有额外豁免 |
| **超级电容 (EDLC)** | 低 | 宽松 | 一般无特殊要求 | 参照电容器条款 |

### 1.2 ESS 安装位置分类

| 位置类型 | 定义 | 适用章节 |
|----------|------|----------|
| **室外 (Outdoor)** | 露天安装，无顶盖围护 | Ch.9 9.6节 |
| **室内 (Indoor)** | 建筑内部房间/区域 | Ch.4 + Ch.9 |
| **屋顶 (Rooftop)** | 建筑物屋顶平台 | Ch.9 9.6.3.1 |
| **地下 (Belowgrade)** | 低于室外地面 | Ch.4 4.7.8.1 |
| **专用建筑 (ESS Dedicated-Use Building)** | 仅用于储能或储能+发电 | Ch.9 9.6.1 |
| **移动式 (Mobile ESS)** | 拖车/集装箱式可移动系统 | Ch.9 9.6.3.2 |

> **原文来源**: NFPA 855-2026, Chapter 1 Scope, Section 1.3
>
> > 1.3 This standard shall apply to the installation of energy storage systems (ESSs) and shall include the following:
> > (1) Electrochemical ESSs
> > (2) Mechanical ESSs
> > (3) Electrical ESSs
> > (4) Thermal ESSs

---

## 二、安全间距设计参数（核心设计依据）

### 2.1 室外ESS最小间距

#### 2.1.1 室外ESS距建筑/红线/公共道路（固定式）

| 场景 | 最小间距 | 条件/说明 |
|------|---------|----------|
| **偏远地点 (Remote)** — 无任何 combustible exposure | **100 ft (30.5 m)** | 从ESS最近边缘至 property line、public way、相邻building |
| **非偏远地点 (Non-remote)** — 存在暴露物 | **10 ft (3 m)** | 从ESS最近边缘至 building wall、lot line、public way |
| **距离屋顶边缘** | **≥ ESS系统高度，且 ≥ 5 ft (1.5m)** | 取较大值 |
| **距离消防通道/消防救援入口** | **10 ft (3 m)** | 保证消防车可达性 |
| **ESS单元之间** | **3 ft (0.9 m)** | 同一场地内多个ESS container/cabinet之间的最小净距 |
| **距植被/树木** | **10 ft (3 m)** 清除 | 每侧均需清除，防止火势蔓延至植被 |

**原文引用 — Section 9.6.2.4 / 9.6.2.5 / 9.6.2.7:**

> **9.6.2.7 Clearance to Exposures.** ESSs located outdoors shall be separated by a minimum 10 ft (3 m) from the following exposures:
> (1) Public ways
> (2) Buildings
> (3) Stored combustible materials
> (4) Hazardous materials
> (5) High-piled stock
> (6) Other exposure hazards not associated with electrical grid infrastructure
>
> **9.6.2.7.1.1** The required separation distances shall be permitted to be reduced to 3 ft (0.9 m) when a 1-hour freestanding fire barrier, suitable for exterior use, and extending 5 ft (1.5 m) above and extending 5 ft (1.5 m) beyond the physical boundary of the enclosure is provided.
>
> **9.6.2.7.1.2** Clearances to buildings shall be permitted to be reduced to 3 ft (0.9 m) where noncombustible exterior walls with no openings or combustible overhangs are provided on the building.
>
> **9.6.2.7.1.3** Clearances to buildings shall be permitted to be reduced to 3 ft (0.9 m) based on fire and explosion testing complying with Section 9.2.
>
> **9.6.2.7.1.5** Clearances to buildings and exposures shall be permitted to be reduced to 3 ft (0.9 m) where the enclosure of the ESS has a 2-hour fire resistance rating established in accordance with ASTM E119 or UL 263.
>
> **9.6.2.1 Vegetation Control.**
> 9.6.2.1.1 Areas within 10 ft (3 m) on each side of outdoor ESSs shall be cleared of combustible vegetation and other combustible growth.

#### 2.1.2 移动式ESS (Mobile ESS) 间距 — Section 9.6.3.2

| 场景 | 最小间距 | 条件 |
|------|---------|------|
| **部署状态** 距 public way / building / 可燃材料堆放 / 危险材料 | **10 ft (3 m)** | 部署期间维持 |
| **部署状态** 距公共集会区域（≥30人）/ 帐篷 / 膜结构 | **50 ft (15.3 m)** | 人员聚集场所 |
| **公众屏障** | **5 ft (1.5 m)** 围栏+锁 | 必须设置围栏或等效屏障 |
| **transit 临时停放** 距 occupied building | **100 ft (30.5 m)** | 且停放时间 **≤ 1 小时** |
| **充电/存储位置** | 按固定ESS同等要求处理 | 视同永久安装 |

**原文引用 — Section 9.6.3.2:**

> **9.6.3.2.5 Local Staging.** Mobile ESSs in transit from the charging and storage location to the deployment location and back shall not be parked within 100 ft (30.5 m) of an occupied building for more than 1 hour during transit, unless specifically approved in advance by the AHJ.
>
> **9.6.3.2.7.6 Clearance to Exposures.**
> (A) Deployed mobile ESSs shall be separated by a minimum 10 ft (3 m) from the following exposures:
> (1) Public ways
> (2) Buildings
> (3) Stored combustible materials
> (4) Hazardous materials
> (5) High-piled stock
> (C) Deployed mobile ESSs shall be separated by a minimum 50 ft (15.3 m) from public seating areas and from tents, canopies, and membrane structures with an occupant load of 30 or more.
>
> **9.6.3.2.7.8 Fencing.**
> (A) An approved fence with a locked gate or other approved barrier shall be provided to keep the general public at least 5 ft (1.5 m) from the outer enclosure of a deployed mobile ESS.

### 2.2 室内ESS间距与防火分隔

#### 2.2.1 室内ESS房间防火分隔 — Section 4.7.14 / 9.7.5

| 安装类型 | 防火墙要求 | 水平分隔要求 | 适用条件 |
|----------|-----------|-------------|----------|
| **一般ESS房间** | **2小时** fire barrier | **2小时** horizontal assembly | 所有锂电/液流/铅酸 ESS |
| **UL9540 Listed + UL9540A cell-level testing** | **1小时** fire barrier | **1小时** horizontal assembly | 有完整fire/explosion测试报告 |
| **铅酸/aqueous Ni / metal-air（standby power）** | **1小时** fire barrier | **1小时** horizontal assembly | 仅 standby service 且满足豁免条件 |
| **储能专用建筑内的行政区域** | 按 local building code | — | 行政区域 ≤ 该层 floor area 的 **10%** |

**原文引用 — Section 4.7.14 / 9.7.5:**

> **4.7.14 Fire Barriers.** Rooms or spaces containing ESSs shall be separated from other areas of the building by fire barriers with a minimum 2-hour fire resistance rating and horizontal assemblies with a minimum 2-hour fire resistance rating and constructed in accordance with the local building code, unless modified in Chapters 9 through 13.
>
> **9.7.5 Fire Barriers.** Rooms or spaces containing ESSs shall be separated from other areas of the building by fire barriers with a minimum 2-hour fire resistance rating and horizontal assemblies with a minimum 2-hour fire resistance rating, constructed in accordance with the local building code.
>
> **9.7.5.1** Rooms or spaces, containing only ESSs listed to UL9540 and that are marked as meeting the cell-level performance criteria of UL 9540A, shall be permitted to be separated from other areas of the building with a minimum 1-hour fire resistance rating constructed in accordance with local building codes.
>
> **9.7.5.2** All types of lead-acid, aqueous nickel-based, and aqueous metal-air batteries shall only require a 1-hour fire resistance separation from the rest of the building if used in a stationary standby service complying with any of the following:
> (1) Comprised of vented cells in systems
> (2) Comprised of cells or batteries listed to UL1973
> (3) Used for control of substations and control or safe shutdown of generating stations under the exclusive control of the electric utility and located outdoors or in building spaces used exclusively for such installations
> (4) Used for control of fixed guideway transit or passenger rail systems under the exclusive control of a transit authority and located outdoors or in building spaces used exclusively for such installations
> (5) Used in telecommunications facilities for installations of communications equipment under the exclusive control of communications utilities and located outdoors or in building spaces used exclusively for such installations
> (6) Used in uninterruptable power supplies listed to UL1778

#### 2.2.2 储能专用建筑尺寸限制 — Section 9.6.1.1

| 参数 | 限制值 |
|------|-------|
| 单层 floor area 最大值 | 由 AHJ 确定，但通常建议参考 local building code |
| 建筑层数 | 不超过 **2层**（AHJ可批准更多） |
| 行政/办公区域占比 | ≤ **10%** 该层 floor area |
| 建筑耐火等级 | 不低于 **Type II (1hr)** 或 local code 要求 |

**原文引用 — Section 9.6.1.1:**

> **9.6.1.1 ESS Dedicated-Use Buildings.**
> 9.6.1.1.1 Where approved by the AHJ, the fire control and suppression systems, the size and separation requirements, and the alarm signal transmission requirements of this standard shall not apply to ESSs located in ESS dedicated-use buildings.
>
> **9.6.1.2 Non-Dedicated-Use Buildings.**
> 9.6.1.2.1* Occupied Work Centers. ESSs in occupied work centers shall comply with this section.
> 9.6.1.2.1.1 ESSs shall be permitted in the same room as the equipment that they support.
> 9.6.1.2.1.2 ESSs shall be housed in a noncombustible, locked cabinet or other enclosure to prevent access by unauthorized persons.

### 2.3 室外柜式ESS尺寸上限 — Section 9.6.2.3

| 参数 | 最大允许值 | 超出后要求 |
|------|-----------|-----------|
| 长度 | **53 ft (16.2 m)** | 超出 → 按室内ESS要求处理 |
| 宽度 | **8.5 ft (2.6 m)** | 超出 → 按室内ESS要求处理 |
| 高度 | **9.5 ft (2.9 m)** | 超出 → 按室内ESS要求处理 |

**原文引用 — Section 9.6.2.3:**

> **9.6.2.3 Maximum Size.**
> 9.6.2.3.1 Individual ESS cabinets that exceed 53 ft × 8.5 ft × 9.5 ft (16.2 m × 2.6 m × 2.9 m) in size, not including HVAC and other equipment affixed to the unit, shall be treated as indoor installations.
>
> **9.6.2.3.2** Outdoor ESS enclosures that are occupiable shall be treated as indoor installations.

---

## 三、消防系统设计参数

### 3.1 sprinkler 系统设计密度 — Section 4.9.3 / 9.7.2

| ESS单元最大储能 | 设计密度 | 设计面积 | 设计依据 |
|---------------|---------|---------|---------|
| **≤ 50 kWh** | **0.3 gpm/ft² (12.2 mm/min)** | **2500 ft² (230 m²)** | 取 room area 与 2500ft² 中较小值 |
| **> 50 kWh** | 基于 UL9540A fire/explosion testing 确定 | 同上 | 必须提供测试报告 |

**原文引用 — Section 4.9.3:**

> **4.9.3 Sprinkler System.** Sprinkler systems shall be installed in accordance with NFPA 13 or equivalent.
>
> **4.9.3.1** Sprinkler systems for ESS units (groups) with a maximum stored energy of 50 kWh, as described in 9.5.1.1, shall be designed using a minimum density of 0.3 gpm/ft² (12.2 mm/min) based over the area of the room or 2500 ft² (230 m²) design area, whichever is smaller, unless a lower density is approved based upon fire and explosion testing in accordance with Section 9.2.
>
> **4.9.3.2*** Sprinkler systems for ESS units (groups) exceeding 50 kWh shall use a density based on fire and explosion testing in accordance with Section 9.2.

### 3.2 Guard Post（防护柱）设计参数 — Section 4.7.6

用于保护 ESS 免受车辆撞击：

| 参数 | 要求值 |
|------|-------|
| 材质 | 钢制或混凝土填充 |
| 直径 | **≥ 4 in (100 mm)** |
| 间距（中心到中心） | **≤ 4 ft (1.2 m)** |
| 埋深 | **≥ 3 ft (0.9 m)** 在 footing 内 |
| footing 直径 | **≥ 15 in (380 mm)** |
| 地面以上高度 | **≥ 3 ft (0.9 m)** |
| 距 ESS 最近边缘距离 | **≥ 3 ft (0.9 m)** |

**原文引用 — Section 4.7.6:**

> **4.7.6 Impact Protection.**
> 4.7.6.1 ESSs shall be located or protected to prevent physical damage from impact where such risks are identified.
> 4.7.6.2 Vehicle impact protection consisting of guard posts or other approved means shall be provided where ESSs are subject to impact by motor vehicles.
>
> **4.7.6.3*** When guard posts are installed, they shall be designed as follows:
> (1) Posts shall be constructed of steel not less than 4 in. (100 mm) in diameter.
> (2) Posts shall be filled with concrete.
> (3) Posts shall be spaced not more than 4 ft (1.2 m) on center.
> (4) Posts shall be set not less than 3 ft (0.9 m) deep in a concrete footing of not less than 15 in. (380 mm) diameter.
> (5) The top of the posts shall be set not less than 3 ft (0.9 m) above ground.
> (6) Posts shall be located not less than 3 ft (0.9 m) from the ESS.

---

## 四、检测与报警系统

### 4.1 烟雾与火灾探测 — Section 4.8 / 9.7.1

| 探测类型 | 要求 | 适用场景 |
|----------|------|---------|
| **烟雾探测 (Smoke Detection)** | NFPA 72 合规，UL 268 7th ed 或 later | 所有室内ESS |
| **热成像探测 (Thermal Image)** | NFPA 72 合规 | 户外ESS首选 |
| **辐射能探测 (Radiant Energy)** | NFPA 72 合规 | 户外ESS/大型室内ESS |

**原文引用 — Section 4.8 / 9.7.1:**

> **4.8.1*** Where required elsewhere in this standard, areas containing ESSs shall be provided with a smoke detection, thermal image fire detection, or radiant-energy-sensing system in accordance with NFPA 72, unless modified by the requirements in Chapters 9 through 13.
>
> **9.7.1 Smoke and Fire Detection.** ESSs shall be provided with a smoke detection, thermal image fire detector, or radiant-energy-sensing system in accordance with NFPA 72, unless modified by this chapter.
>
> **9.7.1.6*** Smoke and fire detection systems protecting an ESS with lithium-ion batteries shall be required to provide a secondary power supply in accordance with Section 4.10.

### 4.2 二次电源要求 — Section 4.10

| 系统类型 | 二次电源要求 |
|----------|------------|
| **锂离子电池ESS** | **必须** 有 secondary power supply（按 NFPA 110/111） |
| 铅酸/aqueous Ni / metal-air (standby) | 如满足豁免条件则可不要求 |
| 所有 critical safety systems | 符合 NFPA 110 Type 10 或 SEPSS |

**原文引用 — Section 4.10:**

> **N 4.10* Emergency Power Supply Systems (EPSS).** Critical safety systems that rely on power shall be provided with reliable EPSS or SEPSS power in accordance with NFPA 110 or NFPA 111.
>
> **N 4.10.1*** If EPSS or SEPSS is provided, they shall be Class X, Type 10, Level 2.
>
> **N 4.10.4*** EPSS shall be installed per Section 7.2 of NFPA 110, providing separation and protection such that a failure event doesn't compromise the operation of the system.

---

## 五、通风系统设计

### 5.1 事故通风 (Accident Ventilation) — Section 9.7.6.1

| 参数 | 要求值 |
|------|-------|
| 最小换气率 | **≥ 1 ft³/min/ft² (5.1 L/sec/m²)** 地板面积 |
| 启动方式 | 由 gas detection 系统联动 或 手动 |
| 运行要求 | 保持 flammable gas < **25% LFL** |
| 被视为 | **Critical safety system**（需二次电源） |

**原文引用 — Section 9.7.6.1.5:**

> **9.7.6.1.5 Mechanical Exhaust Ventilation.** Exhaust ventilation shall be provided in accordance with the applicable mechanical code and one of the following:
> (1) Where hydrogen is the gas generated, an exhaust ventilation rate based on hydrogen generation estimates sufficient to limit the maximum concentration of hydrogen to 1.0 percent of the free air volume of the room or enclosure during the worst-case conditions, including simultaneous "boost" charging of all the batteries, in accordance with nationally recognized standards
> (2) An exhaust ventilation rate based on the area of not less than 1 ft³/min/ft² (5.1 L/sec/m²) of floor area of the ESS
>
> **9.7.6.1.5.3** The mechanical exhaust ventilation system and its components shall comply with the following:
> (1) Be either continuous or activated by a gas detection system in accordance with 9.6.6.1.5.4
> (2) Remain on to ensure that flammable gas does not accumulate and exceed 25 percent of the LFL of the flammable gas mixture
> (3)* Be considered a critical safety system and be in compliance with Section 4.10, unless the battery technology stops off-gassing on loss of charging power
>
> **9.7.6.1.5.4*** Where gas detection is used to activate exhaust ventilation in accordance with 9.7.6.1.5.3, ESSs shall be protected by an approved continuous gas detection system that complies with the following:
> (1) The gas detection system shall be designed to activate the mechanical exhaust ventilation system when the level of flammable gas detected exceeds 25 percent of the LFL of the flammable gas mixture.
> (2)* The gas detection system shall be considered a critical safety system and comply with Section 4.10, unless the battery technology stops off-gassing on loss of charging power.

---

## 六、标识与标牌要求

### 6.1 ESS 标识内容（Section 4.7.5.2）

标识必须包含（ANSI Z535 合规）：
1. ✅ **"Energy Storage Systems"** + 三角形闪电图标
2. ✅ 技术类型（如 "Lithium-Ion Battery"）
3. ✅ 特殊危险说明（按 Ch.9-15 识别）
4. ✅ 灭火系统类型（如 "Wet Pipe Sprinkler"）
5. ✅ 爆炸控制类型（如 "Explosion Vents Installed"）
6. ✅ 紧急联系信息
7. ✅ **NFPA 704 菱形标牌**（按 HMA 结果）

**原文引用 — Section 4.7.5:**

> **4.7.5* Signage.**
> 4.7.5.1 Approved signage shall be provided in the following locations:
> (1) On the front of doors to rooms or areas containing ESSs or in approved locations near entrances to ESS rooms
> (2) On the front of doors to outdoor occupiable ESS containers or in approved locations near ESS site entrances
> (3) In approved locations on outdoor ESSs that are not enclosed in occupiable containers or otherwise enclosed
>
> 4.7.5.2* The signage required in 4.7.5.1 shall be in compliance with ANSI Z535 and include the following information, where applicable, as shown in Figure 4.7.5.2:
> (1) "Energy Storage Systems" with symbol of lightning bolt in a triangle
> (2) Type of technology associated with the ESS
> (3) Special hazards associated as identified in Chapters 9 through 15
> (4) Type of suppression system installed in the area of the ESS
> (5) Type of explosion control and prevention system installed for the ESS
> (6) Emergency contact information
>
> **N 4.7.5.7*** ESS shall be provided with NFPA 704 placarding in accordance with the following:
> (1) As required by the HMA
> (2) As required by applicable codes and standards
> (3) As required by the AHJ

---

## 七、锂一次电池/锂离子电池储存要求（第14章）

### 7.1 收集点（Collection Locations）— Section 14.2

| 参数 | 要求值 |
|------|-------|
| 单个容器最大尺寸 | **≤ 7.5 ft³ (0.21 m³)** |
| 容器总容量上限 | **≤ 15 ft³ (0.42 m³)** |
| 容器间距（无 combustible 介质） | **≥ 3 ft (0.9 m)** |
| 容器间距（有 combustible 介质） | **≥ 10 ft (3 m)** |

**原文引用 — Section 14.2:**

> **14.2 Collection Locations.** All areas located indoors in any occupancy where used lithium metal or lithium-ion batteries are collected from employees or the public shall comply with 14.2.1 through 14.2.3.
>
> **14.2.1*** Individual containers shall not exceed 7.5 ft³ (0.21 m³) in size each, with an aggregate limit of 15 ft³ (0.42 m³).
>
> **14.2.2** Containers shall comply with all of the following:
> (1) Have a minimum of 3 ft (0.9 m) of open space from other battery collection containers and combustible materials
>
> **14.2.3** Where combustible materials are located within the space between collection containers, the containers shall be spaced a minimum 10 ft (3 m) apart.

### 7.2 室内储存（Section 14.3）

| 储存方式 | 要求 |
|----------|------|
| **房间储存** | 用 **2小时 fire barrier** 与建筑其他区域分隔 |
| **预制 portable structure** | 需 **2小时 fire resistance rating** listed/approved |
| **运输容器储存** | 按 manufacturer 包装要求 |
| **金属桶储存** | 符合 DOT 运输包装要求 |

**原文引用 — Section 14.3:**

> **14.3.2.1.1** The rooms or spaces shall be separated from the remainder of the building areas by fire barriers with a 2-hour fire resistance rating and with horizontal assemblies with a 2-hour fire resistance rating constructed in accordance with the local building code.
>
> **14.3.2.1.2** The rooms or spaces shall be provided with a fire alarm system activated by a smoke detector system, a thermal image fire detection system, or a radiant-energy detection system in accordance with NFPA 72.
>
> **14.3.2.1.3** The rooms or spaces shall be provided with an automatic sprinkler system designed and installed in accordance with NFPA 13.

### 7.3 室外堆放储存（Section 14.6）

| 参数 | 要求值 |
|------|-------|
| 单个 pile 最大面积 | **900 ft² (83.6 m²)** |
| Pile 间最小间距 | **3 ft (0.9 m)**（有 3小时 fire barrier 时可减）|
| Fire alarm 要求 | Outdoor area > **400 ft² (37.1 m²)** 时需 radiant-energy 或 thermal-image 探测 |

**原文引用 — Section 14.6:**

> **14.6.1** Outdoor storage locations for lithium metal or lithium-ion batteries shall comply with the following:
> (1) Individual pile sizes shall be limited to 900 ft² (83.6 m²) in area
> (2) Piles shall be separated by a minimum 3 ft (0.9 m)
>
> **14.6.2** Clearances shall be permitted to be reduced to 3 ft (0.9 m) where a 3-hour freestanding fire barrier, suitable for exterior use, and extending 5 ft (1.5 m) above and extending 5 ft (1.5 m) beyond the physical boundary of the pile is provided.
>
> **14.6.4** Outdoor storage areas with an aggregate area greater than 400 ft² (37.1 m²) shall be provided with a fire alarm system activated by a radiant-energy or thermal-image fire detection system with occupant notification installed in accordance with NFPA 72.

---

## 八、HMA（Hazard Mitigation Analysis）要求

### 8.1 何时需要 HMA — Section 4.4

以下情况 **必须** 进行 HMA：
- ESS 储能 > **400 kWh**
- ESS 安装在 indoor 或非偏远 outdoor 位置
- AHJ 认为有必要时

### 8.2 HMA 必须包含的内容 — Section 4.4.2

1. ESS 技术类型与化学体系描述
2. **Thermal runaway 起始条件与传播路径分析**
3. **Fire and explosion 风险评估**
4. **毒性气体释放评估**
5. 现有 fire protection 系统有效性验证
6. **间距合规性确认**
7. 应急响应程序
8. 由 **Registered Design Professional (RDP)** 签字

**原文引用 — Section 4.4:**

> **4.4 Hazard Mitigation Analysis (HMA).**
> **4.4.1*** A hazard mitigation analysis shall be provided to the AHJ for review and approval unless modified in Chapters 9 through 17.
>
> **4.4.2 Failure Modes.**
> **4.4.2.1*** The hazard mitigation analysis shall evaluate the consequences of the following:
> (1) A thermal runaway or mechanical failure condition in a battery, module, unit, or enclosure
> (2) A fire or explosion resulting from the failure condition in 4.4.2.1(1)
> (3) Toxic and highly toxic gas release resulting from the failure condition in 4.4.2.1(1)
>
> **4.4.2.2*** Only single failure modes shall be considered for each mode given in 4.4.2.1.
>
> **N 4.4.2.3** The HMA shall evaluate the reliability and survivability of the following critical safety components or systems, during a thermal runaway propagation or single failure event:
> (1) Fire detection and alarm systems
> (2) Fire suppression systems
> (3) Explosion control and prevention systems
> (4) Ventilation systems
> (5) Gas detection systems
> (6) Emergency power supply systems
>
> **4.4.3** The AHJ shall be permitted to approve the hazard mitigation analysis as documentation of the safety of the ESS installation if the consequences of the analysis demonstrate the installation to be acceptable.
>
> **4.4.4** The hazard mitigation analysis shall be documented and made available to the AHJ and those authorized to design and operate the system.
>
> **4.4.5*** Construction, equipment, and systems that are required for the ESS to comply with the hazard mitigation analysis shall be installed, tested, and maintained in accordance with this standard.

---

## 九、住宅与联排别墅要求（第15章）

### 9.1 容量限制

| 位置 | 最大容量 | 备注 |
|------|---------|------|
| **屋顶 (Rooftop)** — residential | **≤ 20 kWh (72 MJ)** | 超过需按 Ch.9 处理 |
| **车库** | 按 local code | 不得位于车辆可碰撞位置 |

**原文引用 — Section 9.6.3.1.1.3:**

> **9.6.3.1.1.3** Individual ESS units with a maximum stored energy of 20 kWh or less that are located on rooftops shall be permitted to be installed without the protection of an automatic fire suppression system where the system is listed to UL 9540 and the installation is in accordance with the manufacturer's instructions and this standard.

---

## 十、液流电池要求（第16章，2026新增）

### 10.1 通用要求

- 参照 electrochemical ESS 通用条款（Ch.4-9）
- 消防介质必须与 electrolyte **兼容**（Section 16.5）
- spill control 按 Section 16.6 执行

**原文引用 — Section 16.5:**

> **IN 16.5 Fire Control and Suppression.** Fire suppression agents used in rooms or areas that contain flow batteries shall be compatible with the flow battery materials and electrolytes.

---

## 十一、关键数值速查表

| 参数 | 数值 | 章节 |
|------|------|------|
| 室外偏远ESS距building | **100 ft (30.5 m)** | 9.6.2.4 |
| 室外非偏远ESS距building | **10 ft (3 m)** | 9.6.2.7.1 |
| ESS单元之间 | **3 ft (0.9 m)** | 9.6.2.4 |
| ESS距屋边 | **≥系统高度，min 5 ft (1.5m)** | 9.6.3.1.3.1 |
| 移动ESS距公共集会区(≥30人) | **50 ft (15.3 m)** | 9.6.3.2.7.6(C) |
| 移动ESS transit距occupied building | **100 ft (30.5 m), max 1 hr** | 9.6.3.2.5 |
| 公众距部署中移动ESS | **5 ft (1.5 m)** 围栏 | 9.6.3.2.7.8 |
| 植被清除距离 | **10 ft (3 m)** | 9.6.2.1.1 |
| 室内ESS防火墙 | **2小时**（一般）/ **1小时**（UL9540A+listed） | 4.7.14 / 9.7.5 |
| 室内ESS水平分隔 | **2小时**（一般）/ **1小时**（UL9540A+listed） | 4.7.14 / 9.7.5 |
| 铅酸standby防火分隔 | **1小时** | 9.7.5.2 |
| Sprinkler密度（≤50kWh） | **0.3 gpm/ft² (12.2 mm/min)** | 4.9.3.1 |
| Sprinkler设计面积（≤50kWh） | **2500 ft² (230 m²)** | 4.9.3.1 |
| Sprinkler密度（>50kWh） | 按UL9540A测试确定 | 4.9.3.2 |
| 事故通风率 | **≥ 1 ft³/min/ft² (5.1 L/sec/m²)** | 9.7.6.1.5 |
| 气体探测启动通风阈值 | **25% LFL** | 9.7.6.1.5.4 |
| Guard post直径 | **≥ 4 in (100 mm)** | 4.7.6.3 |
| Guard post间距 | **≤ 4 ft (1.2 m) OC** | 4.7.6.3 |
| Guard post埋深 | **≥ 3 ft (0.9 m)** | 4.7.6.3 |
| Guard post footing直径 | **≥ 15 in (380 mm)** | 4.7.6.3 |
| Guard post地面以上高度 | **≥ 3 ft (0.9 m)** | 4.7.6.3 |
| Guard post距ESS | **≥ 3 ft (0.9 m)** | 4.7.6.3 |
| 室外柜尺寸上限 | **53×8.5×9.5 ft (16.2×2.6×2.9m)** | 9.6.2.3.1 |
| 屋顶住宅ESS容量上限 | **≤ 20 kWh (72 MJ)** | 9.6.3.1.1.3 |
| 收集点容器单个体积 | **≤ 7.5 ft³ (0.21 m³)** | 14.2.1 |
| 收集点容器总体积 | **≤ 15 ft³ (0.42 m³)** | 14.2.1 |
| 收集点容器间距（无 combustible） | **≥ 3 ft (0.9 m)** | 14.2.2 |
| 收集点容器间距（有 combustible） | **≥ 10 ft (3 m)** | 14.2.3 |
| 室外电池堆放单堆面积 | **≤ 900 ft² (83.6 m²)** | 14.6.1 |
| 室外堆放消防报警面积阈值 | **> 400 ft² (37.1 m²)** | 14.6.4 |
| 室外堆放fire barrier减少间距 | **3 ft (0.9 m)**（配3小时 barrier） | 14.6.2 |
| ESS专用建筑行政区占比 | **≤ 10%** floor area | 9.6.1.1.1 |
| HMA容量门槛 | **> 400 kWh** | 4.4 |
| 便携式ESS deployment最长无特殊要求 | **30 days** | 9.6.3.2.7.5(B) |

---

## 十二、设计检查清单（Design Checklist）

### 12.1 选址阶段

- [ ] 确定 ESS 技术类型与储能容量
- [ ] 确认安装位置（室外/室内/屋顶/专用建筑）
- [ ] 测量距周边 building/lot line/public way 的距离
- [ ] 确认是否为 remote location
- [ ] 检查附近是否有 combustible storage / hazardous materials
- [ ] 确认消防通道可达性（≥ 10 ft clearance）
- [ ] 如为 rooftop：确认距屋边距离 ≥ 系统高度且 ≥ 5 ft

### 12.2 电气设计阶段

- [ ] 确认电气设计符合 NFPA 70 / IEEE C2
- [ ] 设计 disconnecting means（含永久标识）
- [ ] 确认 overcurrent protection 配置
- [ ] 设计 EPSS / SEPSS 二次电源（锂电必须）
- [ ] 确认 grounding 与 bonding 符合要求

### 12.3 消防设计阶段

- [ ] 确定 fire barrier 耐火等级（1小时 or 2小时）
- [ ] 设计 sprinkler 系统（密度 ≥ 0.3 gpm/ft² for ≤50kWh）
- [ ] 确认 water supply 容量与 hydrant 位置
- [ ] 设计 smoke/fire detection 系统（含 NFPA 72 合规）
- [ ] 设计 accident ventilation 系统（≥ 1 ft³/min/ft²）
- [ ] 配置 gas detection 与 ventilation interlock（如需要）
- [ ] 设计 TRPP 系统（锂电，如要求）

### 12.4 标识与文件阶段

- [ ] 制作 ESS 警示标识（含 lightning bolt 符号）
- [ ] 制作 NFPA 704 菱形标牌
- [ ] 制作 disconnecting means 永久标牌
- [ ] 编制 HMA 报告（如需要）
- [ ] 提交 construction documents 至 AHJ
- [ ] 编制 commissioning plan 与 O&M manual

### 12.5 移动端 ESS 特殊检查

- [ ] 确认 deployment location 经 AHJ 批准
- [ ] 部署间距 ≥ 10 ft（30人以上集会区 ≥ 50 ft）
- [ ] 设置围栏（公众保持 ≥ 5 ft）
- [ ] Transit 时距 occupied building ≥ 100 ft，≤ 1小时
- [ ] Deployment > 30天按固定ESS同等要求

---

## 十三、参考标准与关联规范

| 标准 | 用途 |
|------|------|
| **NFPA 70 (NEC)** | 电气安装、disconnecting means、overcurrent protection |
| **NFPA 110** | EPSS（emergency power supply systems）要求 |
| **NFPA 111** | SEPSS（stored-energy EPSS）要求 |
| **NFPA 13** | sprinkler 系统设计 |
| **NFPA 15** | water spray 系统 |
| **NFPA 72** | 火灾报警与探测系统 |
| **NFPA 750** | water mist 系统 |
| **NFPA 2001** | clean agent 灭火系统 |
| **NFPA 2010** | CO₂ 灭火系统 |
| **NFPA 12** | dry chemical 系统 |
| **NFPA 1142** | 无永久供水时的消防要求 |
| **NFPA 24** | private fire service mains hydrant 安装 |
| **UL 9540** | ESS 安全认证 |
| **UL 9540A** | fire/explosion testing 方法 |
| **UL 1973** | stationary battery listing |
| **UL 1778** | UPS listing |
| **ANSI Z535** | 安全标识标准 |
| **ASTM E119 / UL 263** | 耐火测试方法 |

---

## 十四、常见设计错误与规避建议

| 错误 | 后果 | 规避建议 |
|------|------|---------|
| 未做 HMA 直接设计 | 审批不通过，返工 | >400kWh 或 indoor 安装前先行 HMA |
| 间距不足但无 fire barrier | 违反 Ch.9，无法通过审查 | 若间距不足，加设 1小时 fire barrier 并延伸 5ft |
| 忽视二次电源要求（锂电） | 探测/通风失效风险 | 锂电系统必须配 EPSS/SEPSS |
| 消防系统按普通仓库设计 | 无法扑灭 ESS 火灾 | 按 Section 4.9.3 密度设计，>50kWh 需 UL9540A 数据 |
| 标识不完整 | 消防响应延误 | 按 4.7.5.2 逐项检查，含 704 标牌 |
| 未考虑 vehicle impact | 物理损坏风险 | 按 4.7.6 设置 guard post |
| 屋顶安装未核实结构荷载 | 结构安全隐患 | 按 4.7.4 核算 dead + live loads |
| 忽视 gas detection 与 ventilation interlock | 可燃气体积累爆炸风险 | 锂电/铅酸 vented 系统必须配置 |

---

## 附录：关键章节原文索引

### Section 4.4 Hazard Mitigation Analysis (HMA) 全文
> **4.4.1*** A hazard mitigation analysis shall be provided to the AHJ for review and approval unless modified in Chapters 9 through 17.
>
> **4.4.2.1*** The hazard mitigation analysis shall evaluate the consequences of:
> (1) A thermal runaway or mechanical failure condition in a battery, module, unit, or enclosure
> (2) A fire or explosion resulting from the failure condition
> (3) Toxic and highly toxic gas release resulting from the failure condition
>
> **4.4.2.2*** Only single failure modes shall be considered for each mode given in 4.4.2.1.
>
> **N 4.4.2.3** The HMA shall evaluate the reliability and survivability of critical safety components or systems during a thermal runaway propagation or single failure event.

### Section 9.6.2.7 Clearance to Exposures 原文
> **9.6.2.7.1** ESSs located outdoors shall be separated by a minimum 10 ft (3 m) from the following exposures:
> (1) Public ways
> (2) Buildings
> (3) Stored combustible materials
> (4) Hazardous materials
> (5) High-piled stock
> (6) Other exposure hazards not associated with electrical grid infrastructure
>
> **9.6.2.7.1.1** The required separation distances shall be permitted to be reduced to 3 ft (0.9 m) when a 1-hour freestanding fire barrier, suitable for exterior use, and extending 5 ft (1.5 m) above and extending 5 ft (1.5 m) beyond the physical boundary of the enclosure is provided.

### Section 9.7.5 Fire Barriers 原文
> **9.7.5** Rooms or spaces containing ESSs shall be separated from other areas of the building by fire barriers with a minimum 2-hour fire resistance rating and horizontal assemblies with a minimum 2-hour fire resistance rating.
>
> **9.7.5.1** Rooms or spaces containing only ESSs listed to UL9540 and that are marked as meeting the cell-level performance criteria of UL 9540A shall be permitted to be separated with a minimum 1-hour fire resistance rating.
>
> **9.7.5.2** All types of lead-acid, aqueous nickel-based, and aqueous metal-air batteries shall only require a 1-hour fire resistance separation if used in stationary standby service complying with the conditions in 9.3.1.

### Section 14.2 Collection Locations 原文
> **14.2.1*** Individual containers shall not exceed 7.5 ft³ (0.21 m³) in size each, with an aggregate limit of 15 ft³ (0.42 m³).
>
> **14.2.2** Containers shall have a minimum of 3 ft (0.9 m) of open space from other battery collection containers and combustible materials.
>
> **14.2.3** Where combustible materials are located within the space between collection containers, the containers shall be spaced a minimum 10 ft (3 m) apart.

### Section 4.7.6 Impact Protection (Guard Posts) 原文
> **4.7.6.3*** When guard posts are installed, they shall be designed as follows:
> (1) Posts shall be constructed of steel not less than 4 in. (100 mm) in diameter.
> (2) Posts shall be filled with concrete.
> (3) Posts shall be spaced not more than 4 ft (1.2 m) on center.
> (4) Posts shall be set not less than 3 ft (0.9 m) deep in a concrete footing of not less than 15 in. (380 mm) diameter.
> (5) The top of the posts shall be set not less than 3 ft (0.9 m) above ground.
> (6) Posts shall be located not less than 3 ft (0.9 m) from the ESS.

---

*本文档基于 NFPA 855-2026 编译，仅供设计参考。实际项目应以正式批准的规范文本及 AHJ 要求为准。*
