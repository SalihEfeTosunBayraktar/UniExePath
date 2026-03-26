# Exe Launcher Builder — INFO

## English

**Exe Launcher Builder** creates **portable shortcut EXEs** for any application.

Unlike regular Windows shortcuts (`.lnk`), these launchers search for the target EXE **by name** — so they keep working even if the folder is moved to another drive or computer. Perfect for portable game collections!

### How It Works

1. Enter the name of the target EXE (e.g. `game.exe`)
2. Optionally select a custom icon from your computer, or pull the icon directly from the original EXE
3. Click **Build!** — a portable launcher is compiled that recursively searches its directory tree for the target and starts it

The generated launcher uses the built-in Windows .NET C# compiler (`csc.exe`) and has **zero external dependencies** at runtime. Just place the launcher in the same folder (or a parent folder) as the target EXE and run it — it will find it anywhere in the subdirectories.

> **⚠️ Note:** If multiple EXE files with the same name exist in subdirectories, the launcher will start whichever one it finds first. Make sure the target EXE name is unique within the folder tree.

### Requirements

- Windows 10/11 with .NET Framework 4.x (built-in)
- Python 3.10+ (to run the builder itself)

---

## Türkçe

**Exe Başlatıcı Oluşturucu**, herhangi bir uygulama için **taşınabilir kısayol EXE'leri** oluşturur.

Normal Windows kısayollarından (`.lnk`) farklı olarak, bu başlatıcılar hedef EXE'yi **ada göre arar** — klasör başka bir sürücüye veya bilgisayara taşınsa bile çalışmaya devam eder. Taşınabilir oyun koleksiyonları için mükemmel!

### Nasıl Çalışır

1. Hedef EXE adını girin (örn: `oyun.exe`)
2. İsteğe bağlı olarak bilgisayarınızdan özel bir ikon seçin veya orijinal EXE'den ikonu çekin
3. **Oluştur!** butonuna tıklayın — klasör ağacında hedefi arayıp başlatan taşınabilir bir başlatıcı derlenir

Oluşturulan başlatıcı, yerleşik Windows .NET C# derleyicisini (`csc.exe`) kullanır ve çalışma zamanında **harici bağımlılığı yoktur**. Başlatıcıyı hedef EXE ile aynı klasöre (veya üst klasöre) koyup çalıştırmanız yeterlidir — alt dizinlerde nerede olursa olsun bulacaktır.

> **⚠️ Not:** Alt dizinlerde aynı ada sahip birden fazla EXE dosyası varsa, başlatıcı ilk bulduğunu çalıştırır. Hedef EXE adının klasör ağacında benzersiz olduğundan emin olun.

### Gereksinimler

- .NET Framework 4.x ile Windows 10/11 (yerleşik)
- Python 3.10+ (oluşturucuyu çalıştırmak için)

---

Created by **Legendnoobe**
