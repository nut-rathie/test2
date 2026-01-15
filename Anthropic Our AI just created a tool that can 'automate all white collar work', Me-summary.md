# สรุปวิดีโอ: Anthropic Our AI just created a tool that can 'automate all white collar work', Me

## ภาพรวม

วิดีโอนี้พูดถึง prediction ของ Anthropic ว่า AI จะสามารถ automate งาน white-collar ทั้งหมดได้ภายในปี 2026 โดยใช้ tool ใหม่ชื่อ **Claude Co-work** ซึ่งถูกสร้างขึ้นโดย Claude Opus 4.5 ผู้สร้างวิดีโอได้ทดสอบ tool นี้และแสดงให้เห็นว่าแม้ AI จะมีความสามารถสูง แต่ก็ยังมีข้อจำกัดและไม่ได้ถึงระดับ AGI (Artificial General Intelligence) อย่างที่หลายคนอ้าง นอกจากนี้ยังอธิบายว่าทำไม LLM (Large Language Model) ถึงดูเหมือน "brittle" คือบางครั้งทำงานได้อัจฉริยะมาก แต่บางครั้งก็ล้มเหลวในงานง่ายๆ

---

## ส่วนที่ 1: Prediction และ Claude Co-work

### การทำนายของ Anthropic
- Douglas Schultto จาก Anthropic ได้ทำนายว่าภายในปี 2026 งาน knowledge work ทั้งหมดจะถูก automate โดย AI เหมือนที่เกิดขึ้นกับ software engineers ที่เปลี่ยนจากการพิมพ์ code ส่วนใหญ่เองในต้นปี กลายเป็นแทบไม่ต้องพิมพ์เลยในปลายปี
- เขาเรียกปรากฏการณ์นี้ว่า "Claude Code experience but for all forms of knowledge work"

### Claude Co-work คืออะไร
- เป็น tool ใหม่ที่ออกมาล่าสุดจาก Anthropic สำหรับ automate งานที่ไม่ใช่ coding
- Tool นี้ viral ไปมากด้วย view 42 ล้านครั้ง
- **สิ่งที่น่าสนใจคือ** Claude Co-work เองถูกสร้างขึ้นทั้งหมดด้วย Claude Code ที่ใช้ model Claude Opus 4.5
- Available เฉพาะ Mac OS (ไม่ใช่ Windows) และต้องใช้ tier Max เท่านั้น ($90-$100)

---

## ส่วนที่ 2: การทดสอบจริงและข้อจำกัด

### ตัวอย่างการทดสอบ: Stockport Football Club
ผู้สร้างวิดีโอได้ทดสอบ Claude Co-work ด้วยงาน:
> "สร้าง comparison chart ของตำแหน่ง league ของสโมสรฟุตบอลนี้ในวันนี้สำหรับแต่ละปีในช่วง 5 ปีที่ผ่านมา เพิ่มลงใน PowerPoint บน desktop"

**ผลลัพธ์:**
- ✅ Co-work วางแผนได้ดี ถามคำถาม clarifying questions ได้ดี
- ✅ PowerPoint ที่สร้างออกมามี visual ที่สวยงามและ impressive
- ❌ **แต่มีข้อผิดพลาด!** เมื่อเช็คข้อมูล 2 วันที่ (มกราคม 2023 และ 2025) พบว่า league position ผิดทั้งสองวันที่
- ❌ BBC และ 11v11 (data sources อื่น) บอกว่า Stockport อยู่อันดับที่ 7 แต่ Co-work บอกว่าอันดับที่ 3 สำหรับวันที่ 13 มกราคม 2025
- ❌ Co-work ไม่ได้ให้ caveat หรือเตือนว่าหาข้อมูลที่เชื่อถือได้ไม่ได้

### บทเรียนสำคัญ
ผู้สร้างวิดีโอเตือนว่า:
1. **อย่าคิดว่าตัวเองโง่** ถ้า AI ทำผิดพลาด - ไม่ใช่ความผิดของคุณ
2. **อย่าทิ้ง AI ไปเลย** - มันยังมี productivity gains ที่แท้จริง
3. **ความจริงอยู่ตรงกลาง** - AI ไม่ใช่ AGI แต่ก็ไม่ใช่ useless

---

## ส่วนที่ 3: การยืนยันจาก Developer

Lead developer ของ Claude Code ได้ clarify ว่า:
> "มันไม่ใช่ zero intervention - พวกเรา humans ต้อง plan, design, และ go back and forth กับ Claude"

นี่ทำให้เกิดคำถามสำคัญ:
**มันเร็วกว่าไหมที่จะให้ Claude draft แล้ว redraft หลายรอบ เทียบกับให้ human ทำเองตั้งแต่ต้น?**

---

## ส่วนที่ 4: Research Data - The Tipping Point

### OpenAI Paper (ตุลาคม 2025)
- ใช้ **blind human grading** พบว่าเราผ่าน tipping point แล้ว
- **มี productivity multiplier มากกว่า** ถ้าให้ model พยายามหลายๆ รอบ แล้วให้ human เข้ามา review และ edit
- เทียบกับให้ human ทำทั้งหมดเอง
- Paper นี้ครอบคลุม white-collar industries หลายสิบอุตสาหกรรม

### ตัวอย่างจริง: Stockport PowerPoint
- แม้จะมีข้อมูลผิดบางส่วน แต่ design สวยงาม
- ข้อเท็จจริงส่วนใหญ่ถูกต้อง
- สามารถแก้ตัวเลขไม่กี่ตัว แล้วได้ presentation ที่ดีใน **เวลาน้อยกว่า** การสร้างเองตั้งแต้นต้น

---

## ส่วนที่ 5: ผลกระทบต่อตลาดแรงงาน - ข้อมูลจริง

### Oxford Economics Report (7 มกราคม 2026)

**ข้อมูล unemployment ของ new graduates:**
- ✅ มีการเพิ่มขึ้นเล็กน้อย แต่**ไม่สูงกว่าช่วงก่อนหน้า** เช่น ปี 2015 หรือ 2010
- ✅ จาก March ถึง September ปีที่แล้ว มีแนวโน้ม **ลดลงเล็กน้อย**
- ✅ **ไม่คาดว่า AI จะทำให้ jobless rate เพิ่มขึ้นอย่างมีนัยสำคัญ** ในอีก 1-2 ปีข้างหน้า

**การวิเคราะห์ Labor Productivity:**
- ถ้า AI ทำให้เกิด mass layoffs จริง ควรจะเห็น **labor productivity เพิ่มขึ้น** (output เท่าเดิมแต่ใช้ worker น้อยลง)
- แต่ข้อมูลปี 2025 แสดงว่า productivity per hour growth **ไม่ได้สูงกว่าปีก่อนๆ** อย่างชัดเจน
- ในความเป็นจริง productivity growth ในปี 2025 **น้อยกว่า** ช่วง 2000-2007

### ทำไมบริษัทถึงอ้างว่าลดคนเพราะ AI?
> "การเชื่อมโยง job losses กับ AI แทนที่จะเป็นปัจจัยลบอื่นๆ เช่น weak demand หรือการจ้างคนมากเกินไปในอดีต จะส่ง **positive message ต่อ investors** มากกว่า"

---

## ส่วนที่ 6: Adoption Trends

### การใช้งาน AI ในปัจจุบัน
- เมื่อหลายคนค้นพบว่า LLM มี hallucination มาก initial wave of adoption ก็ **ลดลง** ในช่วงกลางปีที่แล้ว
- แต่มี **uptick** ล่าสุดเมื่อคนเริ่มเปรียบเทียบ models ต่างๆ

### ChatGPT vs คู่แข่ง
- Demis (CEO ของ Google DeepMind) ชี้ว่ามี "relentless progress"
- **Market share ของ ChatGPT กำลังลดลง** อย่างเห็นได้ชัด
- นี่คือเหตุผลที่ผู้สร้างวิดีโอทำ app ชื่อ **lmconsil.ai** เพื่อเปรียบเทียบ answers จาก frontier models ทั้งหมด

---

## ส่วนที่ 7: มุมมองจาก Industry Leaders

### Jensen Huang (NVIDIA)
เขาให้ insight สำคัญว่า:
> "อย่าสับสนระหว่าง **purpose ของงาน** กับ **series ของ tasks ที่สามารถ automate ได้แบบแยกส่วน**"

**ตัวอย่าง Football Commentator:**
- ✅ สามารถ automate เสียงของ commentator ได้
- ✅ สามารถ automate tactical analysis ได้
- ✅ ทำได้เร็วกว่าและถูกกว่า
- ❌ **แต่ purpose ที่แท้จริง** คือการ entertain และทำให้คนดูไม่เบื่อ ซึ่ง AI อาจทำไม่ได้ดีกว่า human

---

## ส่วนที่ 8: ทำไม AI ถึง "Brittle"? - The Why Behind It

### ปรากฏการณ์ที่น่าสนใจ
AI บางครั้งดูเหมือน:
- **200 IQ** - เช่น หา bug เล็กๆ ใน codebase ขนาดใหญ่ได้, เขียน poem ที่ลึกซึ้ง
- **50 IQ** - เช่น ลบไฟล์ 11 GB จาก desktop แบบสุ่ม, ไม่รู้ว่า Mary Stone's husband คือ Tom ทั้งๆ ที่รู้ว่า Tom Smith's wife คือ Mary

---

## ส่วนที่ 9: สามระดับของ "Understanding" ใน LLMs

### ความหมายของคำว่า "Understanding"
- ภาษาอังกฤษเองก็ยังไม่มีคำนิยามที่ชัดเจน
- Etymology ของคำว่า "understand" = "to be between or among the ideas"
- "Comprehend" = "to grasp something"
- "Intelligence" = "to pick between things"

### Three Levels of Understanding (จาก Beckman and Quaos Paper)

**Level 1: Simple Conceptual Understanding**
- แค่ **ตระหนักว่ามี connections** ระหว่างสิ่งต่างๆ
- เพียงแค่หา connections ระหว่างสองสิ่ง

**Level 2: State of the World / Contingent Understanding**
- เข้าใจว่า connections เป็นจริงหรือมีอยู่ **เฉพาะในบางสถานการณ์** บางเวลา

**Level 3: Principled Understanding**
- ความสามารถใน **efficiently deriving new functions**
- เข้าใจ underlying principles หรือ rules ที่รวม facts ต่างๆ เข้าด้วยกัน
- สามารถ derive deep algorithms และ patterns จาก world

---

## ส่วนที่ 10: ทำไม LLMs ถึงมี Mixed Understanding

### การทำงานของ LLMs
LLMs มี **distributed understanding across all three tiers** แบบไม่มีระเบียบ:

**ด้านที่ดี - Deep Understanding:**
- ✅ สามารถ **grok** (เข้าใจลึกซึ้ง) วิธีทำ addition จนสามารถลบ memorized pairs ทิ้งได้
- ✅ มี **circuits สำหรับวางแผน poem** - ก่อน token ของบรรทัดใหม่ใน poem จะมี circuit วางแผน rhyme และ semantics ล่วงหน้า
- ✅ Researchers พบ **computable circuits** สำหรับ:
  - Numerical comparison
  - Multiple-choice question answering
  - Recognizing ว่าควรใช้ introspection

**ด้านที่อ่อน - Brittle Memorization:**
- ❌ พึ่งพา **shallow heuristics (rules of thumb)** แบบเปราะบาง
- ❌ **Toggle ระหว่าง** modeling the state of the world กับใช้ shallow heuristics ขึ้นอยู่กับว่าอันไหนจะ minimize loss ได้ดีกว่า
- ❌ เหมือน **lazy bright kid** ที่บางครั้งเรียนจริงจัง บางครั้งก็แค่ท่อง

---

## ส่วนที่ 11: ตัวอย่างความเปราะบาง - Tom and Mary Problem

### ปัญหาที่แสดงถึง Brittle Understanding

**สิ่งที่ LLM ทำได้:**
- เรียนรู้ว่า "Tom Smith's wife is Mary Stone"
- Update weights เพื่อ predict ว่าหลังจาก "Tom Smith's wife is" ควรเป็น "Mary"

**สิ่งที่ LLM ทำไม่ได้:**
- ❌ ไม่ได้ **bind concepts** เหล่านี้เข้าด้วยกัน
- ❌ ไม่มีเหตุผลที่จะเชื่อว่า "Mary Stone's husband is" ควรจบด้วย "Tom"

**สำหรับ Human:**
- ประโยค "Tom's wife is Mary" เป็น **embodied concept**
- มี **dozens of connotations** รวมถึงข้อสรุปที่ว่า Mary's husband is Tom

---

## ส่วนที่ 12: Speaking to an LLM เหมือนพูดกับ Committee

### Analogy ที่น่าสนใจ
> "When you speak to an LLM, it's like speaking to a **gigantic committee of drastically varying expertise**"

- **Higher quality circuits** บางครั้งถูก reinforce
- แต่บางครั้งก็ถูก **drowned out by lower quality circuits**

### LLMs เป็น Alien Intelligences
- ทำทุกวิธี (ง่ายหรือยาก) เพื่อ **predict the next token**
- ไม่ได้ aspire to simplicity หรือ parsimony
- แค่เรียนรู้ connection อะไรก็ตาม (brittle หรือ algorithmic) ที่จะทำให้งานสำเร็จ

---

## ส่วนที่ 13: ปัญหาของ Epistemic Trust

### ทำไมเราไม่รู้ว่าควรเชื่อถือคำตอบไหน
เมื่อ LLM ตอบถูก เราไม่รู้ว่ามันใช้:
- ✅ **Unifying mechanism** (deep understanding) หรือ
- ❌ **Swarm of shallow heuristics** (surface-level memorization)

นี่คือเหตุผลที่เราไม่สามารถมี **epistemic trust** (ความเชื่อถือทางความรู้) ได้เต็มที่

---

## ส่วนที่ 14: Cognitive Psychology Comparison

### Humans ก็ทำแบบเดียวกัน
- บางครั้ง rely on **shortcuts**
- พูดหรือทำ **first thing that comes to mind** โดยไม่คิด
- บางคนพยายาม **double-check** และคิดลึกซึ้งกว่า

### ข้อแตกต่าง
- Humans มี embodied understanding
- LLMs มีแค่ statistical patterns

---

## ส่วนที่ 15: อนาคตของ LLMs - Possible Breakthroughs

### Data Augmentation
- ปัญหาเรื่อง **Tom and Mary** สามารถแก้ได้ด้วย data augmentation
- แต่ยังมีปัญหาอื่นๆ อีกมากมาย

### Reinforcement Learning
- มี **mixed evidence** ว่า RL สามารถเสริมสร้าง higher circuits ได้
- ปัญหาคือเมื่อ LLM เรียนรู้พอที่จะตอบถูกส่วนใหญ่แล้ว มัน **มี incentive น้อยลง** ที่จะเรียนรู้ higher circuits เพื่อตอบถูกมากขึ้น

### แนวทางที่เป็นไปได้
**จาก Paper:**
- encourage models ให้ถึง **state of almost confusion**
- ตอนนั้นจะสามารถ explore avenues ต่างๆ ได้ productively ที่สุด

**ทิศทางอื่นๆ:**
- **New modalities** - training บน data ประเภทใหม่ๆ
- **Access to national laboratories** - รัฐบาลอเมริกัน ให้ AI labs เข้าถึง dozen national labs
- **Hybrid architectures** - ที่ proven their worth กับ weather forecasting แล้ว

---

## ส่วนที่ 16: MATS Program (Sponsor)

สำหรับคนที่สนใจ **the why behind LLMs:**
- **MATS Program** = training researchers ทำงานเกี่ยวกับ **reducing risks from unaligned AI**
- Deadline: **4 days** จากวันที่วิดีโอออก (summer 2026 program)
- Alumni ไปทำงานที่ Meta, Anthropic, DeepMind
- มี:
  - World-class mentorship
  - Stipend
  - Compute budget
  - Full cost coverage

---

## บทสรุปและ Key Takeaways

### The Middle Path

ผู้สร้างวิดีโอเตือนให้หลีกเลี่ยงทั้งสอง extreme:

**❌ Extreme 1: Dismiss ว่า AI ไร้ประโยชน์**
- คิดว่า AI เป็นแค่ hype
- คิดว่า hallucinate ตลอดเวลา

**❌ Extreme 2: Panic ว่า AGI มาแล้ว**
- คิดว่า career เรา doomed
- คิดว่าต้องใช้ tool ล่าสุดทุกตัวไม่งั้นตกยุค

**✅ The Middle Path:**
- AI **มี productivity gains ที่แท้จริง**
- แต่ยัง**ไม่ได้ถึงระดับ AGI**
- ต้อง **review และ edit** output จาก AI เสมอ
- ใช้เวลา **น้อยกว่าทำเองตั้งแต้นต้น** (ตาม research data)

### Understanding LLMs Better

**สิ่งที่ควรรู้:**
1. LLMs มี understanding **แบบกระจัดกระจาย** ข้าม 3 levels
2. บางครั้งใช้ **deep algorithms**, บางครั้งใช้ **shallow heuristics**
3. เป็น **alien intelligences** ที่ทำงานต่างจาก humans
4. มี potential สำหรับ **breakthrough** ในอนาคต

### ผลกระทบต่อตลาดแรงงาน

**ข้อมูลจริงจาก Oxford Economics:**
- ❌ ยัง**ไม่มี mass layoffs** จาก AI
- ❌ **Labor productivity ไม่ได้พุ่ง** อย่างที่คาดการณ์
- ✅ **New graduate unemployment** ไม่ได้สูงกว่าปีก่อนๆ
- ✅ มีแนวโน้ม**ลดลงเล็กน้อย** ในปีที่แล้ว

### คำแนะนำสุดท้าย

> "Maximal understanding of AI models and productivity using them comes from **that place in the middle**"

- ไม่ต้องกลัวว่า job จะหาย
- แต่ควรเริ่มใช้ AI เพื่อเพิ่ม productivity
- ต้อง review และ fact-check output เสมอ
- อย่าถือว่า AI mistakes = ความผิดของคุณ

---

## คำศัพท์สำคัญ (Keywords)

| คำศัพท์ | ความหมาย |
|---------|----------|
| **AGI (Artificial General Intelligence)** | AI ที่มีความสามารถเท่าเทียมหรือเหนือกว่ามนุษย์ในทุกด้าน |
| **LLM (Large Language Model)** | โมเดลภาษาขนาดใหญ่ เช่น Claude, GPT |
| **Claude Co-work** | Tool ใหม่จาก Anthropic สำหรับ automate งานที่ไม่ใช่ coding |
| **Claude Code** | Tool สำหรับช่วย coding จาก Anthropic |
| **Claude Opus 4.5** | Model ล่าสุดจาก Anthropic ที่ powerful ที่สุด |
| **White-collar work** | งานออฟฟิศ งานที่ใช้ความรู้และทักษะทางปัญญา |
| **Knowledge work** | งานที่ต้องใช้ความรู้เป็นหลัก เช่น วิเคราะห์ วางแผน เขียน |
| **Hallucination** | การที่ AI สร้างข้อมูลเท็จหรือไม่ถูกต้องขึ้นมา |
| **Brittle** | เปราะบาง ไม่แข็งแรง ทำงานไม่สม่ำเสมอ |
| **Heuristics** | กฎเกณฑ์ง่ายๆ หรือ shortcuts ในการตัดสินใจ |
| **Circuits (in neural networks)** | วงจรหรือ pathways ใน neural network ที่ทำหน้าที่เฉพาะ |
| **Token** | หน่วยพื้นฐานของข้อความที่ AI ประมวลผล (อาจเป็นคำหรือส่วนของคำ) |
| **Grok** | เข้าใจอย่างลึกซึ้งและสมบูรณ์ |
| **Embodied concept** | แนวคิดที่มีความหมายลึกซึ้งและเชื่อมโยงกับประสบการณ์ |
| **Tipping point** | จุดเปลี่ยน จุดที่เกิดการเปลี่ยนแปลงอย่างมีนัยสำคัญ |
| **Productivity multiplier** | ตัวคูณประสิทธิภาพ การเพิ่มผลผลิตเป็นเท่าตัว |
| **Blind human grading** | การให้คนประเมินโดยไม่รู้ว่าผลงานมาจาก AI หรือคน |
| **Labor productivity** | ผลผลิตต่อชั่วโมงการทำงาน |
| **Frontier models** | โมเดล AI ที่ล้ำหน้าและทันสมัยที่สุด |
| **Data augmentation** | การเพิ่มข้อมูล training ด้วยวิธีต่างๆ |
| **Reinforcement learning (RL)** | การเรียนรู้โดยการทดลองและรับ feedback |
| **Epistemic trust** | ความเชื่อถือทางความรู้ ความน่าเชื่อถือของข้อมูล |
| **Modalities** | รูปแบบของข้อมูล เช่น ข้อความ รูปภาพ เสียง |
| **Hybrid architectures** | สถาปัตยกรรมแบบผสม รวมหลายเทคนิคเข้าด้วยกัน |
| **State of confusion** | สถานะของความสับสน ช่วงที่ model กำลังสำรวจ options |
| **Alien intelligence** | ปัญญาที่แตกต่างจากมนุษย์โดยสิ้นเชิง |
| **Caveat** | คำเตือน ข้อสงวน |
| **Scaffold** | โครงสร้างหรือกรอบการทำงาน |
