
config_file_path = "./running-config.cfg"

class AccessLister():

    access_list_details = dict()

    def __init__(self, config_file):
        self.fin = open(config_file)

    def get_AL_details(self):
        """This method popualtes access_list_details and returns it """
        for line in self.fin:
            line_stripped = line.strip()
            if line_stripped.find("access-list")!=-1:
                key = hash(line_stripped)
                self.access_list_details[key] = line_stripped
        return self.access_list_details

    def print_AL(self):
        for key in self.access_list_details:
            print(self.access_list_details[key])


def main():
    access_lister = AccessLister(config_file_path)
    access_lister.get_AL_details()
    access_lister.print_AL()

if __name__ == '__main__':
    main()