task: https://eip4dev.lntecc.com/EIPSCMUI/SOPUI/Warehouse/MaterialIssue
      https://eip4bfix.lntecc.com/EIPSCMUI/SOPUI/indent-request/indentReq

--------------------------------------------------------------------------------------------------
Username & Password
--------------------------------------------------------------------------------------------------

(dev)
1. username - mmurali
2. Password - Phnx@2019

(bfix)
1. Username - mmurali
2. Password - E210a#04P1e&bfix


--------------------------------------------------------------------------------------------------
FROM SCRATCH
--------------------------------------------------------------------------------------------------
1: https://eip4dev.lntecc.com/eiproot/login
2: Press other User.
3: username - mmurali  , password - Phnx@2019
4: Press login.
5: Press Search Bar.
6: search Material Issue Request
7: Click it
8: Create New indent


--------------------------------------------------------------------------------------------------
SHORTCUT  -  scratch
--------------------------------------------------------------------------------------------------
1: https://eip4bfix.lntecc.com/EIPSCMUI/SOPUI/indent-request/indentReq
2: Click other User. (By.XPATH,'/html/body/app-root/div/div[2]/app-login/div/form/div/div/div[1]/div/div[2]/div[1]/div/div[1]/ul/li[2]/a')
3: Click on the Username bar.  (By.XPATH, '//*[@id="username"]')         username - mmurali  
4: Click on the Password bar.  (By.XPATH, '//*[@id="password-field"]')   password - Phnx@2019
5: Click the login button.     (By.XPATH, '//*[@id="login-submit"]')
6: Click Create new indent button.(By.XPATH,'//*[@id="ibtINDADD"')
7: Click warehouse. (By.XPATH, '//*[@id="ActxtboxINDCWarehouse"]')
8. Click option. (By.XPATH, '//*[@id="mat-option-26"]/span/span')


--------------------------------------------------------------------------------------------------
LOCAL HOST - starting_local.py
--------------------------------------------------------------------------------------------------
1: Run EIProot (npm start)
2: Run SOPUI (npm start)
3: http://localhost:4200/indent-request/indentReq
4: Click other User. (By.XPATH,'/html/body/app-root/div/div[2]/app-login/div/form/div/div/div[1]/div/div[2]/div[1]/div/div[1]/ul/li[2]/a')
5: Click on the Username bar.  (By.XPATH, '//*[@id="username"]')
6: Click on the Password bar.  (By.XPATH, '//*[@id="password-field"]')
7: Click the login button.     (By.XPATH, '//*[@id="login-submit"]')
8: Click Create new indent button.(By.XPATH,'//*[@id="ibtINDADD"')  
9: Press job bar, add input and click the arrow button.
10: Press Warehouse bar and add input, click the arrow button.




