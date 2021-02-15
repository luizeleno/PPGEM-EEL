BEGIN{
    FS = " - "
}
{
    print "-"
    print "  sigla: " $1;
    print "  nome_br: " "\"" $2 "\"";
    print "  nome_en: ";
    print "  nome_es: ";
}
