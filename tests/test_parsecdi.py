import pathlib

import pytest

from parsecdi import *

SAMPLE_OUTPUT = r"""
----------------------------------------------------------------------------
CrystalDiskInfo 8.12.3 (C) 2008-2021 hiyohiyo
                                Crystal Dew World: https://crystalmark.info/
----------------------------------------------------------------------------

    OS : Windows 10 Professional [10.0 Build 19043] (x64)
  Date : 2023/03/26 12:47:12

-- Controller Map ----------------------------------------------------------
 - ATA Channel 0 (0) [ATA]
 - ATA Channel 1 (1) [ATA]
 + Standard Dual Channel PCI IDE Controller [ATA]
   - ATA Channel 0 (0)
   - ATA Channel 1 (1)
 + LSI MegaRAID SAS 9285CV-8e [SCSI]
   - LSI MR9285CV-8e SCSI Disk Device
   - LSI MR9285CV-8e SCSI Disk Device
   - LSI MegaRAID Virtual Device
 - Microsoft Storage Spaces Controller [SCSI]
 - Intel Chipset SATA RAID Controller [SCSI]

-- Disk List ---------------------------------------------------------------
 (01) INTEL SSDSC2KW256G8 : 256.0 GB [X/3/25, mr] - il
 (02) TOSHIBA HDWQ140 : 4000.7 GB [X/3/26, mr]
 (03) Samsung SSD 980 PRO 1TB : 1000.2 GB [0/2/0, sq] - nv

----------------------------------------------------------------------------
 (01) INTEL SSDSC2KW256G8
----------------------------------------------------------------------------
           Model : INTEL SSDSC2KW256G8
        Firmware : LHF004C
   Serial Number : PHLA82310760256CGN
       Disk Size : 256.0 GB (8.4/137.4/256.0/----)
     Buffer Size : Unknown
     Queue Depth : 32
    # of Sectors : 500118192
   Rotation Rate : ---- (SSD)
       Interface : Serial ATA
   Major Version : ACS-3
   Minor Version : ----
   Transfer Mode : SATA/600 | SATA/600
  Power On Hours : 7864 hours
  Power On Count : 173 count
      Host Reads : 71798 GB
     Host Writes : 64203 GB
     NAND Writes : 78313 GB
     Temperature : 33 C (91 F)
   Health Status : Good (64 %)
        Features : S.M.A.R.T., APM, NCQ, TRIM, DevSleep
       APM Level : 00FEh [ON]
       AAM Level : ----
    Drive Letter :

-- S.M.A.R.T. --------------------------------------------------------------
ID Cur Wor Thr RawValues(6) Attribute Name
05 100 100 __0 000000000000 Re-Allocated Sector Count
09 100 100 __0 000000001EB8 Power-On Hours Count

-- IDENTIFY_DEVICE ---------------------------------------------------------
        0    1    2    3    4    5    6    7    8    9
000: 0040 3FFF C837 0010 0000 0000 003F 0000 0000 0000
010: 5048 4C41 3832 3331 3037 3630 3235 3643 474E 2020
020: 0000 0000 0000 204C 4846 3030 3443 494E 5445 4C20
030: 5353 4453 4332 4B57 3235 3647 3820 2020 2020 2020
040: 2020 2020 2020 2020 2020 2020 2020 8010 4000 2F00
050: 4000 0000 0000 0007 3FFF 0010 003F FC10 00FB B110
060: FFFF 0FFF 0000 0007 0003 0078 0078 0078 0078 4D30
070: 0000 0000 0000 0000 0000 001F 870E 0086 014C 0044
080: 07FC FFFF 746B 7409 6163 7469 B409 6163 407F 0001
090: 0001 00FE FFFE 0000 0000 0000 0000 0000 0000 0000
100: 32B0 1DCF 0000 0000 0000 0008 4000 0000 55CD 2E41
110: 4F8C D343 0000 0000 0000 0000 0000 0000 0000 401C
120: 401C 0000 0000 0000 0000 0000 0000 0000 0021 0002
130: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
140: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
150: 0000 0000 0000 0000 0000 0000 0000 0000 0000 A5A5
160: 0000 0000 0000 0000 0000 0000 0000 0000 0003 0001
170: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
180: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
190: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
200: 0000 0000 0000 0000 0000 0000 003D 0000 0000 4000
210: 0000 0000 0000 0000 0000 0000 0000 0001 0000 0000
220: 0000 0000 10FF 0000 0000 0000 0000 0000 0000 0000
230: 0000 0000 0000 0000 0002 0400 0000 0000 0000 0000
240: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
250: 0000 0000 0000 0000 0000 35A5

-- SMART_READ_DATA ---------------------------------------------------------
     +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
000: 01 00 05 32 00 64 64 00 00 00 00 00 00 00 09 32
010: 00 64 64 B8 1E 00 00 00 00 00 0C 32 00 64 64 AD
020: 00 00 00 00 00 00 AA 33 00 64 64 00 00 00 00 00
030: 00 00 AB 32 00 64 64 00 00 00 00 00 00 00 AC 32
040: 00 64 64 00 00 00 00 00 00 00 AD 33 00 50 50 FA
050: 00 5F 01 2C 01 00 AE 32 00 64 64 88 00 00 00 00
060: 00 00 B7 32 00 64 64 00 00 00 00 00 00 00 B8 33
070: 00 64 64 00 00 00 00 00 00 00 BB 32 00 64 64 00
080: 00 00 00 00 00 00 BE 32 00 21 39 21 00 39 00 10
090: 00 00 C0 32 00 64 64 88 00 00 00 00 00 00 C7 32
0A0: 00 64 64 00 00 00 00 00 00 00 E1 32 00 64 64 7F
0B0: 59 1F 00 00 00 00 E2 32 00 64 64 00 00 00 00 00
0C0: 00 00 E3 32 00 64 64 00 00 00 00 00 00 00 E4 32
0D0: 00 64 64 00 00 00 00 00 00 00 E8 33 00 64 64 00
0E0: 00 00 00 00 00 00 E9 32 00 40 40 00 00 00 00 00
0F0: 00 00 EC 32 00 40 40 00 00 00 00 00 00 00 F1 32
100: 00 64 64 7F 59 1F 00 00 00 00 F2 32 00 64 64 C8
110: 0E 23 00 00 00 00 F9 32 00 64 64 E9 31 01 00 00
120: 00 00 FC 32 00 64 64 2C 01 00 00 00 00 00 00 00
130: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
140: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
150: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
160: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 53
170: 03 00 01 00 02 0F 00 00 00 00 00 00 00 00 00 00
180: 00 00 20 4C 48 46 30 30 34 43 00 00 00 00 00 00
190: 53 4D 32 32 35 39 DC 05 00 00 00 00 00 00 00 00
1A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1B0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 74

-- SMART_READ_THRESHOLD ----------------------------------------------------
     +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
000: 01 00 05 00 00 00 00 00 00 00 00 00 00 00 09 00
010: 00 00 00 00 00 00 00 00 00 00 0C 00 00 00 00 00
020: 00 00 00 00 00 00 AA 0A 00 00 00 00 00 00 00 00
030: 00 00 AB 00 00 00 00 00 00 00 00 00 00 00 AC 00
040: 00 00 00 00 00 00 00 00 00 00 AD 05 00 00 00 00
050: 00 00 00 00 00 00 AE 00 00 00 00 00 00 00 00 00
060: 00 00 B7 00 00 00 00 00 00 00 00 00 00 00 B8 5A
070: 00 00 00 00 00 00 00 00 00 00 BB 00 00 00 00 00
080: 00 00 00 00 00 00 BE 00 00 00 00 00 00 00 00 00
090: 00 00 C0 00 00 00 00 00 00 00 00 00 00 00 C7 00
0A0: 00 00 00 00 00 00 00 00 00 00 E1 00 00 00 00 00
0B0: 00 00 00 00 00 00 E2 00 00 00 00 00 00 00 00 00
0C0: 00 00 E3 00 00 00 00 00 00 00 00 00 00 00 E4 00
0D0: 00 00 00 00 00 00 00 00 00 00 E8 0A 00 00 00 00
0E0: 00 00 00 00 00 00 E9 00 00 00 00 00 00 00 00 00
0F0: 00 00 EC 00 00 00 00 00 00 00 00 00 00 00 F1 00
100: 00 00 00 00 00 00 00 00 00 00 F2 00 00 00 00 00
110: 00 00 00 00 00 00 F9 00 00 00 00 00 00 00 00 00
120: 00 00 FC 00 00 00 00 00 00 00 00 00 00 00 00 00
130: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
140: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
150: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
160: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
170: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
180: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
190: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1B0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 88

----------------------------------------------------------------------------
 (02) TOSHIBA HDWQ140
----------------------------------------------------------------------------
           Model : TOSHIBA HDWQ140
        Firmware : FJ1M
   Serial Number : 287FK1HNFPBE
       Disk Size : 4000.7 GB (8.4/137.4/4000.7/----)
     Buffer Size : Unknown
     Queue Depth : 32
    # of Sectors : 7814037168
   Rotation Rate : 7200 RPM
       Interface : Serial ATA
   Major Version : ATA8-ACS
   Minor Version : ----
   Transfer Mode : SATA/600 | SATA/600
  Power On Hours : 29789 hours
  Power On Count : 92 count
     Temperature : 44 C (111 F)
   Health Status : Bad
        Features : S.M.A.R.T., APM, NCQ
       APM Level : 0080h [ON]
       AAM Level : ----
    Drive Letter :

-- S.M.A.R.T. --------------------------------------------------------------
ID Cur Wor Thr RawValues(6) Attribute Name
01 100 100 _50 000000000000 Read Error Rate
02 100 100 _50 000000000000 Throughput Performance
03 100 100 __1 000000000CED Spin-Up Time

-- IDENTIFY_DEVICE ---------------------------------------------------------
        0    1    2    3    4    5    6    7    8    9
000: 0040 3FFF C837 0010 0000 0000 003F 0000 0000 0000
010: 2020 2020 2020 2020 3238 3746 4B31 484E 4650 4245
020: 0000 0000 0000 464A 314D 2020 2020 544F 5348 4942
030: 4120 4844 5751 3134 3020 2020 2020 2020 2020 2020
040: 2020 2020 2020 2020 2020 2020 2020 8010 0000 2F00
050: 4000 0200 0000 0007 3FFF 0010 003F FC10 00FB 0110
060: FFFF 0FFF 0007 0007 0003 0078 0078 0078 0078 0108
070: 0000 0000 0000 0000 0000 001F E70E 0006 004C 0044
080: 01F8 0000 746B 7D09 4163 7469 BC09 4163 203F 80F5
090: 80F5 0080 FFFE 0000 0000 0000 0000 0000 0000 0000
100: BEB0 D1C0 0001 0000 0000 0000 4000 0000 5000 0398
110: 5BE0 09AA 0000 0000 0000 0000 0000 0000 0000 409C
120: 401C 0000 0000 0000 0000 0000 0000 0000 0021 0000
130: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
140: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
150: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
160: 0000 0000 0000 0000 0000 0000 0000 0000 0002 0000
170: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
180: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
190: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
200: 0000 0000 0000 0000 0000 0000 003D 0000 0000 0000
210: 0000 0000 0000 0000 0000 0000 0000 1C20 0000 0000
220: 0000 0000 103F 0000 0000 0000 0000 0000 0000 0000
230: BEB0 D1C0 0001 0000 0001 1080 0000 0000 0000 0000
240: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
250: 0000 0000 0000 0000 0000 A0A5

-- SMART_READ_DATA ---------------------------------------------------------
     +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
000: 10 00 01 0B 00 64 64 00 00 00 00 00 00 00 02 05
010: 00 64 64 00 00 00 00 00 00 00 03 27 00 64 64 ED
020: 0C 00 00 00 00 00 04 32 00 64 64 5C 00 00 00 00
030: 00 00 05 33 00 64 64 00 00 00 00 00 00 00 07 0B
040: 00 64 64 00 00 00 00 00 00 00 08 05 00 64 64 00
050: 00 00 00 00 00 00 09 32 00 1A 1A 5D 74 00 00 00
060: 00 00 0A 33 00 65 64 00 00 00 00 00 00 00 0C 32
070: 00 64 64 5C 00 00 00 00 00 00 BF 32 00 64 64 F0
080: 03 00 00 00 00 00 C0 32 00 64 64 5A 00 00 00 00
090: 00 00 C1 32 00 64 64 5D 00 00 00 00 00 00 C2 22
0A0: 00 64 64 2C 00 0F 00 43 00 00 C4 32 00 64 64 00
0B0: 00 00 00 00 00 00 C5 32 00 64 64 00 00 00 00 00
0C0: 00 00 C6 30 00 64 64 00 00 00 00 00 00 00 C7 32
0D0: 00 C8 FD 00 00 00 00 00 00 00 DC 02 00 64 64 00
0E0: 00 00 00 00 00 00 DE 32 00 1A 1A 5D 74 00 00 00
0F0: 00 00 DF 32 00 64 64 00 00 00 00 00 00 00 E0 22
100: 00 64 64 00 00 00 00 00 00 00 E2 26 00 64 64 26
110: 02 00 00 00 00 00 F0 01 00 64 64 00 00 00 00 00
120: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
130: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
140: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
150: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
160: 00 00 00 00 00 00 00 00 00 00 82 00 78 00 00 5B
170: 03 00 01 00 02 FF 00 C3 01 00 00 00 00 00 00 00
180: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
190: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1B0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 89

-- SMART_READ_THRESHOLD ----------------------------------------------------
     +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
000: 10 00 01 32 00 00 00 00 00 00 00 00 00 00 02 32
010: 00 00 00 00 00 00 00 00 00 00 03 01 00 00 00 00
020: 00 00 00 00 00 00 04 00 00 00 00 00 00 00 00 00
030: 00 00 05 32 00 00 00 00 00 00 00 00 00 00 07 32
040: 00 00 00 00 00 00 00 00 00 00 08 32 00 00 00 00
050: 00 00 00 00 00 00 09 00 00 00 00 00 00 00 00 00
060: 00 00 0A 1E 00 00 00 00 00 00 00 00 00 00 0C 00
070: 00 00 00 00 00 00 00 00 00 00 BF 00 00 00 00 00
080: 00 00 00 00 00 00 C0 00 00 00 00 00 00 00 00 00
090: 00 00 C1 00 00 00 00 00 00 00 00 00 00 00 C2 00
0A0: 00 00 00 00 00 00 00 00 00 00 C4 00 00 00 00 00
0B0: 00 00 00 00 00 00 C5 00 00 00 00 00 00 00 00 00
0C0: 00 00 C6 00 00 00 00 00 00 00 00 00 00 00 C7 00
0D0: 00 00 00 00 00 00 00 00 00 00 DC 00 00 00 00 00
0E0: 00 00 00 00 00 00 DE 00 00 00 00 00 00 00 00 00
0F0: 00 00 DF 00 00 00 00 00 00 00 00 00 00 00 E0 00
100: 00 00 00 00 00 00 00 00 00 00 E2 00 00 00 00 00
110: 00 00 00 00 00 00 F0 01 00 00 00 00 00 00 00 00
120: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
130: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
140: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
150: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
160: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
170: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
180: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
190: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1B0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 36

----------------------------------------------------------------------------
 (03) Samsung SSD 980 PRO 1TB
----------------------------------------------------------------------------
           Model : Samsung SSD 980 PRO 1TB
        Firmware : 5B2QGXA7
   Serial Number : S5P2NG0NB05964V
       Disk Size : 1000.2 GB
     Buffer Size : Unknown
    # of Sectors :
   Rotation Rate : ---- (SSD)
       Interface : NVM Express
   Major Version : NVM Express 1.3
   Minor Version :
   Transfer Mode : PCIe 4.0 x4 | PCIe 4.0 x4
  Power On Hours : 3450 hours
  Power On Count : 663 count
      Host Reads : 72169 GB
     Host Writes : 126135 GB
     Temperature : 53 C (127 F)
   Health Status : Good (87 %)
        Features : S.M.A.R.T., TRIM, VolatileWriteCache
       APM Level : ----
       AAM Level : ----
    Drive Letter : C:

-- S.M.A.R.T. --------------------------------------------------------------
ID RawValues(6) Attribute Name
01 000000000000 Critical Warning
0A 000000004AC4 Controller Busy Time

-- IDENTIFY_DEVICE ---------------------------------------------------------
        0    1    2    3    4    5    6    7    8    9
000: 144D 144D 3553 3250 474E 4E30 3042 3935 3436 2056
010: 2020 2020 6153 736D 6E75 2067 5353 2044 3839 2030
020: 5250 204F 5431 2042 2020 2020 2020 2020 2020 2020
030: 2020 2020 4235 5132 5847 3741 3802 0025 0700 0006
040: 0300 0001 0D40 0003 9680 0098 0200 0000 0010 0000
050: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
060: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
070: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
080: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
090: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
100: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
110: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
120: 0000 0000 0000 0000 0000 0000 0000 0000 0017 0307
130: 0F16 043F 0101 0163 0166 0000 0000 0000 0000 0000
140: 6000 E0DB 00E8 0000 0000 0000 0000 0000 0000 0000
150: 0000 0000 0000 0000 0000 0000 0000 0000 0023 0000
160: 0000 0001 013E 0164 0003 0000 0000 0000 0000 0000
170: 0001 0000 0000 0000 0000 0000 0000 0000 0000 0000
180: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
190: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
200: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
210: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
220: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
230: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
240: 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
250: 0000 0000 0000 0000 0000 0000

-- SMART_NVME --------------------------------------------------------------
     +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
000: 00 46 01 64 0A 0D 00 00 00 00 00 00 00 00 00 00
010: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
020: A7 6D 05 09 00 00 00 00 00 00 00 00 00 00 00 00
030: A7 58 C4 0F 00 00 00 00 00 00 00 00 00 00 00 00
040: E9 BB DE 2C 01 00 00 00 00 00 00 00 00 00 00 00
050: 4A F1 7B D3 01 00 00 00 00 00 00 00 00 00 00 00
060: C4 4A 00 00 00 00 00 00 00 00 00 00 00 00 00 00
070: 97 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00
080: 7A 0D 00 00 00 00 00 00 00 00 00 00 00 00 00 00
090: 24 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0B0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0C0: 00 00 00 00 00 00 00 00 46 01 4D 01 00 00 00 00
0D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
100: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
110: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
120: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
130: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
140: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
150: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
160: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
170: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
180: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
190: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1B0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
"""


@pytest.fixture
def sample_output(tmp_path):
    p = pathlib.Path(tmp_path / "test.txt")
    p.write_text(SAMPLE_OUTPUT)
    yield p


def test_full_parsing(sample_output):
    disks = CrystalDiskInfo(None).get_disks(sample_output)
    assert len(disks) == 3

    assert disks[0] == Disk(
        model="INTEL SSDSC2KW256G8",
        firmware="LHF004C",
        serial="PHLA82310760256CGN",
        size="256.0 GB",
        health=DiskHealth(
            status="Good",
            smart=(
                DiskSMARTAttribute(
                    id=5,
                    name="Re-Allocated Sector Count",
                    current=100,
                    worst=100,
                    threshold=0,
                    raw=0,
                ),
                DiskSMARTAttribute(
                    id=9,
                    name="Power-On Hours Count",
                    current=100,
                    worst=100,
                    threshold=0,
                    raw=0x1EB8,
                ),
            ),
            percent=64,
        ),
        raw={
            "Model": "INTEL SSDSC2KW256G8",
            "Firmware": "LHF004C",
            "Serial Number": "PHLA82310760256CGN",
            "Disk Size": "256.0 GB (8.4/137.4/256.0/----)",
            "Buffer Size": "Unknown",
            "Queue Depth": "32",
            "# of Sectors": "500118192",
            "Rotation Rate": "---- (SSD)",
            "Interface": "Serial ATA",
            "Major Version": "ACS-3",
            "Minor Version": "----",
            "Transfer Mode": "SATA/600 | SATA/600",
            "Power On Hours": "7864 hours",
            "Power On Count": "173 count",
            "Host Reads": "71798 GB",
            "Host Writes": "64203 GB",
            "NAND Writes": "78313 GB",
            "Temperature": "33 C (91 F)",
            "Health Status": "Good (64 %)",
            "Features": "S.M.A.R.T., APM, NCQ, TRIM, DevSleep",
            "APM Level": "00FEh [ON]",
            "AAM Level": "----",
            "Drive Letter": "",
        },
    )

    assert disks[1] == Disk(
        model="TOSHIBA HDWQ140",
        firmware="FJ1M",
        serial="287FK1HNFPBE",
        size="4000.7 GB",
        health=DiskHealth(
            status="Bad",
            smart=(
                DiskSMARTAttribute(
                    id=1,
                    name="Read Error Rate",
                    current=100,
                    worst=100,
                    threshold=50,
                    raw=0,
                ),
                DiskSMARTAttribute(
                    id=2,
                    name="Throughput Performance",
                    current=100,
                    worst=100,
                    threshold=50,
                    raw=0,
                ),
                DiskSMARTAttribute(
                    id=3,
                    name="Spin-Up Time",
                    current=100,
                    worst=100,
                    threshold=1,
                    raw=0xCED,
                ),
            ),
            percent=None,
        ),
        raw={
            "Model": "TOSHIBA HDWQ140",
            "Firmware": "FJ1M",
            "Serial Number": "287FK1HNFPBE",
            "Disk Size": "4000.7 GB (8.4/137.4/4000.7/----)",
            "Buffer Size": "Unknown",
            "Queue Depth": "32",
            "# of Sectors": "7814037168",
            "Rotation Rate": "7200 RPM",
            "Interface": "Serial ATA",
            "Major Version": "ATA8-ACS",
            "Minor Version": "----",
            "Transfer Mode": "SATA/600 | SATA/600",
            "Power On Hours": "29789 hours",
            "Power On Count": "92 count",
            "Temperature": "44 C (111 F)",
            "Health Status": "Bad",
            "Features": "S.M.A.R.T., APM, NCQ",
            "APM Level": "0080h [ON]",
            "AAM Level": "----",
            "Drive Letter": "",
        },
    )

    assert disks[2] == Disk(
        model="Samsung SSD 980 PRO 1TB",
        firmware="5B2QGXA7",
        serial="S5P2NG0NB05964V",
        size="1000.2 GB",
        health=DiskHealth(
            status="Good",
            smart=(
                DiskSMARTAttribute(id=1, name="Critical Warning", raw=0),
                DiskSMARTAttribute(id=0x0A, name="Controller Busy Time", raw=0x4AC4),
            ),
            percent=87,
        ),
        raw={
            "Model": "Samsung SSD 980 PRO 1TB",
            "Firmware": "5B2QGXA7",
            "Serial Number": "S5P2NG0NB05964V",
            "Disk Size": "1000.2 GB",
            "Buffer Size": "Unknown",
            "# of Sectors": "",
            "Rotation Rate": "---- (SSD)",
            "Interface": "NVM Express",
            "Major Version": "NVM Express 1.3",
            "Minor Version": "",
            "Transfer Mode": "PCIe 4.0 x4 | PCIe 4.0 x4",
            "Power On Hours": "3450 hours",
            "Power On Count": "663 count",
            "Host Reads": "72169 GB",
            "Host Writes": "126135 GB",
            "Temperature": "53 C (127 F)",
            "Health Status": "Good (87 %)",
            "Features": "S.M.A.R.T., TRIM, VolatileWriteCache",
            "APM Level": "----",
            "AAM Level": "----",
            "Drive Letter": "C:",
        },
    )
