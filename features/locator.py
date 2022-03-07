class locator(object):

#Top Menu
    signin                          = "//a[@class='login']"

#Authentication
    email_create                    = "//input[@name='email_create']"
    SubmitCreate                    = "//button[@name='SubmitCreate']"

#Registration Form
    gender_mr                       = "//input[@id='id_gender1']"
    customer_firstname              = "//input[@name='customer_firstname']"
    customer_lastname               = "//input[@name='customer_lastname']"
    password                        = "//input[@name='passwd']"
    days_dob                        = "//select[@name='days']"
    months_dob                      = "//select[@name='months']"
    years_dob                       = "//select[@name='years']"
    firstname                       = "//input[@name='firstname']"
    lastname                        = "//input[@name='lastname']"
    company                         = "//input[@name='company']"
    address                         = "//input[@name='address1']"
    city                            = "//input[@name='city']"
    state                           = "//select[@name='id_state']"
    postcode                        = "//input[@name='postcode']"
    other_info                      = "//textarea[@name='other']"
    phone                           = "//input[@name='phone']"
    mobile                          = "//input[@name='phone_mobile']"
    alias                           = "//input[@name='alias']"
    register_button                 = "//span[contains(.,'Register')]"

    signout_button                  = "//a[@class='logout']"

    email_signin                    = "//input[@name='email']"
    password_signin                 = "//input[@name='passwd']"
    signin_button                   = "//button[@name='SubmitLogin']"

#My Account
    page_heading                    = "//h1[@class='page-heading']"
    info_account                    = "//p[@class='info-account']"
