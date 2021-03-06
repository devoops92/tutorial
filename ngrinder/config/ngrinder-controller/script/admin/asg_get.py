# -*- coding:utf-8 -*-

# A simple example using the HTTP plugin that shows the retrieval of a
# single page via HTTP.
#
# This script is automatically generated by ngrinder.
#
# @author admin
from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from java.util import Date
from HTTPClient import NVPair, Cookie, CookieModule

from net.grinder.plugin.http import HTTPRequest
from net.grinder.plugin.http import HTTPPluginControl

# Uncomment this to use new experimental HTTP client.
# from org.ngrinder.http import HTTPRequest
# from org.ngrinder.http.cookie import Cookie, CookieManager

control = HTTPPluginControl.getConnectionDefaults()
# if you don't want that HTTPRequest follows the redirection, please modify the following option 0.
# control.followRedirects = 1
# if you want to increase the timeout, please modify the following option.
control.timeout = 6000

test1 = Test(1, "172.18.0.11")
request1 = HTTPRequest()

# Set header datas
headers = [] # Array of NVPair
headers.append(NVPair("Content-Type", "application/json"))
# Set param datas
params = [] # Array of NVPair
# Set cookie datas
cookies = [] # Array of Cookie

class TestRunner:
	# initlialize a thread
	def __init__(self):
		test1.record(TestRunner.__call__)
		grinder.statistics.delayReports=True
		pass

	def before(self):
		request1.setHeaders(headers)
		for c in cookies: CookieModule.addCookie(c, HTTPPluginControl.getThreadHTTPClientContext())

	# test method
	def __call__(self):
		self.before()

		result = request1.GET("http://172.18.0.11:8889/users/", params)

		# You get the message body using the getText() method.
		# if result.getText().find("HELLO WORLD") == -1 :
		#	 raise

		# if you want to print out log.. Don't use print keyword. Instead, use following.
		# grinder.logger.info("Hello World")

		if result.getStatusCode() == 200 :
			return
		elif result.getStatusCode() in (301, 302) :
			grinder.logger.warn("Warning. The response may not be correct. The response code was %d." %  result.getStatusCode())
			return
		else :
			raise
