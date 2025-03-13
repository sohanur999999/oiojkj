  0           0 RESUME                   0

  1           2 LOAD_CONST               0 (0)
              4 LOAD_CONST               1 (None)
              6 IMPORT_NAME              0 (os)
              8 STORE_NAME               0 (os)

  2          10 LOAD_CONST               0 (0)
             12 LOAD_CONST               1 (None)
             14 IMPORT_NAME              1 (sys)
             16 STORE_NAME               1 (sys)

  3          18 LOAD_CONST               0 (0)
             20 LOAD_CONST               1 (None)
             22 IMPORT_NAME              2 (time)
             24 STORE_NAME               2 (time)

  4          26 LOAD_CONST               0 (0)
             28 LOAD_CONST               1 (None)
             30 IMPORT_NAME              3 (marshal)
             32 STORE_NAME               3 (marshal)

  5          34 LOAD_CONST               0 (0)
             36 LOAD_CONST               1 (None)
             38 IMPORT_NAME              4 (random)
             40 STORE_NAME               4 (random)

  6          42 LOAD_CONST               0 (0)
             44 LOAD_CONST               1 (None)
             46 IMPORT_NAME              5 (zlib)
             48 STORE_NAME               5 (zlib)

  7          50 LOAD_CONST               0 (0)
             52 LOAD_CONST               1 (None)
             54 IMPORT_NAME              6 (base64)
             56 STORE_NAME               6 (base64)

  8          58 LOAD_CONST               0 (0)
             60 LOAD_CONST               1 (None)
             62 IMPORT_NAME              7 (compileall)
             64 STORE_NAME               7 (compileall)

  9          66 LOAD_CONST               0 (0)
             68 LOAD_CONST               1 (None)
             70 IMPORT_NAME              8 (shutil)
             72 STORE_NAME               8 (shutil)

 12          74 NOP

 13          76 PUSH_NULL
             78 LOAD_NAME                8 (shutil)
             80 LOAD_ATTR                9 (NULL|self + random)
            100 CACHE
            102 CACHE
            104 LOAD_ATTR               10 (zlib)
            124 STORE_NAME              11 (column1)

 15         126 LOAD_NAME               10 (columns)
            128 LOAD_CONST               3 (5)
            130 BINARY_OP                0 (+)
            134 STORE_NAME              12 (column2)

 16         136 LOAD_NAME               10 (columns)
            138 LOAD_CONST               4 (19)
            140 BINARY_OP                0 (+)
            144 STORE_NAME              13 (column3)
            146 JUMP_FORWARD            69 (to 286)
        >>  148 PUSH_EXC_INFO

 17         150 POP_TOP

 18         152 PUSH_NULL
            154 LOAD_NAME                0 (os)
            156 LOAD_ATTR               14 (compileall)
            176 CACHE
            178 CACHE
            180 CACHE
            182 CACHE
            184 STORE_SUBSCR
            188 CACHE
            190 CACHE
            192 CACHE
            194 CACHE
            196 CACHE
            198 CACHE
            200 CACHE
            202 CACHE
            204 CACHE
            206 UNPACK_SEQUENCE          0
            210 CALL                     0
            218 CACHE
            220 STORE_SUBSCR
            224 CACHE
            226 CACHE
            228 CACHE
            230 CACHE
            232 CACHE
            234 CACHE
            236 CACHE
            238 CACHE
            240 CACHE
            242 UNPACK_SEQUENCE          0
            246 CALL                     0
            254 CACHE
            256 UNPACK_SEQUENCE          2
            260 STORE_NAME              17 (rows)
            262 STORE_NAME              10 (columns)

 19         264 LOAD_CONST               0 (0)
            266 STORE_NAME              11 (column1)

 20         268 LOAD_CONST               0 (0)
            270 STORE_NAME              12 (column2)

 21         272 LOAD_CONST               0 (0)
            274 STORE_NAME              13 (column3)
            276 POP_EXCEPT
            278 JUMP_FORWARD             3 (to 286)
        >>  280 COPY                     3
            282 POP_EXCEPT
            284 RERAISE                  1

 24     >>  286 LOAD_CONST               7 (<code object logo at 0x7a94f04ab0, file "PawanJii", line 24>)
            288 MAKE_FUNCTION            0
            290 STORE_NAME              18 (logo)

 45         292 LOAD_CONST               8 (<code object logout at 0x7a94ec8030, file "PawanJii", line 45>)
            294 MAKE_FUNCTION            0
            296 STORE_NAME              19 (logout)

 52         298 LOAD_CONST               9 (<code object banner at 0xb400007b1555d880, file "PawanJii", line 52>)
            300 MAKE_FUNCTION            0
            302 STORE_NAME              20 (banner)

 63         304 LOAD_CONST              10 (<code object psb at 0x7a94ec8330, file "PawanJii", line 63>)
            306 MAKE_FUNCTION            0
            308 STORE_NAME              21 (psb)

 70         310 LOAD_CONST              11 (<code object verInput at 0x7a94d60a30, file "PawanJii", line 70>)
            312 MAKE_FUNCTION            0
            314 STORE_NAME              22 (verInput)

 79         316 LOAD_CONST              12 ('# Encoded By Pyconverter\n# A Product Of PawanJii\n# https://github.com/VIBE81\n\nimport marshal\nexec(marshal.loads(')
            318 STORE_NAME              23 (marshalHead)

 80         320 LOAD_CONST              13 ('))')
            322 STORE_NAME              24 (marshalTail)

 83         324 LOAD_CONST              14 ('# Encoded By Pyconverter\n# A Product Of PawanJii\n# https://github.com/VIBE81\n\nimport base64\nexec(base64.b64decode(')
            326 STORE_NAME              25 (b64Head)

 84         328 LOAD_CONST              13 ('))')
            330 STORE_NAME              26 (b64Tail)

 87         332 LOAD_CONST              15 ('# Encoded By Pyconverter\n# A Product Of PawanJii\n# https://github.com/VIBE81\n\nimport zlib\nexec(zlib.decompress(')
            334 STORE_NAME              27 (zlibHead)

 88         336 LOAD_CONST              13 ('))')
            338 STORE_NAME              28 (zlibTail)

 91         340 LOAD_CONST              16 ('# Encoded By Pyconverter\n# A Product Of PawanJii\n# https://github.com/VIBE81\n\nimport marshal, base64, zlib\nexec(marshal.loads(zlib.decompress(base64.b64decode(')
            342 STORE_NAME              29 (allHead)

 92         344 LOAD_CONST              17 ('))))')
            346 STORE_NAME              30 (allTail)

 95         348 LOAD_CONST              18 (<code object encodeMarshal at 0x7a94ec84b0, file "PawanJii", line 95>)
            350 MAKE_FUNCTION            0
            352 STORE_NAME              31 (encodeMarshal)

105         354 LOAD_CONST              19 (<code object encodeZlib at 0x7a94ec8630, file "PawanJii", line 105>)
            356 MAKE_FUNCTION            0
            358 STORE_NAME              32 (encodeZlib)

115         360 LOAD_CONST              20 (<code object encodeBase64 at 0x7a94ec8c30, file "PawanJii", line 115>)
            362 MAKE_FUNCTION            0
            364 STORE_NAME              33 (encodeBase64)

125         366 LOAD_CONST              21 (<code object encodePyc at 0x7a94f058b0, file "PawanJii", line 125>)
            368 MAKE_FUNCTION            0
            370 STORE_NAME              34 (encodePyc)

137         372 LOAD_CONST              22 (<code object encodeAllOnce at 0x7a94e65250, file "PawanJii", line 137>)
            374 MAKE_FUNCTION            0
            376 STORE_NAME              35 (encodeAllOnce)

149         378 LOAD_CONST              23 (<code object encodeAllStep at 0x7a94e890b0, file "PawanJii", line 149>)
            380 MAKE_FUNCTION            0
            382 STORE_NAME              36 (encodeAllStep)

159         384 LOAD_CONST              24 (<code object getPower at 0x7a94e72a30, file "PawanJii", line 159>)
            386 MAKE_FUNCTION            0
            388 STORE_NAME              37 (getPower)

174         390 LOAD_CONST              25 (<code object getFile at 0xb400007b154e6700, file "PawanJii", line 174>)
            392 MAKE_FUNCTION            0
            394 STORE_NAME              38 (getFile)

193         396 LOAD_CONST              26 (<code object saveFile at 0x7a94d60b70, file "PawanJii", line 193>)
            398 MAKE_FUNCTION            0
            400 STORE_NAME              39 (saveFile)

199         402 LOAD_CONST              27 (<code object moveFile at 0x7a94ed0d50, file "PawanJii", line 199>)
            404 MAKE_FUNCTION            0
            406 STORE_NAME              40 (moveFile)

212         408 LOAD_CONST              28 (<code object encode at 0xb400007b15516c00, file "PawanJii", line 212>)
            410 MAKE_FUNCTION            0
            412 STORE_NAME              41 (encode)

254         414 LOAD_CONST              29 (<code object main at 0xb400007a94b21c00, file "PawanJii", line 254>)
            416 MAKE_FUNCTION            0
            418 STORE_NAME              42 (main)

287         420 LOAD_NAME               43 (__name__)
            422 LOAD_CONST              30 ('__main__')
            424 COMPARE_OP               2 (<)
            428 CACHE
            430 POP_JUMP_IF_FALSE       32 (to 496)

288         432 PUSH_NULL
            434 LOAD_NAME               18 (logo)
            436 UNPACK_SEQUENCE          0
            440 CALL                     0
            448 CACHE
            450 POP_TOP

289         452 PUSH_NULL
            454 LOAD_NAME               20 (banner)
            456 UNPACK_SEQUENCE          0
            460 CALL                     0
            468 CACHE
            470 POP_TOP

290         472 PUSH_NULL
            474 LOAD_NAME               42 (main)
            476 UNPACK_SEQUENCE          0
            480 CALL                     0
            488 CACHE
            490 POP_TOP
            492 LOAD_CONST               1 (None)
            494 RETURN_VALUE

287     >>  496 LOAD_CONST               1 (None)
            498 RETURN_VALUE
ExceptionTable:
  76 to 144 -> 148 [0]
  148 to 274 -> 280 [1] lasti

Disassembly of <code object logo at 0x7a94f04ab0, file "PawanJii", line 24>:
 24           0 RESUME                   0

 25           2 LOAD_CONST               1 ('\x1b[0m')
              4 STORE_FAST               0 (clear)

 26           6 BUILD_LIST               0
              8 LOAD_CONST               2 ((35, 33, 36))
             10 LIST_EXTEND              1
             12 STORE_FAST               1 (colors)

 27          14 LOAD_CONST               3 ("\n                \n»»———————————————————————————\u3000★\u3000——————————————————————————««\n       d8888b.  .d8b.  db   d8b   db  .d8b.  d8b   db \n       88  `8D d8' `8b 88   I8I   88 d8' `8b 888o  88 \n       88oodD' 88ooo88 88   I8I   88 88ooo88 88V8o 88 \n       88~~~   88~~~88 Y8   I8I   88 88~~~88 88 V8o88 \n       88      88   88 `8b d8'8b d8' 88   88 88  V888 \n       88      YP   YP  `8b8' `8d8'  YP   YP VP   V8P \n»»———————————————————————————\u3000★\u3000——————————————————————————««\n           | Tool Purpose ➟ Encode Your Script  | \n»»———————————————————————————\u3000★\u3000——————————————————————————««\n")
             16 STORE_FAST               2 (x)

 40          18 LOAD_GLOBAL              1 (NULL + enumerate)
             28 CACHE
             30 LOAD_FAST                2 (x)
             32 STORE_SUBSCR
             36 CACHE
             38 CACHE
             40 CACHE
             42 CACHE
             44 CACHE
             46 CACHE
             48 CACHE
             50 CACHE
             52 CACHE
             54 LOAD_CONST               4 ('\n')
             56 UNPACK_SEQUENCE          1
             60 CALL                     1
             68 CACHE
             70 UNPACK_SEQUENCE          1
             74 CALL                     1
             82 CACHE
             84 GET_ITER
        >>   86 FOR_ITER                80 (to 250)
             90 CACHE
             92 STORE_FAST               3 (N)
             94 STORE_FAST               4 (line)

 41          96 LOAD_GLOBAL              4 (sys)
            106 CACHE
            108 LOAD_ATTR                3 (NULL|self + split)
            128 CACHE
            130 CACHE
            132 CACHE
            134 CACHE
            136 CACHE
            138 CACHE
            140 LOAD_CONST               5 ('\x1b[1;%dm%s%s\n')
            142 LOAD_GLOBAL             11 (NULL + random)
            152 CACHE
            154 LOAD_ATTR                6 (stdout)
            174 CACHE
            176 CACHE
            178 CACHE
            180 LOAD_FAST                4 (line)
            182 LOAD_FAST                0 (clear)
            184 BUILD_TUPLE              3
            186 BINARY_OP                6 (%)
            190 UNPACK_SEQUENCE          1
            194 CALL                     1
            202 CACHE
            204 POP_TOP

 42         206 LOAD_GLOBAL             15 (NULL + time)
            216 CACHE
            218 LOAD_ATTR                8 (write)
            238 CACHE
            240 CACHE
            242 CACHE
            244 POP_TOP
            246 JUMP_BACKWARD           81 (to 86)

 40         248 LOAD_CONST               0 (None)
        >>  250 RETURN_VALUE

Disassembly of <code object logout at 0x7a94ec8030, file "PawanJii", line 45>:
 45           0 RESUME                   0

 46           2 LOAD_GLOBAL              1 (NULL + psb)
             12 CACHE
             14 LOAD_CONST               1 ('\n    \x1b[94m[\x1b[92m*\x1b[94m]\x1b[92m Thanks For Using Our Tool')
             16 UNPACK_SEQUENCE          1
             20 CALL                     1
             28 CACHE
             30 POP_TOP

 47          32 LOAD_GLOBAL              1 (NULL + psb)
             42 CACHE
             44 LOAD_CONST               2 ('    \x1b[94m[\x1b[92m*\x1b[94m]\x1b[92m For More Tools, Visit: \n')
             46 UNPACK_SEQUENCE          1
             50 CALL                     1
             58 CACHE
             60 POP_TOP

 48          62 LOAD_GLOBAL              3 (NULL + print)
             72 CACHE
             74 LOAD_CONST               3 ('\x1b[93m[ \x1b[92mhttps://github.com/VIBE81 \x1b[93m]\x1b[37m\n')
             76 STORE_SUBSCR
             80 CACHE
             82 CACHE
             84 CACHE
             86 CACHE
             88 CACHE
             90 CACHE
             92 CACHE
             94 CACHE
             96 CACHE
             98 LOAD_GLOBAL              6 (column3)
            108 CACHE
            110 UNPACK_SEQUENCE          1
            114 CALL                     1
            122 CACHE
            124 UNPACK_SEQUENCE          1
            128 CALL                     1
            136 CACHE
            138 POP_TOP

 49         140 LOAD_GLOBAL              9 (NULL + sys)
            150 CACHE
            152 LOAD_ATTR                5 (NULL|self + center)
            172 CACHE
            174 CACHE
            176 POP_TOP
            178 LOAD_CONST               0 (None)
            180 RETURN_VALUE

Disassembly of <code object banner at 0xb400007b1555d880, file "PawanJii", line 52>:
 52           0 RESUME                   0

 53           2 LOAD_GLOBAL              1 (NULL + str)
             12 CACHE
             14 LOAD_GLOBAL              2 (sys)
             24 CACHE
             26 LOAD_ATTR                2 (sys)
             46 CACHE
             48 CACHE
             50 CACHE
             52 LOAD_CONST               2 (0)
             54 BINARY_SUBSCR
             58 CACHE
             60 CACHE
             62 CACHE
             64 UNPACK_SEQUENCE          1
             68 CALL                     1
             76 CACHE
             78 LOAD_CONST               3 ('.')
             80 BINARY_OP                0 (+)
             84 LOAD_GLOBAL              1 (NULL + str)
             94 CACHE
             96 LOAD_GLOBAL              2 (sys)
            106 CACHE
            108 LOAD_ATTR                2 (sys)
            128 CACHE
            130 CACHE
            132 CACHE
            134 LOAD_CONST               4 (1)
            136 BINARY_SUBSCR
            140 CACHE
            142 CACHE
            144 CACHE
            146 UNPACK_SEQUENCE          1
            150 CALL                     1
            158 CACHE
            160 BINARY_OP                0 (+)
            164 LOAD_CONST               3 ('.')
            166 BINARY_OP                0 (+)
            170 LOAD_GLOBAL              1 (NULL + str)
            180 CACHE
            182 LOAD_GLOBAL              2 (sys)
            192 CACHE
            194 LOAD_ATTR                2 (sys)
            214 CACHE
            216 CACHE
            218 CACHE
            220 LOAD_CONST               5 (2)
            222 BINARY_SUBSCR
            226 CACHE
            228 CACHE
            230 CACHE
            232 UNPACK_SEQUENCE          1
            236 CALL                     1
            244 CACHE
            246 BINARY_OP                0 (+)
            250 STORE_FAST               0 (version)

 55         252 LOAD_GLOBAL              7 (NULL + print)
            262 CACHE
            264 LOAD_CONST               6 ('\x1b[93m-')
            266 LOAD_GLOBAL              9 (NULL + int)
            276 CACHE
            278 LOAD_GLOBAL             10 (columns)
            288 CACHE
            290 UNPACK_SEQUENCE          1
            294 CALL                     1
            302 CACHE
            304 BINARY_OP                5 (*)
            308 UNPACK_SEQUENCE          1
            312 CALL                     1
            320 CACHE
            322 POP_TOP

 56         324 LOAD_GLOBAL              2 (sys)
            334 CACHE
            336 LOAD_ATTR                2 (sys)
            356 CACHE
            358 CACHE
            360 CACHE
            362 LOAD_CONST               2 (0)
            364 BINARY_SUBSCR
            368 CACHE
            370 CACHE
            372 CACHE
            374 LOAD_CONST               1 (3)
            376 COMPARE_OP               0 (<)
            380 CACHE
            382 POP_JUMP_IF_FALSE       19 (to 422)

 57         384 LOAD_GLOBAL              7 (NULL + print)
            394 CACHE
            396 LOAD_CONST               7 ('\x1b[92m\t\tPython Version : \x1b[37m')
            398 LOAD_FAST                0 (version)
            400 BINARY_OP                0 (+)
            404 UNPACK_SEQUENCE          1
            408 CALL                     1
            416 CACHE
            418 POP_TOP
            420 JUMP_FORWARD            45 (to 512)

 59     >>  422 LOAD_GLOBAL              7 (NULL + print)
            432 CACHE
            434 LOAD_CONST               8 ('\x1b[92mPython Version : \x1b[37m')
            436 LOAD_FAST                0 (version)
            438 BINARY_OP                0 (+)
            442 STORE_SUBSCR
            446 CACHE
            448 CACHE
            450 CACHE
            452 CACHE
            454 CACHE
            456 CACHE
            458 CACHE
            460 CACHE
            462 CACHE
            464 LOAD_GLOBAL             10 (columns)
            474 CACHE
            476 LOAD_CONST               9 (10)
            478 BINARY_OP                0 (+)
            482 UNPACK_SEQUENCE          1
            486 CALL                     1
            494 CACHE
            496 UNPACK_SEQUENCE          1
            500 CALL                     1
            508 CACHE
            510 POP_TOP

 60     >>  512 LOAD_GLOBAL              7 (NULL + print)
            522 CACHE
            524 LOAD_CONST               6 ('\x1b[93m-')
            526 LOAD_GLOBAL              9 (NULL + int)
            536 CACHE
            538 LOAD_GLOBAL             10 (columns)
            548 CACHE
            550 UNPACK_SEQUENCE          1
            554 CALL                     1
            562 CACHE
            564 BINARY_OP                5 (*)
            568 UNPACK_SEQUENCE          1
            572 CALL                     1
            580 CACHE
            582 POP_TOP
            584 LOAD_CONST               0 (None)
            586 RETURN_VALUE

Disassembly of <code object psb at 0x7a94ec8330, file "PawanJii", line 63>:
 63           0 RESUME                   0

 64           2 LOAD_FAST                0 (z)
              4 LOAD_CONST               1 ('\n')
              6 BINARY_OP                0 (+)
             10 GET_ITER
        >>   12 FOR_ITER                83 (to 182)

 65          16 LOAD_GLOBAL              0 (sys)
             26 CACHE
             28 LOAD_ATTR                1 (NULL|self + sys)
             48 CACHE
             50 CACHE
             52 CACHE
             54 CACHE
             56 CACHE
             58 CACHE
             60 LOAD_FAST                1 (e)
             62 UNPACK_SEQUENCE          1
             66 CALL                     1
             74 CACHE
             76 POP_TOP

 66          78 LOAD_GLOBAL              0 (sys)
             88 CACHE
             90 LOAD_ATTR                1 (NULL|self + sys)
            110 CACHE
            112 CACHE
            114 CACHE
            116 CACHE
            118 CACHE
            120 CACHE
            122 UNPACK_SEQUENCE          0
            126 CALL                     0
            134 CACHE
            136 POP_TOP

 67         138 LOAD_GLOBAL              9 (NULL + time)
            148 CACHE
            150 LOAD_ATTR                5 (NULL|self + write)
            170 CACHE
            172 CACHE
            174 CACHE
            176 POP_TOP
            178 JUMP_BACKWARD           84 (to 12)

 64         180 LOAD_CONST               0 (None)
        >>  182 RETURN_VALUE

Disassembly of <code object verInput at 0x7a94d60a30, file "PawanJii", line 70>:
 70           0 RESUME                   0

 71           2 LOAD_GLOBAL              0 (sys)
             12 CACHE
             14 LOAD_ATTR                1 (NULL|self + sys)
             34 CACHE
             36 CACHE
             38 CACHE
             40 STORE_FAST               1 (version)

 72          42 LOAD_FAST                1 (version)
             44 LOAD_CONST               2 ((3, 0))
             46 COMPARE_OP               0 (<)
             50 CACHE
             52 POP_JUMP_IF_FALSE       16 (to 86)

 73          54 LOAD_GLOBAL              5 (NULL + raw_input)
             64 CACHE
             66 LOAD_FAST                0 (data)
             68 UNPACK_SEQUENCE          1
             72 CALL                     1
             80 CACHE
             82 STORE_FAST               2 (dataInput)
             84 JUMP_FORWARD            15 (to 116)

 75     >>   86 LOAD_GLOBAL              7 (NULL + input)
             96 CACHE
             98 LOAD_FAST                0 (data)
            100 UNPACK_SEQUENCE          1
            104 CALL                     1
            112 CACHE
            114 STORE_FAST               2 (dataInput)

 76     >>  116 LOAD_FAST                2 (dataInput)
            118 RETURN_VALUE

Disassembly of <code object encodeMarshal at 0x7a94ec84b0, file "PawanJii", line 95>:
 95           0 RESUME                   0

 96           2 LOAD_FAST                0 (data)
              4 STORE_FAST               2 (powerData)

 97           6 LOAD_GLOBAL              1 (NULL + range)
             16 CACHE
             18 LOAD_FAST                1 (power)
             20 UNPACK_SEQUENCE          1
             24 CALL                     1
             32 CACHE
             34 GET_ITER
        >>   36 FOR_ITER                70 (to 180)

 98          40 LOAD_GLOBAL              3 (NULL + compile)
             50 CACHE
             52 LOAD_FAST                2 (powerData)
             54 LOAD_CONST               1 ('PawanJii')
             56 LOAD_CONST               2 ('exec')
             58 UNPACK_SEQUENCE          3
             62 CALL                     3
             70 CACHE
             72 STORE_FAST               4 (code)

 99          74 LOAD_GLOBAL              5 (NULL + marshal)
             84 CACHE
             86 LOAD_ATTR                3 (NULL|self + compile)
            106 CACHE
            108 CACHE
            110 CACHE
            112 STORE_FAST               5 (dump)

100         114 LOAD_GLOBAL              8 (marshalHead)
            124 CACHE
            126 LOAD_GLOBAL             11 (NULL + repr)
            136 CACHE
            138 LOAD_FAST                5 (dump)
            140 UNPACK_SEQUENCE          1
            144 CALL                     1
            152 CACHE
            154 BINARY_OP                0 (+)
            158 LOAD_GLOBAL             12 (marshalTail)
            168 CACHE
            170 BINARY_OP                0 (+)
            174 STORE_FAST               2 (powerData)
            176 JUMP_BACKWARD           71 (to 36)

102         178 LOAD_FAST                2 (powerData)
        >>  180 RETURN_VALUE

Disassembly of <code object encodeZlib at 0x7a94ec8630, file "PawanJii", line 105>:
105           0 RESUME                   0

106           2 LOAD_FAST                0 (data)
              4 STORE_FAST               2 (powerData)

107           6 LOAD_GLOBAL              1 (NULL + range)
             16 CACHE
             18 LOAD_FAST                1 (power)
             20 UNPACK_SEQUENCE          1
             24 CALL                     1
             32 CACHE
             34 GET_ITER
        >>   36 FOR_ITER                74 (to 188)

108          40 LOAD_FAST                2 (powerData)
             42 STORE_SUBSCR
             46 CACHE
             48 CACHE
             50 CACHE
             52 CACHE
             54 CACHE
             56 CACHE
             58 CACHE
             60 CACHE
             62 CACHE
             64 UNPACK_SEQUENCE          0
             68 CALL                     0
             76 CACHE
             78 STORE_FAST               4 (code)

109          80 LOAD_GLOBAL              5 (NULL + zlib)
             90 CACHE
             92 LOAD_ATTR                3 (NULL|self + encode)
            112 CACHE
            114 CACHE
            116 CACHE
            118 CACHE
            120 STORE_FAST               5 (dump)

110         122 LOAD_GLOBAL              8 (zlibHead)
            132 CACHE
            134 LOAD_GLOBAL             11 (NULL + repr)
            144 CACHE
            146 LOAD_FAST                5 (dump)
            148 UNPACK_SEQUENCE          1
            152 CALL                     1
            160 CACHE
            162 BINARY_OP                0 (+)
            166 LOAD_GLOBAL             12 (zlibTail)
            176 CACHE
            178 BINARY_OP                0 (+)
            182 STORE_FAST               2 (powerData)
            184 JUMP_BACKWARD           75 (to 36)

112         186 LOAD_FAST                2 (powerData)
        >>  188 RETURN_VALUE

Disassembly of <code object encodeBase64 at 0x7a94ec8c30, file "PawanJii", line 115>:
115           0 RESUME                   0

116           2 LOAD_FAST                0 (data)
              4 STORE_FAST               2 (powerData)

117           6 LOAD_GLOBAL              1 (NULL + range)
             16 CACHE
             18 LOAD_FAST                1 (power)
             20 UNPACK_SEQUENCE          1
             24 CALL                     1
             32 CACHE
             34 GET_ITER
        >>   36 FOR_ITER                73 (to 186)

118          40 LOAD_FAST                2 (powerData)
             42 STORE_SUBSCR
             46 CACHE
             48 CACHE
             50 CACHE
             52 CACHE
             54 CACHE
             56 CACHE
             58 CACHE
             60 CACHE
             62 CACHE
             64 UNPACK_SEQUENCE          0
             68 CALL                     0
             76 CACHE
             78 STORE_FAST               4 (code)

119          80 LOAD_GLOBAL              5 (NULL + base64)
             90 CACHE
             92 LOAD_ATTR                3 (NULL|self + encode)
            112 CACHE
            114 CACHE
            116 CACHE
            118 STORE_FAST               5 (dump)

120         120 LOAD_GLOBAL              8 (b64Head)
            130 CACHE
            132 LOAD_GLOBAL             11 (NULL + repr)
            142 CACHE
            144 LOAD_FAST                5 (dump)
            146 UNPACK_SEQUENCE          1
            150 CALL                     1
            158 CACHE
            160 BINARY_OP                0 (+)
            164 LOAD_GLOBAL             12 (b64Tail)
            174 CACHE
            176 BINARY_OP                0 (+)
            180 STORE_FAST               2 (powerData)
            182 JUMP_BACKWARD           74 (to 36)

122         184 LOAD_FAST                2 (powerData)
        >>  186 RETURN_VALUE

Disassembly of <code object encodePyc at 0x7a94f058b0, file "PawanJii", line 125>:
125           0 RESUME                   0

126           2 LOAD_GLOBAL              1 (NULL + open)
             12 CACHE
             14 LOAD_CONST               1 ('temp.py')
             16 LOAD_CONST               2 ('w')
             18 UNPACK_SEQUENCE          2
             22 CALL                     2
             30 CACHE
             32 STORE_FAST               1 (tmp)

127          34 LOAD_FAST                1 (tmp)
             36 STORE_SUBSCR
             40 CACHE
             42 CACHE
             44 CACHE
             46 CACHE
             48 CACHE
             50 CACHE
             52 CACHE
             54 CACHE
             56 CACHE
             58 LOAD_FAST                0 (data)
             60 UNPACK_SEQUENCE          1
             64 CALL                     1
             72 CACHE
             74 POP_TOP

128          76 LOAD_FAST                1 (tmp)
             78 STORE_SUBSCR
             82 CACHE
             84 CACHE
             86 CACHE
             88 CACHE
             90 CACHE
             92 CACHE
             94 CACHE
             96 CACHE
             98 CACHE
            100 UNPACK_SEQUENCE          0
            104 CALL                     0
            112 CACHE
            114 POP_TOP

129         116 LOAD_GLOBAL              6 (sys)
            126 CACHE
            128 LOAD_ATTR                4 (close)
            148 CACHE
            150 CACHE
            152 CACHE
            154 LOAD_CONST               4 ((3, 0))
            156 COMPARE_OP               0 (<)
            160 CACHE
            162 POP_JUMP_IF_FALSE       21 (to 206)

130         164 LOAD_GLOBAL             11 (NULL + compileall)
            174 CACHE
            176 LOAD_ATTR                6 (sys)
            196 CACHE
            198 CACHE
            200 CACHE
            202 POP_TOP
            204 JUMP_FORWARD            22 (to 250)

132     >>  206 LOAD_GLOBAL             11 (NULL + compileall)
            216 CACHE
            218 LOAD_ATTR                6 (sys)
            238 CALL                     2
            246 CACHE
            248 POP_TOP

134     >>  250 LOAD_CONST               5 (True)
            252 RETURN_VALUE

Disassembly of <code object encodeAllOnce at 0x7a94e65250, file "PawanJii", line 137>:
137           0 RESUME                   0

138           2 LOAD_FAST                0 (data)
              4 STORE_FAST               2 (powerData)

139           6 LOAD_GLOBAL              1 (NULL + range)
             16 CACHE
             18 LOAD_FAST                1 (power)
             20 UNPACK_SEQUENCE          1
             24 CALL                     1
             32 CACHE
             34 GET_ITER
        >>   36 FOR_ITER               110 (to 260)

140          40 LOAD_GLOBAL              3 (NULL + compile)
             50 CACHE
             52 LOAD_FAST                2 (powerData)
             54 LOAD_CONST               1 ('PawanJii')
             56 LOAD_CONST               2 ('exec')
             58 UNPACK_SEQUENCE          3
             62 CALL                     3
             70 CACHE
             72 STORE_FAST               4 (code)

141          74 LOAD_GLOBAL              5 (NULL + marshal)
             84 CACHE
             86 LOAD_ATTR                3 (NULL|self + compile)
            106 CACHE
            108 CACHE
            110 CACHE
            112 STORE_FAST               4 (code)

142         114 LOAD_GLOBAL              9 (NULL + zlib)
            124 CACHE
            126 LOAD_ATTR                5 (NULL|self + marshal)
            146 CACHE
            148 CACHE
            150 CACHE
            152 STORE_FAST               4 (code)

143         154 LOAD_GLOBAL             13 (NULL + base64)
            164 CACHE
            166 LOAD_ATTR                7 (NULL|self + dumps)
            186 CACHE
            188 CACHE
            190 CACHE
            192 STORE_FAST               5 (dump)

144         194 LOAD_GLOBAL             16 (allHead)
            204 CACHE
            206 LOAD_GLOBAL             19 (NULL + repr)
            216 CACHE
            218 LOAD_FAST                5 (dump)
            220 UNPACK_SEQUENCE          1
            224 CALL                     1
            232 CACHE
            234 BINARY_OP                0 (+)
            238 LOAD_GLOBAL             20 (allTail)
            248 CACHE
            250 BINARY_OP                0 (+)
            254 STORE_FAST               2 (powerData)
            256 JUMP_BACKWARD          111 (to 36)

146         258 LOAD_FAST                2 (powerData)
        >>  260 RETURN_VALUE

Disassembly of <code object encodeAllStep at 0x7a94e890b0, file "PawanJii", line 149>:
149           0 RESUME                   0

150           2 LOAD_FAST                0 (data)
              4 STORE_FAST               2 (powerData)

151           6 LOAD_GLOBAL              1 (NULL + range)
             16 CACHE
             18 LOAD_FAST                1 (power)
             20 UNPACK_SEQUENCE          1
             24 CALL                     1
             32 CACHE
             34 GET_ITER
        >>   36 FOR_ITER                53 (to 146)

152          40 LOAD_GLOBAL              3 (NULL + encodeBase64)
             50 CACHE
             52 LOAD_FAST                2 (powerData)
             54 LOAD_CONST               1 (1)
             56 KW_NAMES                 2 (('power',))
             58 UNPACK_SEQUENCE          2
             62 CALL                     2
             70 CACHE
             72 STORE_FAST               4 (code)

153          74 LOAD_GLOBAL              5 (NULL + encodeZlib)
             84 CACHE
             86 LOAD_FAST                4 (code)
             88 LOAD_CONST               1 (1)
             90 KW_NAMES                 2 (('power',))
             92 UNPACK_SEQUENCE          2
             96 CALL                     2
            104 CACHE
            106 STORE_FAST               4 (code)

154         108 LOAD_GLOBAL              7 (NULL + encodeMarshal)
            118 CACHE
            120 LOAD_FAST                4 (code)
            122 LOAD_CONST               1 (1)
            124 KW_NAMES                 2 (('power',))
            126 UNPACK_SEQUENCE          2
            130 CALL                     2
            138 CACHE
            140 STORE_FAST               2 (powerData)
            142 JUMP_BACKWARD           54 (to 36)

156         144 LOAD_FAST                2 (powerData)
        >>  146 RETURN_VALUE

Disassembly of <code object getPower at 0x7a94e72a30, file "PawanJii", line 159>:
159           0 RESUME                   0

160           2 LOAD_GLOBAL              1 (NULL + verInput)
             12 CACHE
             14 LOAD_CONST               1 ('\x1b[92m    [\x1b[37m*\x1b[92m]\x1b[37m Enter Repeat Amount (\x1b[92mMAX: 15\x1b[37m):> \x1b[92m')
             16 UNPACK_SEQUENCE          1
             20 CALL                     1
             28 CACHE
             30 STORE_FAST               0 (power)

161          32 LOAD_FAST                0 (power)
             34 STORE_SUBSCR
             38 CACHE
             40 CACHE
             42 CACHE
             44 CACHE
             46 CACHE
             48 CACHE
             50 CACHE
             52 CACHE
             54 CACHE
             56 UNPACK_SEQUENCE          0
             60 CALL                     0
             68 CACHE
             70 POP_JUMP_IF_TRUE        50 (to 172)

162          72 LOAD_GLOBAL              5 (NULL + psb)
             82 CACHE
             84 LOAD_CONST               2 ('\n\x1b[92m    [\x1b[91m!\x1b[92m]\x1b[37m Enter a Correct Amount!')
             86 UNPACK_SEQUENCE          1
             90 CALL                     1
             98 CACHE
            100 POP_TOP

163         102 LOAD_GLOBAL              1 (NULL + verInput)
            112 CACHE
            114 LOAD_CONST               1 ('\x1b[92m    [\x1b[37m*\x1b[92m]\x1b[37m Enter Repeat Amount (\x1b[92mMAX: 15\x1b[37m):> \x1b[92m')
            116 UNPACK_SEQUENCE          1
            120 CALL                     1
            128 CACHE
            130 STORE_FAST               0 (power)

161         132 LOAD_FAST                0 (power)
            134 STORE_SUBSCR
            138 CACHE
            140 CACHE
            142 CACHE
            144 CACHE
            146 CACHE
            148 CACHE
            150 CACHE
            152 CACHE
            154 CACHE
            156 UNPACK_SEQUENCE          0
            160 CALL                     0
            168 CACHE
