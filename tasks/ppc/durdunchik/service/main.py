import numpy as np
import qrcode, sys, random, string

parts_n = 300
text = "YA v svo3m poznan11 nastol'ko pr31spoln1lsya, chto ya kak budto by uzh3 sto tr1ll1onov m1ll1ardov l3t prozh1vayu na tr1ll1onah 1 tr1ll1onah tak1h zh3 plan3t, kak 3ta Z3mlya, mn3 3tot m1r absolyutno ponyat3n, 1 ya zd3s' 1shchu tol'ko odnogo - pokoya, um1rotvor3n1ya 1 vot 3toj garmon11, ot sl1yan1ya s b3skon3chno v3chnym, ot soz3rcan1ya v3l1kogo fraktal'nogo podob1ya 1 ot vot 3togo zam3chat3l'nogo vs33d1nstva sushch3stva, b3skon3chno v3chnogo, kuda n1 posmotr1, hot' vglub' - b3skon3chno malo3, hot' vvys' - b3skon3chno3 bol'sho3, pon1ma3sh'? A ty mn3 opyat' so svo1m vot 3t1m, 1d1 su3t1s' dal'sh3, 3to tvoyo raspr3d3l3n13, 3to tvoj put' 1 tvoj gor1zont poznan1ya 1 oshchushch3n1ya tvo3j pr1rody, on n3so1zm3r1mo m3lok po sravn3n1yu s mo1m, pon1ma3sh'? YA kak budto by uzh3 davno glubok1j star3c, b3ssm3rtnyj, nu 1l1 tam uzh3 pocht1 b3ssm3rtnyj, kotoryj na 3toj plan3t3 ot 3yo samogo zarozhd3n1ya, 3shchyo kogda tol'ko Solnc3 tol'ko-tol'ko sform1rovalos' kak zv3zda, 1 vot 3to gazopyl3vo3 oblako, vot, posl3 vzryva, Solnca, kogda ono vspyhnulo, kak zv3zda, nachalo formirovat' vot 3t1 koac3rvaty, plan3ty, pon1ma3sh', ya na 3toj Z3ml3 uzh3 kak budto pocht1 pyat' m1ll1ardov l3t zh1vu 1 znayu 3yo vdol' 1 pop3ryok 3tot v3s' m1r, a ty mne kak13-to... mn3 n3 vazhno na tvo1 tachk1, na tvo1 yahty, na tvo1 kvart1ry, tam, na tvoyo blago. YA byl na 3toj plan3t3 b3skon3chnym mnozh3stvom, 1 kruch3 C3zarya, 1 kruch3 G1tl3ra, 1 kruch3 vs3kh v3l1k1h, pon1ma3sh', byl, a gd3-to byl konch3nym govnom, 3shchyo huzh3, ch3m zd3s'. YA mnozh3stvo 3t1h sostoyan1j chuvstvuyu. Gd3-to ya byl bol'sh3 podob3n rast3n1yu, gd3-to ya bol'sh3 byl podob3n pt1c3, tam, ch3rvyu, gd3-to byl prosto sgustok kamnya, 3to vsyo 3st' dusha, pon1ma3sh'? Ona 1m33t gran1 podob1ya sov3rsh3nno mnogoobrazny3, b3skon3chno3 mnozh3stvo. No t3b3 3togo n3 ponyat', po3tomu ty 3zzhaj s3b3 , my v 3tom m1r3 kak by zh1v3m raznym1 oshchushch3n1yam1 1 raznym1 str3ml3n1yam1, sootv3tstv3nno, razno3 nash3 1 m3sto, razno3 1 nash3 raspr3d3l3n13. T3b3 ya zh3layu vs3 samy3 kruty3 tachk1 chtob byl1 u t3bya, 1 vs3 samy3 luchsh3 samk1, 3sl1 malo 1dej, obrashchajsya ko mn3, ya t3b3 na kazhduyu tvoyu 1d3yu pr3dlozhu sotnyu tr1ll1onov, kak vsyo d3lat'. Nu a ya vsyo, ya 1du kak glubok1j star3c,uzr3vsh1j v3chno3, pr1kosnuvsh1jsya k Bozh3stv3nnomu, sam stal bogopodob3n 1 ustr3ml3n v 3to b3skon3chno3, 1 kotoryj v um1rotvor3n11, poko3, garmon11, blagodat1, v 3tom sokrovennom blazh3nstv3 pr3byva3t, vovl3ch3nnyj vo vsyo 1 vo vsya, pon1ma3sh', vot 1 vsyo, v 3tom nasha razn1ca. Tak chto ya 1du lyubovat'sya m1rozdan13m, a ty 1dyosh' pr31spolnyat'sya v GRANYAH kak1h-to, vot 1 vsya razn1ca, pon1ma3sh', ty ne zr1sh' 3to v3chno3 b3skon3chno3, ono t3b3 n3 nuzhno. Nu zato ty, tak skazat', bol33 akt1v3n, kak vot 3tot dyat3l dolbyashch1j, 1l1 murav3j, kotoryj och3n' akt1v3n v svo3j st3z3, po3tomu davaj, nash1 put1 zdes', kon3chno, 1m3yut gran1 podob1ya, potomu chto vsyo 3d1no, no ya-to t3bya pr3krasno pon1mayu, a vot ty m3nya - vryad li, potomu chto ya kak by t3bya v s3b3 sod3rzhu, vsyu tvoyu pr1rodu, ona sostavlya3t odnu mal3n'kuyu tam p3sch1nochku, ot togo chto 3st' vo mn3, vot 1 vsyo, po3tomu davaj, stupaj, 3zzhaj, a ya posh3l naslazhdat'sya pr3krasnym os3nn1m zakatom na b3r3gu t3ploj yuzhnoj r3k1. Vsyo, stupaj, 1 ya pojdu. Kstat1, flag surctf_durdunch1k_ph1losophy_1s_ab0ut_you_not_h1m"
part_size = len(text) // parts_n + 1
parts_n = len(text) // part_size + 1

parts = [text[i * part_size: (i + 1) * part_size] for i in range(0, parts_n)]
for i, part in enumerate(parts):
    img = qrcode.make(part, box_size=1).convert('L')
    img = np.array(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            print("▩▩" if img[i][j] == 255 else "  ", end="")
        print()

    decoded = input("Decoded: ")
    if (decoded != part):
        print("BYE, LOSER!!!111!")
        sys.exit()