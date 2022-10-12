
def getresult(df_inner,ww,mw,tmw,smw,yw):
    symlst = [] 
    pricelst = []

    for ind in df_inner.index:

        s =float( ww)*(df_inner['tp'][ind]/df_inner['wp'][ind]) + mw*(df_inner['tp'][ind]/df_inner['mp'][ind]) + tmw*(df_inner['tp'][ind]/df_inner['tmp'][ind])  + smw*(df_inner['tp'][ind]/df_inner['smp'][ind] ) + yw*(df_inner['tp'][ind]/df_inner['yp'][ind] )
        symlst.append(s)
        
    df_inner['Value'] = symlst
    r = df_inner.sort_values(by=['Value'],ascending=False)
    return r