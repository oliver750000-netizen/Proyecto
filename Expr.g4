grammar Expr;

root: expr EOF ;

expr: NUM | IDF ;


SUDO: 'sudo';
TCPDUMP: 'tcpdump';
CURL: 'curl';
DIG: 'dig';
GREP: 'grep';
UFW: 'ufw';
NMAP: 'nmap';
SS: 'ss';
JOURNALCTL: 'journalctl';
OPCION_SV: '-sV';
OPCION_SN: '-sn';
OPCION_TULN: '-tuln';
OPCION_I: '-I';
OPCION_CORTA: '-' [a-zA-Z];
OPCION_LARGA: '--' [a-zA-Z]+;
NUM: [0-9]+;
IDF: [a-zA-Z_][a-zA-Z0-9_]*;
IP: [0-9]{1,3} '.' [0-9]{1,3} '.' [0-9]{1,3} '.' [0-9]{1,3};
CIDR: [0-9]{1,3} '.' [0-9]{1,3} '.' [0-9]{1,3} '.' [0-9]{1,3} '/' [0-9]{1,2};
RUTA: '/' [a-zA-Z0-9_/.]+;
PUNTO: '.';
IGUAL: '=';
WS: [ \t\r\n]+ -> skip;