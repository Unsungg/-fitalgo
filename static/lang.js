const TR = {
    // Plan page
    'Daily Macronutrients': 'Günlük Makro Besinler',
    'Protein': 'Protein',
    'Carbohydrates': 'Karbonhidrat',
    'Fat': 'Yağ',
    'Weekly Workout Plan': 'Haftalık Antrenman Planı',
    'Daily Meal Plan': 'Günlük Öğün Planı',
    'Log Your Progress': 'İlerleme Kaydet',
    'Update My Plan': 'Planımı Güncelle',
    'Progress History': 'İlerleme Geçmişi',
    'Create New Plan': 'Yeni Plan Oluştur',
    'Weight Progress Chart': 'Kilo Takip Grafiği',
    // Buttons
    'AI Coach': 'AI Koç',
    'Detailed Workout': 'Detaylı Antrenman',
    'Supplements': 'Takviyeler',
    'Meal Recipes': 'Yemek Tarifleri',
    'Start Timer': 'Zamanlayıcıyı Başlat',
    'Back to Dashboard': 'Dashboard\'a Dön',
    'Ask AI Coach': 'AI Koça Sor',
    'View Supplements': 'Takviyeleri Gör',
    // Supplement page
    'Supplement Guide': 'Takviye Rehberi',
    'Essential Supplements': 'Temel Takviyeler',
    'Essential': 'Temel',
    'Recommended': 'Önerilen',
    'Optional': 'İsteğe Bağlı',
    'Dosage': 'Doz',
    'When': 'Ne Zaman',
    'Benefit': 'Faydası',
    'Natural & Organic Options': 'Doğal ve Organik Seçenekler',
    // Recipe page
    'Ingredients': 'Malzemeler',
    'How to prepare': 'Nasıl Hazırlanır',
    'Breakfast': 'Kahvaltı',
    'Lunch': 'Öğle Yemeği',
    'Dinner': 'Akşam Yemeği',
    // Workout page
    'Your detailed workout plan': 'Detaylı antrenman planın',
    'Your Goal': 'Hedefin',
    'Training Frequency': 'Antrenman Sıklığı',
    'Session Duration': 'Seans Süresi',
    'Rest day — focus on recovery, hydration and sleep': 'Dinlenme günü — toparlanma, su içme ve uykuya odaklan',
    'Form tip': 'Form ipucu',
    'Common mistake': 'Yaygın hata',
    // Timer page
    'Workout Timer': 'Antrenman Zamanlayıcısı',
    'Ready to start your workout!': 'Antrenmanına başlamaya hazır mısın!',
    'Total Workout Time': 'Toplam Antrenman Süresi',
    'Calories Burned': 'Yakılan Kalori',
    'Exercises Done': 'Tamamlanan Egzersiz',
    'Total Exercises': 'Toplam Egzersiz',
    'Start Workout': 'Antrenmanı Başlat',
    'Pause': 'Duraklat',
    'Resume': 'Devam Et',
    'Reset': 'Sıfırla',
    "Today's Exercises": 'Bugünün Egzersizleri',
    'Done': 'Tamamlandı',
    'Workout Complete!': 'Antrenman Tamamlandı!',
    // AI Coach
    'Ask me anything about fitness and nutrition!': 'Fitness ve beslenme hakkında her şeyi sorabilirsin!',
    'Quick questions': 'Hızlı sorular',
    'Send': 'Gönder',
    'Back to Dashboard': 'Dashboard\'a Dön',
    // Days
    'Monday': 'Pazartesi',
    'Tuesday': 'Salı',
    'Wednesday': 'Çarşamba',
    'Thursday': 'Perşembe',
    'Friday': 'Cuma',
    'Saturday': 'Cumartesi',
    'Sunday': 'Pazar',
    'Rest day': 'Dinlenme Günü',
};

document.addEventListener('DOMContentLoaded', function() {
    // Add language button to every page
    var btn = document.createElement('button');
    btn.id = 'langBtn';
    btn.style = 'position:fixed;top:15px;right:15px;z-index:9999;background:rgba(102,126,234,0.9);border:none;color:white;border-radius:20px;padding:6px 16px;font-size:13px;cursor:pointer;';
    document.body.appendChild(btn);

    var currentLang = localStorage.getItem('fitalgo_lang') || 'en';
    btn.innerText = currentLang === 'tr' ? '🌐 English' : '🌐 Türkçe';

    if (currentLang === 'tr') translatePage();

    btn.addEventListener('click', function() {
        if (currentLang === 'en') {
            currentLang = 'tr';
            localStorage.setItem('fitalgo_lang', 'tr');
            btn.innerText = '🌐 English';
            translatePage();
        } else {
            currentLang = 'en';
            localStorage.setItem('fitalgo_lang', 'en');
            location.reload();
        }
    });

    function translatePage() {
        // Translate data-tr elements
        document.querySelectorAll('[data-tr]').forEach(function(el) {
            el.innerText = el.getAttribute('data-tr');
        });

        // Translate all text elements
        document.querySelectorAll('h1,h2,h3,h4,h5,h6,p,span,button,a,label,small,th,td').forEach(function(el) {
            if (el.id === 'langBtn') return;
            if (el.children.length === 0 && el.innerText) {
                var text = el.innerText.trim();
                if (TR[text]) el.innerText = TR[text];
            }
        });
    }
});