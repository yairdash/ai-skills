# Video Production Kit — ערכת עריכה ומושן גרפיקס

גרסה 1.0.0. שם הסקיל: `video-production-kit`.

חבילה לעבודה מקומית עם Herk Edit Kit, FFmpeg, HyperFrames ו־Remotion:
סרטוני רשת, עריכת דיבור, כתוביות, אינפוגרפיקה ואנימציה.

| רכיב | שימוש | מה כלול |
| --- | --- | --- |
| Herk Edit Kit 2.0.0 | חיתוך שתיקות, בדיקת טייקים, סיפור ו־Shorts | 15 מודולי סקיל, כלי עזר ובדיקות, 406 כרטיסי עיצוב ראשוניים |
| FFmpeg | חיתוך, חיבור, המרה, אודיו ובדיקת תוצר | מדריך וחיבור להתקנה המקומית |
| HyperFrames 0.7.109 | אנימציה ב־HTML/GSAP | תלות נעולה דרך Herk ותבנית התחלה |
| Remotion 4.0.536 | אנימציה ב־React וסרטונים מבוססי נתונים | תבנית עצמאית וקובץ נעילת תלויות |
| עברית ותמלול | RTL, כתוביות ותזמון | הנחיות QA וממיר Whisper לפורמט Herk |

## התקנה

העתיקו את **כל התיקייה**, כולל vendor, references ו־templates, לתיקיית
הסקילים של הפרויקט, למשל `.agents/skills/video-production-kit` בקודקס.
אין להעתיק רק SKILL.md. הסקיל הראשי מפנה למודולים לפי המשימה; המודולים
המשובצים אינם מיועדים להתקנה עצמאית ללא ספריות העזר שלהם.

נדרשים Node.js 22.13+ או 24+, npm, ו־FFmpeg עם ffprobe.
Python 3.10+ נחוץ רק לממיר התמלול ולכלי האריזה/העתקה.
מתוך תיקיית הסקיל:

```text
node kit.mjs doctor
node kit.mjs setup
node kit.mjs setup-remotion
node kit.mjs hyperframes browser ensure
node kit.mjs remotion browser ensure
```

ההתקנה מורידה תלויות npm ודפדפן. אין כאן התקנת אופליין מלאה, מודלי תמלול
או חשבונות לשירותי מדיה. אין צורך במפתח API לדוגמאות הבדיקה.
אם FFmpeg אינו ב־PATH, הגדירו את תיקיית bin המקומית:

```text
node kit.mjs configure ffmpegDir "ABSOLUTE_PATH_TO_FFMPEG_BIN"
```

אפשר להגדיר גם `npmCli` ל־npm-cli.js ו־`browser` ל־Chrome Headless Shell.
ההגדרות נשמרות ב־local.config.json המוחרג מ־Git. אין לפרסם את הקובץ.
מומלץ להתקין גם את תוסף Remotion הרשמי; הוא אינו נכלל בחבילה הזו.

## שימוש

דוגמה: ״השתמש ב־$video-production-kit לעריכת סרטון הדיבור הזה. שמור על
המשמעות, קצר שתיקות והכן MP4 יחד עם פרויקט ותמלול מעודכן.״

לאינפוגרפיקה: ״הכן סרטון של 12 שניות ב־Remotion, בעברית, כולל קובץ סופי
ופרויקט לעריכה.״ בחירה מפורשת במנוע מכובדת; אין מעבר אוטומטי בין המנועים.

בדיקות ויצירת פרויקט HyperFrames:

```text
node kit.mjs npm test
node kit.mjs herk scripts/check-kit.mjs
node kit.mjs herk scripts/smoke-media.mjs
node kit.mjs herk scripts/new-video.mjs my-video
```

מתוך runtime/herk/video-projects/my-video:

```text
node ../../../../kit.mjs hyperframes lint
node ../../../../kit.mjs hyperframes preview
node ../../../../kit.mjs hyperframes render --quality draft --output renders/draft.mp4
```

בדיקת Remotion, מתוך תיקיית הסקיל:

```text
node kit.mjs remotion studio --no-open
node kit.mjs remotion render src/index.tsx KitSmoke out/smoke.mp4 --codec=h264
```

ל־Whisper נדרשות חותמות זמן ברמת המילה. הממיר אינו מנחש אותן:

```text
python normalize_transcript.py whisper.json herk-transcript.json --duration 60.5
```

המשך הוא הזמן האמיתי של המדיה לפי ffprobe. תמלול מקומי, זיהוי דוברים
ושירותים בתשלום מוגדרים בנפרד לפי הצורך; הם אינם מותקנים אוטומטית.

## ניידות, מקורות ומגבלות

אפשר להעביר את התיקייה למחשב אחר ולהריץ setup מחדש. לשמירת עותק ZIP של
המקורות, הריצו `python package_kit.py`; הפלט אינו כולל runtime או הגדרות מקומיות.
העתקה לפרויקט אחר: `python package_kit.py --install "PROJECT/.agents/skills/video-production-kit"`.
הכלי מסרב לדרוס תיקייה קיימת. יש לשמור התאמות לפני עדכון.

נבדקו ב־Windows חיתוכים, תזמון ושני מנועי רינדור; פירוט ב־[VERIFY.md](VERIFY.md).
אין טענה לבדיקת macOS/Linux, ענן או נייד, או לאיכות הפקה של כל כרטיס.
פרויקטי HTML ו־React ניתנים לעריכה בכליהם; אין כאן ייצוא מאומת לטיימליין
מקורי של CapCut או DaVinci.

תיעוד HyperFrames החדש יותר נשמר לעיון בלבד תחת references/hyperframes;
קובצי הכניסה שלו נקראים REFERENCE.md כדי שלא יותקנו כסקילים חלקיים.
הכלים המבוצעים משתמשים בגרסה הנעולה של Herk, ולא בהכרח בגרסה החדשה ביותר.

ראו [PROVENANCE.json](PROVENANCE.json), [מקורות ורישיונות](THIRD_PARTY_NOTICES.md)
ו־sources.lock.json. נכסי AIS, סרטוני דוגמה מוגנים, חומרי משתמש, סודות,
גופני Windows וקובצי הרצה אינם מופצים בחבילה.
