
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
    _______________________________________________________________________________
    Hallo Schließfachbesitzer*in,

    es ist wieder Zeit für die jährliche Schließfachverlängerung. 
    Bitte sende mir dazu deine Studienbescheinigung (kurz) zu.
    Da wir im Herbst letzten Jahres auf digitale Verträge umgestellt haben, möchte ich dich bitten, den beiliegenden Vertrag auszufüllen und mit deiner Unterschrift in der dickgedruckten Unterschriftenzeile an mich zurückzusenden (Anleitung siehe unten).

    Wenn du deinen Schließfachschlüssel zurückgeben möchtest oder die Erstellung des digitalen Vertrages lieber persönlich erledigen möchtest, kann ich dir folgende Termine in der nächsten Woche vorschlagen, bitte gib mir rechtzeitig Bescheid, wann genau.
    Mo, Di, Fr 13:00
    Mi, Do 12:30-13:00, 13:45-14:45

    Viele Grüße

    LUGGGI (Lukas Beck, Schließfachbeauftragter)

    _______________________________________________________________________________

    Hello locker owner,

    It's time again for the annual locker renewal. 
    Please send me your Certificate of enrolment (short version).
    Since we switched to digital contracts last autumn, I would like you to fill out the enclosed contract and return it to me with your signature on the thick signature line (see below for instructions).

    If you would like to return your locker key and complete the digital contract in person, I can suggest the following dates in the next week, please let me know the exact time.
    Mon, Tue, Fri 13:00
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
        es ist wieder Zeit für die jährliche Schließfachverlängerung. <br>
        Bitte sende mir dazu deine Studienbescheinigung (kurz) zu.<br>
        Da wir im Herbst letzten Jahres auf digitale Verträge umgestellt haben, möchte ich dich bitten, den beiliegenden Vertrag auszufüllen und mit deiner Unterschrift in der dickgedruckten Unterschriftenzeile an mich zurückzusenden (Anleitung siehe unten).<br>
        <br>
        Wenn du deinen Schließfachschlüssel zurückgeben möchtest oder die Erstellung des digitalen Vertrages lieber persönlich erledigen möchtest, kann ich dir folgende Termine in der nächsten Woche vorschlagen, bitte gib mir rechtzeitig Bescheid, wann genau.<br>
        <ul>
        <li>Mo, Di, Fr 13:00</li>
        <li>Mi, Do 12:30-13:00, 13:45-14:45</li>
        </ul>
        <br>
        Viele Grüße<br>
        <br>
        LUGGGI (Lukas Beck, Schließfachbeauftragter)<br>

        <hr>

        Hello locker owner,<br>
        <br>
        It's time again for the annual locker renewal. <br>
        Please send me your Certificate of enrolment (short version).<br>
        Since we switched to digital contracts last autumn, I would like you to fill out the enclosed contract and return it to me with your signature on the thick signature line (see below for instructions).<br>

        If you would like to return your locker key or complete the digital contract in person, I can suggest the following dates in the next week, please let me know the exact time.<br>
        <ul>
        <li>Mon, Tue, Fri 13:00</li>
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