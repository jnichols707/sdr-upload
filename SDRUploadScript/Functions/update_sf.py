def update_sf(data, batch):
    from simple_salesforce import Salesforce
    import Functions.Credentials.credentials_SFDC as cred
    sf = Salesforce(username=cred.username, password=cred.password, security_token=cred.security_token)

    bulk_data = []
    for row in data.itertuples():
        d = row._asdict()
        del d['Index']
        bulk_data.append(d)

    x=0
    y=batch
    while x < len(bulk_data):
        bulk_data_batch = bulk_data[x:y]
        sf.bulk.Account.update(bulk_data_batch)
        print(y)
        x+=batch
        y+=batch
    return "Updated."