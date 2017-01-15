import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import sys
#from pandas.tools.plotting import scatter_matrix


def dumDrop(df, dkey):
    dummies = pd.get_dummies(df[dkey], prefix=dkey)
    df =  pd.concat([df, dummies], axis=1)
    df = df.drop([dkey], axis=1)
    return df

def splitNan(df, dkey):
    df[dkey] = df[dkey].apply(lambda x: 0.0 if pd.isnull(x) else 1.0)
    return df

## Full list of data columns.
#['jurisdiction', 'nbhd', 'dp', 'gp', 'house', 'dir', 'street', 'suffix', 'suffix_dir', 'apt', 'city', 'state', 'zip', 'zip4', 'class', 'land_full', 'bldg_full', 'total_full', 'land_adj', 'bldg_adj', 'total_adj', 'land_sf', 'land_acres', 'occupancy', 'residence_type', 'bldg_style', 'exterior_wall_type', 'percent_brick', 'roof_type', 'roof_material', 'main_living_area', 'upper_living_area', 'fin_attic_area', 'total_living_area', 'unfin_attic_area', 'foundation', 'basement_area', 'fin_bsmt_area_tot', 'bsmt_walkout', 'bsmt_gar_capacity', 'att_garage_area', 'garage_brick', 'open_porch_area', 'enclose_porch_area', 'patio_area', 'deck_area', 'canopy_area', 'veneer_area', 'carport_area', 'bathrooms', 'toilet_rooms', 'extra_fixtures', 'whirlpools', 'hottubs', 'saunas', 'fireplaces', 'bedrooms', 'rooms', 'families', 'year_built', 'year_remodel', 'eff_year_built', 'condition', 'grade', 'heating', 'air_conditioning', 'percent_complete', 'detached_structs', 'lname_th1', 'fname_th1', 'initial_th1', 'transfer_th1', 'book_th1', 'pg_th1', 'lname_th2', 'fname_th2', 'initial_th2', 'lname_cb1', 'fname_cb1', 'initial_cb1', 'transfer_cb1', 'book_cb1', 'pg_cb1', 'lname_cb2', 'fname_cb2', 'initial_cb2', 'mail_house', 'mail_house_portion', 'mail_dir', 'mail_street', 'mail_suffix', 'mail_suffix_dir', 'mail_unit_type', 'mail_unit_number', 'mail_city', 'mail_state', 'mail_zip', 'mail_zip4', 'mail_zip2', 'mail_county', 'mail_lname', 'mail_fname', 'mail_initial', 'mail_business', 'revenue_stamps', 'x', 'y', 'tif', 'tif_descr', 'condo_unit_address', 'condo_fin_liv_area', 'condo_year_built', 'platname', 'begin_of_legal', 'school_district', 'frontage', 'depth', 'fin_bsmt_area1', 'fin_bsmt_qual1', 'fin_bsmt_area2', 'fin_bsmt_qual2']

df = pd.read_csv('POLKCOUNTY.txt', sep='\t', low_memory=False)
df = df.drop(['zip4','dp', 'gp', 'house', 'dir', 'street', 'suffix', 'suffix_dir', 'state',  'land_full', 'bldg_full', 'total_full', 'land_adj', 'bldg_adj', 'total_adj', 'patio_area', 'lname_th1', 'fname_th1', 'initial_th1', 'transfer_th1', 'book_th1', 'pg_th1', 'lname_th2', 'fname_th2', 'initial_th2', 'lname_cb1', 'fname_cb1', 'initial_cb1', 'transfer_cb1', 'book_cb1', 'pg_cb1', 'lname_cb2', 'fname_cb2', 'initial_cb2', 'mail_house', 'mail_house_portion', 'mail_dir', 'mail_street', 'mail_suffix', 'mail_suffix_dir', 'mail_unit_type', 'mail_unit_number', 'mail_city', 'mail_state', 'mail_zip', 'mail_zip4', 'mail_zip2', 'mail_county', 'mail_lname', 'mail_fname', 'mail_initial', 'mail_business', 'revenue_stamps',  'tif', 'tif_descr',  'platname', 'begin_of_legal'], axis=1)
#df = df.fillna('-1')
#scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
#vc = df['Recipient State'].value_counts()
#print( vc)

##Get the list of headers
#print list(df.keys())
#print df.dtypes()
#df = df[['land_full', 'bldg_full', 'total_full', 'bedrooms']]

#dummies = pd.get_dummies(df['jurisdiction'], prefix='juris')
#df =  pd.concat([df, dummies], axis=1)
#df = df.drop(['jurisdiction'], axis=1)
df = dumDrop(df, 'jurisdiction')
df = dumDrop(df,'zip')
df = dumDrop(df,'nbhd')
df = dumDrop(df,'city')
df= dumDrop(df,'foundation')
df = dumDrop(df, 'class')

df = splitNan(df,'apt')

pd.set_option('display.max_columns', None)
#print df.describe()

print df.dtypes

#print df['apt']

#d3 = d2.drop(['jurisdiction'], inplace=True, axis=1)

#print d3


sys.exit(0)
df = df[['total_full']]


#plot = df.plot()
#fig = plot.get_figure()
#fig.savefig("output.png")


data = df.as_matrix().flatten()
data = np.add(data,1.0)
data = np.log(data)
print data
print min(data)
print max(data)
print "turkey"
#print data
#sys.exit(0)
#plt.xlim([min(data), max(data)])

plt.hist(data, bins=300)
#plt.title('Iowa Obamacare Prices for 2017')
#plt.xlabel('Grouped in $20 bins')

#plt.ylabel('Count')
#fig, ax = plt.subplots()
#ax.set_xscale('log')
#ax.xaxis.set_major_formatter(formatter)



plt.savefig('IowaACA.png')





#time.sleep(1000)
#vc.plot(kind='barh', rot=0)

#print( df['Recipient Name'].value_counts())


#df = df.drop(['Shipment Duty and Tax Charge','Pieces in Shipment','Pay Type','Shipment Tracking Number', 'Invoice number'] , axis=1)
#, 'Shipment Tracking Number')
#print df
#df['Shipment Freight Charge Amount'].plot()
#print(df.mean())
print(df.describe())
