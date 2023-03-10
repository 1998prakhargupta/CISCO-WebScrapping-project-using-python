import requests

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

params = (
    ('sn', 'FGL191326F1'),
    ('ccoId', 'vpodelhi18733'),
    ('loggedId', 'vpodelhi18733'),
    ('requestType', 'FMP'),
    ('rtobFlag', 'N'),
    ('rtobAuditId', ''),
    ('endCustGuId', ''),
    ('billToGuId', ''),
)

response = requests.post('https://mycase.cloudapps.cisco.com/ws/entitlement/searchBySerial', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://mycase.cloudapps.cisco.com/ws/entitlement/searchBySerial?sn=FGL191326F1&ccoId=vpodelhi18733&loggedId=vpodelhi18733&requestType=FMP&rtobFlag=N&rtobAuditId=&endCustGuId=&billToGuId=', headers=headers, cookies=cookies)

