
import pandas as pd
import os
def preparation_data_for_clusturing():

    # Construct absolute paths based on the location of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_dir, '..', 'data', 'unsupervised-lerning-data-insurance.csv')
    output_file_path = os.path.join(script_dir, '..', 'data', 'preparation_data_for_clusturing.csv')

    # Read the CSV file
    insurance = pd.read_csv(input_file_path, sep=';')
    
    columns_to_drops = ['ID', 'Date_start_contract', 'Date_last_renewal', 'Date_next_renewal', 'Date_birth', 'Date_driving_licence','Distribution_channel', 'Policies_in_force','Max_policies', 'Max_products','Date_lapse', 'Lapse', 'Payment', 'Premium', 'Cost_claims_year',
       'N_claims_year', 'N_claims_history', 'R_Claims_history', 'Area', 'Second_driver', 'Year_matriculation', 'Length'  ,'Type_risk' ]
    insurance = insurance.drop(columns= columns_to_drops, axis=1)
    insurance.drop_duplicates(inplace=True)
    insurance = insurance.dropna()
    insurance_type = {
    'P':1,
    'D':2
    }
    insurance['Type_fuel'] = insurance['Type_fuel'].map(insurance_type)
    insurance.to_csv(output_file_path, index=False)
    
if __name__ == "__main__":
    preparation_data_for_clusturing()