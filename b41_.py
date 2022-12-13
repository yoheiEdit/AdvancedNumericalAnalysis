data='450001ae8c46400040069325852d835b684ba90aac1c0050d451a38314bc44dd801800731b7f00000101080a0f9a2fd22d9c012a474554202f32303134303532325f32362f666a727a6c676e6c776e735f3134303037353330333533333169434758535f4749462f7061636b65745f666f726d6174325f45746865725065656b2e6769663f747970653d773220485454502f312e310d0a486f73743a20626c6f677468756d62322e6e617665722e6e65740d0a557365722d4167656e743a204d6f7a696c6c612f352e3020285831313b204c696e7578207838365f36343b2072763a34352e3029204765636b6f2f32303130303130312046697265666f782f34352e300d0a4163636570743a20696d6167652f706e672c696d6167652f2a3b713d302e382c2a2f2a3b713d302e350d0a4163636570742d4c616e67756167653a20656e2d55532c656e3b713d302e350d0a4163636570742d456e636f64696e673a20677a69702c206465666c6174650d0a526566657265723a2068747470733a2f2f7777772e676f6f676c652e636f2e6a700d0a436f6e6e656374696f6e3a206b6565702d616c6976650d0a0d0a'

print('---(1)---')
print('1_1:',(len(data)//2),'Byte')
print('1_2:',int(data[4:8],16),'Byte')

print('---(2)---')
print('送信元IPアドレス: '+str(int(data[24:26],16))+'.'+str(int(data[26:28],16))+'.'+str(int(data[28:30],16))+'.'+str(int(data[30:32],16)))
print('送信先IPアドレス: '+str(int(data[32:34],16))+'.'+str(int(data[34:36],16))+'.'+str(int(data[36:38],16))+'.'+str(int(data[38:40],16)))

print('---(3)---')
print('送信元ポート番号:',int(data[40:44],16))
print('送信先ポート番号:',int(data[44:48],16))

print('---(4)---')
readable_data = bytearray.fromhex(data[104:]).decode()
print(readable_data)