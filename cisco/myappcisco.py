import requests
import json
from crawlmethods import get_content, get_elem, get_tag, dbinsert
import time

cookies = {
    'AMCV_B8D07FF4520E94C10A490D4C%40AdobeOrg': '281789898%7CMCIDTS%7C18490%7CMCMID%7C69135834459860787296271574525442906565%7CMCOPTOUT-1597480543s%7CNONE%7CMCAID%7CNONE%7CMCAAMLH-1598078143%7C9%7CMCAAMB-1598078143%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C4.1.0%7CMCCIDH%7C1889524496',
    'anchorvalue': '',
    'AMCVS_B8D07FF4520E94C10A490D4C%40AdobeOrg': '1',
    'discovery': 'T1RLAQIBNn1BX4qiOy1d-cbwsyH9si7ClBA350yn-7BBt3oUFRBR23D6AACguHAmifJEPrkwbk1FblW-w4HM1BUXjZApTKZBwtpvHAfQSlcmTYvnxnTLD6RHLioSFaXyt-u8vE9SOtX_aMVmPA3qO-7Ssq09tsxtwa1KqE82nOYHyYKb96IgQk7K6puFj17Jfwq91DVo8JJXWxxq-t1zKseLwsZU8C4q3IiBFJmZPBysJbk7xf9YSGJ70LyXVHBucDuVOQ9qvVi91xM41Q**',
    'oneid_locale': 'en-US',
    'ADRUM': 's=1597473259891&r=https%3A%2F%2Fidentity.cisco.com%2Fapi%2Ftenants%2Fglobal%2Fv1%2Fam%2Flogin-actions%2Fauthenticate%3F1246605657',
    'authorization': 'Customer',
    'wamsessiontracker': 'T1RLAQJE6NglayeWzyNT1PYa9y2dBy617RDgLZQevk5wSuWVnCrE9m4HAACAfzSQsdb6-tOv8U2J12eB2cqpRpocYW0MZxy2s1VdD4C_yOuwwejzkjErd2tomTlfuxDArzyXJK3HKkJzwksCtRCD7nvSjr1mCLMFQfCyhsHpT0JSGAiUoH3Q4goj6W0g_D9A6rVXplrql78vIf2FpA4NN7SebMaSVc8QLq8GGsc*',
    'CSPROD.CAEAXprod': 'eyJraWQiOiI2MSIsImFsZyI6IkVTMjU2IiwicGkuc3JpIjoidVdtVHprUEVSV3FXT2ltTVVsRXJobW5pa0NZLi5ONEhFIn0.eyJzdWIiOiJWUE9EZWxoaTE4NzMzIiwiaWF0IjoxNTk3NDczMjYzLCJpc3MiOiJjaXNjbyIsImF1ZCI6IkNBRUFYcHJvZCIsImp0aSI6Ijc1NzIzMWVmLWUyZmEtNDU2MC1hMDcyLTY1MjhmNDkzYmE4OCIsImV4cCI6MTU5NzUwOTM0NCwicGkucGEucmF0IjoxNTk3NDczMzQ0LCJhY2Nlc3NfdG9rZW4iOiJmMlVoZVVUTHNCNjV4dUJmbGdPM3hMU1M5eXlhIiwiYWNyIjoic3Rkbm9tZmEiLCJwaS5wYS5hdHRyX2V4cCI6MTU5NzQ3NDE4NH0.pG9VLPfEma8BtfaAY_AG-7_IFd49NX9e23GWHYk0M4E1a0wmNef1BKoeHLSnbmvxdk_CmXdduO6Y4xkhS50zJQ',
    'CP_GUTC': '173.37.145.91.1597473263647206',
    '549aac268da384d494efe4a5ec046dfe': '0f3946ae05d258995cab3b25af6dbe06',
    'utag_main': 'v_id:0173f0d3b51c0020742b68b9f2f80004c002f00900bd0$_sn:1$_ss:0$_st:1597475177023$ses_id:1597473273118%3Bexp-session$_pn:3%3Bexp-session$consent_prompt:true$ctm_ss:true%3Bexp-session$vapi_domain:cisco.com',
    'JSESSIONID': 'mfl+I2Dl3smcveLPQ8FwmUGb',
    '53886bbadd566ca69c3078ef3c2ff618': 'ca0e602804c8de8c8077a1beca4742ad',
    'CONSENTMGR': 'ts:1597473282511%7Cconsent:true',
    '_gcl_au': '1.1.1590325442.1597473283',
    'cdcSsoTimer': 'LoggedIn',
    'cdcUniqueKey': 'b26907aba1j8',
    'check': 'true',
    'mbox': 'session#b32a7dd937d142bd83ca311937cbca60#1597475199|PC#b32a7dd937d142bd83ca311937cbca60.35_0#1660718139',
    '_cs_mk': '0.9769616942442433_1597473341550',
    'gpv_v9': 'cisco.com',
    's_ptc': '%5B%5BB%5D%5D',
    's_cc': 'true',
    's_ppvl': '%5B%5BB%5D%5D',
    's_ppv': 'cisco.com%2C30%2C30%2C913%2C1850%2C913%2C1920%2C1080%2C1%2CP',
    '_evga_7055': '{%22uuid%22:%2259c4678461652958%22%2C%22puid%22:%22x6aEqK4uGxdkMULQ6jFAZ_H3Xi7KlAR0eWrRrD3VqdLP19mLCNUrF2VBAZYnSHjv%22}',
    'aam_uuid': '62285877985115774806811839387164328004',
    '_cs_c': '0',
    '_fbp': 'fb.1.1597473343165.1176736410',
    'ctm': '{\'pgv\':1161484377922082|\'vst\':4507823957643268|\'vstr\':1176767490879763|\'intr\':1597473343372|\'v\':1}',
    '__CT_Data': 'gpv=1&ckp=tld&dm=cisco.com',
    '_cs_cvars': '%7B%222%22%3A%5B%22Template%20Name%22%2C%22responsive_homepage%22%5D%2C%223%22%3A%5B%22Title%22%2C%22cisco%20-%20global%20home%20page%22%5D%2C%224%22%3A%5B%22Page%20Channel%22%2C%22home%20pages%2F%22%5D%2C%225%22%3A%5B%22Page%20Name%22%2C%22cisco.com%22%5D%2C%226%22%3A%5B%22Content%20Type%22%2C%22presales%22%5D%7D',
    '_ga': 'GA1.2.1992182000.1597473344',
    '_gid': 'GA1.2.507756555.1597473344',
    '_gat_gtag_UA_584538_1': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'CSRFTOKEN': 'bfa8d912-78a9-43aa-88d5-a21f560a0511',
    'TAB_ID': '1597473282077',
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json; charset=UTF-8',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT',
    'ADRUM': 'isAjax:true',
    'Origin': 'https://mycase.cloudapps.cisco.com',
    'Connection': 'keep-alive',
    'Referer': 'https://mycase.cloudapps.cisco.com/create/start',
    'TE': 'Trailers',
}


serial_numbers = ['1921-SINABB-AMDP ## FGL191326F1',
'1921-SINABB-AMDP01 ## FGL212894J4',
'1921-SINABB-ASE01 ## FGL191326F3',
'1921-SINABB-ASE02 ## FGL212894J2',
'1921-SINABB-ASEKH ## FGL1912226B',
'1921-SINABB-ASEKH02 ## FGL1912226A',
'1921-SINABB-ASEM ## FGL191326F4',
'1921-SINABB-ASEM02 ## FGL212894J1',
'1921-SINABB-INARI ## FGL191326F2',
'1921-SINABB-INARI02 ## FGL212894J3',
'4451-SINABB-H01 ## FJC2019D0S1',
'4451-SINABB-H02 ## FJC2021D18Z',
'acc-wan-bdr1 ## FXS2342Q055',
'acc-wan-bdr2 ## FXS2338Q01E',
'acc-wan-sr1 ## FXS2345Q0LM',
'acc-wan-sr2 ## FXS2345Q0LY',
'AMB-WAN-SR1 ## FJC2025D0FS',
'AMB-WAN-SR2 ## FTX1540AJ1U',
'amk-wan-sr1 ## FDO2331M43M',
'and-wan-sr1 ## FJC2021D0B9',
'and-wan-sr2 ## FJC2022D0MV',
'anr-wan-bdr1 ## FOX2004G7NF',
'anr-wan-sr1 ## FGL202110M1',
'anr-wan-sr2 ## FGL202110L6',
'apt-wan-sr1 ## FJC2024D0N2',
'apt-wan-sr2 ## FJC2024D0ND',
'ard-wan-sr1 ## FDO2331M43W',
'ash-wan-bdr1 ## FXS2049Q1L4',
'ash-wan-bdr2 ## FXS2034Q4AA',
'ash-wan-br1 ## FTX1923AHUH',
'ash-wan-eavbr1 ## FJC2022D0N0',
'ash-wan-sr2 ## FXS2145Q2FB',
'ash-wan-sr3 ## FXS2145Q2FE',
'ath-wan-sr1 ## FJC2205D12G',
'ath-wan-sr2 ## FJC2024D0NC',
'atl-wan-sr1 ## FJC2021D0EX',
'atl-wan-sr2 ## FJC2022D08Q',
'auf-wan-sr1 ## FJC2021D0FK',
'auf-wan-sr2 ## FJC2021D0P4',
'avn-wan-sr1 ## FCZ2318702G',
'avn-wan-sr2 ## FCZ2318701V',
'BEC-WAN-BDR1 ## FGL213581DV',
'BEC-WAN-SR1 ## FXS2132Q00J',
'BEC-WAN-SR2 ## FXS2132Q013',
'bes-wan-sr1 ## FXS1943Q0HU',
'bes-wan-sr2 ## FXS2339Q1TB',
'BGV-WAN-SR1 ## FJC2204D179',
'BGV-WAN-SR2 ## FJC2104D0RN',
'bji-wan-sr1 ## FGL2249307A',
'bji-wan-sr2 ## FGL20361265',
'bpl-wan-sr1 ## FJC2024D0N5',
'bpl-wan-sr2 ## FJC2205D17Y',
'bra-wan-sr1 ## FJC2205D12F',
'bra-wan-sr2 ## FJC2205D0TU',
'bri-wan-sr1 ## FJC2025D04M',
'bri-wan-sr2 ## FTX1802AJG1',
'brm-wan-sr1 ## FJC2021D0FT',
'brm-wan-sr2 ## FJC2019D0Q1',
'Broadcom ME Primary connex @BIAD670 ## SSI1635048Q',
'bso-wan-sr1 ## FJC2205D0U0',
'bso-wan-sr2 ## FJC2205D17Z',
'bsp-wan-sr1 ## FJC2039D0B4',
'bsp-wan-sr2 ## FJC2039D0B3',
'btk-wan-sr1 ## FJC2021D10U',
'btk-wan-sr2 ## FJC2022D06X',
'btk-wan-sr3 ## FGL164111KK',
'bun-wan-sr1 ## FJC2024D0JT',
'bun-wan-sr2 ## FJC2024D0HL',
'bva-wan-sr1 ## FCZ23077052',
'bva-wan-sr2 ## FCZ2307800J',
'cam-wan-sr1 ## FJC2024D0LM',
'cam-wan-sr2 ## FTX1605AKBQ',
'chn-wan-sr1 ## FGL175010PL',
'chs-wan-bdr1 ## FJC2025D05Y',
'chs-wan-bdr2 ## FJC2025D042',
'chs-wan-sr1 ## FXS2003Q4B8',
'chs-wan-sr2 ## FXS2003Q43D',
'cos-wan-bdr1 ## FJC2128D0QF',
'cos-wan-sr1 ## FJC2019D0N7',
'cos-wan-sr2 ## FJC2019D0NG',
'cpr-wan-sr1 ## FCZ23178073',
'cpr-wan-sr2 ## FGL194510YN',
'csj-wan-sr2 ## FJC2346A0P9',
'CVC-WAN-SR1 ## FJC2404A068',
'CVC-WAN-SR2 ## FJC2404A05Q',
'DCW-WAN-SR1 ## FJC2120D0F5',
'edn-wan-sr1 ## FTX1446AJUE',
'edn-wan-sr2 ## FTX1511AH92',
'est-wan-sr2 ## FCZ2403M056',
'frk-wan-bdr1 ## FXS2342Q036',
'frk-wan-bdr2 ## FXS2342Q034',
'frk-wan-sr1 ## FXS2345Q0MS',
'frk-wan-sr2 ## FXS2345Q0MN',
'frp-wan-sr1 ## FCZ2311400B',
'frp-wan-sr2 ## FGL212780VG',
'ftc-wan-bdr1 ## FJC2019D0NJ',
'ftc-wan-bdr2 ## FJC2019D0M7',
'ftc-wan-sr1 ## SSI182106N0',
'ftc-wan-sr2 ## SSI182200CZ',
'gen-wan-sr1 ## FJC2026D0HP',
'gen-wan-sr2 ## FJC2206D04R',
'GRD-WAN-SR2 ## FCZ23118028',
'hsi-wan-bdr1 ## FTX1729AMDN',
'hsi-wan-sr1 ## FJC2024D0JS',
'hsi-wan-sr2 ## FJC2024D0HR',
'ibn-wan-bdr1 ## FJC2019D02P',
'ibn-wan-bdr2 ## FJC2019D02N',
'IBN-WAN-BPR1 ## FGL1808120W',
'ibn-wan-br1 ## FJC1935D0YD',
'ibn-wan-eavbr01 ## FDO1919A09D',
'ibn-wan-sr1 ## FXS2228Q1DD',
'ibn-wan-sr2 ## FXS2207Q011',
'IGP-WAN-BDR1 ## FJC2128D0QE',
'IGP-WAN-SR1 ## FXS2114Q0T6',
'IGP-WAN-SR2 ## FXS2111Q33R',
'ihl-temp-sr2 ## FXS2003Q43F',
'ihl-wan-bdr1 ## FXS2411Q423',
'ihl-wan-bdr2 ## FXS2411Q41C',
'ihy-wan-bdr1 ## FXS1704Q34K',
'ihy-wan-sr1 ## FOX1844GJ4Z',
'ihy-wan-sr2 ## FOX1834GQ2X',
'ils-wan-sr1 ## FJC2018D0YX',
'ils-wan-sr2 ## FJC2015A0X6',
'INP-WAN-BDR1 ## FGL2351LBSD',
'inp-wan-sr1 ## FGL2351LBLS',
'inp-wan-sr2 ## FGL2351LCY7',
'ird-wan-redlabr1 ## FCZ2411M0B7',
'isr4451-irvbb-01 ## FJC2213A0WN',
'ist-wan-sr1 ## FJC2205D0WC',
'ist-wan-sr2 ## FJC2205D0TE',
'ITM-WAN-SR1 ## FCZ23104050',
'itr-wan-sr1 ## FCZ2310403V',
'itr-wan-sr2 ## FCZ2310802Q',
'jmn-wan-sr1 ## FGL2409LHWF',
'jsi-wan-sr1 ## FGL191523A4',
'kye-wan-sr1 ## FDO2331M446',
'lan-wan-sr1 ## FJC2019D0N1',
'lan-wan-sr2 ## FJC2104D0EF',
'lgh-wan-sr1 ## FGL2226806W',
'lvn-wan-bdr1 ## FXS2103Q0GF',
'lvn-wan-bdr2 ## FXS2103Q0GP',
'lvn-wan-br1 ## FXS1950Q32H',
'lvn-wan-eavbr01 ## FJC2019D0FF',
'lvn-wan-eavbr02 ## FJC2019D0FG',
'LVN-WAN-GCPSR1 ## TTM22010530',
'lvn-wan-sr2 ## FXS2145Q2FD',
'lvn-wan-sr3 ## FXS2145Q2FF',
'lvn-wan-vr1 ## FTX1836AKHE',
'MAB-WAN-SR1 ## FJC2005D0NZ',
'MAB-WAN-SR2 ## FJC2018D07Q',
'man-wan-sr1 ## FJC2026D0HQ',
'man-wan-sr2 ## FJC2025D0NV',
'mcl-wan-bdr1 ## FJC2022D0CL',
'mcl-wan-bdr2 ## FJC2022D0CK',
'mcl-wan-br1 ## FJC2022D0CU',
'mcl-wan-sr1 ## FXS1949Q3D6',
'mcl-wan-sr2 ## FXS1952Q1VL',
'mec-wan-sr1 ## FJC2026D02R',
'mec-wan-sr2 ## FJC2025D0FR',
'mho-wan-sr1 ## FGL2403LPLN',
'mic-wan-sr1 ## FDO2412M0BH',
'mic-wan-sr2 ## FDO2412M0BF',
'mit-wan-1fmdf-sr1 ## FDO2132A1UC',
'mnm-wan-sr1 ## FJC2019D0NC',
'mnm-wan-sr2 ## FJC2019D0NR',
'mun-wan-sr1 ## FJC2025D10Z',
'mun-wan-sr2 ## FJC2022D0MN',
'mvj-wan-1fmdf-sr1 ## FDO2132A1TR',
'nan-wan-sr1 ## FGL225030DN',
'nan-wan-sr2 ## FGL184210RS',
'ncc-wan-sr1 ## FJC1935D12A',
'ncc-wan-sr2 ## FJC2019D0NT',
'NHP-WAN-SR1 ## FJC2018D0BR',
'NHP-WAN-SR2 ## FJC2019D021',
'nje-wan-sr1 ## FJC2018D11Q',
'nje-wan-sr2 ## FJC2015D0UT',
'NLU-WAN-SR2 ## FGL210111G6',
'nni-wan-sr1 ## FGL221880UA',
'nni-wan-sr2 ## FGL221880U7',
'nym-wan-sr1 ## FJC2336A01N',
'nym-wan-sr2 ## FJC2335A0UT',
'nzr-wan-sr1 ## FJC2205D0WJ',
'nzr-wan-sr2 ## FJC2205D0TA',
'omc-wan-sr1 ## FTX1617AHWL',
'omc-wan-sr2 ## FGL172812Q5',
'opi-wan-sr1 ## FGL2404L6GP',
'ose-wan-sr1 ## FGL2411LAZG',
'pal-wan-sr1 ## FJC2019D0NF',
'pal-wan-sr2 ## FJC2202D1F5',
'par-wan-sr1 ## FJC2216A03S',
'par-wan-sr2 ## FJC2219A09H',
'pcf-wan-sr1 ## FDO2131A0JN',
'pet-wan-sr1 ## FJC2021D0H4',
'pet-wan-sr2 ## FJC2022D08M',
'phx-wan-sr1 ## FJC2021D0FW',
'phx-wan-sr2 ## FJC2022D0SH',
'pit-wan-sr1 ## FTX1906AH44',
'pit-wan-sr2 ## FTX1906AH43',
'PNG-WAN-BDR1 ## FJC2022D08P',
'PNG-WAN-BDR2 ## FJC2022D06W',
'png-wan-inarip13bpr1 ## FGL210610FN',
'png-wan-inarip3bpr1 ## FGL21081104',
'png-wan-sr1 ## FXS1951Q186',
'png-wan-sr2 ## FXS1949Q3E0',
'pti-wan-sr1 ## FDO2331M442',
'pwa-wan-sr1 ## FCZ2404M0FK',
'pwa-wan-sr2 ## FCZ2404M0FJ',
'ren-wan-bdr1 ## FXS2222Q2XT',
'ren-wan-bdr2 ## FXS2330Q2EL',
'ren-wan-sr1 ## FXS2237Q191',
'ren-wan-sr2 ## FXS2237Q19R',
'rgb-wan-sr1 ## FJC2205D12H',
'rgb-wan-sr2 ## FJC2205D0TR',
'ric-wan-sr1 ## FJC2021D0FL',
'ric-wan-sr2 ## FJC2022D0ML',
'rtp-wan-sr1 ## FJC2021D0H2',
'rtp-wan-sr2 ## FJC2022D08L',
'sak-wan-sr1 ## FGL2402L49N',
'sco-wan-sr1 ## FCZ2311802H',
'sco-wan-sr2 ## FCZ2311802B',
'sdg-wan-sr1 ## FJC2021D0FV',
'sdg-wan-sr2 ## FJC2022D09T',
'SDJ-WAN-SR1 ## FGL221780J6',
'SDJ-WAN-SR2 ## FGL1713120B',
'sel-wan-bdr1 ## FGL163813LP',
'sel-wan-sr1 ## FOX1719H7LH',
'sel-wan-sr2 ## FOX1622GQZ2',
'sen-wan-bdr1 ## FJC2022D06V',
'sen-wan-bdr2 ## FJC2020D0TS',
'sen-wan-sr1 ## FXS1952Q239',
'sen-wan-sr2 ## FXS1848Q15A',
'SFR-WAN-SR1 ## FJC2404A052',
'SFR-WAN-SR2 ## FJC2404A02Y',
'sft-wan-sr1 ## FJC2347A0SK',
'sft-wan-sr2 ## FJC2347A0W4',
'sgd-wan-sr1 ## FJC2205D0WE',
'sgd-wan-sr2 ## FJC2205D13X',
'sgn-wan-bbeavbr1 ## FJC2021D0WE',
'sgn-wan-bdr1 ## FXS1952Q1XF',
'sgn-wan-bdr2 ## FXS1941Q13U',
'sgn-wan-bdr3 ## SSI182106NX',
'sgn-wan-eavbr1 ## FJC2022D06Z',
'sgn-wan-sr1 ## FXS2110Q4V7',
'sgn-wan-sr2 ## FXS2110Q4UF',
'sgs-wan-sr1 ## FJC2205D0WG',
'sgs-wan-sr2 ## FJC2205D0TD',
'sha-wan-bdr1 ## FGL202710PS',
'sha-wan-bdr2 ## FGL202710PT',
'sha-wan-eavbr1 ## FOX1615G78D',
'sha-wan-sr1 ## FOX1930G81H',
'sha-wan-sr2 ## FOX1735GPL8',
'she-wan-sr1 ## FGL225030V0',
'she-wan-sr2 ## FGL221280JF',
'sjf-wan-sr1 ## FJC2215A0Y2',
'SJI-WAN-BDR1 ## FJC2128D0T8',
'SJI-WAN-SR1 ## FXS2113Q2UL',
'SJI-WAN-SR2 ## FXS2115Q14S',
'sjs-wan-bdr1 ## FJC2019D0FB',
'sjs-wan-bdr2 ## FJC2019D0FC',
'sjs-wan-sr1 ## FXS1948Q0JS',
'sjs-wan-sr2 ## FXS1948Q0J4',
'SJU-WAN-SR1 ## FJC2404A05T',
'SJU-WAN-SR2 ## FJC2404A030',
'slk-wan-sr1 ## FJC2206D0P9',
'slk-wan-sr2 ## FJC2206D0D2',
'sma-wan-sr1 ## FJC2024D0JW',
'sma-wan-sr2 ## FJC2205D0TQ',
'soh-wan-sr1 ## FGL192211WJ',
'spi-wan-sr1 ## FDO2331M43Z',
'spr-wan-sr1 ## FJC2205D0WB',
'spr-wan-sr2 ## FJC2205D0TG',
'SUO-WAN-SR1 ## FGL2409LHWL',
'swm-wan-sr1 ## FCZ2316702T',
'swm-wan-sr2 ## FCZ23168021',
'tai-wan-sr1 ## FJC2024D0JU',
'tai-wan-sr2 ## FGL220880P8',
'tdo-wan-sr2 ## FJC2215A0Y1',
'ths-wan-1fmdf-sr1 ## FDO2129A1MM',
'tky-wan-bdr1 ## FXS2347Q0YS',
'tky-wan-bdr2 ## FXS2347Q0YC',
'tky-wan-eavbr1 ## FJC2408D06L',
'tky-wan-sr1 ## FXS2347Q0Z4',
'tky-wan-sr2 ## FXS2347Q0Z0',
'tla-wan-sr1 ## FJC2404A0EP',
'tla-wan-sr2 ## FJC2109D0G9',
'tlv-wan-sr1 ## FJC2205D0WF',
'tlv-wan-sr2 ## FJC2205D0TB',
'tok-wan-sr1 ## FJC2206D0NV',
'tok-wan-sr2 ## FJC2206D0KL',
'TXP-WAN-SR1 ## FJC2018D0UK',
'TXP-WAN-SR2 ## FJC2018D0US',
'usilgr48 ## SSI17080BPH',
'usilgr49 ## SSI17080BM1',
'utd-wan-bdr1 ## FJC2404A02Z',
'utd-wan-sr1 ## FJC2404A05S',
'utd-wan-sr2 ## FJC2404A05R',
'VAH-WAN-SR1 ## FJC2125D0LW',
'VAH-WAN-SR2 ## FJC2022D08R',
'vic-wan-sr1 ## FJC2206D0MM',
'vic-wan-sr2 ## FJC2206D0CT',
'vnh-wan-sr1 ## FGL233031WM',
'vnh-wan-sr2 ## FGL2329303X',
'WAC-WAN-SR1 ## FJC2404A062',
'WAC-WAN-SR2 ## FJC2404A032',
'wat-wan-bdr1 ## FXS2346Q0X5',
'wat-wan-bdr2 ## FXS2346Q0XG',
'wat-wan-sr1 ## FXS2345Q0LH',
'wat-wan-sr2 ## FXS2345Q0LL',
'wux-wan-bpr1 ## FHK093520VJ',
'yak-wan-sr1 ## FJC2205D0WH',
'yak-wan-sr2 ## FJC2205D0TC',
'yis-wan-sr1 ## SSI182204VE',
'yis-wan-sr2 ## FJC2205D0TJ',
'zsh-wan-sr1 ## FGL2409LHWH',
]
for s in serial_numbers:
    time.sleep(0.2)
    x = s.split("##")
    router = x[0].strip()
    sn = x[1].strip()
    print (router, '-->', sn)
    #fieldnames  = [ "serial_number",]
    #fieldvalues = (  s,  )
    #dbinsert(dbname='cisco', tablename='serial_numbers',fieldnames =fieldnames, fieldvalues=fieldvalues)
    params = (
        ('sn', sn),
        ('ccoId', 'vpodelhi18733'),
        ('loggedId', 'vpodelhi18733'),
        ('requestType', 'FMP'),
        ('rtobFlag', 'N'),
        ('rtobAuditId', ''),
        ('endCustGuId', ''),
        ('billToGuId', ''),
    )
    response = requests.post('https://mycase.cloudapps.cisco.com/ws/entitlement/searchBySerial', headers=headers, params=params, cookies=cookies)
    result = json.loads(response.text)
    print (result)
##    fieldnames  = [ "serial_number", "router", "result"]
##    fieldvalues = (  sn,   router, json.dumps(result) )
##    dbinsert(dbname='cisco', tablename='serial_numbers',fieldnames =fieldnames, fieldvalues=fieldvalues)
                    
#
#print (response.text)

# https://mycase.cloudapps.cisco.com/create/start
# UserName : vpo.delhi@orange.com
# Password: Cisco123
