from PIL import ImageTk, Image
def BImage():
    #Balance Logo
    bl_logo = Image.open('img/balance.png')
    bl_logo = bl_logo.resize((25,25), Image.Resampling.LANCZOS)
    balance_img = ImageTk.PhotoImage(bl_logo)
    return balance_img
def DImage():
    #Deposit Logo
    dep_logo = Image.open('img/deposit.png')
    dep_logo = dep_logo.resize((25,25), Image.Resampling.LANCZOS)
    deposit_img = ImageTk.PhotoImage(dep_logo)
    return deposit_img
def WImage():
     #Withdraw Logo
    wi_logo = Image.open('img/withdraw.png')
    wi_logo = wi_logo.resize((25,25), Image.Resampling.LANCZOS)
    withdraw_img = ImageTk.PhotoImage(wi_logo)
    return withdraw_img
def TImage():
    #Transfer Logo
    tf_logo = Image.open('img/transfer.png')
    tf_logo = tf_logo.resize((25,25), Image.Resampling.LANCZOS)
    transfer_img = ImageTk.PhotoImage(tf_logo)
    return transfer_img
def CPImage():
    #ChangePIN Logo
    cp_logo = Image.open('img/pin.png')
    cp_logo = cp_logo.resize((25,25), Image.Resampling.LANCZOS)
    changepin_img = ImageTk.PhotoImage(cp_logo)
    return changepin_img
def EImage():
    #Exit Logo
    ex_logo = Image.open('img/exit.png')
    ex_logo = ex_logo.resize((25,25), Image.Resampling.LANCZOS)
    exit_img = ImageTk.PhotoImage(ex_logo)
    return exit_img