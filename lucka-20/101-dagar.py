lista = ['trenoll6', 'sjunoll72nionio', 'sexfemtrenolltvå', 'fyratre47åttanoll', 'femåtta23tre', 'fyra4', 'åtta9', 'tre', 'niosex3', 'ettfyra9', 'sju', 'tre5nollsex24sju', 'nioett', 'tvåtre', 'fyratre8nollnollfem', 'tre99åttatre5', 'sexsexfem', 'två4', 'nio28', 'sex9femfyra4nio', 'sex', 'två1niofyrasex1', 'åtta8', 'tvååttafyra', 'nioniofyra20nollett', 'ett2801', 'fyra76fem', 'ett529tresju1', 'fyrafyra8', 'åtta0', 'sexåtta50ett4tre', 'åtta6ettnionioett3', 'sex2nionollåttasju', 'ett', 'tre7tretre74', 'fem792nio', 'nio0', 'sju1454', 'åtta2femnio9', 'sexfyra78två6', 'fyraett962fem2', 'femtre13sjufem3', 'sex0', 'fyrasju9sexniofem', 'sexfem50', 'ett2sju343', 'åtta6tvåtvå3', 'fem8767', 'treett0sex16sju', 'niotre1', 'två', 'fyranollsju99', 'ettåtta141', 'nio5två6fem', 'tre75sjunioniofem', 'nio', 'sjuåtta43', 'sex9fyra', 'tvåsju6sex', 'åtta9432fem', 'åttafyra96sex', 'niosexett', 'ett85ettnioåtta8', 'fyra1fyra6sex', 'fem2', 'niofem09trenoll', 'två778', 'fyrafyra0ett', 'två73åtta9', 'sjufyra', 'fem', 'sextvå869åtta', 'sextre', 'sex1fyra2nio8', 'åtta4sju2åtta8', 'ettsju', 'åttasju66trefyra', 'nio', 'etttvååtta', 'åtta5', 'tresju65tre0ett', 'tre73', 'åtta5sju0två4två', 'åtta', 'sju', 'trenollfem4sex', 'sex8tre48ett', 'trefyra', 'fem89', 'två8fyra28ettåtta', 'sjutretvå20', 'ettsex7nollett59', 'tre4åttasju6åtta', 'fyrafem5', 'sextre0nio760', 'två14fem', 'tretreåtta', 'fyrafyra9åttafyra2sju', 'fyra', 'tvååtta', 'sexettsex21två']
total_made = 0

for number in lista:
    number = number.replace('noll', '0')
    number = number.replace('ett', '1')
    number = number.replace('två', '2')
    number = number.replace('tre', '3')
    number = number.replace('fyra', '4')
    number = number.replace('fem', '5')
    number = number.replace('sex', '6')
    number = number.replace('sju', '7')
    number = number.replace('åtta', '8')
    number = number.replace('nio', '9')
    int_number = int(number)
    total_made += int_number

print(total_made)
