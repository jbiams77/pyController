toFile = [b'\xfeH\xa9\x00\x00\x00\x81\x00', b'\xfeH\xa9\x00\x00\x00\x81\x01', b'\xfeH\xa9\x00\x00\x00\x81\x02',
          b'\xfeH\xa9\x00\x00\x00\x81\x03', b'\xfeH\xa9\x00\x00\x00\x81\x04', b'\xfeH\xa9\x00\x00\x00\x81\x05',
          b'\xfeH\xa9\x00\x00\x00\x81\x06', b'\xfeH\xa9\x00\x00\x00\x81\x07', b'\xfeH\xa9\x00\x00\x00\x81\x08',
          b'\xfeH\xa9\x00\x00\x00\x81\t', b'\xfeH\xa9\x00\x00\x00\x81\n', b'\xfeH\xa9\x00\x00\x00\x81\x0b',
          b'\xfeH\xa9\x00\x00\x00\x81\x0c', b'\xfeH\xa9\x00\x00\x00\x82\x00', b'\xfeH\xa9\x00\x00\x00\x82\x01',
          b'\xfeH\xa9\x00\x01\x80\x82\x02', b'\xfeH\xa9\x00\x00\x00\x82\x03', b'\xfeH\xa9\x00\x00\x00\x82\x04',
          b'\xfeH\xa9\x00\x01\x80\x82\x05', b'\xfeH\xa9\x00\x00\x00\x82\x06', b'\xfeH\xa9\x00\x00\x00\x82\x07',
          b'JM\xa9\x00\xff\x7f\x02\x01', b'JM\xa9\x00\xab\x1f\x02\x00', b'\x86M\xa9\x00\x00\x00\x02\x00',
          b'\x86M\xa9\x00\x01\x00\x01\x0b', b'\xeaM\xa9\x00\x00\x00\x01\x0b', b'\xf4M\xa9\x00\xab\x1f\x02\x00',
          b'\xf4M\xa9\x00Id\x02\x03', b'&N\xa9\x00\xf8b\x02\x00', b'&N\xa9\x00\x00\x00\x02\x01',
          b'&N\xa9\x00\xff\x7f\x02\x03', b'0N\xa9\x00\x00\x00\x02\x00', b'0N\xa9\x00\xed\xe6\x02\x01',
          b'NN\xa9\x00\x00\x00\x02\x01', b'\xeeN\xa9\x00\x07\x1d\x02\x01', b'\xf8N\xa9\x00\xff\x7f\x02\x00',
          b'\xf8N\xa9\x00\xff\x7f\x02\x01', b'\xf8N\xa9\x00\x00\x00\x02\x03', b'\xf8N\xa9\x00\x05>\x02\x04',
          b'*O\xa9\x00Id\x02\x04', b'4O\xa9\x00\xe2j\x02\x04', b'zO\xa9\x00\x00\x00\x02\x04',
          b'\x98O\xa9\x00\xff\x7f\x02\x03', b'\x98O\xa9\x00\xae\xfe\x02\x04', b'\xb6O\xa9\x00:*\x02\x01',
          b'\xb6O\xa9\x00\x12\x99\x02\x04', b'\xd4O\xa9\x00\x00\x00\x02\x01', b'\xf2O\xa9\x00\xf0\xc5\x02\x01',
          b'\xfcO\xa9\x00\x00\x00\x02\x00', b'\xfcO\xa9\x00\x00\x00\x02\x01', b'8P\xa9\x00\x01\x80\x02\x04',
          b'BP\xa9\x00\x01\x00\x01\x05', b'tP\xa9\x00\x17\xd7\x02\x04', b'~P\xa9\x00\x93H\x02\x03',
          b'~P\xa9\x00\x1f\xf4\x02\x04', b'\xbaP\xa9\x00\x00\x00\x02\x03', b'\xbaP\xa9\x00\x00\x00\x02\x04',
          b'V_\xa9\x00\x00\x00\x81\x00', b'V_\xa9\x00\x00\x00\x81\x01', b'V_\xa9\x00\x00\x00\x81\x02',
          b'V_\xa9\x00\x00\x00\x81\x03', b'V_\xa9\x00\x00\x00\x81\x04', b'V_\xa9\x00\x00\x00\x81\x05',
          b'V_\xa9\x00\x00\x00\x81\x06', b'V_\xa9\x00\x00\x00\x81\x07', b'V_\xa9\x00\x00\x00\x81\x08',
          b'V_\xa9\x00\x00\x00\x81\t', b'V_\xa9\x00\x00\x00\x81\n', b'V_\xa9\x00\x00\x00\x81\x0b',
          b'V_\xa9\x00\x00\x00\x81\x0c', b'V_\xa9\x00\x00\x00\x82\x00', b'V_\xa9\x00\x00\x00\x82\x01',
          b'V_\xa9\x00\x01\x80\x82\x02', b'V_\xa9\x00\x00\x00\x82\x03', b'V_\xa9\x00\x00\x00\x82\x04',
          b'V_\xa9\x00\x01\x80\x82\x05', b'V_\xa9\x00\x00\x00\x82\x06', b'V_\xa9\x00\xff\x7f\x82\x07',
          b'\x88_\xa9\x00\x01\x00\x01\x00', b'\xb0_\xa9\x00\x00\x00\x02\x07', b'\xd8_\xa9\x00\x00\x00\x01\x00',
          b'\n`\xa9\x00\xff\x7f\x02\x07', b'P`\xa9\x00\x01\x00\x01\x00', b'x`\xa9\x00\x00\x00\x02\x07',
          b'\xb4`\xa9\x00\x00\x00\x01\x00', b'|a\xa9\x00\x01\x00\x01\x03', b'\xcca\xa9\x00\x00\x00\x01\x03',
          b'vb\xa9\x00\x01\x00\x01\x02', b'\xd0b\xa9\x00\x00\x00\x01\x02', b'4c\xa9\x00\x01\x00\x01\x02',
          b'\xb6c\xa9\x00\x00\x00\x01\x02', b'~d\xa9\x00\x01\x00\x01\x05', b',f\xa9\x00\x00\x00\x01\x05',
          b'\x06i\xa9\x00\x01\x00\x01\x07', b'\xcei\xa9\x00n\x96\x02\x05', b'\xd8i\xa9\x00\xe5\xc9\x02\x05',
          b'\xf6i\xa9\x00,\xcf\x02\x05', b'2j\xa9\x00\x93\xc8\x02\x05', b'<j\xa9\x00\xa8\xc0\x02\x05',
          b'nj\xa9\x00\xd3\xb0\x02\x05', b'xj\xa9\x00\xea\x87\x02\x05', b'\xb4j\xa9\x00\x01\x80\x02\x05',
          b'\x04k\xa9\x00\x00\x00\x01\x07', b'Vn\xa9\x00\x01\x00\x01\x07', b'\x9cn\xa9\x00\xa3\x82\x02\x05',
          b'\xf6n\xa9\x00\x01\x80\x02\x05', b'\x1eo\xa9\x00\x00\x00\x01\x07', b'\x86p\xa9\x00\x01\x00\x01\x06',
          b'\x86p\xa9\x00\xd3\xb0\x02\x02', b'\x86p\xa9\x00\xff\x7f\x02\x02', b'~s\xa9\x00\xb3\xbc\x02\x02',
          b'~s\xa9\x00\x00\x00\x01\x06', b'~s\xa9\x00\x01\x80\x02\x02', b'\xc4s\xa9\x00\x01\x00\x01\x06',
          b'\xc4s\xa9\x00\xab\x9f\x02\x02', b'\x00t\xa9\x00\xff\x7f\x02\x02', b'Ft\xa9\x00i\xd8\x02\x02',
          b'\x82t\xa9\x00\x00\x00\x01\x06', b'\x82t\xa9\x00\x01\x80\x02\x02', b'\x82t\xa9\x00\x01\x00\x01\x06',
          b'\x82t\xa9\x00Q\x01\x02\x02', b'\xaat\xa9\x00\xff\x7f\x02\x02', b'Ju\xa9\x00\x00\x00\x01\x06',
          b'Ju\xa9\x00\x01\x80\x02\x02', b'\xdav\xa9\x00\x01\x00\x01\x0c', b'\\w\xa9\x00\xa0#\x02\x03',
          b'\\w\xa9\x00\x00\x00\x02\x03', b'\\w\xa9\x00\x00\x00\x01\x0c', b'\xa2w\xa9\x00\x01\x00\x01\x0c',
          b'Bx\xa9\x00\x00\x00\x01\x0c', b'\xa6x\xa9\x00\x01\x00\x01\x0b', b'2y\xa9\x00\x00\x00\x01\x0b',
          b'\x82y\xa9\x00\x01\x00\x01\x0b', b'\xb4y\xa9\x00\xd30\x02\x01', b'\xbey\xa9\x00\xc5U\x02\x01',
          b'\xfay\xa9\x00AG\x02\x01', b'\xfay\xa9\x00\xe0\x0b\x02\x01', b'"z\xa9\x00\x00\x00\x02\x01',
          b'\x90z\xa9\x00\x00\x00\x01\x0b', b'b{\xa9\x00\x01\x00\x01\x00', b'\xb8\x7f\xa9\x00\x00\x00\x01\x00',
          b'\x94\x80\xa9\x00\xff\x7f\x02\x07', b'\x1a\x82\xa9\x00\x00\x00\x02\x07', b'\xd8\x82\xa9\x00\x01\x80\x02\x06',
          b'\xbe\x83\xa9\x00\x00\x00\x02\x06', b'^\x84\xa9\x00\x01\x80\x02\x07', b'v\x85\xa9\x00\x00\x00\x02\x07',
          b'*\x86\xa9\x00\xff\x7f\x02\x06', b'8\x87\xa9\x00\x00\x00\x02\x06', b'\x94\x8a\xa9\x00\x01\x00\x01\x07',
          b'\x94\x8a\xa9\x00\x00\x00\x02\x05', b'\x9e\x8a\xa9\x00\xff\x7f\x02\x05', b'4\x8b\xa9\x00\x01\x00\x01\x06',
          b'4\x8b\xa9\x00\x0f\xba\x02\x02', b'4\x8b\xa9\x00\\}\x02\x05', b'>\x8b\xa9\x00\x00\x00\x01\x07',
          b'>\x8b\xa9\x00\xff\x7f\x02\x02', b'>\x8b\xa9\x00\x01\x80\x02\x05', b'\x98\x8b\xa9\x00\x01\x00\x01\x07',
          b'\x98\x8b\xa9\x00\x91\xe9\x02\x05', b'\xa2\x8b\xa9\x00\x07\x9d\x02\x02', b'\xa2\x8b\xa9\x00\xff\x7f\x02\x05',
          b'\xd4\x8b\xa9\x00\x00\x00\x01\x06', b'\xd4\x8b\xa9\x00\x01\x80\x02\x02', b'\x06\x8c\xa9\x00\xab\x9f\x02\x05',
          b'$\x8c\xa9\x00\x01\x00\x01\x06', b'$\x8c\xa9\x00\x00\x00\x01\x07', b'$\x8c\xa9\x00\xff\x7f\x02\x02',
          b'$\x8c\xa9\x00\x01\x80\x02\x05', b'V\x8c\xa9\x00\x01\x00\x01\x07', b'V\x8c\xa9\x00D\xa6\x02\x05',
          b'`\x8c\xa9\x00tT\x02\x05', b'~\x8c\xa9\x00\x07\x9d\x02\x02', b'~\x8c\xa9\x00\xd8n\x02\x05',
          b'\x9c\x8c\xa9\x00\x00\x00\x01\x06', b'\x9c\x8c\xa9\x00\x01\x80\x02\x02', b'\xa6\x8c\xa9\x00,O\x02\x05',
          b'\xc4\x8c\xa9\x00\x01\x00\x01\x06', b'\xc4\x8c\xa9\x00\xb0]\x02\x02', b'\xc4\x8c\xa9\x00\x05\xbe\x02\x05',
          b'\xce\x8c\xa9\x00\x00\x00\x01\x07', b'\xce\x8c\xa9\x00\xff\x7f\x02\x02', b'\xce\x8c\xa9\x00\x01\x80\x02\x05',
          b'P\x8d\xa9\x00\x00\x00\x01\x06', b'P\x8d\xa9\x00\x01\x80\x02\x02', b'\x8c\x8d\xa9\x00\x01\x00\x01\x05',
          b'6\x8e\xa9\x00\x00\x00\x01\x05', b'|\x8e\xa9\x00\x01\x00\x01\x05', b'\x84\x90\xa9\x00\x00\x00\x01\x05',
          b'\xd4\x90\xa9\x00\x01\x00\x01\x02', b't\x91\xa9\x00\x00\x00\x01\x02', b'\x9c\x91\xa9\x00\x01\x00\x01\x02',
          b'\x1e\x92\xa9\x00\x00\x00\x01\x02', b'x\x92\xa9\x00\x01\x00\x01\x02', b'\xc8\x92\xa9\x00\x00\x00\x01\x02',
          b'@\x93\xa9\x00\x01\x00\x01\x02', b'\x90\x93\xa9\x00\x00\x00\x01\x02', b'\xf4\x93\xa9\x00\x01\x00\x01\x02',
          b'\x98\x95\xa9\x00\x00\x00\x01\x02', b'$\x96\xa9\x00\x01\x00\x01\x01', b'\x00\x97\xa9\x00\x00\x00\x01\x01',
          b'Z\x97\xa9\x00\x01\x00\x01\x00', b'\x0e\x98\xa9\x00\x00\x00\x01\x00', b'^\x98\xa9\x00\x01\x00\x01\x03',
          b'\xfe\x98\xa9\x00\x00\x00\x01\x03', b'4\x9a\xa9\x00\x01\x00\x01\x03', b'\xca\x9a\xa9\x00\x00\x00\x01\x03',
          b'\x1e\x9c\xa9\x00\x01\x00\x01\t', b'6\x9d\xa9\x00\x00\x00\x01\t', b'\x94\x9e\xa9\x00\x01\x00\x01\t',
          b'R\x9f\xa9\x00\x00\x00\x01\t', b'8\xa0\xa9\x00\x01\x00\x01\x08', b'\x82\xa1\xa9\x00\x00\x00\x01\x08']

f = open("test.txt", "wb")

for var in toFile:
    f.write(var)
f.close