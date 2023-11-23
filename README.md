# DictionaryPrint
A python utility for printing out dictionary contents in an easily readable format.

Example:

    dict_print(<book data>)

Result:

    Books: 
       > Herbert, Frank:
                       > ___________ Dune:
                                         > Published: 1965
                                         > ___ Pages: 896
                                         > ___ Genre: Science Fiction
                                         > __ Series: Dune Series
                       > ___ Dune Messiah:
                                         > Published: 1969
                                         > ___ Pages: 256
                                         > ___ Genre: Science Fiction
                                         > __ Series: Dune Series
                       > Children of Dune:
                                         > Published: 1976
                                         > ___ Pages: 444
                                         > ___ Genre: Science Fiction
                                         > __ Series: Dune Series
       > Orwell, George:
                       > Animal Farm:
                                    > Published: 1945
                                    > ___ Pages: 92
                                    > ___ Genre: Political Satire
                       > ______ 1984:
                                    > Published: 1949
                                    > ___ Pages: 328
                                    > ___ Genre: Political Fiction

Example:

    dict_print(
        <random data>,
        num_format=".3e",
        pad_char="=",
        sort_kwargs={"reverse": True, "key": lambda x: len(x)}, # equivalent to the shortcut `sort_kwargs="revlen"`
    )

Result:

    GYQSAYHN: <__main__.dummy object at 0x000001D38CAA7200>
    KMYPCPWS: ()
    = EOFSCJ:
            > UBRSLUNON:
                       > NVQALIBK: 1.665e+01
                       > ==== TFW: ('0.000e+00', '1.000e+00', '2.000e+00', '3.000e+00', '4.000e+00', '5.000e+00')
                       > ====== C: 5.976e+01
                       > ====== G: ('0.000e+00',)
            > ==== TMTI: <__main__.dummy object at 0x000001D38CAA08C0>
            > ====== TD: 8.861e+01
            > ====== UQ:
                       > GGCUEU_PIL: ('0.000e+00', '1.000e+00', '2.000e+00', '3.000e+00', '4.000e+00')
                       >  BKIYZQKYR: ('0.000e+00', '1.000e+00', '2.000e+00')
                       > === ISDALJ: 3.281e+01
    === ECJJ: <__main__.dummy object at 0x000001D38CAA7050>
    ==== EOQ: ('0.000e+00', '1.000e+00', '2.000e+00', '3.000e+00')


# Config

    dict_print(
        data,                # The dictionary structure to be printed
        level_char=">",      # Indicates the key of the current dictionary
        offset_char=" ",     # Used for spacing between levels
        pad_char="_",        # Used for padding names/values
        rounding=None,       # Optional rounding for numbers, specified as an integer. Higher priority than num_format
        num_format=None,     # Standard python number formatting specified (Ex: ".3f")
        sort_kwargs=None,    # A dictionary with kwargs for the .sort function are passed unless "len" or "revlen" are specified, which sort by length
        compact=False,       # If enabled then the first value for a given key is printed on the same line as the key instead of the next line
        exclude=None,        # A list of any keys to NOT print (applies to all levels of nesting)
        _offset=0,           # Internal
        _first=False,        # Internal
    )

![image](https://github.com/nhansendev/DictionaryPrint/assets/9289200/df104966-7ecf-46f6-bf52-fca50ad08f05)

