
class Message:
    '''Holds a plain text and a html version of an eMail'''
    def __init__(self, plain_text: str, html: str) -> None:
        '''Create a Messsage object with a plain text and a html version of an eMail.
        
        :plain_text: String of a plain text version
        :html: String of a html formatted version
        '''
        self.plain_text = plain_text
        self.html = html

new_contract = Message(
    """\
    For English see below!
    _______________________________________________________________________________

    Hallo,
    hier ist dein Vertrag für das Schließfach.
    Die Nutzungsbedingungen findest du unter https://fs-ei.de/de/services/lockers_guidelines/ .
    Wenn du Fragen hast oder etwas kaputt ist, melde dich gerne (schliessfach@fs-ei.de).

    Gruß

    LUGGGI (Lukas Beck)

    _______________________________________________________________________________

    Hello,
    Here is your contract for the locker.
    You can find the terms of use at https://fs-ei.de/de/services/lockers_guidelines/ .
    If you have any questions or if something is broken, please contact us (schliessfach@fs-ei.de).

    

    LUGGGI (Lukas Beck)
    """,

    """\
    <html>
        <p>For English see below!<br>
        <br>
        Hallo,<br>
        hier ist dein Vertrag für das Schließfach.<br>
        Die Nutzungsbedingungen findest du unter <a href="https://fs-ei.de/de/services/lockers_guidelines/">Nutzerbedingungen</a>. <br>
        Wenn du Fragen hast oder etwas kaputt ist, melde dich gerne (<a href = "mailto: schliessfach@fs-ei.de">schliessfach@fs-ei.de</a>).<br>
        <br>
        Gruß<br>
        <br>
        LUGGGI (Lukas Beck)<br>
        <hr>

        <br>
        Hello,<br>
        Here is your contract for the locker.<br>
        You can find the terms of use at <a href="https://fs-ei.de/de/services/lockers_guidelines/">Nutzerbedingungen</a>. <br>
        If you have any questions or if something is broken, please contact us (<a href = "mailto: schliessfach@fs-ei.de">schliessfach@fs-ei.de</a>).<br>
        <br>
        Greetings<br>
        <br>
        LUGGGI (Lukas Beck)
        </p>
    </html>
    """
)

check_with_new_contract = Message(
    '''For English see below!
    
    Hallo Schließfachbesitzer*in,

    es ist wieder Zeit für die jährliche Schließfachverlängerung. Bitte sende mir dazu deine Studienbescheinigung (kurz) zu.

    Da wir im Herbst letzten Jahres auf digitale Verträge umgestellt haben, möchte ich dich bitten, den beiliegenden Vertrag auszufüllen und mit deiner Unterschrift in der dickgedruckten Unterschriftenzeile an mich zurückzusenden (Anleitung siehe unten). Der Anhang und eine Version, auf der digitale Signaturen möglich sind, finden sich auch noch einmal hier: https://1drv.ms/f/s!Ak_DBIEupa3pwAQqOs7n1Qp0obPm?e=7lu7gO .

    Deine Schließfachnummer: {number}
    Dein Vertrags Name: {name}


    Wenn du deinen Schließfachschlüssel zurückgeben möchtest oder die Erstellung des digitalen Vertrages lieber persönlich erledigen möchtest, kann ich dir folgende Termine in dieser Woche (17.-21.) vorschlagen, bitte gib mir rechtzeitig Bescheid, wann genau.
    Mo 14:00
    Di, Fr 13:00
    Mi, Do 12:30-13:00, 13:45-14:45

    Viele Grüße

    LUGGGI (Lukas Beck, Schließfachbeauftragter)

    _______________________________________________________________________________

    Hello locker owner,

    It's time again for the annual locker renewal. Please send me your Certificate of enrolment (short version).

    Since we switched to digital contracts last autumn, I would like you to fill out the attached contract and return it to me with your signature on the thick signature line (see below for instructions). The attachment and a version on which digital signatures are possible can also be found here: https://1drv.ms/f/s!Ak_DBIEupa3pwAQqOs7n1Qp0obPm?e=7lu7gO .

    Your locker number: {number}
    Your contract name: {name}

    If you would like to return your locker key and complete the digital contract in person, I can suggest the following dates this week(17.-21.), please let me know the exact time.
    Mon 14:00 
    Tue, Fri 13:00
    Wed, Thu 12:30-13:00, 13:45-14:45

    Greetings

    LUGGGI (Lukas Beck, Locker Manager)



    Anleitung zum Signieren von PDF-Dateien

    - Adobe Acrobat Reader: https://helpx.adobe.com/de/reader/using/sign-pdfs.html
    - Pdf XChange: entweder mit dem Stifttool direkt mit Maus oder Stift unterschreiben oder ein Bild der Unterschrift einfügen
    - Browser wie Edge, Firefox (evtl. Chrome): Stiftwerkzeug auswählen und mit Maus oder digitalem  Stift unterschreiben


    Instructions for signing PDF files

    - Adobe Acrobat Reader: https://helpx.adobe.com/reader/using/sign-pdfs.html
    - Pdf XChange: either sign directly with the mouse or digital pen using the pen tool or insert a picture of the signature.
    - Browser such as Edge, Firefox (possibly Chrome): Select pen tool and sign with mouse or digital pen
    ''',

    '''\
    <html>
        <p>For English see below!<br>
        <br>
        Hallo Schließfachbesitzer*in,<br>
        <br>
        es ist wieder Zeit für die jährliche Schließfachverlängerung. Bitte sende mir dazu deine Studienbescheinigung (kurz) zu.<br>
        <br>
        Da wir im Herbst letzten Jahres auf digitale Verträge umgestellt haben, möchte ich dich bitten, den beiliegenden Vertrag auszufüllen und mit deiner Unterschrift in der dickgedruckten Unterschriftenzeile an mich zurückzusenden (Anleitung siehe unten). Den Anhang und eine Version auf dem Digitale Signaturen möglich sind findest du auch nochmal hier: https://1drv.ms/f/s!Ak_DBIEupa3pwAQqOs7n1Qp0obPm?e=7lu7gO .<br>
        <br>
        Deine Schließfachnummer: {number}<br>
        Dein Vertrags Name: {name}<br>
        <br>
        Wenn du deinen Schließfachschlüssel zurückgeben möchtest oder die Erstellung des digitalen Vertrages lieber persönlich erledigen möchtest, kann ich dir folgende Termine in dieser Woche (17.-21.) vorschlagen, bitte gib mir rechtzeitig Bescheid, wann genau.<br>
        <ul>
        <li>Mo 14:00</li>
        <li>Di, Fr 13:00</li>
        <li>Mi, Do 12:30-13:00, 13:45-14:45</li>
        </ul>
        <br>
        Viele Grüße<br>
        <br>
        LUGGGI (Lukas Beck, Schließfachbeauftragter)<br>
        <br>
        <hr>

        Hello locker owner,<br>
        <br>
        It's time again for the annual locker renewal. Please send me your Certificate of enrolment (short version).<br>
        <br>
        Since we switched to digital contracts last autumn, I would like you to fill out the attached contract and return it to me with your signature on the thick signature line (see below for instructions). The attachment and a version on which digital signatures are possible can also be found here: https://1drv.ms/f/s!Ak_DBIEupa3pwAQqOs7n1Qp0obPm?e=7lu7gO .<br>
        <br>
        Your locker number: {number}<br>
        Your contract name: {name}<br>
        <br>
        If you would like to return your locker key or complete the digital contract in person, I can suggest the following dates this week(17.-21.), please let me know the exact time.<br>
        <ul>
        <li>Mon 14:00</li>
        <li>Tue, Fri 13:00</li>
        <li>Wed, Thu 12:30-13:00, 13:45-14:45</li>
        </ul>
        <br>
        Greetings<br>
        <br>
        LUGGGI (Lukas Beck, Locker Manager)<br>
        <br>
        <br>
        <hr>

        Anleitung zum Signieren von PDF-Dateien<br>

        <ul>
        <li>Adobe Acrobat Reader: https://helpx.adobe.com/de/reader/using/sign-pdfs.html</li>
        <li>Pdf XChange: entweder mit dem Stifttool direkt mit Maus oder Stift unterschreiben oder ein Bild der Unterschrift einfügen</li>
        <li>Browser wie Edge, Firefox (evtl. Chrome): Stiftwerkzeug auswählen und mit Maus oder digitalem  Stift unterschreiben</li>
        </ul>
        <br>
        Instructions for signing PDF files<br>
        <ul>           
        <li>Adobe Acrobat Reader: https://helpx.adobe.com/reader/using/sign-pdfs.html</li>
        <li>Pdf XChange: either sign directly with the mouse or digital pen using the pen tool or insert a picture of the signature.</li>
        <li>Browser such as Edge, Firefox (possibly Chrome): Select pen tool and sign with mouse or digital pen</li>
        </ul>
    </html>
    '''
)


check_with_new_contract_25 = Message(
    '''For English see below!
    
    Hallo Schließfachbesitzer*in,

    es ist wieder Zeit für die jährliche Schließfachverlängerung. Bitte sende mir dazu deine Studienbescheinigung (kurz) zu.

    In diesem Jahr wurde beschlossen, alle Verträge mit dem derzeitigen Pfand in Höhe von 50 € neu anzulegen. Du hast damals nur 25€ bezahlt, das muss jetzt auf 50€ erhöht werden. Der Einfachheit halber kannst du mir die Differenz von 25€ auf folgendes Konto überweisen:
    Lukas Beck
    Volksbank Mittlerer Neckar eG
    IBAN: DE82 6129 0120 0415 5220 05
    Verwendungszweck: {Schließfachnummer}, {Name}

    Da wir im Herbst letzten Jahres auf digitale Verträge umgestellt haben, möchte ich dich bitten, den beiliegenden Vertrag auszufüllen und mit deiner Unterschrift in der dickgedruckten Unterschriftenzeile an mich zurückzusenden (Anleitung siehe unten). Der Anhang und eine Version, auf der digitale Signaturen möglich sind, finden sich auch noch einmal hier: https://1drv.ms/f/s!Ak_DBIEupa3pwAQqOs7n1Qp0obPm?e=7lu7gO .

    Deine Schließfachnummer: {number}
    Dein Vertrags Name: {name}


    Wenn du deinen Schließfachschlüssel zurückgeben möchtest oder die Erstellung des digitalen Vertrages lieber persönlich erledigen möchtest, kann ich dir folgende Termine in dieser Woche (17.-21.) vorschlagen, bitte gib mir rechtzeitig Bescheid, wann genau.
    Mo 14:00
    Di, Fr 13:00
    Mi, Do 12:30-13:00, 13:45-14:45

    Viele Grüße

    LUGGGI (Lukas Beck, Schließfachbeauftragter)

    _______________________________________________________________________________

    Hello locker owner,

    It's time again for the annual locker renewal. Please send me your Certificate of enrolment (short version).

    This year it was decided to reinstate all contracts with the current deposit of €50. You only paid 25€ at that time, this now has to be increased to 50€. For the sake of simplicity, you can transfer the difference of 25€ to the following account:
    Lukas Beck
    Volksbank Mittlerer Neckar eG
    IBAN: DE82 6129 0120 0415 5220 05
    Reference: {locker number}, {name}

    Since we switched to digital contracts last autumn, I would like you to fill out the attached contract and return it to me with your signature on the thick signature line (see below for instructions). The attachment and a version on which digital signatures are possible can also be found here: https://1drv.ms/f/s!Ak_DBIEupa3pwAQqOs7n1Qp0obPm?e=7lu7gO .

    Your locker number: {number}
    Your contract name: {name}

    If you would like to return your locker key and complete the digital contract in person, I can suggest the following dates this week(17.-21.), please let me know the exact time.
    Mon 14:00 
    Tue, Fri 13:00
    Wed, Thu 12:30-13:00, 13:45-14:45

    Greetings

    LUGGGI (Lukas Beck, Locker Manager)



    Anleitung zum Signieren von PDF-Dateien

    - Adobe Acrobat Reader: https://helpx.adobe.com/de/reader/using/sign-pdfs.html
    - Pdf XChange: entweder mit dem Stifttool direkt mit Maus oder Stift unterschreiben oder ein Bild der Unterschrift einfügen
    - Browser wie Edge, Firefox (evtl. Chrome): Stiftwerkzeug auswählen und mit Maus oder digitalem  Stift unterschreiben


    Instructions for signing PDF files

    - Adobe Acrobat Reader: https://helpx.adobe.com/reader/using/sign-pdfs.html
    - Pdf XChange: either sign directly with the mouse or digital pen using the pen tool or insert a picture of the signature.
    - Browser such as Edge, Firefox (possibly Chrome): Select pen tool and sign with mouse or digital pen
    ''',

    '''\
    <html>
        <p>For English see below!<br>
        <br>
        Hallo Schließfachbesitzer*in,<br>
        <br>
        es ist wieder Zeit für die jährliche Schließfachverlängerung. Bitte sende mir dazu deine Studienbescheinigung (kurz) zu.<br>
        <br>
        In diesem Jahr wurde beschlossen, alle Verträge mit dem derzeitigen Pfand in Höhe von 50 € neu anzulegen. Du hast damals nur 25€ bezahlt, das muss jetzt auf 50€ erhöht werden. Der Einfachheit halber kannst du mir die Differenz von 25€ auf folgendes Konto überweisen:<br>
        Lukas Beck<br>
        Volksbank Mittlerer Neckar eG<br>
        IBAN: DE82 6129 0120 0415 5220 05<br>
        Verwendungszweck: {Schließfachnummer}, {Name}<br>
        <br>
        Da wir im Herbst letzten Jahres auf digitale Verträge umgestellt haben, möchte ich dich bitten, den beiliegenden Vertrag auszufüllen und mit deiner Unterschrift in der dickgedruckten Unterschriftenzeile an mich zurückzusenden (Anleitung siehe unten). Den Anhang und eine Version auf dem Digitale Signaturen möglich sind findest du auch nochmal hier: https://1drv.ms/f/s!Ak_DBIEupa3pwAQqOs7n1Qp0obPm?e=7lu7gO .<br>
        <br>
        Deine Schließfachnummer: {number}<br>
        Dein Vertrags Name: {name}<br>
        <br>
        Wenn du deinen Schließfachschlüssel zurückgeben möchtest oder die Erstellung des digitalen Vertrages lieber persönlich erledigen möchtest, kann ich dir folgende Termine in dieser Woche (17.-21.) vorschlagen, bitte gib mir rechtzeitig Bescheid, wann genau.<br>
        <ul>
        <li>Mo 14:00</li>
        <li>Di, Fr 13:00</li>
        <li>Mi, Do 12:30-13:00, 13:45-14:45</li>
        </ul>
        <br>
        Viele Grüße<br>
        <br>
        LUGGGI (Lukas Beck, Schließfachbeauftragter)<br>
        <br>
        <hr>

        Hello locker owner,<br>
        <br>
        It's time again for the annual locker renewal. Please send me your Certificate of enrolment (short version).<br>
        <br>
        This year it was decided to reinstate all contracts with the current deposit of €50. You only paid 25€ at that time, this now has to be increased to 50€. For the sake of simplicity, you can transfer the difference of 25€ to the following account:<br>
        Lukas Beck<br>
        Volksbank Mittlerer Neckar eG<br>
        IBAN: DE82 6129 0120 0415 5220 05<br>
        Reference: {locker number}, {name}<br>
        <br>
        Since we switched to digital contracts last autumn, I would like you to fill out the attached contract and return it to me with your signature on the thick signature line (see below for instructions). The attachment and a version on which digital signatures are possible can also be found here: https://1drv.ms/f/s!Ak_DBIEupa3pwAQqOs7n1Qp0obPm?e=7lu7gO .<br>
        <br>
        Your locker number: {number}<br>
        Your contract name: {name}<br>
        <br>
        If you would like to return your locker key or complete the digital contract in person, I can suggest the following dates this week(17.-21.), please let me know the exact time.<br>
        <ul>
        <li>Mon 14:00</li>
        <li>Tue, Fri 13:00</li>
        <li>Wed, Thu 12:30-13:00, 13:45-14:45</li>
        </ul>
        <br>
        Greetings<br>
        <br>
        LUGGGI (Lukas Beck, Locker Manager)<br>
        <br>
        <br>
        <hr>

        Anleitung zum Signieren von PDF-Dateien<br>

        <ul>
        <li>Adobe Acrobat Reader: https://helpx.adobe.com/de/reader/using/sign-pdfs.html</li>
        <li>Pdf XChange: entweder mit dem Stifttool direkt mit Maus oder Stift unterschreiben oder ein Bild der Unterschrift einfügen</li>
        <li>Browser wie Edge, Firefox (evtl. Chrome): Stiftwerkzeug auswählen und mit Maus oder digitalem  Stift unterschreiben</li>
        </ul>
        <br>
        Instructions for signing PDF files<br>
        <ul>           
        <li>Adobe Acrobat Reader: https://helpx.adobe.com/reader/using/sign-pdfs.html</li>
        <li>Pdf XChange: either sign directly with the mouse or digital pen using the pen tool or insert a picture of the signature.</li>
        <li>Browser such as Edge, Firefox (possibly Chrome): Select pen tool and sign with mouse or digital pen</li>
        </ul>
    </html>
    '''
)

check_with_new_contract_fs_25 = Message(
    '''For English see below!
    
    Hallo Schließfachbesitzer*in,

    In diesem Jahr wurde beschlossen, alle Verträge mit dem derzeitigen Pfand in Höhe von 50 € neu anzulegen. Du hast damals nur 25€ bezahlt, das muss jetzt auf 50€ erhöht werden. Der Einfachheit halber kannst du mir die Differenz von 25€ auf folgendes Konto überweisen dann pack ich das in die Kasse:
    Lukas Beck
    Volksbank Mittlerer Neckar eG
    IBAN: DE82 6129 0120 0415 5220 05
    Verwendungszweck: {Schließfachnummer}, {Name}

    Paypal geht auch: https://www.paypal.me/LUGGGI/

    Da wir im Herbst letzten Jahres auf digitale Verträge umgestellt haben, möchte ich dich bitten, den beiliegenden Vertrag auszufüllen und mit deiner Unterschrift in der dickgedruckten Unterschriftenzeile an mich zurückzusenden (Anleitung siehe unten). Der Anhang und eine Version, auf der digitale Signaturen möglich sind, finden sich auch noch einmal hier: https://1drv.ms/f/s!Ak_DBIEupa3pwAQqOs7n1Qp0obPm?e=7lu7gO .

    Deine Schließfachnummer: {number}
    Dein Vertrags Name: {name}


    Wenn du deinen Schließfachschlüssel zurückgeben möchtest oder die Erstellung des digitalen Vertrages lieber persönlich erledigen möchtest, kann ich dir folgende Termine in dieser Woche (17.-21.) vorschlagen, bitte gib mir rechtzeitig Bescheid, wann genau. (Telegram 0176 82750111)
    Di, Fr 13:00
    Mi, Do 12:30-13:00, 13:45-14:45

    Die nächsten Wochen bin ich sonst auch meist zur Mittagszeit an der Uni.

    Gruß

    LUGGGI (Lukas Beck, Schließfachbeauftragter)

    _______________________________________________________________________________

    Anleitung zum Signieren von PDF-Dateien

    - Adobe Acrobat Reader: https://helpx.adobe.com/de/reader/using/sign-pdfs.html
    - Pdf XChange: entweder mit dem Stifttool direkt mit Maus oder Stift unterschreiben oder ein Bild der Unterschrift einfügen
    - Browser wie Edge, Firefox (evtl. Chrome): Stiftwerkzeug auswählen und mit Maus oder digitalem  Stift unterschreiben
    ''',

    '''\
    <html>
        <p>Hallo Schließfachbesitzer*in,<br>
        <br>
        In diesem Jahr wurde beschlossen, alle Verträge mit dem derzeitigen Pfand in Höhe von 50 € neu anzulegen. Du hast damals nur 25€ bezahlt, das muss jetzt auf 50€ erhöht werden. Der Einfachheit halber kannst du mir die Differenz von 25€ auf folgendes Konto überweisen dann pack ich das in die Kasse:<br>
        Lukas Beck<br>
        Volksbank Mittlerer Neckar eG<br>
        IBAN: DE82 6129 0120 0415 5220 05<br>
        Verwendungszweck: {Schließfachnummer}, {Name}<br>
        <br>
        Paypal geht auch: https://www.paypal.me/LUGGGI/<br>
        <br>
        Da wir im Herbst letzten Jahres auf digitale Verträge umgestellt haben, möchte ich dich bitten, den beiliegenden Vertrag auszufüllen und mit deiner Unterschrift in der dickgedruckten Unterschriftenzeile an mich zurückzusenden (Anleitung siehe unten). Den Anhang und eine Version auf dem Digitale Signaturen möglich sind findest du auch nochmal hier: https://1drv.ms/f/s!Ak_DBIEupa3pwAQqOs7n1Qp0obPm?e=7lu7gO .<br>
        <br>
        Deine Schließfachnummer: {number}<br>
        Dein Vertrags Name: {name}<br>
        <br>
        Wenn du deinen Schließfachschlüssel zurückgeben möchtest oder die Erstellung des digitalen Vertrages lieber persönlich erledigen möchtest, kann ich dir folgende Termine in dieser Woche (17.-21.) vorschlagen, bitte gib mir rechtzeitig Bescheid, wann genau. (Telegram 0176 82750111)<br>
        <ul>
        <li>Di, Fr 13:00</li>
        <li>Mi, Do 12:30-13:00, 13:45-14:45</li>
        </ul>
        <br>
        Die nächsten Wochen bin ich sonst auch meist zur Mittagszeit an der Uni.
        <br>
        Gruß<br>
        <br>
        LUGGGI (Lukas Beck, Schließfachbeauftragter)<br>
        <br>
        <hr>

        Anleitung zum Signieren von PDF-Dateien<br>

        <ul>
        <li>Adobe Acrobat Reader: https://helpx.adobe.com/de/reader/using/sign-pdfs.html</li>
        <li>Pdf XChange: entweder mit dem Stifttool direkt mit Maus oder Stift unterschreiben oder ein Bild der Unterschrift einfügen</li>
        <li>Browser wie Edge, Firefox (evtl. Chrome): Stiftwerkzeug auswählen und mit Maus oder digitalem  Stift unterschreiben</li>
        </ul>
    </html>
    '''
)
check_with_new_contract_fs = Message(
    '''For English see below!
    
    Hallo Schließfachbesitzer*in,

    Da wir im Herbst letzten Jahres auf digitale Verträge umgestellt haben, möchte ich dich bitten, den beiliegenden Vertrag auszufüllen und mit deiner Unterschrift in der dickgedruckten Unterschriftenzeile an mich zurückzusenden (Anleitung siehe unten). Der Anhang und eine Version, auf der digitale Signaturen möglich sind, finden sich auch noch einmal hier: https://1drv.ms/f/s!Ak_DBIEupa3pwAQqOs7n1Qp0obPm?e=7lu7gO .

    Deine Schließfachnummer: {number}
    Dein Vertrags Name: {name}


    Wenn du deinen Schließfachschlüssel zurückgeben möchtest oder die Erstellung des digitalen Vertrages lieber persönlich erledigen möchtest, kann ich dir folgende Termine in dieser Woche (17.-21.) vorschlagen, bitte gib mir rechtzeitig Bescheid, wann genau. (Telegram 0176 82750111)
    Di, Fr 13:00
    Mi, Do 12:30-13:00, 13:45-14:45

    Die nächsten Wochen bin ich sonst auch meist zur Mittagszeit an der Uni.

    Gruß

    LUGGGI (Lukas Beck, Schließfachbeauftragter)

    _______________________________________________________________________________

    Anleitung zum Signieren von PDF-Dateien

    - Adobe Acrobat Reader: https://helpx.adobe.com/de/reader/using/sign-pdfs.html
    - Pdf XChange: entweder mit dem Stifttool direkt mit Maus oder Stift unterschreiben oder ein Bild der Unterschrift einfügen
    - Browser wie Edge, Firefox (evtl. Chrome): Stiftwerkzeug auswählen und mit Maus oder digitalem  Stift unterschreiben
    ''',

    '''\
    <html>
        <p>Hallo Schließfachbesitzer*in,<br>
        <br>
        Da wir im Herbst letzten Jahres auf digitale Verträge umgestellt haben, möchte ich dich bitten, den beiliegenden Vertrag auszufüllen und mit deiner Unterschrift in der dickgedruckten Unterschriftenzeile an mich zurückzusenden (Anleitung siehe unten). Den Anhang und eine Version auf dem Digitale Signaturen möglich sind findest du auch nochmal hier: https://1drv.ms/f/s!Ak_DBIEupa3pwAQqOs7n1Qp0obPm?e=7lu7gO .<br>
        <br>
        Deine Schließfachnummer: {number}<br>
        Dein Vertrags Name: {name}<br>
        <br>
        Wenn du deinen Schließfachschlüssel zurückgeben möchtest oder die Erstellung des digitalen Vertrages lieber persönlich erledigen möchtest, kann ich dir folgende Termine in dieser Woche (17.-21.) vorschlagen, bitte gib mir rechtzeitig Bescheid, wann genau. (Telegram 0176 82750111)<br>
        <ul>
        <li>Di, Fr 13:00</li>
        <li>Mi, Do 12:30-13:00, 13:45-14:45</li>
        </ul>
        <br>
        Die nächsten Wochen bin ich sonst auch meist zur Mittagszeit an der Uni.
        <br>
        Gruß<br>
        <br>
        LUGGGI (Lukas Beck, Schließfachbeauftragter)<br>
        <br>
        <hr>

        Anleitung zum Signieren von PDF-Dateien<br>

        <ul>
        <li>Adobe Acrobat Reader: https://helpx.adobe.com/de/reader/using/sign-pdfs.html</li>
        <li>Pdf XChange: entweder mit dem Stifttool direkt mit Maus oder Stift unterschreiben oder ein Bild der Unterschrift einfügen</li>
        <li>Browser wie Edge, Firefox (evtl. Chrome): Stiftwerkzeug auswählen und mit Maus oder digitalem  Stift unterschreiben</li>
        </ul>
    </html>
    '''
)