# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_resourcebase_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcebase',
            name='language',
            field=models.CharField(default='eng', help_text='language used within the dataset', max_length=3, verbose_name='language', choices=[('abk','Abkhazian'), ('aar','Afar'), ('afr','Afrikaans'), ('amh','Amharic'), ('ara','Arabic'), ('asm','Assamese'), ('aym','Aymara'), ('aze','Azerbaijani'), ('bak','Bashkir'), ('ben','Bengali'), ('bih','Bihari'), ('bis','Bislama'), ('bre','Breton'), ('bul','Bulgarian'), ('bel','Byelorussian'), ('cat','Catalan'), ('cos','Corsican'), ('dan','Danish'), ('dzo','Dzongkha'), ('eng','English'), ('fra','French'), ('epo','Esperanto'), ('est','Estonian'), ('fao','Faroese'), ('fij','Fijian'), ('fin','Finnish'), ('fry','Frisian'), ('glg','Gallegan'), ('ger','German'), ('gre','Greek'), ('kal','Greenlandic'), ('grn','Guarani'), ('guj','Gujarati'), ('hau','Hausa'), ('heb','Hebrew'), ('hin','Hindi'), ('hun','Hungarian'), ('ind','Indonesian'), ('ina','Interlingua (International Auxiliary language Association)'), ('iku','Inuktitut'), ('ipk','Inupiak'), ('ita','Italian'), ('jpn','Japanese'), ('kan','Kannada'), ('kas','Kashmiri'), ('kaz','Kazakh'), ('khm','Khmer'), ('kin','Kinyarwanda'), ('kir','Kirghiz'), ('kor','Korean'), ('kur','Kurdish'), ('oci', b"Langue d 'Oc (post 1500)"), ('lao','Lao'), ('lat','Latin'), ('lav','Latvian'), ('lin','Lingala'), ('lit','Lithuanian'), ('mlg','Malagasy'), ('mlt','Maltese'), ('mar','Marathi'), ('mol','Moldavian'), ('mon','Mongolian'), ('nau','Nauru'), ('nep','Nepali'), ('nor','Norwegian'), ('ori','Oriya'), ('orm','Oromo'), ('pan','Panjabi'), ('pol','Polish'), ('por','Portuguese'), ('pus','Pushto'), ('que','Quechua'), ('roh','Rhaeto-Romance'), ('run','Rundi'), ('rus','Russian'), ('smo','Samoan'), ('sag','Sango'), ('san','Sanskrit'), ('scr','Serbo-Croatian'), ('sna','Shona'), ('snd','Sindhi'), ('sin','Singhalese'), ('ssw','Siswant'), ('slv','Slovenian'), ('som','Somali'), ('sot','Sotho'), ('spa','Spanish'), ('sun','Sudanese'), ('swa','Swahili'), ('tgl','Tagalog'), ('tgk','Tajik'), ('tam','Tamil'), ('tat','Tatar'), ('tel','Telugu'), ('tha','Thai'), ('tir','Tigrinya'), ('tog','Tonga (Nyasa)'), ('tso','Tsonga'), ('tsn','Tswana'), ('tur','Turkish'), ('tuk','Turkmen'), ('twi','Twi'), ('uig','Uighur'), ('ukr','Ukrainian'), ('urd','Urdu'), ('uzb','Uzbek'), ('vie','Vietnamese'), ('vol','Volap\xc3\xbck'), ('wol','Wolof'), ('xho','Xhosa'), ('yid','Yiddish'), ('yor','Yoruba'), ('zha','Zhuang'), ('zul','Zulu')]),
        ),
    ]
