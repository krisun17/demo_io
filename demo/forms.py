from django.forms import *

class MainForm(Form):
    choices=(
            (4, '---'),
            (11, '5.5'),
            (10, '5'),
            (9, '4.5'),
            (8, '4'),
            (7, '3.5'),
            (6, '3'),
            (5, '2'),
        )

    PMAT = ChoiceField(required=False, choices=choices)
    AM1 = ChoiceField(required=False, choices=choices)
    GAL = ChoiceField(required=False, choices=choices)
    WPI = ChoiceField(required=False, choices=choices)
    AM2 = ChoiceField(required=False, choices=choices)
    MD = ChoiceField(required=False, choices=choices)
    IPP = ChoiceField(required=False, choices=choices)
    PO = ChoiceField(required=False, choices=choices)
    AKS = ChoiceField(required=False, choices=choices)
    JNP1 = ChoiceField(required=False, choices=choices)
    ASD = ChoiceField(required=False, choices=choices)
    RPiS = ChoiceField(required=False, choices=choices)
    BD = ChoiceField(required=False, choices=choices)
    SO = ChoiceField(required=False, choices=choices)
    SIK = ChoiceField(required=False, choices=choices)
    JAO = ChoiceField(required=False, choices=choices)
    WWW = ChoiceField(required=False, choices=choices)
    IO = ChoiceField(required=False, choices=choices)
    JNP2 = ChoiceField(required=False, choices=choices)


    def __init__(self, *args, **kwargs):
        super(MainForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control'