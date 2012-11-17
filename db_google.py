import gdata.docs
import gdata.docs.service
import gdata.spreadsheet.service

import datetime
import json

credentials = json.load(open('credentials.json', 'r'))

def writeEntry(entry,link):
    name = credentials['username']
    password = credentials['password']
    title = 'linksaver'

    if password == '':
        print 'please change the password.'
    else:
        client = gdata.spreadsheet.service.SpreadsheetsService()
        client.ClientLogin(name, password)

        client.ProgrammaticLogin()

        q = gdata.spreadsheet.service.DocumentQuery()
        q['title'] = title
        q['title-exact'] = 'true'
        feed = client.GetSpreadsheetsFeed(query=q)
        spreadsheet_id = feed.entry[0].id.text.rsplit('/',1)[1]
        # print spreadsheet_id
        feed = client.GetWorksheetsFeed(spreadsheet_id)
        worksheet_id = feed.entry[0].id.text.rsplit('/',1)[1]

        rows = client.GetListFeed(spreadsheet_id, worksheet_id).entry

        for row in rows:
            for key in row.custom:
                print " %s: %s" % (key, row.custom[key].text)
            print


        dict = {}
        dict['entry'] = entry
        dict['link'] = link
        dict['timestamp'] = str(datetime.datetime.now())
        print dict


        entry = client.InsertRow(dict, spreadsheet_id, worksheet_id)
        if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
          print "Insert row succeeded."
        else:
          print "Insert row failed."


if __name__ == '__main__':
    writeEntry('333','http://google.com')