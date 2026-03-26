"""Localization strings for English and Turkish."""

STRINGS = {
    "en": {
        "window_title": "Exe Launcher Builder",
        "output_label": "Output Launcher EXE Name (e.g.: Launch.exe):",
        "output_default": "Launch.exe",
        "target_label": "Target EXE Name to Search For (e.g.: game.exe):",
        "select_icon_btn": "Select Icon from Computer (.ico)",
        "icon_default_text": "(Default Icon Selected)",
        "pull_header": "Or point to a target .EXE file to pull all its original settings:",
        "pull_btn": "⚡ Pull Data from Original .EXE",
        "build_btn": "Build!",
        "pull_dialog_title": "Select the Original Application to Extract Icon and Name",
        "pull_filter_exe": "Original Application",
        "pull_filter_all": "All Files",
        "pull_status_pulling": "⚙️ Pulling data from original application...",
        "pull_status_success": "✅ Original .EXE icon and name copied successfully!",
        "pull_status_icon_fail": "⚠️ Warning: Could not extract icon, only names were copied.",
        "pull_status_error": "⚠️ Error: {error}",
        "pulled_label": "Pulled: {name}..",
        "select_icon_title": "Select an Image or Icon",
        "select_icon_filter": "Supported Images",
        "icon_converted": "Converted: {name}..",
        "icon_converted_status": "✅ Your image was converted to HD Icon!",
        "icon_convert_warn": "⚠️ Warning: Image could not be processed, will be used directly.",
        "warn_target_empty": "Please enter the target EXE name to launch!",
        "warn_output_empty": "Please enter the output file name!",
        "error_csc_missing": "C# compiler (csc.exe) was not found on your system.",
        "error_file_locked": (
            "The file '{name}' is currently open, being scanned by Windows, or locked!\n"
            "Please close it, delete it, or change the output name and try again."
        ),
        "success_msg": "Launcher was built successfully:\n{path}",
        "error_compile": "Compiler error:\n{error}",
        "error_compile_unknown": "Unknown Compiler Error",
        "error_generic": "An error occurred:\n{error}",
        "output_suffix": "_Launch.exe",
        "lang_label": "Language:",
        "info_title": "About Exe Launcher Builder",
        "info_text": (
            "Exe Launcher Builder creates portable shortcut EXEs for any application.\n\n"
            "Unlike regular Windows shortcuts (.lnk), these launchers search for the\n"
            "target EXE by name — so they keep working even if the folder is moved\n"
            "to another drive or computer. Perfect for portable game collections!\n\n"
            "How it works:\n"
            "1. Enter the target EXE name (e.g. game.exe)\n"
            "2. Optionally set a custom icon or pull it from the original EXE\n"
            "3. Click Build — a portable launcher is compiled\n\n"
            "The launcher searches the folder it is placed in and all its\n"
            "subfolders to find and start the target EXE.\n\n"
            "⚠️ If multiple EXEs with the same name exist in subfolders,\n"
            "the launcher will start whichever it finds first.\n\n"
            "Created by Legendnoobe"
        ),
        "welcome_title": "Welcome!",
        "welcome_text": (
            "Welcome to Exe Launcher Builder!\n\n"
            "Create portable shortcut EXEs that find and launch any application\n"
            "by name — works even if the folder is moved to another drive.\n\n"
            "Click the ℹ️ button at any time for more details."
        ),
    },
    "tr": {
        "window_title": "Exe Başlatıcı Oluşturucu",
        "output_label": "Oluşturulacak Başlatıcı EXE Adı (örn: Baslat.exe):",
        "output_default": "Baslat.exe",
        "target_label": "İçinde Aranacak Hedef EXE Adı (örn: oyun.exe):",
        "select_icon_btn": "Bilgisayardan İkon Seç (.ico)",
        "icon_default_text": "(Varsayılan İkon Seçili)",
        "pull_header": "Veya Hedef Bir .EXE Dosyası Gösterip Tüm Orijinal Ayarlarını Çekebilirsiniz:",
        "pull_btn": "⚡ Hedef Orijinal .EXE'den Verileri Çek",
        "build_btn": "Oluştur!",
        "pull_dialog_title": "Simgesi ve Adı Çekilecek Orijinal Uygulamayı Seçin",
        "pull_filter_exe": "Orijinal Uygulama",
        "pull_filter_all": "Tüm Dosyalar",
        "pull_status_pulling": "⚙️ Orijinal uygulamadan veriler çekiliyor...",
        "pull_status_success": "✅ Orijinal .EXE Simgesi ve Adı başarıyla kopyalandı!",
        "pull_status_icon_fail": "⚠️ Uyarı: İkon çekilemedi, sadece isimler kopyalandı.",
        "pull_status_error": "⚠️ Hata oluştu: {error}",
        "pulled_label": "Çekildi: {name}..",
        "select_icon_title": "Bir Görsel veya İkon Seçin",
        "select_icon_filter": "Desteklenen Görseller",
        "icon_converted": "Dönüştürüldü: {name}..",
        "icon_converted_status": "✅ Kendi görseliniz HD İkona dönüştürüldü!",
        "icon_convert_warn": "⚠️ Uyarı: Resim işlenemedi, direkt kullanılacak.",
        "warn_target_empty": "Lütfen başlatılacak hedef EXE adını giriniz!",
        "warn_output_empty": "Lütfen oluşturulacak dosya adını giriniz!",
        "error_csc_missing": "Sisteminizde C# derleyicisi (csc.exe) bulunamadı.",
        "error_file_locked": (
            "'{name}' adlı dosya şu an açık, Windows tarafından taranıyor veya kilitli!\n"
            "Lütfen önce arka planda kapatın, silin veya Oluşturulacak Adı değiştirip tekrar deneyin."
        ),
        "success_msg": "Başlatıcı başarıyla oluşturuldu:\n{path}",
        "error_compile": "Derleyici hatası:\n{error}",
        "error_compile_unknown": "Bilinmeyen Derleyici Hatası",
        "error_generic": "Bir sorun oluştu:\n{error}",
        "output_suffix": "_Baslat.exe",
        "lang_label": "Dil:",
        "info_title": "Exe Başlatıcı Oluşturucu Hakkında",
        "info_text": (
            "Exe Başlatıcı Oluşturucu, herhangi bir uygulama için taşınabilir\n"
            "kısayol EXE'leri oluşturur.\n\n"
            "Normal Windows kısayollarından (.lnk) farklı olarak, bu başlatıcılar\n"
            "hedef EXE'yi ada göre arar — klasör başka bir sürücüye veya bilgisayara\n"
            "taşınsa bile çalışmaya devam eder. Taşınabilir oyun koleksiyonları\n"
            "için mükemmel!\n\n"
            "Nasıl çalışır:\n"
            "1. Hedef EXE adını girin (örn: oyun.exe)\n"
            "2. İsteğe bağlı olarak özel bir ikon seçin veya orijinal EXE'den çekin\n"
            "3. Oluştur'a tıklayın — taşınabilir bir başlatıcı derlenir\n\n"
            "Başlatıcı, yerleştirildiği klasörü ve tüm alt klasörlerini\n"
            "tarayarak hedef EXE'yi bulur ve çalıştırır.\n\n"
            "⚠️ Alt klasörlerde aynı ada sahip birden fazla EXE varsa,\n"
            "başlatıcı ilk bulduğunu çalıştırır.\n\n"
            "Legendnoobe tarafından geliştirilmiştir"
        ),
        "welcome_title": "Hoş Geldiniz!",
        "welcome_text": (
            "Exe Başlatıcı Oluşturucu'ya hoş geldiniz!\n\n"
            "Herhangi bir uygulamayı ada göre bulup başlatan taşınabilir\n"
            "kısayol EXE'leri oluşturun — klasör başka bir sürücüye\n"
            "taşınsa bile çalışır.\n\n"
            "Daha fazla bilgi için istediğiniz zaman ℹ️ butonuna tıklayın."
        ),
    },
}
