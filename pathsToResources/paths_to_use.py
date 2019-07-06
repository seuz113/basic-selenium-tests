#!/usr/bin/python

google_url="https://www.google.com"

#CSS Input field and search button from main page
main_input = ".gLFyf"
search_button=".FPdoLc > center:nth-child(1) > input:nth-child(1)"

#CSS all suggestion list element
all_suggestion_list_element = "html body#gsr.hp.vasq.big div#viewport.ctr-p div#searchform.jhp.big form#tsf.tsf.nj div div.A8SBwf.emcav div.UUbT9"

#Button search available inside of the suggestion list
search_button_from_suggestion = ".aajZCb > div:nth-child(4) > center:nth-child(2) > input:nth-child(1)"

#CSS first option in suggestion list displayed
first_option_suggestion = "html body#gsr.hp.vasq.big div#viewport.ctr-p div#searchform.jhp.big form#tsf.tsf.nj div div.A8SBwf.emcav div.UUbT9 div.aajZCb ul.erkvQe li.sbct div.suggestions-inner-container div.sbtc div.sbl1 span"

#CSS first page result link
link_first_result_page = "#rso > div:nth-child(1) > div > div:nth-child(1) > div > div > div.r > a > h3"

#CSS page The Books - Patrick Rothfuss
link_page_the_books = "#rso > div:nth-child(1) > div > div:nth-child(4) > div > div.rc > div.r > a > div > cite"

#link to first result displayed in google
link_first_result_displayed = "#rso > div:nth-child(1) > div > div:nth-child(1) > div > div.rc > div.r > a > div > cite"

#ID title page displayed using first link
title_page_first_link = "firstHeading"

#CSS google result page
result_page_google = "#rhscol"