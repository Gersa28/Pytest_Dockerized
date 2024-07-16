class MapData():
    def __init__(self, data, updated=False):
        self._data = data
        self._updated = updated  
        # Define _updated as False if not provided or if provided
        if self._updated:  # if this value is True
            if not self.is_data_updated():
                self._updated = False

    def get_data(self):
        """
        Returns:
        list: Data object that is a list of dictionaries
        """
        return self._data

    def is_data_updated(self):
        """
        Check if the data has been updated with 'Population' and 'Updated' columns.

        Returns:
        boolean: True if each row has 'Population' and 'Updated' columns, False otherwise.
        """
        for row in self._data:
            if 'Population' not in row or 'Updated' not in row:
                return False
        return True

    def add_population(self, pop_map):
        """
        If the data has not been updated, this function cross-references
        a dictionary containing countries and their respective populations.
        Using this information, it updates each row entry to include
        the population for the country it represents.

        Parameters:
        pop_map (dict): Dictionary of countries and their populations

        Returns:
        None
        """
        if not self.is_data_updated():
            for row in self._data:
                if row['Country'] in pop_map:
                    row['Population'] = pop_map[row['Country']]
                else:
                    row['Population'] = None
                row['Updated'] = True
        else:
            raise Exception('You cannot transform the data twice')
