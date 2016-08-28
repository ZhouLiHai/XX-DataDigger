import struct
import string

"""
	将PQDIF文件解析为文本文件
	指定PQDIF二进制数组，以及输出文件的句柄，输出True（出现异常输出False）
"""


class PQdeal(object):
	"""docstring for PQdeal"""
	def __init__(self, arg = None):
		self.arg = arg
		self.tag =  {
		b'\x40\x14\x11\x4a\x9f\xe4\xcf\x11\x99\x00\x50\x51\x44\x49\x46\x00' : 'guidRecordSignaturePQDIF', 
		b'\x18\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagBlank',
		b'\x06\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagContainer',
		b'\x19\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagRecDataSource',
		b'\x8c\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagRecMonitorSettings',
		b'\x1a\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagRecObservation',
		b'\x07\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagVersionInfo',
		b'\x08\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagFileName',
		b'\x09\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagCreation',
		b'\x0a\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagLastSaved',
		b'\x0b\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagTimesSaved',
		b'\x0c\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagLanguage',
		b'\x0d\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagTitle',
		b'\x0e\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagSubject',
		b'\x0f\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagAuthor',
		b'\x10\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagKeywords',
		b'\x11\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagComments',
		b'\x12\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagLastSavedBy',
		b'\x23\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagApplication',
		b'\x13\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagSecurity',
		b'\x14\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagOwner',
		b'\x15\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagCopyright',
		b'\x16\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagTrademarks',
		b'\x17\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagNotes',
		b'\x1b\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagCompressionStyleID',
		b'\x1c\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagCompressionAlgorithmID',
		b'\x1d\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagCompressionChecksum',
		b'\xa2\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagName',
		b'\xa3\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagAddress1',
		b'\xa4\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagAddress2',
		b'\xa5\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagCity',
		b'\xa6\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagState',
		b'\xa7\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagPostalCode',
		b'\xa8\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagCountry',
		b'\xa9\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagPhoneVoice',
		b'\x81\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagDataSourceTypeID',
		b'\x82\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagVendorID',
		b'\x83\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagEquipmentID',
		b'\x84\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagCustomSourceInfo',
		b'\x85\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagSerialNumberDS',
		b'\x86\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagVersionDS',
		b'\x87\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagNameDS',
		b'\x88\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagOwnerDS',
		b'\x89\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagLocationDS',
		b'\x8a\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagTimeZoneDS',
		b'\x8b\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagCoordinatesDS',
		b'\x8d\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagChannelDefns',
		b'\x8e\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagOneChannelDefn',
		b'\x90\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagChannelName',
		b'\x91\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagPhaseID',
		b'\x93\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagOtherChannelIdentifier',
		b'\x94\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagGroupName',
		b'\x72\xe8\x90\xc6\x55\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagQuantityMeasuredID',
		b'\x92\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagQuantityTypeID',
		b'\x95\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagQuantityName',
		b'\x96\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagPrimarySeriesIdx',
		b'\x98\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagSeriesDefns',
		b'\x9a\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagOneSeriesDefn',
		b'\x9c\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagValueTypeID',
		b'\x9b\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagQuantityUnitsID',
		b'\x9e\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagQuantityCharacteristicID',
		b'\xa1\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagStorageMethodID',
		b'\x9d\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagValueTypeName',
		b'\x9e\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagHintGreekPrefixID',
		b'\x9f\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagHintPreferredUnitsID',
		b'\xa0\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagHintDefaultDisplayID',
		b'\x41\xd4\x47\x27\x2b\xd0\xd2\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagProbInterval',
		b'\x40\xd4\x47\x27\x2b\xd0\xd2\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagProbPercentile',
		b'\xc8\x18\xa1\x0f\xcb\x4a\xd2\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagSeriesNominalQuantity',
		b'\x83\x81\xf2\x62\xc4\xf9\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagEffective',
		b'\xc3\x18\xa1\x0f\x4a\xcb\xd2\x11\xb3\x0b\xfe\x25\xcb\x9a\x17\x60' : 'tagNominalFrequency',
		b'\x8f\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagChannelDefnIdx',
		b'\x84\x81\xf2\x62\xc4\xf9\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagTriggerTypeID',
		b'\x8a\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagObservationName',
		b'\x8b\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagTimeCreate',
		b'\x8c\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagTimeStart',
		b'\x8d\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagTriggerMethodID',
		b'\x8e\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagTimeTriggered',
		b'\x8f\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagChannelTriggerIdx',
		b'\x90\x86\x73\x89\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagObservationSerial',
		b'\x97\x85\x8d\xb4\xf5\xf5\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagDisturbanceCategoryID',
		b'\x91\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagChannelInstances',
		b'\x92\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagOneChannelInst',
		b'\x93\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagSeriesInstances',
		b'\xc7\x18\xa1\x0f\x4a\xcb\xd2\x11\xb3\x0b\xfe\x25\xcb\x9a\x17\x60' : 'tagChanTriggerModuleInfo',
		b'\xc6\x18\xa1\x0f\x4a\xcb\xd2\x11\xb3\x0b\xfe\x25\xcb\x9a\x17\x60' : 'tagChanTriggerModuleName',
		b'\xc5\x18\xa1\x0f\x4a\xcb\xd2\x11\xb3\x0b\xfe\x25\xcb\x9a\x17\x60' : 'tagCrossTriggerDeviceName',
		b'\xc4\x18\xa1\x0f\x4a\xcb\xd2\x11\xb3\x0b\xfe\x25\xcb\x9a\x17\x60' : 'tagCrossTriggerChanIdx',
		b'\xc2\x18\xa1\x0f\x4a\xcb\xd2\x11\xb3\x0b\xfe\x25\xcb\x9a\x17\x60' : 'tagChanTriggerTypeID',
		b'\x42\xd4\x47\x27\xd0\x2b\xd2\x11\xae\x42\x00\x60\x08\x3a\x26\x28' : 'tagChannelFrequency',
		b'\x94\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagOneSeriesInstance',
		b'\x95\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagSeriesBaseQuantity',
		b'\x96\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagSeriesScale',
		b'\x97\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagSeriesOffset',
		b'\x99\x6f\x78\x3d\x6e\xf7\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagSeriesValues',
		b'\x1f\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagSeriesShareChannelIdx',
		b'\x20\x86\x73\x89\xc3\xf1\xcf\x11\x9d\x89\x00\x80\xc7\x2e\x70\xa3' : 'tagSeriesShareSeriesIdx',
		}

	def construction(self, data, fp, body = 0, head = 0, tab = 0):
		inner_offset = head
		chip_size = 0
		while data[inner_offset:inner_offset+16] in self.tag.keys():
			Type, Physical, isEmbedded, fill, link, size = struct.unpack("bbbbII",data[inner_offset+16:inner_offset+16+12])
			fp.write ('    ' * tab + '%s %d %d %d %d %d %d\n' % (self.tag[data[inner_offset:inner_offset+16]], Type, Physical, isEmbedded, fill, link, size))

			if not isEmbedded:
				chip_size = link + size
				if Type == 1:
					#print ('body',body, 'inner_offset', inner_offset)
					res = self.construction(data, fp, body, link + body, tab + 1)
					if res > chip_size:
						chip_size = res
				if Type == 3 and Physical == 41:
					inner_data = struct.unpack("I",data[body + link - 4:body + link])
					fp.write ("%d\n" %inner_data[0])
					for x in range(0, inner_data[0]):
						real_data = struct.unpack("d",data[body + link + 8 * x:body + link + 8 * (x + 1)])
						fp.write ("%9.4f;" %real_data[0])
					fp.write ('\n')

			else:
				if Type == 2 and Physical == 32:
					inner_data = struct.unpack("I",data[inner_offset+16+4:inner_offset+16+8])
					fp.write ("%d\n" %inner_data[0])
				if Type == 2 and Physical == 41:
					inner_data = struct.unpack("d",data[inner_offset+16+4:inner_offset+16+12])
					fp.write ("%d\n" %inner_data[0])
			inner_offset = inner_offset + 16 + 12
		return chip_size

	def chipCut(self, data, fp, tab = 0):
		head = 64 + 4

		while head < len(data):
			fp.write ("========== New record ==========\n")
			res = self.construction(data, fp, head, head, tab)
			head = res + 64 + head

	def afterdeal(self, filename):
		fp = open(filename, 'r')

		def detail(line, nums):
			line = line.replace('\n', '')
			m = line.split(';')
			res = []
			for i, x in enumerate(m):
				if i == nums:
					break
				res.append(float(x))

			#if res[1] == 60:
			print (res)
			return res

		data_name = []
		ignore_first = True
		while True:
			line = fp.readline()
			if line is '':
				break

			if line.find('New record') != -1:
				ignore_first = True
			if line.find('tagChannelDefnIdx') != -1:
				idex = int(fp.readline())
			if line.find('tagChannelFrequency') != -1:
				freq = int(fp.readline())
			if line.find('tagSeriesValues') != -1:
				if ignore_first == True:
					ignore_first = False
					continue
				nums = int(fp.readline())
				res = detail (fp.readline(), nums)
				data_name.append ([idex, freq, nums, res])

		print (len(data_name), data_name[0][3])
		fp.close()



def main():
	pq = PQdeal();
	pq.afterdeal('Data/01-0320151103T005911.pqd.data')
	return

	
	fp = open('20151103T005911.pqd','rb')
	data = fp.read()
	fp.close()
	fp = open('20151103T005911' + '.data', 'w')

	pq.chipCut(data, fp)


	fp.close()
if __name__ == '__main__':
	main()






















