from model_root import ModelRoot
print("test")


class DAOMember():

    def __init__(self, filename):
        self.filename = filename

    def import_data(self):
        return __extract_imported_data()

    def __extract_imported_data(self):
        self.imported_data = []
        with open(self.filename, "r", encoding="utf-8") as myfile:
            for item in myfile.split("\n"):
                self.imported_data.append(line)
        return self.imported_data

    def export_data(self):
        with open(self.filename, "w", encoding="utf-8") as myfile:
            for i in self.data_for_export:
                myfile.write(i)

    def __pass_data_for_export(self):
        return self.data_for_export = ControllerMemberContainer().member_container
