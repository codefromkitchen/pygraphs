import things_you_need


def auth_tasks():
	"""set up googl auth here"""
	# see https://developers.google.com/gmail/api/quickstart/python


def get_max_value_column(self, search_range="!A2:A"):
		"""returns a [[]] with max values"""
		
		# init vars
        max_len = 0
        max_title = ''
        
        # get spreadsheet metadata, comes with a list of sheet names
        spreadsheet_metadata = self.service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
        
        
        # Tip: always use dict.get(key[, value]), never use json.loads() 
        sheets = spreadsheet_metadata.get('sheets', '')

        # first 10 sheets (most recent first)
        for i in range(0, 10):
            # get sheet title
            title = str(sheets[i].get("properties", {}).get("title", ""))
     
            projection_ = title + search_range
            sheet_metadata = self.sheet_service.values().get(spreadsheetId=SPREADSHEET_ID,
                                                             range=projection_).execute()
            values = sheet_metadata.get('values', '')
            if len(values) > max_len:
                max_len = len(values)
                max_title = title

        max_sheet_metadata = self.sheet_service.values().get(spreadsheetId=SPREADSHEET_ID,
                                                         range=max_title + search_range).execute()
        return max_sheet_metadata.get('values', '')
