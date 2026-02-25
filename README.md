# React yordamida Full Stack loyiha yaratish

Ushbu qo‘llanmada **Vite** orqali React loyihasini yaratish, o‘rnatish va ishga tushirish bosqichlari keltirilgan.

---

## 1. React o‘rnatish (Vite orqali)

Yangi React loyihasini yaratish uchun terminalda quyidagi buyruqni ishga tushiring:

```bash
npm create vite@latest frontend -- --template react

Ushbu buyruq quyidagilarni bajaradi:
frontend nomli papka yaratadi
React template asosida loyiha generatsiya qiladi

2. Yaratilgan loyiha papkasiga kirish
cd frontend

3. Kerakli kutubxonalarni o‘rnatish
npm install

Ushbu buyruq loyiha uchun zarur barcha paketlarni (node_modules) o‘rnatadi.

4. Loyihani ishga tushirish (Development mode)
npm run dev

Shundan so‘ng terminalda lokal manzil chiqadi. Odatda quyidagi manzil hosil bo‘ladi:
http://localhost:5173/
Brauzer orqali ushbu manzilga kirib loyihani ko‘rishingiz mumkin.

------------------------------------------------------------------------------------------------------------------------------------------
# React (Vite) loyiha strukturasi tushuntirishi

Ushbu hujjatda React (Vite) loyihasidagi asosiy papka va fayllarning vazifalari tushuntirilgan.

---

## public/

Statik fayllar saqlanadigan papka.

Bu yerga rasm, favicon va boshqa o‘zgarmaydigan fayllar joylanadi. Build vaqtida bu fayllar qayta ishlanmaydi va to‘g‘ridan-to‘g‘ri brauzerga uzatiladi.

---

## src/

Loyihaning asosiy React kodi joylashgan papka.

Bu yerda:
- App.jsx
- main.jsx
- componentlar
- sahifalar
- css fayllar

saqlanadi.

Ilovaning barcha mantiqi shu yerda yoziladi.

---

## .env

Muhit o‘zgaruvchilari saqlanadi.

Masalan:

VITE_API_URL=http://localhost:8000

Vite loyihasida environment variable lar VITE_ bilan boshlanishi shart.

---

## .gitignore

Git qaysi fayllarni repozitoriyga qo‘shmasligini belgilaydi.

Masalan:
- node_modules
- .env
- dist

---

## README.md

Loyiha haqida umumiy ma’lumot beruvchi hujjat.

Unda:
- loyiha tavsifi
- o‘rnatish bosqichlari
- ishlatish yo‘riqnomasi

yoziladi.

---

## eslint.config.js

ESLint konfiguratsiya fayli.

JavaScript kodni tekshiradi, xatolarni aniqlaydi va kod stilini nazorat qiladi.

---

## index.html

Asosiy HTML fayl.

React ilovasi ushbu fayldagi `div#root` elementiga render qilinadi.

---

## package.json

Loyiha konfiguratsiyasi va dependency lar ro‘yxati.

Unda:
- loyiha nomi va versiyasi
- scripts
- dependencies
- devDependencies

saqlanadi.

---

## package-lock.json

Paketlarning aniq versiyalarini saqlaydi.

Barcha developerlarda bir xil dependency versiyasi ishlashi uchun kerak.

---

## vite.config.js

Vite konfiguratsiya fayli.

Bu yerda:
- server sozlamalari
- proxy
- pluginlar
- aliaslar

kabi sozlamalar yoziladi.
