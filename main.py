#!/usr/bin/env python
from __future__ import print_function
import pickle
import engine
import auth_google
import skills
import Audio
import openfun
import os
import datetime
import requests,json
import urllib
import strlists
import voicetyping



SERVICE = auth_google.authenticate_google()
while True:
    print ("listening....")
    text = Audio.get_audio()


    if text.count(strlists.WAKE1) > 0:
        engine.speak("yes master proceed")
        text = Audio.get_audio()
    if text.count(strlists.WAKE2) > 0:
        engine.speak("I am ready master")
        text = Audio.get_audio()
    if text.count(strlists.WAKE3) > 0:
        engine.speak("yes master,i am here")
        text = Audio.get_audio()
    if text.count(strlists.WAKE4) > 0:
        engine.speak("I am ready master")
        text = Audio.get_audio()
    if text.count(strlists.WAKE5) > 0:
        engine.speak("yeah master")
        text = Audio.get_audio()
    if text.count(strlists.WAKE6) > 0:
        engine.speak("I am ready master")
        text = Audio.get_audio()
    if text.count(strlists.WAKE7) > 0:
        engine.speak("yes master")
        text = Audio.get_audio()
    if text.count(strlists.WAKE8) > 0:
        engine.speak("I am ready master")
        text = Audio.get_audio()
    if text.count(strlists.WAKE9) > 0:
        engine.speak("yes i am master")
        text = Audio.get_audio()

    
    for phrase in strlists.GREETING_STR1:
        if phrase in text:
            engine.speak("yes master")
        else:
            pass
   
    for phrase in strlists.GREETING_STR2:
        if phrase in text:
            engine.speak("I am fine master")

     
    





    for phrase in strlists.CALENDAR_STRS:
        if phrase in text:
            date = skills.get_date(text)
            if date:
                skills.get_events(date,SERVICE)
            else:
                engine.speak("Please say again master ,I can't understand")

    for phrase in strlists.WEATHER_STRS:
        if phrase in text:
            engine.speak("which place master?")
            area = Audio.get_audio()
            skills.get_weather(area)
            engine.speak("Anything Else Master?")
            break

   




    for phrase in strlists.SEARCH_STRS:
        for phrase in strlists.SEARCH_GOOGLE_STR:
            if phrase in text:
                engine.speak("what to search master?,please tell me again")
                text = Audio.get_audio()
                skills.google_search(text)
                engine.speak("searching master!")
                break
        
        for phrase in strlists.SEARCH_WIKIPEDIA_STR:
            if phrase in text:
                skills.wikipedia_search()
                break
            
        for phrase in strlists.SEARCH_YOUTUBE_STR:
            if phrase in text:
                engine.speak("what to search master ?,please tell me!")
                query = Audio.get_audio()
                skills.youtube_search(query)
                break
            

    for phrase in strlists.NOTE_STRS:
        if phrase in text:
            engine.speak("what would you like me to write down master?")
            note_text = Audio.get_audio()
            skills.note(note_text)
            engine.speak("I've made a note of that.")
            break
        


    for phrase in strlists.SCREENSHOT_STR:
        if phrase in text:
            engine.speak("taking screen shot master")
            skills.scrnshot()
            
            break
        

    for phrase in strlists.ASKFOR_GAME:
        if phrase in text:
            engine.speak("do you want to play chess master?")
            text = Audio.get_audio()
            if "yes" in text:
                openfun.xboard()
            else:
                engine.speak("ok master")
            
    

    for phrase in strlists.VOICETYPING_STR:
        if phrase in text:
            for phrase in strlists.ON_STR:
                if phrase in text:
                    engine.speak("voice typing ready master")
                    engine.speak("please use the command switch off voice typing to return me to the normal mode master")
                    voicetyping.typein()
                    break    
            

    
    for phrase in strlists.START_STR:
        if phrase in text:
            for phrase in strlists.HTTP_STR:
                if phrase in text:
                    engine.speak("turning on the ngnix http server master")
                    openfun.http_start()
                    break
                
            for phrase in strlists.POSTGRESQL_STR:
                if phrase in text:
                    engine.speak("turning on the postgresql server master")
                    openfun.postgresql_start()
                    break
               
            for phrase in strlists.SSHD_STR:
                if phrase in text:
                    engine.speak("turning on the sshd sever master")
                    openfun.sshd_start()
                    break
            
            for phrase in strlists.WIFI_STR:
                if phrase in text:
                    engine.speak("turning on the wifi master")
                    openfun.wifi_on()
                    break
              
            for phrase in strlists.BLUETOOTH_STR:
                if phrase in text:
                    engine.speak("turning on the bluetooth master")
                    openfun.bluetooth_on()
                    break
                
   
    for phrase in strlists.RESTART_STR:
        if phrase in text:

            for phrase in strlists.HTTP_STR:
                if phrase in text:
                    engine.speak("restarting the ngnix http server master")
                    openfun.http_restart()
                    break
            for phrase in strlists.POSTGRESQL_STR:
                if phrase in text:
                    engine.speak("restarting the postgresql server master")
                    openfun.postgresql_restart()
                    break
            for phrase in strlists.SSHD_STR:
                if phrase in text:
                    engine.speak("restarting the sshd sever master")
                    openfun.sshd_restart()
                    break
            for phrase in strlists.WIFI_STR:
                if phrase in text:
                    engine.speak("restarting the wifi master")
                    openfun.wifi_off()
                    openfun.wifi_on()
                    break
            for phrase in strlists.BLUETOOTH_STR:
                if phrase in text:
                    engine.speak("restarting the bluetooth master")
                    openfun.bluetooth_off()
                    openfun.bluetooth_on()
                    break
        else:
            pass  


    for phrase in strlists.STOP_STR:
        if phrase in text:

            for phrase in strlists.HTTP_STR:
                if phrase in text:
                    engine.speak("turning off ngnix http server master")
                    openfun.http_stop()
                    break
            for phrase in strlists.POSTGRESQL_STR:
                if phrase in text:
                    engine.speak("turning off postgresql server master")
                    openfun.postgresql_stop()
                    break
            for phrase in strlists.SSHD_STR:
                if phrase in text:
                    engine.speak("turning off sshd sever master")
                    openfun.sshd_stop()
                    break
            for phrase in strlists.WIFI_STR:
                if phrase in text:
                    engine.speak("turning off wifi master")
                    openfun.wifi_off()
                    break
            for phrase in strlists.BLUETOOTH_STR:
                if phrase in text:
                    engine.speak("turning off  bluetooth master")
                    openfun.bluetooth_off()
                    break            
        else:
            pass

   #opeing the apps loop starts here 
   ####################################
   ####################################
   ####################################

    for phrase in strlists.OPEN_STR:
        if phrase in text:

            
            for phrase in strlists.GOOGLE_STR:
                if phrase in text:
                    engine.speak("opening google chrome master")
                    openfun.google()
                    break
                

            for phrase in strlists.FIREFOX_STR:
                if phrase in text:
                    engine.speak("opening firefox master")
                    openfun.firefox()
                    break
                
            for phrase in strlists.CAMERA_STR:
                if phrase in text:
                    engine.speak("opening the camera master")
                    openfun.camera()
                    break
              
            for phrase in strlists.AIRCRACK_STR:
                if phrase in text:
                    engine.speak("opening the aircrack-ng master")
                    openfun.aircrack()
                    break
                
            
            for phrase in strlists.AIRGEDDON_STR:
                if phrase in text:
                    engine.speak("opening the the airgeddon master")
                    openfun.airgeddon()
                    break
               
            for phrase in strlists.BURPSUITE_STR:
                if phrase in text:
                    engine.speak("opening the burpsuiute master!")
                    openfun.burpsuite()
                    break
                
           
            for phrase in strlists.ETTERCAP_GRAPH_STR:
                if phrase in text:
                    engine.speak("opening the ettercap graph")
                    openfun.ettercap_graphical()
                    break
                

            for phrase in strlists.GO_BUSTER_STR:
                if phrase in text:
                    engine.speak("opening the go buster master!")
                    openfun.gobuster()
                    break
                
            for phrase in strlists.JOHNNY_STR:
                if phrase in text:
                    engine.speak("opening the johnny tool master!")
                    openfun.johnny()
                    break
               
            for phrase in strlists.KAYAK_CAR_HACKING_TOOL:
                if phrase in text:
                    engine.speak("opening the kayak car tool master!")
                    openfun.ophcrack()
                    break
               

            for phrase in strlists.OWASP_STR:
                if phrase in text:
                    engine.speak("opening the owasp master!")
                    openfun.owasp()
                    break
                
            for phrase in strlists.WEEVELY_STR:
                if phrase in text:
                    engine.speak("opening the weevely master!")
                    openfun.weevely()
                    break
                
            for phrase in strlists.WIRESHARK_STR:
                if phrase in text:
                    engine.speak("opening the wire shark master!")
                    openfun.wireshark()
                    break
               
            for phrase in strlists.ZENMAP_STR:
                if phrase in text:
                    engine.speak("opening the zenmap tool master!")
                    openfun.zenmap()
                    break
                
            for phrase  in strlists.DNS_ANALYSIS:
                if phrase in text:
                    engine.speak("opening the dns analysis tootl master!")
                    openfun.dnsanalysis()
                    break
                
            for phrase in strlists.IDPS_IPS_IDENTOFICATION_STR:
                if phrase in text:
                    engine.speak("openin the idps ips identification tool master!")
                    openfun.idps_ips_identification()
                    break
               
            for phrase in strlists.LIVE_HOST_IDENTIFIER_STR:
                if phrase in text:
                    engine.speak("opeing the idps ips identifying tool master!")
                    openfun.live_host_identification()
                    break
                
            for phrase in strlists.NETWORK_OR_PORT_SCANNER_STR:
                if phrase in text:
                    engine.speak("opening the network or port scanner tool master!") 
                    openfun.network_or_port_scanner()
                    break
                

            for phrase in strlists.OSINT_ANALYSIS_STR:
                if phrase in text:
                    engine.speak("opening the o s i n t tool master!")
                    openfun.osint_analysis()
                    break
            
            for phrase in strlists.ROUTE_ANALYSIS_STR:
                if phrase in text:
                    engine.speak("opening the route analysis tool master!")
                    openfun.route_analysis()
                    break
                
            for phrase in strlists.MALTEGO_STR:
                if phrase in text:
                    engine.speak("opening the maltego tool master!")
                    openfun.maltego()
                    break
               
            for phrase in strlists.ARMITAGE_STR:
                if phrase in text:
                    engine.speak("opening the  armitage tool master!")
                    openfun.armitage()
                    break
                
            for phrase in strlists.SBM_ANALYSIS_STR:
                if phrase in text:
                    engine.speak("opening the SBM analysis tools master")
                    openfun.sbm_analysis()
                    break
                
            for phrase in strlists.SNMP_ANALYSIS_STR:
                if phrase in text:
                    engine.speak("opening the SNMP analysis master")            
                    openfun.snmp_analysis()
                    break
                
            for phrase in strlists.SSL_ANALYSIS_STR:
                if phrase in text:
                    engine.speak("opening the SSL analysis master")
                    openfun.ssl_analysis()
                    break
                
            for phrase in strlists.AMAP_STR:
                if phrase in text:
                    engine.speak("opening the AMAP master")
                    openfun.amap()
                    break
                
            for phrase in strlists.DMITRY_STR:
                if phrase in text:
                    engine.speak("opening the Dimitri master")
                    openfun.dmitry()
                    break
                
            for phrase in strlists.DNMAP_SERVER_STR:
                if phrase in text:
                    engine.speak("opening the dnmap server master!")
                    openfun.dnmap_server()
                    break
               
            for phrase in strlists.DNMAP_CLIENT_STR:
                if phrase in text:
                    engine.speak("opening the dnmap client master")
                    openfun.dnmap_client()
                    break
               
            for phrase in strlists.IKE_STR:
                if phrase in text:
                    engine.speak("opening the ike tool master!")
                    openfun.ike_scan()
                    break
                
            for phrase in strlists.NET_DISCOVER_STR:
                if phrase in text:
                    engine.speak("opening the net discover master")
                    openfun.net_discover()
                    break
                
            for phrase in strlists.POF_TOOL_STR:
                if phrase in text:
                    engine.speak("opening the pof master!")
                    openfun.pOf()
                    break
                
            for phrase in strlists.RECON_NG_STR:
                if phrase in text:
                    engine.speak("opening the recon ng master")
                    openfun.recon_ng()
                    break
               
            for phrase in strlists.CISCO_STR:
                if phrase in text:
                    engine.speak("opening the cisco master")
                    openfun.cisco_tools()
                    break
                
            for phrase in strlists.FUZZING_TOOL_STR:
                if phrase in text:
                    engine.speak("opening the fuzzing tool master")
                    openfun.fuzzing_tools()
                    break
                          
            for phrase in strlists.OPEN_VAS_SCANNER_TOOL_STR:
                if phrase in text:
                    engine.speak("opening the open vas scanner master")
                    openfun.open_vas_scanner()
                    break
                
            for phrase in strlists.STRESS_TESTING_TOOL_STR:
                if phrase in text:
                    engine.speak("opening the stress testing tools master")
                    openfun.stress_testing()
                    break
                
            
            for phrase in strlists.VOIP_TOOLS_STR:
                if phrase in text:
                    engine.speak("opening the voip tools master")
                    openfun.voip_tool()
                    break
                

            for phrase in strlists.GOLISMERO_STR:
                if phrase in text:
                    engine.speak("opening the golismero master")
                    openfun.golismero()
                    break
               
            for phrase in strlists.LYNIS_STR:
                if phrase in text:
                    engine.speak("opening the lynis tool master")
                    openfun.lynis()
                    break
                
            for phrase in strlists.UNIX_PRISEV_CHECK:
                if phrase in text:
                    engine.speak("opening the unix preserve check master")
                    openfun.unix_privesv_check()
                    break
               
            for phrase in strlists.FILE_MANAGER_STR:
                if phrase in text:
                    engine.speak("opening the file manager master")
                    openfun.file_manger_or_places()
                    break
                
            for phrase in strlists.DOCUMENTS_STR:
                if phrase in text:
                    engine.speak("opening the documents master")
                    openfun.documents()
                    break
                
            for phrase in strlists.DESKTOP_STR:
                if phrase in text:
                    engine.speak("opening the desktop master")
                    openfun.desktop()
                    break
               
            for phrase in strlists.DOWNLOADS_STR:
                if phrase in text:
                    engine.speak("opening the downloads master")
                    openfun.Downloads()
                    break
                
            for phrase in strlists.MUSIC_STR:
                if phrase in text:
                    engine.speak("opening the pictures master")
                    openfun.pictures()
                    break
              
            for phrase in strlists.PICTURES_STR:
                if phrase in text:
                    engine.speak("opening the pictures master")
                    openfun.pictures()
                    break
               

            for phrase in strlists.VIDEOS_STR:
                if phrase in text:
                    engine.speak("opening the videos master")
                    openfun.videos()
                    break
                
            for phrase in strlists.TRASH_STR:
                if phrase in text:
                    engine.speak("opening the trash master")
                    openfun.trash()
                    break
                
            for phrase in strlists.CMS_AND_FRAMEWORK_STR:
                if phrase in text:
                    engine.speak("opening the cms and framework master")
                    openfun.cms_and_framework()
                    break
              
            for phrase in strlists.WPSCAN_STR:
                if phrase in text:
                    engine.speak("opening the wps scan master")
                    openfun.cms_and_framework()
                    break
               
            for phrase in strlists.WIG_STR:
                if phrase in text:
                    engine.speak("opening the wig master")
                    openfun.wig()
                    break
              
            for phrase in strlists.UA_TESTER_STR:
                if phrase in text:
                    engine.speak("opening the ua tester master")
                    openfun.ua_tester()
                    break
                
            for phrase in strlists.WEBCRAWLER_AND_DIRECTORY_STR:
                if phrase in text:
                    engine.speak("opening the webcrawler and directory tool master")
                    openfun.web_crawlers_and_directory()
                    break
               
            for phrase in strlists.APACHE_USER_STR:
                if phrase in text:
                    engine.speak("opening the apache user tool master")
                    openfun.apache_users()
                    break
                
            
            for phrase in strlists.UNISCAN_STR:
                if phrase in text:
                    engine.speak("opening the uni scan master")
                    openfun.uniscan_gui()
                    break
               
            for phrase in strlists.WEB_VULNERABILITY_STR:
                if phrase in text:
                    engine.speak("opening the web vulnerability master")
                    openfun.web_vulnerability_scanner()
                    break
              
            for phrase in strlists.CADAVAR_STR:
                if phrase in text:
                    engine.speak("opening the cadavar master")
                    openfun.cadaver()
                    break
              
            for phrase in strlists.CLUSTERD_STR:
                if phrase in text:
                    engine.speak("opening the clustered master")
                    openfun.clusterd()
                    break
              
            for phrase in strlists.DAV_TEST_STR:
                if phrase in text:
                    engine.speak("opening the dav test master")
                    openfun.davtest()
                    break
               
            for phrase in strlists.DEBLAZE_STR:
                if phrase in text:
                    engine.speak("opening the de blaze master")
                    openfun.deblaze()
                    break
              
            for phrase in strlists.FIMAP_STR:
                if phrase in text:
                    engine.speak("opening the fimap master")
                    openfun.fimap()
                    break
                
            for phrase in strlists.GRABBER_STR:
                if phrase in text:
                    engine.speak("opening the grabber master")
                    openfun.grabber()
                    break
                
                
            for phrase in strlists.JBOSS_AUTOPWN_WIN_STR:
                if phrase in text:
                    engine.speak("opening the jboss auto pwn master")
                    openfun.jboss_autopwn_win()
                    break
                
            for phrase in strlists.JBOSS_AUTOPWN_LINUX_STR:
                if phrase in text:
                    engine.speak("opening the jboss auto pwn linux master")
                    openfun.jboss_autopwn_linux()
                    break
                
                
            for phrase in strlists.JOOMSCAN_STR:
                if phrase in text:
                    engine.speak("opening the joom scan master")
                    openfun.joomscan()
                    break
                
                
            for phrase in strlists.JQSL_STR:
                if phrase in text:
                    engine.speak("opening the jqsl master")
                    openfun.jsql()
                    break
                
                
            for phrase in strlists.PAD_BUSTER_STR:
                if phrase in text:
                    engine.speak("opening the pad buster master")
                    openfun.padbuster()
                    break
              
              
            for phrase in strlists.SKIP_FISH_STR:
                if phrase in text:
                    engine.speak("opening the skip fish master")
                    openfun.skipfish()
                    break
               
               
            for phrase in strlists.WAPITI_STR:
                if phrase in text:
                    engine.speak("opening the wapiti master")
                    openfun.wapiti()
                    break
               
               
            for phrase in strlists.WEBSPLOIT_STR:
                if phrase in text:
                    engine.speak("opening the web sploit master")
                    openfun.websploit()
                    break
             
             
            for phrase in strlists.WHATWEB_STR:
                if phrase in text:
                    engine.speak("opening the what web master")
                    openfun.whatweb()
                    break
             
             
            for phrase in strlists.XSSER_STR:
                if phrase in text:
                    engine.speak("opening the xsser master")
                    openfun.xsser()
                    break
              
              
            for phrase in strlists.COMMIX_STR:
                if phrase in text:
                    engine.speak("opening the commix master")
                    openfun.commix()
                    break
               
               
            for phrase in strlists.HTTRACK_STR:
                if phrase in text:
                    engine.speak("opening the httrack master")
                    openfun.httrack()
                    break
              
              
            for phrase in strlists.WEBSCARAB_STR:
                if phrase in text:
                    engine.speak("opening the webscarab master")
                    openfun.webscarab()
                    break
                
                
            for phrase in strlists.DATABASE_EXPLOIT:
                if phrase in text:
                    engine.speak("opening the database exploit master")
                    openfun.database_exploit()
                    break
                
                
            for phrase in strlists.MDB_EXPORT_STR:
                if phrase in text:
                    engine.speak("opening the mdb export master")
                    openfun.mdb_export()
                    break
                
                
            for phrase in strlists.MDB_HEXDUMP_STR:
                if phrase in text:
                    engine.speak("opening the mdb hex dump master")
                    openfun.mdb_hexdump()
                    break
              
              
            for phrase in strlists.MDB_PARSER_CSV_STR:
                if phrase in text:
                    engine.speak("opening the mdb parser csv master")
                    openfun.mdb_parsecsv()
                    break
              
              
            for phrase in strlists.MDB_SQL_STR:
                if phrase in text:
                    engine.speak("opening the mdb sql master")
                    openfun.mdb_sql()
                    break
               
               
            for phrase in strlists.MDB_TABLES_STR:
                if phrase in text:
                    engine.speak("opening the mdb tables master")
                    openfun.mdb_tables()
                    break
               
               
            for phrase in strlists.OSCANNER_STR:
                if phrase in text:
                    engine.speak("opening the os scanner master")
                    openfun.oscanner()
                    break
                
                
            for phrase in strlists.SID_GUESSER_STR:
                if phrase in text:
                    engine.speak("opening the sid guesser master")
                    openfun.sidguesser()
                    break
               
               
            for phrase in strlists.SQL_LITE_DATABASE_BROWSER_STR:
                if phrase in text:
                    engine.speak("opening the sql lite database browser master")
                    openfun.sql_lite_database_browser()
                    break
               
               
            for phrase in strlists.POMPEM_STR:
                if phrase in text:
                    engine.speak("opening the pompem master")
                    openfun.pompem()
                    break
                
                
            for phrase in strlists.SANDI_GUI_STR:
                if phrase in text:
                    engine.speak("opening the sandi gui master")
                    openfun.sandi_gui()
                    break
                
                
            for phrase in strlists.IPV6_TOOLS_STR:
                if phrase in text:
                    engine.speak("opening the ipv6 tools master")
                    openfun.ipv6_tools()
                    break
                
                
            
            for phrase in strlists.FAKE_ROUTER_STR:
                if phrase in text:
                    engine.speak("opening the fake router master")
                    openfun.fake_router6()
                    break
                
                

            for phrase in strlists.DENIAL6_STR:
                if phrase in text:
                    engine.speak("opening the denial 6 master")
                    openfun.denial6
                    break
                
                
            for phrase in strlists.MSFVENOM_STE:
                if phrase in text:
                    engine.speak("opening the msf venom master")
                    openfun.msfvenom()
                    break
                
                
            for phrase in strlists.METASPLOIT_STR:
                if phrase in text:
                    engine.speak("opening the metasploit master")
                    openfun.metasploit()
                    break
                
                
            for phrase in strlists.PAYLOAD_GENERATOR_STR:
                if phrase in text:
                    engine.speak("opening the payload generator master")
                    openfun.payload_generator()
                    break
                
                
            for phrase in strlists.SHELL_NOOB_STR:
                if phrase in text:
                    engine.speak("opening the shell noob master")
                    openfun.shellnoob()
                    break
               
               
            for phrase in strlists.SOCIAL_ENGINEERING_TOOLS_STR:
                if phrase in text:
                    engine.speak("opening the social engineering tool master")
                    openfun.social_engineering_tool()
                    break
                
                
            for phrase in strlists.TERMINETER_STR:
                if phrase in text:
                    engine.speak("opening the termineter master")
                    openfun.termineter()
                    break
                
                
            for phrase in strlists.SQL_MAP_STR:
                if phrase in text:
                    engine.speak("opening the sql map master")
                    openfun.sqlmap()
                    break
                
                
            for phrase in strlists.BEEF_XSS_FRAMEWORK:
                if phrase in text:
                    engine.speak("opening the beef xss framework master")
                    openfun.beef_xss_framework()
                    break
                
                
            for phrase in strlists.BBQSQL_STR:
                if phrase in text:
                    engine.speak("opening the bbsql master")
                    openfun.bbqsql()
                    break
                
                
            for phrase in strlists.AV_EVASION_STR:
                if phrase in text:
                    engine.speak("opening the av evasion master")
                    openfun.av_evasion()
                    break
                
                
            for phrase in strlists.HYPERION_STR:
                if phrase in text:
                    engine.speak("opening the hyperion master")
                    openfun.hyperion()
                    break
               
               
            for phrase in strlists.SHELLTER_STR:
                if phrase in text:
                    engine.speak("opening the shellter master")
                    openfun.shellter()
                    break
               
               
            for phrase in strlists.OS_BACKDOOR_STR:
                if phrase in text:
                    engine.speak("opening the os back door master")
                    openfun.os_backdoors()
                    break
                
                
                
            for phrase in strlists.CRYPT_CAT_STR:
                if phrase in text:
                    engine.speak("opening the crypt cat master")
                    openfun.crypt_cat()
                    break
                
                


            for phrase in strlists.DBD_STR:
                if phrase in text:
                    engine.speak("opening the dbd master")
                    openfun.dbd()
                    break
              
              
            for phrase in strlists.SBD_STR:
                if phrase in text:
                    engine.speak("opening the sbd master")
                    openfun.sbd()
                    break
                
                
            for phrase in strlists.TUNNELING_AND_EXFILTRATION_TOOL_STR:
                if phrase in text:
                    engine.speak("opening the tunneling and exfiltration master")
                    openfun.tunneling_and_exfiltration_tool()
                    break
                
                
            for phrase in strlists.IODINE_STR:
                if phrase in text:
                    engine.speak("opening the iodine master")
                    openfun.iodine()
                    break
               
               
            for phrase in strlists.PROXY_CHAINS_STR:
                if phrase in text:
                    engine.speak("opening the proxy chains master")
                    openfun.proxychains()
                    break
               
               
            for phrase in strlists.PTUNNEL_STR:
                if phrase in text:
                    engine.speak("opening the ptunnel master")
                    openfun.ptunnel()
                    break
               
               
            for phrase in strlists.SSLH_STR:
                if phrase in text:
                    engine.speak("opening the sslh master")
                    openfun.sslh()
                    break
               
               
            for phrase in strlists.UDP_TUNNEL_STR:
                if phrase in text:
                    engine.speak("opening the udp tunnel master")
                    openfun.udp_tunnel()
                    break
                
                
            for phrase in strlists.WEB_BACKDOOR_STR:
                if phrase in text:
                    engine.speak("opening the web backdoor master")
                    openfun.web_backdoor()
                    break
                
                
            for phrase in strlists.NISHANG_STR:
                if phrase in text:
                    engine.speak("opening the nishang master")
                    openfun.nishang()
                    break
               
               
            for phrase in strlists.WEBACOO_STR:
                if phrase in text:
                    engine.speak("opening the webacoo master")
                    openfun.webacoo()
                    break
                
                
            for phrase in strlists.BDF_PROXY_STR:
                if phrase in text:
                    engine.speak("opening the bdf proxy master")
                    openfun.bdf_proxy()
                    break
                
                
            for phrase in strlists.WINDOWS_BINARIES_STR:
                if phrase in text:
                    engine.speak("opening the windows binaries master")
                    openfun.windows_binaries()
                    break
               
               
            for phrase in strlists.HASH_AND_PASSWORD_STR:
                if phrase in text:
                    engine.speak("opening the hash and password attack master")
                    openfun.hash_and_password_dump()
                    break
                
                
            for phrase in strlists.WCE_STR:
                if phrase in text:
                    engine.speak("opening the wce master")
                    openfun.wce()
                    break
               
               
            for phrase in strlists.PASSING_HASH_ATTACK_TOOL_STR:
                if phrase in text:
                    engine.speak("opening the passing hash attack tool master")
                    openfun.passing_hash_attack_tool()
                    break
                
                
            for phrase in strlists.PTH_NET_STR:
                if phrase in text:
                    engine.speak("opening the pth net master")
                    openfun.pth_net()
                    break
               
            for phrase in strlists.PTH_OPEN_CLIENT_STR:
                if phrase in text:
                    engine.speak("opening the pth open client master")
                    openfun.pth_open_change_client()
                    break
                
            for phrase in strlists.PTH_SMGGET_STR:
                if phrase in text:
                    engine.speak("opening the pth smgget master")
                    openfun.pth_smbget()
                    break
               
            for phrase in strlists.CYMOTHOA_STR:
                if phrase in text:
                    engine.speak("opening the cymothoa master")
                    openfun.cymothoa()
                    break
                
            for phrase in strlists.INTERSECT_STR:
                if phrase in text:
                    engine.speak("opening the intersect master")
                    openfun.intersect()
                    break
              
            for phrase in strlists.POWERSPLOIT_STR:
                if phrase in text:
                    engine.speak("opening the power sploit master")
                    openfun.powersploit()
                    break
                
            for phrase in strlists.LOCAL_ATTACK_TOOLS:
                if phrase in text:
                    engine.speak("opening the local attack tool master")
                    openfun.local_attack_tool()
                    break
                
            for phrase in strlists.CACHE_DUMP_STR:
                if phrase in text:
                    engine.speak("opening the cache dump master")
                    openfun.cachedump()
                    break
               
            for phrase in strlists.OPHCRACK_CLI_STR:
                if phrase in text:
                    engine.speak("opening the ophcrack cli master")
                    openfun.ophcrackcli()
                    break
                
            for phrase in strlists.PWDUMP_STR:
                if phrase in text:
                    engine.speak("opening the pw dump master")
                    openfun.pwdump()
                    break
              
            for phrase in strlists.SAMDUMP_STR:
                if phrase in text:
                    engine.speak("opening the sam dump master")
                    openfun.samdump2()
                    break
               
            for phrase in strlists.OFFLINE_PASSWORD_ATTACK_TOOL_STR:
                if phrase in text:
                    engine.speak("opening the offline password attack tool master")
                    openfun.offline_password_attack_tool()
                    break
               
            for phrase in strlists.CRACKLE_STR:
                if phrase in text:
                    engine.speak("opening the crackle master")
                    openfun.crackle()
                    break
                
            for phrase in strlists.FCRAKZIP_STR:
                if phrase in text:
                    engine.speak("opening the f crack zip master")
                    openfun.fcrakzip()
                    break
               
            for phrase in strlists.HASH_CAT_STR:
                if phrase in text:
                    engine.speak("opening the hash cat master")
                    openfun.hashcat()
                    break
               
            for phrase in strlists.JOHN_STR:
                if phrase in text:
                    engine.speak("opening the john  master")
                    openfun.john()
                    break
               
            for phrase in strlists.PDF_CRACK_STR:
                if phrase in text:
                    engine.speak("opening the pdf crack master")
                    openfun.pdfcrack()
                    break
                
            for phrase in strlists.PYRIT_STR:
                if phrase in text:
                    engine.speak("opening the  pyrit master")
                    openfun.pyrit()
                    break
                
            for phrase in strlists.RAINBOW_CRACK_STR:
                if phrase in text:
                    engine.speak("opening the rainbow master")
                    openfun.rainbowcrack()
                    break
               
            for phrase in strlists.RAR_CRACK_STR:
                if phrase in text:
                    engine.speak("opening the rar crack master")
                    openfun.rarcrack()
                    break
                
            for phrase in strlists.SIP_CRACK_STR:
                if phrase in text:
                    engine.speak("opening the sip crack master")
                    openfun.sipcrack()
                    break
                
            for phrase in strlists.SUCRACK_STR:
                if phrase in text:
                    engine.speak("opening the sucrack master")
                    openfun.sucrack()
                    break
               
            for phrase in strlists.TRUE_CRACK_STR:
                if phrase in text:
                    engine.speak("opening the true crack master")
                    openfun.truecrack()
                    break
                
            for phrase in strlists.ONLINE_PASSWORD_CRACK_STR:
                if phrase in text:
                    engine.speak("opening the online password crack master")
                    openfun.online_password_attack_tool()
                    break
                
            
            for phrase in strlists.BRUTESPRAY_STR:
                if phrase in text:
                    engine.speak("opening the brutespray master")
                    openfun.brutespray()
                    break
            
            for phrase in strlists.CHANGE_ME_STR:
                if phrase in text:
                    engine.speak("opening the change me master")
                    openfun.changeme()
                    break
                
            
            for phrase in strlists.HYDRA_STR:
                if phrase in text:
                    engine.speak("opening the hydra master")
                    openfun.hydra()
                    break
                
            for phrase in strlists.MEDUSA_STR:
                if phrase in text:
                    engine.speak("opening the medusa master")
                    openfun.medusa()
                    break
                
            for phrase in strlists.NCRACK_STR:
                if phrase in text:
                    engine.speak("opening the ncrack master")
                    openfun.webscarab()
                    break
                
            for phrase in strlists.ONE_SIXTY_ONE:
                if phrase in text:
                    engine.speak("opening the one sixty one master")
                    openfun.onesixtyone()
                    break
               
            for phrase in strlists.PATATOR_STR:
                if phrase in text:
                    engine.speak("opening the patator master")
                    openfun.patator()
                    break
                
            for phrase in strlists.XHYDRA_STR:
                if phrase in text:
                    engine.speak("opening the xhydra master")
                    openfun.xhydra()
                    break
                
            for phrase in strlists.WORDLIST_TOOLS:
                if phrase in text:
                    engine.speak("opening the wordlist master")
                    openfun.wordlist_tools()
                    break
                
            for phrase in strlists.CEWL_STR:
                if phrase in text:
                    engine.speak("opening the CEWL master")
                    openfun.cewl()
                    break
                
            for phrase in strlists.CRUNCH_STR:
                if phrase in text:
                    engine.speak("opening the crunch master")
                    openfun.crunch()
                    break
                
            for phrase in strlists.MASKGEN_STR:
                if phrase in text:
                    engine.speak("opening the mask gen master")
                    openfun.maskgen()
                    break
                
            for phrase in strlists.PIPAL_STR:
                if phrase in text:
                    engine.speak("opening the pipal master")
                    openfun.pipal()
                    break
               
            for phrase in strlists.POLICY_GEN:
                if phrase in text:
                    engine.speak("opening the policy gen master")
                    openfun.policygen()
                    break
                
            for phrase in strlists.STATSGEN_STR:
                if phrase in text:
                    engine.speak("opening the stats gen master")
                    openfun.statsgen()
                    break
               
            for phrase in strlists.WORDLISTS_STR:
                if phrase in text:
                    engine.speak("opening the wordlists master")
                    openfun.wordlists()
                    break
                
            for phrase in strlists.FIND_MY_HASH:
                if phrase in text:
                    engine.speak("opening the find my hash  master")
                    openfun.find_my_hash()
                    break
               
            for phrase in strlists.HASHID_STR:
                if phrase in text:
                    engine.speak("opening the hash id  master")
                    openfun.hashid()
                    break
                
            for phrase in strlists.HASH_IDENTIFIER_STR:
                if phrase in text:
                    engine.speak("opening the hash identifier master")
                    openfun.hash_identifier()
                    break
                
            for phrase in strlists.WIFITE_STR:
                if phrase in text:
                    engine.speak("opening the wifite master")
                    openfun.webscarab()
                    break
                
            for phrase in strlists.BLUETOOTH_STR:
                if phrase in text:
                    engine.speak("opening the bluetooth hacking tool master")
                    openfun.bluetooth_hackingtool()
                    break
                
            for phrase in strlists.BLUELOG_STR:
                if phrase in text:
                    engine.speak("opening the blue log master")
                    openfun.bluelog()
                    break
               
            for phrase in strlists.BLUE_RANGER_STR:
                if phrase in text:
                    engine.speak("opening the blue ranger master")
                    openfun.blueranger()
                    break
                
            for phrase in strlists.BT_SCANNER_STR:
                if phrase in text:
                    engine.speak("opening the bt scanner master")
                    openfun.btscanner()
                    break
                
            for phrase in strlists.RED_FANG_STR:
                if phrase in text:
                    engine.speak("opening the red fang scanner master")
                    openfun.redfang()
                    break
               
            for phrase in strlists.GEN_KEYS_STR:
                if phrase in text:
                    engine.speak("opening the gen keys scanner master")
                    openfun.genkeys()
                    break
               
            for phrase in strlists.HACK_RF_INFO_STR:
                if phrase in text:
                    engine.speak("opening the bt hack rf info master")
                    openfun.hackrf_info()
                    break
                
            for phrase in strlists.UBERTOOTH_UTIL:
                if phrase in text:
                    engine.speak("opening the bt ubertooth util master")
                    openfun.ubertooth_util()
                    break
                
            for phrase in strlists.RFID_AND_NFC_TOOLS:
                if phrase in text:
                    engine.speak("opening the rfid and nfc tools  master")
                    openfun.rfid_and_nfc_tools()
                    break
               
            for phrase in strlists.SOFTWARE_DETAILED_RADIO_STR:
                if phrase in text:
                    engine.speak("opening the software detailed radio  master")
                    openfun.software_detailed_radio()
                    break
               
            for phrase in strlists.INSPECTRUM_STR:
                if phrase in text:
                    engine.speak("opening the inspectrum master")
                    openfun.inspectrum()
                    break
               
            for phrase in strlists.RFCAT_STR:
                if phrase in text:
                    engine.speak("opening the scanner master")
                    openfun.btscanner()
                    break
                
            for phrase in strlists.GNU_RADIO_COMPANION_STR:
                if phrase in text:
                    engine.speak("opening the gnu radio companion master")
                    openfun.gnu_radio_companion()
                    break
                
            for phrase in strlists.FERN_WIFI_CRACKER_STR:
                if phrase in text:
                    engine.speak("opening the fern wifi cracker master")
                    openfun.fern_wifi_cracker()
                    break
               
            for phrase in strlists.MDK3_STR:
                if phrase in text:
                    engine.speak("opening the mdk3 master")
                    openfun.mdk3()
                    break
                
            for phrase in strlists.PIXIE_WPS_STR:
                if phrase in text:
                    engine.speak("opening the pixie wps master")
                    openfun.pixiewps()
                    break
                
            for phrase in strlists.REAVER_STR:
                if phrase in text:
                    engine.speak("opening reaver master")
                    openfun.reaver()
                    break
               
            for phrase in strlists.NETWORK_SNIFFERS_STR:
                if phrase in text:
                    engine.speak("opening network sniffers master")
                    openfun.network_sniffers()
                    break
               
            for phrase in strlists.HEX_INJECT_STR:
                if phrase in text:
                    engine.speak("opening the hex inject master")
                    openfun.hexinject()
                    break
                
            for phrase in strlists.CHAOS_READER_STR:
                if phrase in text:
                    engine.speak("opening the chaos reader master")
                    openfun.chaosreader()
                    break
               
            for phrase in strlists.DARK_STAT_STR:
                if phrase in text:
                    engine.speak("opening dark stat master")
                    openfun.darkstat()
                    break
                
            for phrase in strlists.NET_SNIFF_STR:
                if phrase in text:
                    engine.speak("opening net sniff master")
                    openfun.netsniff_ng()
                    break
                
            for phrase in strlists.NFSPY_STR:
                if phrase in text:
                    engine.speak("opening NF spy master")
                    openfun.nfspy()
                    break
                
            for phrase in strlists.WEBSPY_STR:
                if phrase in text:
                    engine.speak("opening webspy master")
                    openfun.webspy()
                    break
                
            for phrase in strlists.SSLSNIFF_STR:
                if phrase in text:
                    engine.speak("opening SSL sniff master")
                    openfun.sslsniff()
                    break
                
            for phrase in strlists.SPOOFING_AND_MITM_STR:
                if phrase in text:
                    engine.speak("opening spoofing and mitm")
                    openfun.spoofing_and_mitm()
                    break
                
            for phrase in strlists.PARASITE6_STR:
                if phrase in text:
                    engine.speak("opening parasite 6 master")
                    openfun.parasite6()
                    break
                
            for phrase in strlists.WIFI_HONEY_STR:
                if phrase in text:
                    engine.speak("opening wifi  honey master")
                    openfun.wifi_honey()
                    break
                
            for phrase in strlists.BETTTER_CAP_SRT:
                if phrase in text:
                    engine.speak("opening better cap master")
                    openfun.bettercap()
                    break
            
            for phrase in strlists.ETHERRAPE_STR:
                if phrase in text:
                    engine.speak("opening ether rape master")
                    openfun.etherrape()
                    break
                
            for phrase in strlists.HAMSTER_STR:
                if phrase in text:
                    engine.speak("opening hamster master")
                    openfun.hamster()
                    break
                
            for phrase in strlists.IMPACKET_STR:
                if phrase in text:
                    engine.speak("opening impacket master")
                    openfun.impacket()
                    break
            
            for phrase in strlists.MACCHANGER_STR:
                if phrase in text:
                    engine.speak("opening mac changer master")
                    openfun.macchanger()
                    break
                
            for phrase in strlists.MITM_PROXY_STR:
                if phrase in text:
                    engine.speak("opening MITM proxy master")
                    openfun.mitm_proxy()
                    break
                
            for phrase in strlists.RESPONDER_STR:
                if phrase in text:
                    engine.speak("opening  responder master")
                    openfun.responder()
                    break
                
            for phrase in strlists.DIGITAL_FORENSIC_TOOL:
                if phrase in text:
                    engine.speak("opening  digital forensic tool master")
                    openfun.digital_forensic_tool()
                    break
                
            for phrase in strlists.FORENSIC_CARVING_TOOL:
                if phrase in text:
                    engine.speak("opening  forensic carving tool master")
                    openfun.forensic_carving_tools()
                    break
                
            for phrase in strlists.PDF_FORENSIC_TOOL:
                if phrase in text:
                    engine.speak("opening  pdf forensic tool master")
                    openfun.pdf_forensic_tool()
                    break
                
            for phrase in strlists.AUTOSPY_STR:
                if phrase in text:
                    engine.speak("opening auto spy master")
                    openfun.autospy()
                    break
               
            for phrase in strlists.BIN_WALK_STR:
                if phrase in text:
                    engine.speak("opening bin walk master")
                    openfun.binwalk()
                    break
              
            for phrase in strlists.BULK_EXTRACTOR_STR:
                if phrase in text:
                    engine.speak("opening  bulk extractor master")
                    openfun.bulk_extractor()
                    break
                
            for phrase in strlists.CHKROOTKIT_STR:
                if phrase in text:
                    engine.speak("opening  chk root kit master")
                    openfun.chkrootkit()
                    break
               
            for phrase in strlists.FOREMOST_STR:
                if phrase in text:
                    engine.speak("opening  fore most master")
                    openfun.foremost()
                    break
               
            for phrase in strlists.GALLETA_STR:
                if phrase in text:
                    engine.speak("opening galleta master")
                    openfun.galleta()
                    break
                
            for phrase in strlists.HASH_DEEP_STR:
                if phrase in text:
                    engine.speak("opening hash deep master")
                    openfun.hashdeep()
                    break
                
            for phrase in strlists.RKHUNTER_STR:
                if phrase in text:
                    engine.speak("opening rkhunter master")
                    openfun.rkhunter()
                    break
               
            for phrase in strlists.VOLA_FOX_STR:
                if phrase in text:
                    engine.speak("opening vola fox master")
                    openfun.volafox()
                    break
                
            for phrase in strlists.VOLATILITY_STR:
                if phrase in text:
                    engine.speak("opening volatility master")
                    openfun.volatility()
                    break
               
            for phrase in strlists.VARA_STR:
                if phrase in text:
                    engine.speak("opening vara master")
                    openfun.vara()
                    break
                
            for phrase in strlists.AUTOMOTIVE_STR:
                if phrase in text:
                    engine.speak("opening  automotive master")
                    openfun.automotive_tools()
                    break
              
            for phrase in strlists.DEBUGER_STR:
                if phrase in text:
                    engine.speak("opening  debugger master")
                    openfun.debugger()
                    break
               
            for phrase in strlists.JAVA_SNOOP_STR:
                if phrase in text:
                    engine.speak("opening  javasnoop master")
                    openfun.javasnoop()
                    break
                
            for phrase in strlists.DECOMPILERS_STR:
                if phrase in text:
                    engine.speak("opening  decompilers master")
                    openfun.decompilers()
                    break
                
            for phrase in strlists.JAD_STR:
                if phrase in text:
                    engine.speak("opening jad master")
                    openfun.jad()
                    break
                


            for phrase in strlists.DIASSEMBLER_STR:
                if phrase in text:
                    engine.speak("opening  diassembler master")
                    openfun.diassembler()
                    break
               
            for phrase in strlists.FLASM_STR:
                if phrase in text:
                    engine.speak("opening flasm master")
                    openfun.flasm()
                    break
               
            for phrase in strlists.RADARE_2_FRAMEWORK_STR:
                if phrase in text:
                    engine.speak("opening  radare 2 frame work master")
                    openfun.radare_2_framework()
                    break
               
            for phrase in strlists.APK_TOOL_STR:
                if phrase in text:
                    engine.speak("opening  apk tool master")
                    openfun.apktool()
                    break
               
            for phrase in strlists.CLANG_STR:
                if phrase in text:
                    engine.speak("opening  clang master")
                    openfun.clang()
                    break
              
            for phrase in strlists.CASEFILES_STR:
                if phrase in text:
                    engine.speak("opening  case files master")
                    openfun.casefile()
                    break
               
            for phrase in strlists.EYE_WITNESS_STR:
                if phrase in text:
                    engine.speak("opening  eye witness master")
                    openfun.eyewitness()
                    break
               
            for phrase in strlists.META_GOOFIL_STR:
                if phrase in text:
                    engine.speak("opening  meta goofil master")
                    openfun.metagoofil()
                    break
                
            for phrase in strlists.FARADAY_IDE_STR:
                if phrase in text:
                    engine.speak("opening  faraday ide master")
                    openfun.faradayide()
                    break
                
            for phrase in strlists.DBEAVER_STR:
                if phrase in text:
                    engine.speak("opening  d beaver master")
                    openfun.dbeaver()
                    break
                
            for phrase in strlists.GEANY_STR:
                if phrase in text:
                    engine.speak("opening  geany master")
                    openfun.geany()
                    break
                
            for phrase in strlists.GIT_COLA_STR:
                if phrase in text:
                    engine.speak("opening  git cola master")
                    openfun.git_cola()
                    break
               
            for phrase in strlists.GIT_DAG_STR:
                if phrase in text:
                    engine.speak("opening git dag master")
                    openfun.git_dag()
                    break
               
            for phrase in strlists.MELD_STR:
                if phrase in text:
                    engine.speak("opening  meld master")
                    openfun.meld()
                    break
              
            for phrase in strlists.SUBLIME_STR:
                if phrase in text:
                    engine.speak("opening  sublime master")
                    openfun.sublime()
                    break
                else:
                    pass
            
            for phrase in strlists.ZEAL_STR:
                if phrase in text:
                    engine.speak("opening  zeal master")
                    openfun.zeal()
                    break
                
            for phrase in strlists.XRC_STR:
                if phrase in text:
                    engine.speak("opening XRC tool master")
                    openfun.XRC_ed()
                    break
                
            for phrase in strlists.BRASERO_STR:
                if phrase in text:
                    engine.speak("opening  brasero master")
                    openfun.brasero()
                    break
                
            for phrase in strlists.CHEESE_STR:
                if phrase in text:
                    engine.speak("opening cheese  master")
                    openfun.cheese()
                    break
                

            for phrase in strlists.LMMS_STR:
                if phrase in text:
                    engine.speak("opening  lmms master")
                    openfun.lmms()
                    break
                
            for phrase in strlists.MPV_MEDIA_PLAYER_STR:
                if phrase in text:
                    engine.speak("opening MPV media player master")
                    openfun.mpv_media_player()
                    break
                

            for phrase in strlists.SOUND_KONVERTER:
                if phrase in text:
                    engine.speak("opening sound converter master")
                    openfun.sound_konverter()
                    break
                

            for phrase in strlists.TIMIDITY_STR:
                if phrase in text:
                    engine.speak("opening tmidity master")
                    openfun.timidity()
                    break
                


            for phrase in strlists.VOKO_SCREEN_STR:
                if phrase in text:
                    engine.speak("opening voko screen master")
                    openfun.vokoscreen()
                    break
                
            for phrase in strlists.BLEACH_BIT_STR:
                if phrase in text:
                    engine.speak("opening bleach bit master")
                    openfun.bleach_bit()
                    break
                
            for phrase in strlists.CAJA_STR:
                if phrase in text:
                    engine.speak("opening caja  master")
                    openfun.caja()
                    break
               
            for phrase in strlists.DCONFEDITOR_STR:
                if phrase in text:
                    engine.speak("opening dconfeditor master")
                    openfun.dconfeditor()
                    break
              
            for phrase in strlists.DVDISASTER_STR:
                if phrase in text:
                    engine.speak("opening dv disaster master")
                    openfun.dvdisaster()
                    break
                
            for phrase in strlists.GDEBI_STR:
                if phrase in text:
                    engine.speak("opening gdebi master")
                    openfun.gdebi()
                    break
                
            for phrase in strlists.GPARTED_STR:
                if phrase in text:
                    engine.speak("opening gparted master")
                    openfun.gparted()
                    break
             
            for phrase in strlists.GUYMAGER_STR:
                if phrase in text:
                    engine.speak("opening guymager master")
                    openfun.guymager()
                    break
            
            for phrase in strlists.HTOP_STR:
                if phrase in text:
                    engine.speak("opening H top  master")
                    openfun.htop()
                    break
                
            for phrase in strlists.LOG_FILE_VIEWER_STR:
                if phrase in text:
                    engine.speak("opening log file viewer master")
                    openfun.log_file_viewer()
                    break
                   
            for phrase in strlists.NEOVIM_STR:
                if phrase in text:
                    engine.speak("opening  neovim master")
                    openfun.neovim()
                    break
            

            for phrase in strlists.GQRX_STR:
                if phrase in text:
                    engine.speak("opening  gqrx master")
                    openfun.gqrx()
                    break
               

          
            for phrase in strlists.QBITTORRENT_STR:
                if phrase in text:
                    engine.speak("opening  qbittorrent master")
                    openfun.qbittorrent()
                    break
                

            for phrase in strlists.REMMINA_BROWSER_STR:
                if phrase in text:
                    engine.speak("opening  remmina master")
                    openfun.remmina_browser()
                    break
               

            for phrase in strlists.TOR_BROWSER_STR:
                if phrase in text:
                    engine.speak("opening tor browser master")
                    openfun.tor_Browser()
                    break
               

            for phrase in strlists.CONTROL_CENTER_0R_SETTINGS_STR:
                if phrase in text:
                    engine.speak("opening  control center master")
                    openfun.control_center_or_settings()
                    break
               
            for phrase in strlists.TWEAKS_STR:
                if phrase in text:
                    engine.speak("opening tweaks  master")
                    openfun.tweaks()
                    break
                
            for phrase in strlists.SYSTEM_MONITOR_PROCESSOR_USE:
                if phrase in text:
                    engine.speak("opening  system monitor master")
                    openfun.system_monitor_processor_use()
                    break
                
            for phrase in strlists.NMAP_STR:
                if phrase in text:
                    engine.speak("opening nmap")
                    openfun.nmap()
                    break
              
            
            for phrase in strlists.TERMINAL_STR:
                if phrase in text:
                    engine.speak("opening terminal master")
                    openfun.terminal()
                    break
               
            
            for pharse in strlists.PLUMA_STR:
                if phrase in text:
                    engine.speak("opening pluma master")
                    openfun.pluma()
                    break
               

            for phrase in strlists.NITKO_STR:
                if phrase in text:
                    engine.speak("opening the nitko scanner master!")
                    openfun.nitko()
                    break
               
        
                    
            for phrase in strlists.CALC_STR:
                if phrase in text:
                    engine.speak("opening calculator master!")
                    openfun.calc()
                    break
               
            for phrase in strlists.NVIM_STR:
                if phrase in text:
                    engine.speak("openig the nvim text editor master")
                    openfun.nvim()
                    break
                
            for phrase in strlists.VSCODE_STR:
                if phrase in text:
                    engine.speak("opening visual studio code master!")
                    openfun.vscode()
                    break
               
            for pharse in strlists.ANONSURF_STR:
                if phrase in text:
                    engine.speak("starting anonsurf master")
                    openfun.anonsurf()
                    break
               
            for phrase in strlists.LIBREOFFICE_STR:
                if phrase in text:
                    for phrase in strlists.LIBREOFFICE_BASE:
                        if phrase in text:
                            engine.speak("opening the libre office base master!")
                            openfun.libre_office_base()
                            break
                        
                    for phrase in strlists.LIBREOFFICE_CALC:
                        if phrase in text:
                            engine.speak("opening the libreoffice calc master!")
                            openfun.libre_office_calc()
                      
                    for phrase in strlists.LIBREOFFICE_DRAW:
                        if phrase in text:
                            engine.speak("opening the libreoffice draw master!")
                            openfun.libre_office_draw()
                            break
                      
                    
                    for phrase in strlists.LIBREOFFICE_IMPRESS:
                        if phrase in text:
                            engine.speak("opening the libreoffice impress master!")
                            openfun.libre_office_impress()
                            break
                      
                    for phrase in strlists.LIBREOFFICE_WRITER:
                        if phrase in text:
                            engine.speak("opening the libre office writer master!")
                            openfun.libre_office_writer()
                            break
                        
                    for phrase in strlists.LIBREOFFICE_MATH:
                        if phrase in text:
                            engine.speak("opneing the libreoffice maths master!")
                            openfun.libre_office_math()
                            break
                        
                    break
               

            for phrase in strlists.CHESS_STR:
                if phrase in text:
                    engine.speak("opening the xboard master!")
                    openfun.xboard()
                    break
               

            for phrase in strlists.PHOTOEDITOR_STR:
                if phrase in text:
                    engine.speak("opening the gimp image manupulation program")
                    openfun.photoeditor()
                    break
              
    
    ####################################
    #open apps loop closes here
   ####################################
   ####################################
