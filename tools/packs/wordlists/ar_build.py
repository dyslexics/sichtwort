# -*- coding: utf-8 -*-
"""Trimmt den Rohpool ar_raw.WORDS auf genau 500 Eintraege und schreibt ar500.json."""
import json, collections, sys
import ar_raw

REMOVE = set("""
بلى كي معظم سريعا ضد نحو هكذا إذن أولئك هن بينما مئة ألف نصف كذلك يا
حفيد عجوز شاب ضيف والد والدة إنسان شخص
طباشير خريطة نشيد لغة خط مدير جرس حساب قراءة كتابة صفحة واجب امتحان
ماعز زرافة عنكبوت سلحفاة بومة غراب ببغاء حوت قرش كتكوت عش ريشة ذئب ثعلب حمامة
معكرونة حساء فراولة ليمون تين رمان مشمش خوخ كمثرى طماطم بطاطا ثوم فلفل مربى بسكويت شوكولاتة كأس إبريق قدر شوكة حلوى
شفة خد جبين ظفر عظم جلد دمعة ابتسامة
بحيرة غصن صحراء طين برق رعد طقس فجر ظل موجة جزيرة حقل رمل عشب
سجادة ستارة قفل حوض راديو غسالة مكنسة منشفة وسادة بطانية سلة حبل خيط إبرة مقص
تنورة وشاح قفاز زر خاتم
ساحة دكان صيدلية فندق بريد متحف مصنع ميناء عجلة نجار خباز صياد تاجر طباخ رسام جندي أمير
أرجوحة مكعب بالون سر موسيقى كلام راحة سعر حرية صدق
جار طالبة تلميذة صديقة ظهر عقل دم سن تراب نهار دقيقة سلم رف صندوق مرآة جيب ثوب نظارة شاحنة عامل
همس أشار وعد قاس عد سقى أطعم نما قطف زرع نادى أرسل أحضر احتاج استطاع توقف فقد غادر صار أصبح دعا قابل حسب رتب خلع
""".split())

ADJ_KEEP = set("""
أحمر أزرق أخضر أصفر أبيض أسود بني رمادي برتقالي وردي بنفسجي ذهبي فضي
كبير صغير طويل قصير جديد قديم جميل سريع بطيء قوي ضعيف سهل صعب نظيف
حار بارد ثقيل خفيف غني فقير سعيد حزين غاضب خائف متعب مريض لذيذ حلو
واسع ضيق فارغ مفتوح مغلق هادئ لطيف قريب بعيد
""".split())

out = []
for w, t in ar_raw.WORDS:
    if w in REMOVE:
        continue
    if t == "a" and w not in ADJ_KEEP:
        continue
    out.append([w, t])

# --- Validierung ---
errs = []
if len(out) != 500:
    errs.append("Anzahl=%d (soll 500)" % len(out))
c = collections.Counter(w for w, _ in out)
dups = [k for k, v in c.items() if v > 1]
if dups:
    errs.append("Duplikate: %s" % dups)
bad = [w for w, _ in out if "-" in w]
if bad:
    errs.append("Silbentrennung: %s" % bad)
art = [w for w, _ in out if w.startswith("ال")]
if art:
    errs.append("Artikel: %s" % art)
sp = [w for w, _ in out if " " in w or not w.strip()]
if sp:
    errs.append("Mehrwort/leer: %s" % sp)
bt = sorted({t for _, t in out} - {"n", "v", "a", "o"})
if bt:
    errs.append("Typen: %s" % bt)
if errs:
    print("FEHLER: " + " | ".join(errs))
    sys.exit(1)

data = {
    "id": "ar500",
    "language": "ar",
    "nameDE": "Grundwortschatz Arabisch",
    "nameEN": "Arabic basic vocabulary",
    "words": out,
}
path = "/home/mario/sichtwort/tools/packs/wordlists/ar500.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
    f.write("\n")

t = collections.Counter(t for _, t in out)
print("OK ar %d Wörter, 0 mit Silbentrennung, n=%d v=%d a=%d o=%d"
      % (len(out), t["n"], t["v"], t["a"], t["o"]))
