import VEnCode


class GetVencodes:
    def __init__(self, data_type, algorithm, cell_type, k, number_vencodes):
        # Define initial Parameters
        if algorithm == "heuristic":
            reg_element_sparseness = 0
        else:
            reg_element_sparseness = 90
        if data_type == "promoters":
            data_path = "resources/promoters_154cells_non_binarized.csv"
            target_celltype_activity = 0.5
        else:
            data_path = "resources/enhancers_154cells_non_binarized.csv"
            target_celltype_activity = 0.1
        # Open the data from FANTOM5
        data_tpm = VEnCode.DataTpm(data_path, sep=";")
        data_tpm.load_data()
        data_tpm.make_data_celltype_specific(target_celltype=cell_type, replicates=False)
        # Filter the data
        data_tpm.filter_by_target_celltype_activity(threshold=target_celltype_activity, binarize=False)
        data_tpm.define_non_target_celltypes_inactivity(threshold=0)
        data_tpm.filter_by_reg_element_sparseness(threshold=reg_element_sparseness)
        if algorithm != "sampling":
            data_tpm.sort_sparseness()
        # Find VEnCodes
        vencodes = VEnCode.Vencodes(data_tpm, algorithm=algorithm, number_of_re=k)
        vencodes.next(amount=number_vencodes)
        if vencodes.vencodes:
            self.vencodes = vencodes
        else:
            raise Exception("No VEnCodes found for {}!".format(cell_type))
