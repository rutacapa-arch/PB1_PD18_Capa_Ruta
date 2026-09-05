# CI refleksija  

## Kas notika, kad tests bija kļūdains?  

Kad apzināti sabojāju testu un veicu push (commit e457167), GitHub Actions sadaļā parādījās sarkans indikators. Tas neļāva "pabeigt" uzdevunu, kamēr netika izlabota kļūda test_kalkulators.py failā.  
   
## Kāpēc CI palīdz ātri pamanīt kļūdas?  

CI palaiž testus automātiski uzreiz pēc katra push, tāpēc kļūda ir redzama dažu sekunžu laikā, nevis vēlāk, kad to būtu daudz grūtāk izsekot.  
  
## Kā DoD palīdz komandai?  

Definition of Done nosaka skaidrus, pārbaudāmus kritērijus tam, kas nozīmē "pabeigts" - tā visi komandas locekļi saprot uzdevuma statusu vienādi, nevis subjektīvi.  
  
## Kā mainījās tava attieksme pret git push?  
  
Tagad git push man nav tikai koda sūtīšana, bet gan "pārbaudes pieprasījums". Es jūtos drošāk, zinot, ka sistēma mani pārbauda - kad pēc labojuma (commit 1cace9b) redzēju zaļu statusu, bija skaidrs apstiprinājums, ka darbs tiešām ir pabeigts.  
