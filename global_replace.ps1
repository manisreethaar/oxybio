 = Get-ChildItem -Path "e:\OXYBIO" -Filter "*.html" -File
foreach ( in ) {
     = Get-Content -Path .FullName -Raw -Encoding UTF8
     =  -replace 'Join Waitlist', 'Follow Our R&D Journey'
     =  -replace 'href="index.html#join"', 'href="index.html#updates"'
     =  -replace 'href="#join"', 'href="#updates"'
     =  -replace 'Unlocking millet bioavailability and mushroom fortification', 'Researching millet bioavailability and mushroom fortification'
     =  -replace 'Efficacy Study Planned \(Pre-Launch\)', 'In Active Research & Development'
     =  -replace 'Efficacy Study Planned', 'Research & Development Phase'
    [IO.File]::WriteAllText(.FullName, , [Text.Encoding]::UTF8)
}
