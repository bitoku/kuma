import pyautogui as pg

pg.PAUSE = 0.02
col = 192
col_diff = 84
row = 707
row_diff = 57

script = "yo---isuta-to!!" \
         "zo-nntilyarennzinohazimarida" \
         "akasatanahamayarawasokonootokonokonokokoro" \
         "sakanahasakana" \
         "nazekonnnakoto?" \
         "siterunoka?" \
         "soukanngaehazimeta" \
         "anataha" \
         "kiltutomou" \
         "zo-nnzilyoutai" \
         "kokomadede" \
         "sou" \
         "mou" \
         "daitaihilyakumozi" \
         "nakanakayaruna" \
         "gohoubino" \
         "bo-nasu" \
         "zo--------------" \
         "---------nn!!!!!!!!!" \
         "ketaxtamasiku" \
         "huriltukusuru" \
         "anatanote" \
         "ketaxtamasiku" \
         "zituhamogultuteru" \
         "ketaxtamasikuugokukuma" \
         "zilyuunenngono" \
         "hatigatumokiltuto" \
         "anataniaisareru" \
         "silyouhinnninaritaidesu" \
         "konnnatokomadekitilyaltutakimiha" \
         "matigainakuzo-nnzilyoutai" \
         "mosikasitarasilyoukinngeltutositilyaukamo!" \
         "amedetou" \
         "omedetou" \
         "omedetou!"
idx = 0

pg.click(361, 817)
pg.click(361, 817)
pg.sleep(3)


def c(n):
    return col + col_diff * (n - 1)


def r(n):
    return row + row_diff * (n - 1)


def m(x, y, vo):
    if vo == 'a':
        return None, None
    elif vo == 'i':
        return - col_diff, 0
    elif vo == 'u':
        return 0, - row_diff
    elif vo == 'e':
        return col_diff, 0
    elif vo == 'o':
        return 0, row_diff
    raise Exception


while len(script) > idx:
    char = script[idx]
    print(char, end='')

    xx, yy = None, None
    small = 0
    if char == 'x':
        x, y = c(5), r(2)
    elif char == '-':
        x, y = c(3), r(4)
        xx, yy = m(x, y, 'e')
    elif char == '!':
        x, y = c(4), r(4)
        xx, yy = m(x, y, 'e')
    elif char == '?':
        x, y = c(4), r(4)
        xx, yy = m(x, y, 'u')
    elif char in 'aiueo':
        x, y = c(2), r(1)
        if char != 'a':
            xx, yy = m(x, y, char)
    elif char in 'kg':
        x, y = c(3), r(1)
    elif char in 'sz':
        x, y = c(4), r(1)
    elif char in 'td':
        x, y = c(2), r(2)
    elif char == 'n':
        x, y = c(3), r(2)
        idx += 1
        char = script[idx]
        print(char, end='')
        if char == 'n':
            x, y = c(3), r(4)
            xx, yy = m(x, y, 'u')
        else:
            char = script[idx]
            print(char, end='')
            xx, yy = m(x, y, char)
    elif char in 'hbp':
        x, y = c(4), r(2)
    elif char == 'm':
        x, y = c(2), r(3)
    elif char == 'y':
        x, y = c(3), r(3)
    elif char == 'r':
        x, y = c(4), r(3)
    elif char == 'w':
        x, y = c(3), r(4)
    elif char == 'l':
        idx += 1
        char = script[idx]
        print(char, end='')
        if char == 't':
            x, y = c(2), r(2)
        else:
            x, y = c(3), r(3)
        idx += 1
        char = script[idx]
        print(char, end='')
        xx, yy = m(x, y, char)
        small = 1
    else:
        raise Exception
    if char in 'kgsztdhbpmyrw':
        if char in 'gzdb':
            small = 1
        elif char in 'p':
            small = 2
        idx += 1
        char = script[idx]
        print(char, end='')
        xx, yy = m(x, y, char)

    if xx is None:
        pg.click(x, y, button='left')
    else:
        pg.moveTo(x, y)
        pg.dragRel(xx, yy, button='left')

    if small > 0:
        pg.click(c(2), r(4), button='left')
    idx += 1

