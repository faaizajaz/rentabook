from libgenapi.search_request import SearchRequest


class LibgenSearch:

	def search_any_epub_or_mobi(self, query):
		self.search_request = SearchRequest(query, search_type="any")
		data = self.search_request.aggregate_request_data()
		
		#filtered_data = data
		#for f in filters:
		#	filtered_data = [d for d in filtered_data if d[f] in filters.values()]
		#return filtered_data

		filtered_data = []

		# for d in data:
		# 	for k, v in filters.items():
		# 		if d[k] == v:
		# 			filtered_data.append(d)
		# return filtered_data

		for d in data:
			if d['Extension'] == "mobi" or d['Extension'] == "epub":
				filtered_data.append(d)
		return filtered_data


