'''
Created on May 29, 2017

@author: Dave
'''


class HtmlOutputer(object):
    
    def __init__(self):
        self.data = []
    
    
    def collect_data(self,data):
        if data in None:
            return
        self.data.append(data)
    
    def output_html(self):
        fout = open('output.html', 'w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        
        for item in self.data:
            fout.write("<tr>")
            fout.write("<td> %s </td>" % item['url'])
            fout.write("<td> %s </td>" % item['title'])
            fout.write("<td> %s </td>" % item['summary'])
            fout.write("<tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        
        
        fout.close()
    
    
    
    



